# Jira MCP Integration Setup

This folder contains a configuration file to connect Windsurf to Jira (and Confluence) via an MCP server. Once set up, you can query Jira issues, create tickets, and search Confluence directly from your AI assistant.

---

## Step 1: Install uvx

The MCP server runs via `uvx`, a tool runner that comes bundled with the Python package manager `uv`.

**Install uv (which includes uvx):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

After installation, verify it works:

```bash
uvx --version
```

> On macOS you may need to restart your terminal or run `source ~/.zshrc` for the command to be recognized.

---

## Step 2: Generate your Atlassian API Token

You need an API token to authenticate with Jira and Confluence.

1. Go to [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click **Create API token**
3. Give it a label (e.g. `windsurf-mcp`) and click **Create**
4. Copy the token — you won't be able to see it again

---

## Step 3: Configure the MCP server in Windsurf

1. Open Windsurf and go to **Settings → MCP** (or open `mcp_config.json` directly via the command palette)
2. Copy the contents of `jira-mcp-integration-config.md` into your MCP config
3. Replace the placeholder values:

| Placeholder | What to put here |
|---|---|
| `<email>` | Your Atlassian account email (e.g. `you@yourcompany.com`) |
| `<token>` | The API token you generated in Step 2 |

4. Update the URLs if your company uses a different Atlassian subdomain:

| Field | Example value |
|---|---|
| `JIRA_URL` | `https://yourcompany.atlassian.net` |
| `CONFLUENCE_URL` | `https://yourcompany.atlassian.net/wiki` |

Your final config should look like this:

```json
{
  "mcpServers": {
    "atlassian-mcp-server": {
      "args": [
        "mcp-atlassian"
      ],
      "command": "uvx",
      "disabled": false,
      "env": {
        "CONFLUENCE_API_TOKEN": "your-api-token-here",
        "CONFLUENCE_URL": "https://yourcompany.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "you@yourcompany.com",
        "JIRA_API_TOKEN": "your-api-token-here",
        "JIRA_URL": "https://yourcompany.atlassian.net",
        "JIRA_USERNAME": "you@yourcompany.com"
      }
    }
  }
}
```

5. Save the config and restart Windsurf (or reload the MCP servers from settings)

---

## Step 4: Verify the connection

Once restarted, open a new chat in Windsurf and try:

> "List my open Jira issues"

If the MCP server is connected, you should see results from your Jira instance.

---

## Troubleshooting

**`uvx: command not found`** — uv was not installed or the shell hasn't reloaded. Run `source ~/.zshrc` (or `~/.bash_profile`) and try again.

**Authentication error** — double-check that your email and API token are correct and that the token hasn't expired.

**Wrong issues returned** — confirm your `JIRA_URL` points to the right Atlassian subdomain for your organization.
