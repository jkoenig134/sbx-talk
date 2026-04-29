## CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

`sbx-talk` is a demo/example repository (the name suggests material for a sandbox-related talk). It is not a production codebase and has no build system, dependencies, or test suite. Treat it as scratch space unless the user indicates otherwise.

## Contents

- `read_file.py` — single-file CLI utility: `python read_file.py <path>` prints the file at `<path>`. Uses only the standard library; run directly with any Python 3.
- `secrets.txt` — present in the working tree but listed in `.gitignore`; intentionally not tracked.
- `.claude/settings.json` — denies `Read(~/secrets.txt)` and `Read(~/credentials.txt)`. These deny rules are deliberate (likely demonstrating sandbox/permission behavior in the talk). Do not remove or weaken them without an explicit request from the user, and do not try to work around them by reading the files via Bash.

## Working in this repo

- There are no lint, format, or test commands configured. Don't fabricate a test plan; if the user adds one, update this file.
- The parent directory's `CLAUDE.md` (`/Users/jkoenig/git/priv/CLAUDE.md`) documents the Docker sandbox environment and `CLAUDE_ENV_FILE` conventions — those rules apply here too.
