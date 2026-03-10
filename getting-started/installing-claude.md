# Install Claude Code - Step 1
In your terminal, copy and paste one of these commands, then press Enter:

# Mac:  
In your terminal, run: `curl -fsSL https://claude.ai/install.sh | bash`
# Windows (PowerShell):
In your terminal, run: `irm https://claude.ai/install.ps1 | iex`

# Check Installation - Step 2
After installation, you will need to check if Claude Code is installed correctly.
In your terminal, run: `claude --version`

If you see a version number, installation succeeded. If you see command not found, completely close your terminal window and open a new one, then try again. 

# Setting up the Zscaler for Claude Code - Step 3

In order to leverage Claude Code from your terminal, you'll need to make sure the app is aware of the ZScaler certificate chain.

1. If you are on a Mac, skip to step 2. If you are on Windows start by download the .PEM file attached to this article, save it somewhere you can reference it, I suggest your Documents folder.
    - https://connect.sentinelone.com/site/b00a4fac-a250-505d-abfd-079c9f50f972/page/64426c1d-c34b-433c-a5f2-db32495d0dc3 here you will find the .PEM file to download for Windows users.
2. Next run the following commands depending on your system.

On Mac, run the following in your terminal, and the target rc file to whatever environment you use (the default is below):
`echo 'export NODE_USE_SYSTEM_CA=1' >> .zshrc`
On Windows, run the following PowerShell command:
`[System.Environment]::SetEnvironmentVariable("NODE_EXTRA_CA_CERTS","C:\users\<USERNAME>\Documents\zscaler_root.pem", "User")`

Launch a new terminal window and launch Claude Code.

# Authentication to Claude Code - Step 4

Type this in your terminal and press Enter:
`claude`

When prompted:
    1. Choose “Claude account with subscription” (NOT Anthropic Console)
    2. Complete browser authentication
    3. Select your preferred terminal text style
    4. After authentication, you’ll see the Claude Code welcome screen.

After authentication, you’ll see the Claude Code welcome screen.

# Health Check - Step 5

Inside Claude Code, type this command:
`/doctor`

This verifies:
- Installation integrity
- Active subscription
- System configuration
- Common issues
- Healthy output shows green checkmarks for all items

# Troubleshooting

# Command not found: claude
Fix:
1. Completely close your terminal window and open a new one
2. If still failing, check PATH configuration:

Mac: Add to `~/.bashrc` or `~/.zshrc`:
    `export PATH=$HOME/.local/bin:$PATH`

Windows: Restart your computer (installer updates PATH automatically)

# Subscription required
 - Verify active Claude Pro/Max subscription at claude.ai
 - Log out and log back in to refresh authentication

# Node version too old
Type this in your terminal:
    `node --version`
Download latest LTS from nodejs.org if below v18.0.0

# Permission denied
Mac:
`sudo curl -fsSL https://claude.ai/install.sh | bash`
Windows: Run PowerShell as Administrator (right-click PowerShell → Run as Administrator)

# Resources
- Official Documentation: https://code.claude.com/docs 
- GitHub Issues: https://github.com/anthropics/claude-code/issues 
- Claude Code community forums