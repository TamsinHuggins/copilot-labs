# Spotify Data Explorer

An interactive Spotify dashboard built with **Streamlit** and **Plotly Express**, designed for teaching junior data scientists about Python and GitHub Copilot.

## Project Structure

```
├── data/
│   └── spotify.csv          # Raw dataset
├── src/
│   ├── data_loader.py       # Loads and filters the DataFrame
│   ├── visualization.py     # Plotly chart functions
│   └── app.py               # Streamlit UI entry point
└── requirements.txt
```

## Running the App

```bash
pip install -r requirements.txt
streamlit run src/app.py
```

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
