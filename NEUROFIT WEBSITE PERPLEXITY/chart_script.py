import plotly.express as px
import pandas as pd

# Create the data
data = [
    {"year": "2024", "value": 2.8, "status": "actual"}, 
    {"year": "2025", "value": 2.9, "status": "projected"}, 
    {"year": "2026", "value": 3.0, "status": "projected"}, 
    {"year": "2027", "value": 3.2, "status": "projected"}, 
    {"year": "2028", "value": 3.4, "status": "projected"}, 
    {"year": "2029", "value": 3.6, "status": "projected"}, 
    {"year": "2030", "value": 3.8, "status": "projected"}, 
    {"year": "2031", "value": 4.0, "status": "projected"}, 
    {"year": "2032", "value": 4.2, "status": "projected"}, 
    {"year": "2033", "value": 4.5, "status": "projected"}
]

df = pd.DataFrame(data)

# Create the bar chart
fig = px.bar(df, x='year', y='value', color='status',
             title='UK Corporate Wellness Market CAGR 4.7%',
             color_discrete_map={'actual': '#1FB8CD', 'projected': '#DB4545'})

# Update layout
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Value (£B)",
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update traces
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image('uk_wellness_market_chart.png')