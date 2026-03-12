# Getting Started with Claude Cowork

Go from zero to running your first autonomous task in under 15 minutes.

**Time required:** 15–30 minutes (setup + first task)
**Tool:** Claude Desktop (Claude Pro account required)

---

## What You'll Get

- Claude Desktop installed with Cowork enabled
- A folder connected and secured
- A completed file organisation task run autonomously by Claude
- A clear understanding of what Cowork can and can't do right now

**Good first tasks for PMs:**
- Organise a folder of user research screenshots or interview recordings
- Rename and file a backlog of invoice documents
- Sort a Downloads folder that's been growing for months

---

## Before You Start

> Prerequisites:
> - A Claude Pro account ($17/month)
> - Mac or Windows (x64)
> - Google Chrome (for web browsing tasks in Step 6)
> - A messy folder you'd like organised — Downloads, Screenshots, or Invoices work well

---

## Step-by-Step

### Step 1: Download and Install Claude Desktop

**Goal:** Get off the web version and onto the desktop app where Cowork lives.

1. Log into [claude.ai](https://claude.ai)
2. Click the download button in the bottom-left corner, or go directly to [claude.ai/downloads](https://claude.ai/downloads)
3. Download Claude Desktop for your operating system (Mac or Windows x64)
4. Install it and log in with your existing Claude account

You'll see the familiar chat window, sidebar, projects, and artifacts — everything works the same as the web version. But you'll now see **Cowork** and **Code** tabs at the top. That's what we're here for.

> After this step: Claude Desktop installed, logged in, and the Cowork tab visible.

---

### Step 2: Open Cowork and Choose Your Working Folder

**Goal:** Give Claude permission to access one specific folder — and only that folder.

1. Click the **Cowork** tab at the top of Claude Desktop
2. Click **Choose a folder** and select a folder you want Claude to work in

Two approaches:

- **Dedicated Cowork folder:** Create a new folder called "Cowork" somewhere on your computer. This becomes Claude's permanent workspace — safe, contained, nothing else gets touched.
- **The folder you actually need help with:** If you have a messy Screenshots or Downloads folder, point Claude straight at it.

3. Confirm when Claude asks "Allow Claude to change files in [folder name]"

> Claude can only access the folders you explicitly give it permission to. It won't access anything else on your hard drive.

4. Select your model in the right-hand panel. **Sonnet 4.5** is the right choice for most tasks. **Opus 4.6** is more powerful but uses more of your usage allowance.

> After this step: Cowork open with a specific folder connected and your model selected.

---

### Step 3: Run Your First File Organisation Task

**Goal:** Your first taste of autonomous AI — Claude organises your files without you lifting a finger.

Give Claude a plain-language task. No special prompt syntax needed:

```
Go through my screenshots, rename them so it's obvious what they are, and then place them in a folder structure that makes them easier to find in the future.
```

Or for a Downloads folder:

```
Go through my Downloads folder. File everything away neatly into categorised folders. Flag any duplicates or files I should review for deletion.
```

What happens next:
- Claude asks for file access confirmation if needed — click **Allow**
- A progress panel on the right shows what Claude is doing in real time
- It scans, catalogues, renames, and reorganises everything
- The whole thing takes roughly 3–5 minutes depending on how many files you have

> After this step: A neatly organised folder with renamed files sorted into logical subfolders.

---

### Step 4: Review What Claude Built

**Goal:** Sanity-check the output before moving on.

1. Open the folder you gave Claude access to
2. Check the new subfolder structure — do the categories make sense?
3. Spot-check a few renamed files — are the names descriptive and accurate?
4. If something's off, tell Claude in the same chat:

```
Actually, move the travel screenshots into a separate folder.
```

or

```
Rename the sports files to include the date.
```

> Pro tip: If you're happy with how Claude organised things, note the structure. You can reference it in future tasks: "Use the same folder structure as last time."

> After this step: Confidence that Cowork actually works — and a tidy folder.

---

### Step 5: Level Up — Create Files and Spreadsheets

**Goal:** Get Claude to create new files, not just organise existing ones.

Example with invoices:

1. Start a new Cowork chat (click the new chat button)
2. Choose the folder containing your invoices
3. Give Claude the task:

```
Go through these invoice files. Rename each one using this format: [Date]-[Vendor Name]-[Amount]. Organise them into monthly folders by invoice date. Then generate a spreadsheet giving me a complete overview of all invoices with auto-calculated totals and a monthly summary.
```

What happens next:
- Claude may ask a few clarifying questions about naming format or spreadsheet layout — answer them as you would with a human assistant
- It processes the files, renames and reorganises them, then generates a CSV or Excel file
- You can preview the spreadsheet inside Cowork, or open it in Excel or Google Sheets

> After this step: Invoices renamed and filed into monthly folders, plus a working spreadsheet tracker.

---

### Step 6: Add Web Browsing with Claude in Chrome

**Goal:** Let Claude browse the web on your behalf.

1. Open Google Chrome
2. Go to the Chrome Web Store and search for the **Claude in Chrome** extension by Anthropic
3. Install the extension
4. Back in Cowork, you can now give tasks that involve web browsing

Example task:

```
Use Chrome to go to my YouTube Studio. Write a report on the current performance of my YouTube channel.
```

What happens next:
- Claude opens Chrome and navigates to the site
- You may get a permission prompt — choose your comfort level (allow for this website / allow always)
- Active Claude-controlled tabs show up highlighted in orange in your browser
- Claude captures the data and compiles a report back in Cowork

> After this step: Claude in Chrome installed and your first web-browsing task completed.

---

### Step 7: Explore Plugins, Connectors, and Projects

**Goal:** Understand what else Cowork can connect to.

Click the **+** button in the bottom-left of the Cowork chat.

**Connectors** — connect Claude directly to your tools:
- Gmail — search and draft emails
- Google Drive — access and work with Drive files
- Notion — read and update your Notion workspace

**Plugins** — add specialised capabilities:
1. Click **Plugins** in the left sidebar
2. Browse Anthropic's built-in plugins: Sales, Marketing, Productivity, Finance, Legal, Data, and more
3. Click to install any that fit your workflow
4. You can also add community skill packs from GitHub (search "Awesome Claude Skills")

**Projects** — use your existing Claude Projects (custom knowledge bases) inside Cowork:
1. Click **Include project** from the + menu
2. Cowork downloads the project files to your computer
3. Now your custom knowledge bases are available inside Cowork tasks

> After this step: A clear picture of the full Cowork ecosystem and at least one connector or plugin installed.

---

## Tips for Best Results

- **Start with file and document management tasks** — they're the easiest way to see immediate value and build confidence
- **Be specific** — you don't need fancy prompts, but clear goals make a big difference
- **Keep the desktop app open** — if you close it, the task stops. Your computer needs to stay awake too
- **Watch your usage** — Cowork burns through credits faster than normal chat because it runs multi-step autonomous tasks. Use Sonnet for everyday tasks, save Opus for heavy work
- **Use dedicated folders** — give Claude access to specific folders rather than your entire Documents directory
- **Batch related work** — do similar tasks in one session rather than spread across several

---

## Current Limitations

> This feature is still a research preview.

- **No memory across sessions** — Claude doesn't remember previous Cowork sessions. Keep files and notes in your working folder for continuity
- **No chat sharing** — you can't send your Cowork sessions to other people
- **Desktop only** — no web or mobile access. You need the desktop app
- **Session persistence** — the app must stay open. Close it and the task stops
- **Uses your computer's resources** — tasks run locally, so your machine is doing the work

---

## What to Try Next

Once you're comfortable with the basics:

- **Research and analysis** — get Claude to synthesise web searches, articles, and your own notes into reports
- **Document creation** — turn messy notes into polished spreadsheets, formatted reports, or slide outlines
- **Data analysis** — drop datasets into a folder and let Claude run analysis and clean your data
- **Chain tasks together** — combine file access + web browsing + connectors for more powerful workflows

---

## Helpful Links

- [Download Claude Desktop](https://claude.ai/downloads)
- [Claude in Chrome Extension — Chrome Web Store](https://chromewebstore.google.com/)

---

*Last updated: March 2026*
