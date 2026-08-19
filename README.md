# Spotify Data Explorer

An interactive, not-very-good-yet Spotify dashboard built with **Plotly Express**. You will use Copilot to explore the codebase, understand how it works, and improve it.

---

## Part 1: Explore the Codebase with Copilot

Before making any changes, use Copilot to understand the project.

### `#` vs `/` — what's the difference?

- **`#` (context)** — attaches something to your message so Copilot has more information to work with. Think of it as _giving Copilot something to read_. Examples: `#codebase`, `#file`, `#selection`.
- **`/` (commands)** — tells Copilot _what to do_. It triggers a specific action. Examples: `/explain`, `/fix`, `/tests`.
- **`@` (agents)** — routes your message to a specialised agent with extra tools or knowledge. Examples: `@github` (search issues/PRs), `@vscode` (editor settings and commands).

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

> **Lab task:** Use Copilot to figure out how to run this project — don't skip ahead!
>
> Open Copilot Chat (`Ctrl+Shift+I`) and ask:
>
> `#codebase what is the entry point of this project? What do I need to install, how do I run it, and what should I see if it is working correctly?`
>
> Copilot will tell you which file to run, what command to use, and what to expect as output. Follow its instructions in the VS Code terminal (`` Ctrl+` ``).
>
> **Hint:** if Copilot mentions a file or command you don't understand, ask a follow-up — for example: _"what does `python src/app.py` actually do?"_

---

## GitHub Copilot Exercises

Use these prompts while working through the codebase. Highlight code and open Copilot Chat, or type in the inline chat (`Ctrl+I`).

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
