{
  "mcpServers": {
    "atlassian-mcp-server": {
      "args": [
        "mcp-atlassian"
      ],
      "command": "uvx",
      "disabled": false,
      "env": {
        "CONFLUENCE_API_TOKEN": "<token>",
        "CONFLUENCE_URL": "https://sentinelone.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "<email>",
        "JIRA_API_TOKEN": "<token>",
        "JIRA_URL": "https://sentinelone.atlassian.net",
        "JIRA_USERNAME": "<email>"
      }
    }
  }
}