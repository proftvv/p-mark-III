# P-Mark-III - AI Memory File

**Last Updated**: 2025-12-15  
**Current Version**: 1.0.1  
**Current Phase**: P-1  
**Latest Update**: Mars

---

## Project Purpose & Overview

### Main Goal
Create a web-based business data collection system that:
- Searches for businesses based on keywords/categories
- Searches within a specified radius from a starting location
- Collects: website, phone numbers, social media accounts, and other business information
- Exports data to a well-formatted Excel file
- Runs locally via CMD command
- Requires user authentication (initial user: proftvv / password: 2503)

### Technical Requirements
- Web-based application
- Localhost deployment (initially)
- Simple CMD startup
- Authentication system
- Debug capabilities
- Automated testing

---

## Project Structure

```
P-Mark-III/
├── versions/           # Version control and update history
├── debug/             # Testing and debugging files
├── src/               # Source code
├── docs/              # Documentation
└── memory.md          # This file
```

---

## Versioning System

**Format**: v1.x.x

- **1.x.x**: Stable versions (only change when explicitly requested)
- **x.1.x**: Major updates (changes when P- phase changes)
- **x.x.1**: Bug fixes and hotfixes (auto-increment)

**Update Naming**: Space-themed names (Mars, James Webb, Hubble, etc.)

---

## Phase Structure

### P-1: Foundation Phase
The project is divided into general phases (P-1, P-2, etc.). Each phase has specific goals broken into smaller tasks.

**P-1 Sub-phases** (to be defined):
1. Authentication & Login System
2. Location Search Infrastructure
3. Google Maps/Places API Integration
4. Data Collection Module
5. Excel Export System
6. Web Interface
7. CMD Startup System
8. Debug & Testing Framework

---

## Completed Tasks

### Version 1.0.1 - Mars (2025-12-15)
- ✅ Created project folder structure
- ✅ Initialized version control system (`version-control.json`)
- ✅ Created full update history file (`full-updates.md`)
- ✅ Created memory file for AI context
- ✅ Established documentation infrastructure

---

## Pending Tasks

### Immediate Next Steps
- [ ] Create individual update file for Mars update
- [ ] Create P-1 phases documentation
- [ ] Set up debug infrastructure
- [ ] Initialize git repository
- [ ] Configure GitHub remote and push

### Future Development
- [ ] Implement authentication system
- [ ] Set up Google Maps API integration
- [ ] Build data collection engine
- [ ] Create Excel export functionality
- [ ] Develop web interface
- [ ] Create CMD launcher

---

## Known Issues & Errors

*No issues yet - fresh project*

---

## Important Notes for Future AI Assistants

1. **Always check version-control.json before making changes** to know current version and phase
2. **Update full-updates.md** after every change with detailed information
3. **Create individual update files** in versions/ folder for each prompt/update
4. **Follow versioning rules strictly** - only increment x.x.1 automatically for hotfixes
5. **Use space-themed names** for updates (coordinate with user for naming)
6. **Test everything** - always use debug folder for testing
7. **Auto-push to GitHub** after every prompt: https://github.com/proftvv/p-mark-III

---

## GitHub Repository
**URL**: https://github.com/proftvv/p-mark-III  
**Auto-push**: After every prompt/update

---

## Authentication Credentials (Development)
- **Username**: proftvv
- **Password**: 2503

---

## Technology Stack (Planned)

*To be determined based on development needs:*
- Backend: Node.js/Python/Flask (TBD)
- Frontend: HTML/CSS/JavaScript
- API: Google Maps Places API
- Export: Excel library (openpyxl/xlsx)
- Authentication: Simple session-based auth

---
