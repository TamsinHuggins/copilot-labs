import sys
import os
import webbrowser

sys.path.insert(0, os.path.dirname(__file__))

from data_loader import load_data
from visualization import (
    plot_popularity_histogram,
    plot_energy_vs_danceability,
    plot_avg_audio_features,
)


def build_html(figures):
    chart_divs = []
    for i, fig in enumerate(figures):
        # only embed the plotly.js bundle once to keep the file small
        chart_divs.append(fig.to_html(full_html=False, include_plotlyjs=(i == 0)))

    body = "\n".join(f'<div class="chart">{div}</div>' for div in chart_divs)

    return f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Spotify Explorer</title>
  <style>
    body {{ font-family: sans-serif; background: #0e1117; color: #fafafa; padding: 2rem; }}
    h1 {{ color: #1DB954; }}
    p  {{ color: #b3b3b3; }}
    .chart {{ margin-bottom: 3rem; }}
  </style>
</head>
<body>
  <h1>Spotify Data Explorer</h1>
  <p>Tip: click legend entries to show/hide genres. Scroll to zoom, double-click to reset.</p>
  {body}
</body>
</html>"""


def main():
    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df):,} tracks across {df['track_genre'].nunique()} genres.")

    figures = [
        plot_popularity_histogram(df),
        plot_energy_vs_danceability(df),
        plot_avg_audio_features(df),
    ]

    html = build_html(figures)

    output_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "dashboard.html")
    )
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Dashboard saved to: {output_path}")
    webbrowser.open(f"file:///{output_path}")


if __name__ == "__main__":
    main()