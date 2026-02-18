# AI-Employee-Atlas

Personal AI Employee (Atlas) for Bronze layer. Uses a Python watcher to track Inbox & Claude Code to automate planning and execution. Tasks are managed via an Obsidian vault with automated logging in Dashboard.md. This system demonstrates a local-first, autonomous workflow for processing files from /Inbox to /Done following CLAUDE.md rules.

## Features

- **Automated File Watching**: Python watcher monitors `/Inbox` and moves files to `/Needs_Action`
- **AI-Powered Task Processing**: Claude Code (Atlas) processes tasks following the workflow in `CLAUDE.md`
- **Structured Workflow**: Tasks move through `/Needs_Action` → `/Plans` → `/Done` or `/Pending_Approval`
- **Automatic Logging**: All actions logged in `/Logs` with daily entries
- **Dashboard Tracking**: Real-time status updates in `Dashboard.md`

## Directory Structure

```
AI_Employee_Vault/
├── Inbox/              # Drop files here - watcher moves them automatically
├── Needs_Action/       # Tasks waiting to be processed
├── Plans/              # Generated plans for each task
├── Done/               # Completed tasks and plans
├── Pending_Approval/   # Tasks requiring human approval
├── Logs/               # Daily activity logs
├── Skills/             # Reusable agent skills
├── CLAUDE.md           # Master instructions for Atlas
├── Company_Handbook.md # Rules and guidelines
├── Dashboard.md        # Current status and recent activity
└── watcher.py          # Python file watcher script
```

## How It Works

1. **Drop a file** in `/Inbox`
2. **Watcher moves it** to `/Needs_Action`
3. **Atlas reads the task** and creates a plan in `/Plans`
4. **Atlas executes** the plan step-by-step
5. **Sensitive tasks** go to `/Pending_Approval`
6. **Completed tasks** move to `/Done`
7. **Dashboard updates** automatically

## Setup

1. Install Python 3.x
2. Run the watcher: `python watcher.py`
3. Open the vault in Obsidian (optional)
4. Use Claude Code to process tasks

## Usage

Simply drop a text file with your task in the `/Inbox` folder. Atlas will handle the rest according to the workflow defined in `CLAUDE.md`.

## Owner

Syed Izhan (@syedizhan007)
