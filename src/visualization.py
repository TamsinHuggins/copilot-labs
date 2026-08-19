import plotly.express as px


def plot_popularity_histogram(df):
    fig = px.histogram(
        df,
        x="popularity",
        nbins=30,
        title="Track Popularity Distribution",
        labels={"popularity": "Popularity Score"},
        color_discrete_sequence=["#1DB954"],
    )
    fig.update_xaxes(rangeslider_visible=True)
    return fig


def plot_energy_vs_danceability(df):
    fig = px.scatter(
        df,
        x="energy",
        y="danceability",
        color="track_genre",
        hover_data=["track_name", "artists"],
        title="Energy vs Danceability by Genre",
        opacity=0.6,
    )
    return fig


def plot_avg_audio_features(df):
    features = ["danceability", "energy", "acousticness", "valence", "speechiness"]
    avg = df.groupby("track_genre")[features].mean().reset_index()
    melted = avg.melt(id_vars="track_genre", var_name="feature", value_name="average")
    fig = px.bar(
        melted,
        x="track_genre",
        y="average",
        color="feature",
        barmode="group",
        title="Average Audio Features by Genre",
        labels={"track_genre": "Genre", "average": "Average Value"},
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig
