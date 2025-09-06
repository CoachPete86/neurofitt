import plotly.graph_objects as go
import plotly.io as pio

# Data for the radar chart
data = [
    {"metric": "Executive Function", "effectiveness": 8.5},
    {"metric": "Attention/Focus", "effectiveness": 9.0},
    {"metric": "Impulse Control", "effectiveness": 7.5},
    {"metric": "Working Memory", "effectiveness": 7.0},
    {"metric": "Cognitive Flexibility", "effectiveness": 8.0},
    {"metric": "Motor Skills", "effectiveness": 8.5},
    {"metric": "Mood Regulation", "effectiveness": 8.0},
    {"metric": "Social Behaviour", "effectiveness": 6.5}
]

# Abbreviate metric names to stay within 15 character limit
abbreviated_metrics = [
    "Exec Function",
    "Attention/Focus", 
    "Impulse Control",
    "Working Memory",
    "Cogn Flexiblty",
    "Motor Skills",
    "Mood Regulatn",
    "Social Behav"
]

effectiveness_values = [item["effectiveness"] for item in data]

# Create radar chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=effectiveness_values,
    theta=abbreviated_metrics,
    fill='toself',
    fillcolor='rgba(31, 184, 205, 0.3)',  # #1FB8CD with transparency
    line=dict(color='#1FB8CD', width=3),
    name='Effectiveness'
))

# Update layout
fig.update_layout(
    title="Exercise Effects on ADHD Symptoms",
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10],
            tickmode='linear',
            tick0=0,
            dtick=2
        )
    ),
    showlegend=False
)

# Update traces to clip on axis
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("adhd_exercise_radar_chart.png")