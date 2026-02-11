# My Claude Skills

Custom Claude Code skills for personal productivity and automation.

## Skills

### notion-project-upload

**Version**: 1.2.0  
**Category**: Productivity

Upload projects to Notion with optimized portfolio templates. Automatically analyzes project type (business/exploratory/technical/learning) and applies recruiter-friendly templates.

**Features**:
- 🎯 Auto-detects project type (4 types)
- 👥 Collaboration & Impact section (v1.2+)
- 📊 Statistical Validation for analysis projects (v1.2+)
- 🚀 Deployment & Usage tracking (v1.2+)
- 📁 Dataset section for data transparency (v1.1+)
- 🎨 Emoji + English sections
- 📝 14 property fields auto-populated
- 🏷️ Tech stack tagging
- 🎨 Glow color selection
- 📅 Auto date updates

**Templates**:
- Type 1: Business Impact (Before/After, ROI, metrics, collaboration, deployment)
- Type 2: Exploratory Analysis (EDA, findings, statistical validation, insights)
- Type 3: Technical Implementation (Code 15-20 lines, architecture, deployment)
- Type 4: Learning Project (Kaggle, courses, practice, reflection)

**What's New in v1.2**:
- ✨ **Collaboration & Impact** - Show teamwork, stakeholder management
- 📊 **Statistical Validation** - Hypothesis testing, p-values, effect sizes
- 🚀 **Deployment & Usage** - Production status, real-world impact
- 💻 **Better Code Blocks** - 15-20 lines (up from 10)
- 🎯 **Business Context** - Always explain "why this matters"
- 🔍 **Differentiation** - Less template-y, more personality

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

### v1.2.0 (2026.02.11) - Major Improvements
- ✨ Added **Collaboration & Impact** section (Type 1/2/3)
  - Show stakeholder interaction
  - Communication methods
  - Real-world usage and feedback
- 📊 Added **Statistical Validation** section (Type 2)
  - Hypothesis testing (H0/H1)
  - p-values, effect sizes
  - Confidence intervals
- 🚀 Added **Deployment & Usage** section (Type 1/3)
  - Production status
  - Real usage metrics
  - User feedback
- 💻 Increased code block limit: 10 → 15-20 lines
- 🎯 Enhanced business context requirement
- 🔍 Removed duplicate "데이터 특성" in Type 2
- 📋 Updated Quality Checklist

**Why v1.2?** Based on feedback from recruiters and data professionals:
- Show teamwork ability (not just solo projects)
- Demonstrate statistical rigor (not just charts)
- Prove real-world impact (not just toy projects)
- Less template-y, more personality

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

## Roadmap

**v1.3.0 (Planned)**
- [ ] Multi-language support (English templates)
- [ ] Custom template creation
- [ ] Batch upload support

## Contributing

Feel free to submit issues or pull requests!

## License

MIT
