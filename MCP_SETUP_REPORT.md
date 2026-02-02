# MCP Configuration Report for Coding Agents

## ✅ Official Notion MCP Server
**URL:** `https://mcp.notion.com/mcp`  
**SSE URL (Legacy):** `https://mcp.notion.com/sse`  
**Auth:** OAuth (automatic browser flow)

---

## Configuration Status

### 1. ✅ Gemini CLI
**Config File:** `C:\Users\acerr\.gemini\settings.json`  
**Status:** CONFIGURED  
**How to add MCP:**
```json
"mcpServers": {
  "notion": {
    "url": "https://mcp.notion.com/mcp"
  }
}
```

### 2. ✅ Amp
**Config File:** `C:\Users\acerr\.config\amp\settings.json`  
**Status:** CONFIGURED  
**How to add MCP:**
```json
"amp.mcpServers": {
  "notion": {
    "url": "https://mcp.notion.com/mcp"
  }
}
```
**CLI Command:** `amp mcp add notion https://mcp.notion.com/mcp`

### 3. ✅ OpenCode
**Config File:** `C:\Users\acerr\opencode.json`  
**Status:** CONFIGURED  
**How to add MCP:**
```json
{
  "mcp": {
    "notion": {
      "type": "remote",
      "url": "https://mcp.notion.com/mcp"
    }
  }
}
```

### 4. ✅ OpenAI Codex CLI
**Config File:** `C:\Users\acerr\.codex\config.toml`  
**Status:** CONFIGURED  
**How to add MCP (TOML format):**
```toml
[mcp_servers.notion]
url = "https://mcp.notion.com/mcp"
```
**CLI Command:** `codex mcp add notion -- npx -y @notionhq/notion-mcp-server` (for local)

### 5. ✅ Factory Droid
**Config File:** `C:\Users\acerr\.factory\mcp.json`  
**Status:** CONFIGURED  
**How to add MCP:**
```json
{
  "mcpServers": {
    "notion": {
      "type": "http",
      "url": "https://mcp.notion.com/mcp"
    }
  }
}
```
**CLI Command:** `droid mcp add notion https://mcp.notion.com/mcp --type http`

### 6. ⚠️ Trae
**Status:** REQUIRES MANUAL UI SETUP  
**How to add MCP:**
1. Open Trae IDE
2. Click Settings icon in chat panel → **MCP**
3. Click **+ Add MCP Servers** → **Configure Manually**
4. Paste:
```json
{
  "notion": {
    "url": "https://mcp.notion.com/mcp"
  }
}
```
5. Click **Confirm**

### 7. ⚠️ Antigravity (Google)
**Status:** REQUIRES MANUAL UI SETUP  
**How to add MCP:**
1. Open Antigravity
2. Open the "..." dropdown at top of agent panel
3. Select **MCP Servers** → **MCP Store**
4. Click **Manage MCP Servers** → **View raw config**
5. Add to `mcp_config.json`:
```json
{
  "notion": {
    "serverUrl": "https://mcp.notion.com/mcp"
  }
}
```
6. Save and refresh

---

## Authentication

After adding the Notion MCP server to any agent, you'll need to complete OAuth authentication:

1. When you first use a Notion tool, a browser window will open
2. Log in to your Notion account
3. Select your workspace
4. Click **Authorize**

The authorization will be cached for future sessions.

---

## Available Notion MCP Tools

| Tool | Description |
|------|-------------|
| `search` | Semantic search across pages and connected apps |
| `get_page` | Retrieve page content |
| `create_page` | Create new pages |
| `update_page` | Update page content (Markdown supported) |
| `query_data_source` | Query databases with filters/sorts |
| `create_data_source` | Create new databases |
| `update_data_source` | Update database properties |
| `retrieve_a_data_source` | Get database metadata/schema |
| `create_comment` | Add comments to pages |
| `get_comments` | Retrieve comments |
| `move_page` | Move pages to different parents |
| `list_data_source_templates` | List templates in a database |
| `get_user` | Get user information |

---

## Quick Reference

| Agent | Config Location | Format |
|-------|-----------------|--------|
| Gemini CLI | `~/.gemini/settings.json` | JSON |
| Amp | `~/.config/amp/settings.json` | JSON |
| OpenCode | `~/opencode.json` or `.opencode/opencode.json` | JSON |
| Codex | `~/.codex/config.toml` | TOML |
| Droid | `~/.factory/mcp.json` | JSON |
| Trae | UI Settings → MCP | JSON |
| Antigravity | UI MCP Store → Raw Config | JSON |

---

Generated: 2026-02-01
