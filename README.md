# Spotify Data Explorer

An interactive, not-very-good-yet Spotify dashboard built with **Plotly Express**. You will use Copilot to explore the codebase, understand how it works, and improve it.

---

## Part 1: Explore the Codebase with Copilot

Before making any changes, use Copilot to understand the project.

### GitHub Copilot Commands

- **`#` (context)** — attaches something to your message so Copilot has more information to work with. Think of it as _giving Copilot something to read_. Examples: `#codebase`, `#file`, `#selection`.

- **`/` (commands)** — tells Copilot _what to do_. It triggers a specific action. Examples: `/explain`, `/fix`, `/tests`.

  > **Why use `/explain` instead of just typing "explain this"?** According to the GitHub Copilot docs, slash commands exist to _"avoid writing complex prompts for common scenarios."_ `/explain` is a predefined shortcut — Copilot knows exactly what it means, what context to use (your current selection or open file), and how to format the response. It's more reliable and faster than natural language for tasks you do repeatedly.

You can combine them: `/explain #file:visualization.py` means "explain the contents of this file".

Try these in the **Copilot Chat** panel (`Ctrl+Shift+I`):

| Copilot feature | How to use it                               | Try asking...                                             |
| --------------- | ------------------------------------------- | --------------------------------------------------------- |
| `#codebase`     | Includes your **entire project** as context | `#codebase explain the overall structure of this project` |
| `#file`         | Attaches a specific file as context         | `#file:data_loader.py what does this module do?`          |
| `/explain`      | Explains **selected code** in the editor    | Select a function, then type `/explain` in chat           |
| Inline chat     | Opens chat **at your cursor** in the file   | Press `Ctrl+I` inside any file                            |

**Your first task:** Use `#codebase` to explore the project, then use Copilot to write the **Project Structure** section below. Try this prompt:

> `#codebase generate a markdown project structure tree for this repo with a one-line description for each file`

Then paste Copilot's output into the empty section below.

## Project Structure

<!-- Task: use Copilot to fill this section in — see instructions above -->

---

## Running the App

> **Lab task:** Use Copilot to figure out how to run this project
>
> Open Copilot Chat and ask something like:
>
> `#codebase what is the entry point of this project? What do I need to install, how do I run it, and what should I see if it is working correctly?`
>
> Copilot will tell you which file to run, what command to use, and what to expect as output.
>
> **Also try:** Use `@terminal` to find out what command to run in the terminal.
>
> `@terminal how do I run this project?`

---

## ✅ Checkpoint — Ensure you can run the app and view the dashboard

## Explaining the Codebase

Take some time to explore the code using Copilot. Use `/explain` on selected code, `#file` in Chat, or `Ctrl+I` for inline explanations.

Use Copilot to answer these questions:

**Packages**

- What does each package do, and which part of the app would break without it?

**How the files relate**

- How does `app.py` get access to the functions in `data_loader.py` and `visualization.py`?
- If you wanted to add a new chart, which file would you edit — and what changes would be needed in the others?

## 💬 Checkpoint — Opportunity to discuss with the group any parts of the code that are new to participants.

---

## Part 2: Repository-Wide Copilot Instructions

GitHub Copilot supports a special file — `.github/copilot-instructions.md` — that lets you give Copilot persistent, repository-wide guidance. Any natural language instructions you write there are **automatically included in every Copilot request** made in the context of this repo, without you needing to repeat them in every prompt.

You can verify instructions were applied by expanding the **References** list at the top of any Copilot Chat response and checking that `.github/copilot-instructions.md` appears.

### Task: Set a colour theme

1. Create the file `.github/copilot-instructions.md` in this project (create the `.github` folder if it doesn't exist).

2. Add the following instruction:

   ```markdown
   All Plotly charts in this project must use a pink and purple colour theme.
   Use colours from this palette: #FF69B4 (hot pink), #DA70D6 (orchid), #9B59B6 (purple), #6C3483 (dark purple).
   Never use the default Plotly colour sequence.
   ```

3. Save the file — instructions take effect immediately with no restart required.

### Task: Test that it works

Without specifying any colours in your prompt, ask Copilot to add a new chart. For example, in Copilot Chat:

> `#file:visualization.py add a new function that creates a bar chart showing the top 10 most popular tracks by average popularity`

Then check `visualization.py` — the generated chart should use pink/purple colours without you having to ask. If Copilot didn't follow the instructions, expand the References list in the Chat response and confirm the instructions file is listed.

Use these prompts while working through the codebase. Highlight code and open Copilot Chat.

### Understanding Code

> "Explain what this function does line by line."

> "What does `melt()` do here and why are we using it?"

> "What is `index_col=0` doing in `pd.read_csv`?"

> "Why do we use `os.path.dirname(__file__)` instead of a relative path?"

### Improving Code

> "Add a docstring to this function."

> "Rewrite this groupby expression to be easier to read."

> "How can I add error handling if the CSV file doesn't exist?"

> "Can you suggest a more descriptive variable name for `melted`?"

### Extending the App

> "How do I add a new chart showing the top 10 most popular tracks?"

> "How do I let the user pick which audio features to compare on the bar chart?"

> "How do I add a data table below the charts that shows the filtered results?"

> "How do I cache the `load_data()` call so the CSV is only read once?"
