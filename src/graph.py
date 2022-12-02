import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



df_indi = pd.read_csv("src/data/df_individuals.csv", index_col=[0])
df = pd.read_csv("src/data/df_region.csv", index_col=[0])
df_decade = pd.read_csv("src/data/df_region_decade.csv", index_col=[0])


def make_figure(
    min_time=800,
    max_time=1800,
    meta_country="Spain",
    width=1300,
    height=700,
    top_individuals=10,
):

    df_filter = df[(df["period"] >= min_time) & (df["period"] <= max_time)]
    df_filter = df_filter[df_filter["meta_country"] == meta_country].reset_index(
        drop=True
    )
    df_filter["cultural_index"] = (
        df_filter["cultural_index"] - min(df_filter["cultural_index"])
    ) / (max(df_filter["cultural_index"]) - min(df_filter["cultural_index"]))

    df_indi_filter = df_indi[
        (df_indi["period"] >= min_time) & (df_indi["period"] <= max_time)
    ]
    df_indi_filter = df_indi_filter[
        df_indi_filter["meta_country"] == meta_country
    ].reset_index(drop=True)
    df_indi_filter["cultural_index"] = (
        df_indi_filter["cultural_index"] - min(df_indi_filter["cultural_index"])
    ) / (max(df_indi_filter["cultural_index"]) - min(df_indi_filter["cultural_index"]))

    fig_trend = px.line(
        df_filter.sort_values(by=["period"], ascending=[True]),
        x="period",
        y="cultural_index",
        color="meta_country",
    )

    top_indi = df_indi_filter.head(top_individuals).copy()

    top_indi["link"] = "https://www.wikidata.org/wiki/" + top_indi["individual_id"]
    top_indi["hyperlink"] = (
        '<a href="' + top_indi["link"] + '">' + top_indi["individualLabel"] + "</a>"
    )

    fig = px.scatter(
        top_indi, x="productive_year", y="cultural_index", text="hyperlink", log_y=False
    )

    fig = fig.update_traces(textposition="top center")
    fig = fig.update_traces(line_color="red", line_width=5)

    final_fig = go.Figure(data=fig_trend.data + fig.data)
    final_fig = final_fig.update_xaxes(rangeslider_visible=True)

    final_fig = final_fig.update_layout(autosize=False, width=width, height=height,)

    final_fig = final_fig.update_layout(
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        title_text=meta_country,
        title_x=0.5,
    )

    final_fig = final_fig.update_layout(showlegend=False)

    return final_fig
