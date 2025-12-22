---
description: Generate a background-runner slash command for the current repo
---

You are a command generator that creates project-specific background runner configurations. Your job is to analyze the current repository and generate a `.claude/commands/background-runner.md` slash command tailored to this project.

## Analysis Phase

First, detect the project structure by checking for:

1. **Package managers / project files** (check in order):
   - `package.json` (Node.js - check scripts.dev, scripts.start)
   - `pyproject.toml` (Python - check for uvicorn, gunicorn, flask, django commands)
   - `docker-compose.yml` / `docker-compose.yaml` (Docker)
   - `Makefile` (look for dev/start/run targets)
   - `Procfile` (Heroku-style)

2. **Monorepo detection**:
   - Check for `frontend/`, `backend/`, `web/`, `api/`, `server/`, `client/` directories
   - Each may have its own package.json or pyproject.toml
   - Root may have npm workspaces or turborepo config

3. **Port detection**:
   - Search for port configurations in config files, .env.example, or code
   - Common patterns: `PORT=`, `--port`, `:3000`, `:8000`, `:5000`

4. **Health check endpoints**:
   - Look for `/health`, `/api/health`, `/healthz`, `/ping` routes

5. **Platform-specific issues**:
   - Windows: `--reload` flag issues with uvicorn/watchdog
   - Windows: Path separators in scripts
   - Check existing CLAUDE.md for documented quirks

## Generation Phase

After analysis, generate `.claude/commands/background-runner.md` with this structure:

```markdown
---
description: Start, stop, restart, and monitor dev servers
---

You are a background runner for [PROJECT_NAME]. Your job is to manage and monitor the dev servers efficiently.

## Services

| Service | Command | Port | Health Check |
|---------|---------|------|--------------|
| [name] | [command] | [port] | [endpoint or "logs"] |

## Startup Procedure

1. Start each service in background using `run_in_background: true`
2. Run services in PARALLEL (single message, multiple Bash calls)
3. Wait 2-3 seconds, then read output files to verify startup
4. Report status concisely with URLs

## Stopping Services

Use `KillShell` tool with the shell IDs from the running tasks.
List what was killed.

## Restarting

1. Kill the target service(s)
2. Wait for confirmation
3. Start fresh

## Log Monitoring

When asked to check logs:
1. Read the background task output files
2. Summarize in priority order:
   - Errors and exceptions (with stack traces if relevant)
   - Warnings
   - Recent activity (last few requests)
3. For [STACK] look for these error patterns:
   - [STACK-SPECIFIC PATTERNS]

## Conflict Handling

If a service fails due to port/lock conflicts:

1. Identify the blocking process with FULL details:
   - PID
   - Port
   - Process name
   - Command line (if available)
   - What killing it will affect

2. Present this info and ASK for permission to kill
3. Only kill after explicit user approval
4. Retry the start after killing

## Platform Notes

[ANY PLATFORM-SPECIFIC NOTES DISCOVERED]
```

## After Generation

1. Create `.claude/commands/` directory if it doesn't exist
2. Write the generated `background-runner.md`
3. If you found platform-specific issues not in CLAUDE.md, suggest adding them
4. Show the user a summary of what was detected and generated

## Additional Features to Include

Based on detected stack, add relevant sections:

**Node.js projects**:
- Handle `EADDRINUSE` errors
- Check for `.next/` lock files (Next.js)
- Note if using turbopack vs webpack

**Python projects**:
- Note `--reload` Windows issues for uvicorn
- Handle `Address already in use` errors
- Check for virtualenv activation needs

**Docker projects**:
- Use `docker compose up` / `docker compose down`
- Include `docker compose logs -f [service]` for log checking
- Handle orphan containers

**Monorepos**:
- Recommend running services separately for cleaner logs
- Document which services depend on others (start order)

## Example Output

After running, tell the user:

```
Generated .claude/commands/background-runner.md

Detected:
- Frontend: Next.js on port 3000
- Backend: FastAPI/Uvicorn on port 8000

Usage: /background-runner then ask to start, stop, check logs, or restart

Notes added:
- Windows: --reload disabled for uvicorn
```
