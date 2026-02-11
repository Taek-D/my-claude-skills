# My Claude Skills

Custom Claude Code skills for personal productivity and automation.

## Skills

### notion-project-upload

**Version**: 1.1.0  
**Category**: Productivity

Upload projects to Notion with optimized portfolio templates. Automatically analyzes project type (business/exploratory/technical/learning) and applies recruiter-friendly templates.

**Features**:
- 🎯 Auto-detects project type (4 types)
- 📊 Dataset section for data transparency (v1.1+)
- 🎨 Emoji + English sections
- 📝 14 property fields auto-populated
- 🏷️ Tech stack tagging
- 🎨 Glow color selection
- 📅 Auto date updates

**Templates**:
- Type 1: Business Impact (Before/After, ROI, metrics)
- Type 2: Exploratory Analysis (EDA, findings, insights)
- Type 3: Technical Implementation (Code, architecture, optimization)
- Type 4: Learning Project (Kaggle, courses, practice)

## Installation

### Via Claude Code Marketplace (Recommended)

```bash
# In Claude Code CLI
/install-skill https://github.com/Taek-D/my-claude-skills
```

### Manual Installation

```bash
# Clone repository
git clone https://github.com/Taek-D/my-claude-skills.git

# Copy to Claude Code skills directory
cp -r my-claude-skills/skills/* ~/.claude/skills/
```

## Usage

In any Claude conversation:

```
"노션에 업로드해줘"
"Upload this project to Notion"
"프로젝트 포트폴리오 업로드"
```

The skill will:
1. Analyze your project
2. Select appropriate template
3. Generate optimized content
4. Upload to your Notion database

## Configuration

Set your Notion database ID in user memories or provide it when uploading:

```
Database ID: ce6722a9-00b2-4d0e-8eda-190f4ce97cb6
```

## Version History

### v1.1.0 (2026.02.11)
- ✨ Added Dataset section to Type 1/2/3 templates
- 📊 Improved portfolio credibility with data transparency
- 🔍 Quality checklist updated with Dataset verification
- 📝 Version info added to SKILL.md

### v1.0.0 (2026.02.10)
- 🎉 Initial release
- 4 project type templates
- 14 property auto-population
- Emoji + English sections
- Tech stack tagging
- Glow color selection

## Contributing

Feel free to submit issues or pull requests!

## License

MIT
