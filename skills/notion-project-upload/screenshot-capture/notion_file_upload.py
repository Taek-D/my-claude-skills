"""
Notion File Upload API Wrapper
==============================
Notion API의 File Upload 기능을 사용하여
로컬 이미지를 Notion 페이지에 직접 업로드한다.

3-Step Flow:
1. File Upload 객체 생성 → file_upload_id
2. 파일 바이너리 전송
3. 이미지 블록으로 페이지에 첨부

Usage:
    uploader = NotionFileUploader(notion_token="ntn_xxx")
    file_upload_id = uploader.upload_image("screenshot.png")
    uploader.attach_image_to_page(page_id, file_upload_id, caption="메인 화면")
"""

import json
import mimetypes
import os
import requests
from pathlib import Path
from typing import Optional


NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

# 지원 이미지 포맷
SUPPORTED_IMAGE_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
}

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB


class NotionFileUploader:
    """Notion File Upload API를 통한 이미지 업로드 관리"""

    def __init__(self, notion_token: str):
        self.token = notion_token
        self.headers = {
            "Authorization": f"Bearer {notion_token}",
            "Notion-Version": NOTION_VERSION,
        }

    # ─────────────────────────────────────────────
    # Step 1: File Upload 객체 생성
    # ─────────────────────────────────────────────
    def _create_file_upload(self, filename: str, content_type: str) -> dict:
        """File Upload 객체를 생성하고 id와 upload_url을 반환"""
        response = requests.post(
            f"{NOTION_API_BASE}/file_uploads",
            headers={**self.headers, "Content-Type": "application/json"},
            json={"filename": filename, "content_type": content_type},
        )

        if response.status_code != 200:
            raise NotionUploadError(
                f"File Upload 생성 실패 (HTTP {response.status_code}): {response.text}"
            )

        data = response.json()
        return {
            "id": data["id"],
            "upload_url": data.get("upload_url"),
            "expiry_time": data.get("expiry_time"),
        }

    # ─────────────────────────────────────────────
    # Step 2: 파일 바이너리 전송
    # ─────────────────────────────────────────────
    def _send_file_content(self, file_upload_id: str, filepath: str, content_type: str) -> dict:
        """파일 내용을 Notion에 전송 (multipart/form-data)"""
        filename = os.path.basename(filepath)

        with open(filepath, "rb") as f:
            files = {"file": (filename, f, content_type)}
            response = requests.post(
                f"{NOTION_API_BASE}/file_uploads/{file_upload_id}/send",
                headers={
                    "Authorization": f"Bearer {self.token}",
                    "Notion-Version": NOTION_VERSION,
                },
                files=files,
            )

        if response.status_code != 200:
            raise NotionUploadError(
                f"파일 전송 실패 (HTTP {response.status_code}): {response.text}"
            )

        data = response.json()
        if data.get("status") != "uploaded":
            raise NotionUploadError(f"파일 상태 이상: {data.get('status')}")

        return data

    # ─────────────────────────────────────────────
    # Step 3: 이미지 블록으로 페이지에 첨부
    # ─────────────────────────────────────────────
    def _attach_image_block(
        self,
        page_id: str,
        file_upload_id: str,
        caption: str = "",
    ) -> dict:
        """이미지 블록을 페이지에 추가"""
        caption_rich_text = []
        if caption:
            caption_rich_text = [{"type": "text", "text": {"content": caption}}]

        payload = {
            "children": [
                {
                    "type": "image",
                    "image": {
                        "type": "file_upload",
                        "file_upload": {"id": file_upload_id},
                        "caption": caption_rich_text,
                    },
                }
            ]
        }

        response = requests.patch(
            f"{NOTION_API_BASE}/blocks/{page_id}/children",
            headers={**self.headers, "Content-Type": "application/json"},
            json=payload,
        )

        if response.status_code != 200:
            raise NotionUploadError(
                f"이미지 블록 첨부 실패 (HTTP {response.status_code}): {response.text}"
            )

        return response.json()

    # ─────────────────────────────────────────────
    # Public API: 이미지 업로드 (3-Step 통합)
    # ─────────────────────────────────────────────
    def upload_image(self, filepath: str) -> str:
        """
        로컬 이미지 파일을 Notion에 업로드하고 file_upload_id를 반환.
        이 ID를 사용하여 나중에 페이지에 첨부할 수 있다.

        Args:
            filepath: 이미지 파일 경로

        Returns:
            file_upload_id (str)

        Raises:
            NotionUploadError: 업로드 실패 시
            FileValidationError: 파일 검증 실패 시
        """
        # 파일 검증
        self._validate_file(filepath)

        filename = os.path.basename(filepath)
        ext = Path(filepath).suffix.lower()
        content_type = SUPPORTED_IMAGE_TYPES.get(ext, "application/octet-stream")

        # Step 1: File Upload 객체 생성
        upload_obj = self._create_file_upload(filename, content_type)

        # Step 2: 파일 전송
        self._send_file_content(upload_obj["id"], filepath, content_type)

        return upload_obj["id"]

    def attach_image_to_page(
        self,
        page_id: str,
        file_upload_id: str,
        caption: str = "",
    ) -> dict:
        """
        업로드된 이미지를 Notion 페이지에 첨부.

        Args:
            page_id: Notion 페이지 ID
            file_upload_id: upload_image()에서 반환된 ID
            caption: 이미지 캡션

        Returns:
            Notion API 응답 dict
        """
        return self._attach_image_block(page_id, file_upload_id, caption)

    def upload_and_attach(
        self,
        filepath: str,
        page_id: str,
        caption: str = "",
    ) -> dict:
        """
        이미지 업로드 + 페이지 첨부를 한 번에 수행.

        Args:
            filepath: 이미지 파일 경로
            page_id: Notion 페이지 ID
            caption: 이미지 캡션

        Returns:
            {"file_upload_id": str, "response": dict}
        """
        file_upload_id = self.upload_image(filepath)
        response = self.attach_image_to_page(page_id, file_upload_id, caption)
        return {"file_upload_id": file_upload_id, "response": response}

    def set_page_cover(self, page_id: str, file_upload_id: str) -> dict:
        """업로드된 이미지를 페이지 커버로 설정"""
        payload = {
            "cover": {
                "type": "file_upload",
                "file_upload": {"id": file_upload_id},
            }
        }

        response = requests.patch(
            f"{NOTION_API_BASE}/pages/{page_id}",
            headers={**self.headers, "Content-Type": "application/json"},
            json=payload,
        )

        if response.status_code != 200:
            raise NotionUploadError(
                f"커버 설정 실패 (HTTP {response.status_code}): {response.text}"
            )

        return response.json()

    # ─────────────────────────────────────────────
    # Batch: 여러 이미지를 한 페이지에 첨부
    # ─────────────────────────────────────────────
    def upload_batch(
        self,
        images: list[dict],
        page_id: str,
    ) -> list[dict]:
        """
        여러 이미지를 순차 업로드하고 페이지에 첨부.

        Args:
            images: [{"path": str, "caption": str, "type": "main"|"detail"|"terminal"}, ...]
            page_id: Notion 페이지 ID

        Returns:
            [{"path": str, "file_upload_id": str, "success": bool, "error": str|None}, ...]
        """
        results = []

        for img in images:
            try:
                file_upload_id = self.upload_image(img["path"])
                self.attach_image_to_page(page_id, file_upload_id, img.get("caption", ""))
                results.append({
                    "path": img["path"],
                    "file_upload_id": file_upload_id,
                    "success": True,
                    "error": None,
                })
            except (NotionUploadError, FileValidationError) as e:
                results.append({
                    "path": img["path"],
                    "file_upload_id": None,
                    "success": False,
                    "error": str(e),
                })

        return results

    # ─────────────────────────────────────────────
    # Notion 블록 빌더 (이미지 섹션)
    # ─────────────────────────────────────────────
    @staticmethod
    def build_screenshot_section(
        screenshots: list[dict],
        section_title: str = "Demo",
    ) -> list[dict]:
        """
        스크린샷 목록을 Notion 블록 리스트로 변환.
        기존 템플릿의 블록 리스트에 삽입할 수 있다.

        Args:
            screenshots: [{"file_upload_id": str, "caption": str, "type": str}, ...]
            section_title: 섹션 제목

        Returns:
            Notion API children 블록 리스트
        """
        blocks = []

        # 섹션 헤딩
        blocks.append({
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": section_title}}],
            },
        })

        # 구분선
        blocks.append({"type": "divider", "divider": {}})

        for shot in screenshots:
            blocks.append({
                "type": "image",
                "image": {
                    "type": "file_upload",
                    "file_upload": {"id": shot["file_upload_id"]},
                    "caption": [
                        {
                            "type": "text",
                            "text": {"content": shot.get("caption", "")},
                        }
                    ]
                    if shot.get("caption")
                    else [],
                },
            })

        return blocks

    # ─────────────────────────────────────────────
    # 유틸리티
    # ─────────────────────────────────────────────
    def _validate_file(self, filepath: str) -> None:
        """파일 유효성 검증"""
        path = Path(filepath)

        if not path.exists():
            raise FileValidationError(f"파일을 찾을 수 없음: {filepath}")

        if not path.is_file():
            raise FileValidationError(f"파일이 아님: {filepath}")

        ext = path.suffix.lower()
        if ext not in SUPPORTED_IMAGE_TYPES:
            raise FileValidationError(
                f"지원하지 않는 이미지 포맷: {ext} "
                f"(지원: {', '.join(SUPPORTED_IMAGE_TYPES.keys())})"
            )

        size = path.stat().st_size
        if size > MAX_FILE_SIZE:
            size_mb = size / (1024 * 1024)
            raise FileValidationError(
                f"파일 크기 초과: {size_mb:.1f}MB (최대: 20MB)"
            )

        if size == 0:
            raise FileValidationError(f"빈 파일: {filepath}")


class NotionUploadError(Exception):
    """Notion API 업로드 관련 에러"""
    pass


class FileValidationError(Exception):
    """파일 검증 에러"""
    pass


# ─────────────────────────────────────────────
# CLI 테스트
# ─────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("Usage: python notion_file_upload.py <token> <page_id> <image_path> [caption]")
        sys.exit(1)

    token = sys.argv[1]
    page_id = sys.argv[2]
    image_path = sys.argv[3]
    caption = sys.argv[4] if len(sys.argv) > 4 else ""

    uploader = NotionFileUploader(token)
    result = uploader.upload_and_attach(image_path, page_id, caption)
    print(f"✅ 업로드 완료: {result['file_upload_id']}")
