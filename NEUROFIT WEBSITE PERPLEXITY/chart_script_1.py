import plotly.graph_objects as go
import json

# Data provided
data = [
    {"region": "London", "average": 100, "min": 50, "max": 150}, 
    {"region": "South East", "average": 60, "min": 40, "max": 80}, 
    {"region": "South West", "average": 45, "min": 30, "max": 60}, 
    {"region": "Midlands", "average": 37, "min": 25, "max": 50}, 
    {"region": "North England", "average": 32, "min": 20, "max": 45}, 
    {"region": "Scotland", "average": 45, "min": 30, "max": 60}, 
    {"region": "Wales/N.Ireland", "average": 37, "min": 25, "max": 50}
]

# Extract data for plotting
regions = []
averages = []
error_minus = []
error_plus = []

for item in data:
    # Abbreviate long region names to stay under 15 characters
    region_name = item["region"]
    if region_name == "Wales/N.Ireland":
        region_name = "Wales/N.Ire"
    
    regions.append(region_name)
    averages.append(item["average"])
    error_minus.append(item["average"] - item["min"])
    error_plus.append(item["max"] - item["average"])

# Create horizontal bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    y=regions,
    x=averages,
    orientation='h',
    error_x=dict(
        type='data',
        symmetric=False,
        array=error_plus,
        arrayminus=error_minus,
        color='rgba(0,0,0,0.3)',
        thickness=2
    ),
    marker_color='#1FB8CD',
    hovertemplate='<b>%{y}</b><br>Avg Price: £%{x}<br>Range: £%{customdata[0]}-£%{customdata[1]}<extra></extra>',
    customdata=[[item["min"], item["max"]] for item in data]
))

# Update layout
fig.update_layout(
    title='Training Prices by UK Region',
    xaxis_title='Avg Price (£)',
    yaxis_title='Region',
    showlegend=False
)

# Update traces
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image('training_prices_chart.png')