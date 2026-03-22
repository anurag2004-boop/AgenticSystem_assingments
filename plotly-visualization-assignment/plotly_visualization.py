import pandas as pd
import plotly.express as px
# Create a dataset
data = {
    "Epoch": list(range(1, 11)),
    "Loss": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1]
}
df = pd.DataFrame(data)
# Create a line chart using Plotly Express
fig = px.line(df, x="Epoch", y="Loss", title="Training Loss Over Epochs")
# Add axis labels
fig.update_layout(xaxis_title="Epoch", yaxis_title="Loss")
# Add an annotation to highlight where the loss stabilizes
fig.add_annotation(
    x=8,  # Epoch where loss stabilizes
    y=0.2,  # Loss value at that epoch
    text="Loss Stabilizes",
    showarrow=True,
    arrowhead=1
)
# Show the figure
fig.show()

