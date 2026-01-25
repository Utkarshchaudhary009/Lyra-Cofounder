---
name: project-organization
description: Organize project folders for maximum efficiency, scalability, and maintainability. Use when setting up new projects, reorganizing existing codebases, creating knowledge bases, or advising on file structure. Triggers on project setup, folder structure questions, file organization, and monorepo architecture contexts.
---

# Project Organization

The best folder structure is one you'll actually use. Consistency beats perfection.

## Core Principles

1. **Consistency is King** — Same conventions everywhere
2. **Clarity Over Cleverness** — Descriptive names, no "misc" folders
3. **The 3-Click Rule** — Reach any file within 3 clicks
4. **Shallow Hierarchy** — Maximum 3-4 levels deep
5. **Start Simple, Evolve Gradually** — Don't over-engineer initially

## Naming Conventions

### Files
- Lowercase + hyphens: `lyra-cofounder-research.md` ✅
- Include dates for versions: `YYYY-MM-DD` format
- No spaces (use hyphens instead)
- Descriptive, not generic: `user-auth-flow.md` ✅, `document1.md` ❌

### Folders
- Plural for collections: `/components`, `/images`
- Numbered for sequence: `01_planning`, `02_design`, `03_development`
- No special characters: `@, #, %, &, *` ❌

## The PARA Method

Best for personal knowledge management:

```
/Projects       → Active efforts with defined outcomes
/Areas          → Ongoing responsibilities (no end date)
/Resources      → Topics of interest, reference material
/Archives       → Completed projects, inactive areas
```

## Research/Documentation Project

```
project-name/
├── 0_admin/                # Administrative docs
├── 1_research/             # Literature, papers
├── 2_data/
│   ├── raw/                # Original (READ-ONLY)
│   └── processed/          # Cleaned, transformed
├── 3_code/                 # All scripts
├── 4_outputs/              # Results, figures
├── 5_writing/              # Drafts, published
└── README.md               # Project overview
```

## Software Monorepo

```
my-monorepo/
├── apps/                   # Deployable applications
│   ├── web/
│   ├── mobile/
│   └── api/
├── packages/               # Shared libraries
│   ├── ui/
│   ├── auth/
│   └── utils/
├── tools/                  # Internal scripts
├── docs/                   # Documentation
└── README.md
```

**Key Principle: Group by feature, not by type.**

❌ Bad (Type-Based):
```
/components/ProfileCard.tsx
/services/profileService.ts
```

✅ Good (Feature-Based):
```
/profile/ProfileCard.tsx
/profile/profileService.ts
```

## What to NEVER Do

- ❌ Create "Misc" or "Other" folders (becomes a dumping ground)
- ❌ Use dates in folder names (unless archiving)
- ❌ Defer organization ("I'll organize later" → never)
- ❌ Over-categorize at start (create as needed)
- ❌ Use ambiguous names ("Work stuff")
- ❌ Forget to archive old projects

## Maintenance Habits

### Daily
- Save in the right place immediately
- Use descriptive names as you create
- Delete what you don't need

### Weekly
- Audit Downloads/Desktop
- Review recent files for correct categorization
- Clean up duplicates

### Monthly
- Archive completed projects
- Update README/index files
- Prune archives

## The Index Pattern

Create `README.md` in each major folder:

```markdown
# Folder Name

## Purpose
What belongs here.

## Naming Convention
How to name files in this folder.

## Key Documents
- [Link to important file](./file.md)
```

This makes navigation instant for collaborators.

## Quick Decision Tree

**Starting a new project?**
→ Create minimal structure, expand as needed

**Project has many phases?**
→ Use numbered folders: `01_`, `02_`, `03_`

**Multiple apps sharing code?**
→ Monorepo with `/apps` and `/packages`

**Personal knowledge?**
→ PARA method (Projects, Areas, Resources, Archives)

**Deep nesting emerging?**
→ Stop. Flatten. Recategorize.
