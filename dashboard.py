import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Sample data
data = {
    "Model": ["BART", "BERT", "T5"],
    "ROUGE-1": [0.55, 0.45, 0.52],
    "ROUGE-2": [0.30, 0.21, 0.27],
    "ROUGE-L": [0.50, 0.42, 0.48],
    "BLEU": [0.40, 0.33, 0.37],
    "METEOR": [0.35, 0.28, 0.32]
}
df = pd.DataFrame(data)

st.set_page_config(page_title="Model Metrics Dashboard", layout="wide")

st.title("🚀 Model Performance Dashboard")

# Sidebar filters
selected_metrics = st.sidebar.multiselect(
    "Select metrics to display",
    options=list(df.columns[1:]),
    default=list(df.columns[1:])
)

selected_models = st.sidebar.multiselect(
    "Select models to compare",
    options=df["Model"].tolist(),
    default=df["Model"].tolist()
)

filtered_df = df[df["Model"].isin(selected_models)][["Model"] + selected_metrics]

# KPIs summary - best model per metric
st.markdown("### 🔍 Key Performance Indicators")

kpi_cols = st.columns(len(selected_metrics))
for i, metric in enumerate(selected_metrics):
    best_model = filtered_df.loc[filtered_df[metric].idxmax()]["Model"]
    best_score = filtered_df[metric].max()
    kpi_cols[i].metric(label=metric, value=f"{best_score:.3f}", delta=f"Best: {best_model}")

st.markdown("---")

# Layout: Bar charts and Pie charts side by side
bar_col, pie_col = st.columns(2)

# Bar Chart (Altair)
melted = filtered_df.melt(id_vars="Model", var_name="Metric", value_name="Score")
bar_chart = (
    alt.Chart(melted[melted["Metric"].isin(selected_metrics)])
    .mark_bar()
    .encode(
        x=alt.X('Metric:N', title='Metric'),
        y=alt.Y('Score:Q', title='Score'),
        color='Model:N',
        column='Model:N',
        tooltip=['Model', 'Metric', 'Score']
    )
    .properties(width=150, height=300)
)
bar_col.altair_chart(bar_chart, use_container_width=True)

# Pie Charts (Plotly) - one combined interactive pie per selected metric
st.markdown("### 🥧 Metric-wise Distribution (Pie Charts)")
metrics_to_plot = ["ROUGE-1", "ROUGE-2", "BLEU", "METEOR"]  # Choose any 4

# Use containers and columns to separate layout
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        for i in range(0, len(metrics_to_plot), 2):
            metric = metrics_to_plot[i]
            pie_data = df[["Model", metric]].rename(columns={metric: "Score"})
            fig = px.pie(pie_data, values="Score", names="Model", title=metric,
                         color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        for i in range(1, len(metrics_to_plot), 2):
            metric = metrics_to_plot[i]
            pie_data = df[["Model", metric]].rename(columns={metric: "Score"})
            fig = px.pie(pie_data, values="Score", names="Model", title=metric,
                         color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)

# Radar Chart with Plotly (multi-metric comparison per model)
if len(selected_metrics) > 1:
    st.markdown("---")
    st.markdown("### 📈 Radar Chart: Multi-metric Model Comparison")
    
    # Prepare data for radar
    radar_df = filtered_df.set_index("Model")[selected_metrics]
    radar_df = radar_df.reset_index()
    melted_df = df.melt(id_vars=["Model"], var_name="Metric", value_name="Score")
    fig = px.line_polar(melted_df, r='Score', theta='Metric', color='Model',
                    line_close=True, template='plotly_white', markers=True)
    fig.update_traces(fill='toself')
    st.plotly_chart(fig, use_container_width=True)

st.markdown(
        """
        <div style='margin-top: 20px; padding: 10px; background-color: #f0f2f6; border-left: 4px solid #4CAF50; border-radius: 5px;'>
        <span style='font-size: 14px; color: #333;'>
        ℹ️ <em>Note:</em> The ROUGE scores shown above are based on pre-calculated results using fixed evaluation datasets.
        </span>
        </div>
        """,
        unsafe_allow_html=True
)