import pandas as pd
import plotly.graph_objects as go


colors_all= [
                    "rgba(31, 119, 180, 0.8)",
                    "rgba(255, 127, 14, 0.8)",
                    "rgba(44, 160, 44, 0.8)",
                    "rgba(214, 39, 40, 0.8)",
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(188, 189, 34, 0.8)",
                    "rgba(23, 190, 207, 0.8)",
                    "rgba(31, 119, 180, 0.8)",
                    "rgba(255, 127, 14, 0.8)",
                    "rgba(44, 160, 44, 0.8)",
                    "rgba(214, 39, 40, 0.8)",
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(188, 189, 34, 0.8)",
                    "rgba(23, 190, 207, 0.8)",
                    "rgba(31, 119, 180, 0.8)",
                    "rgba(255, 127, 14, 0.8)",
                    "rgba(44, 160, 44, 0.8)",
                    "rgba(214, 39, 40, 0.8)",
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(188, 189, 34, 0.8)",
                    "rgba(23, 190, 207, 0.8)",
                    "rgba(31, 119, 180, 0.8)",
                    "rgba(255, 127, 14, 0.8)",
                    "rgba(44, 160, 44, 0.8)",
                    "rgba(214, 39, 40, 0.8)",
                    "rgba(148, 103, 189, 0.8)",
                    "magenta",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)",
                    "rgba(188, 189, 34, 0.8)",
                    "rgba(23, 190, 207, 0.8)",
                    "rgba(31, 119, 180, 0.8)",
                    "rgba(255, 127, 14, 0.8)",
                    "rgba(44, 160, 44, 0.8)",
                    "rgba(214, 39, 40, 0.8)",
                    "rgba(148, 103, 189, 0.8)",
                    "rgba(140, 86, 75, 0.8)",
                    "rgba(227, 119, 194, 0.8)",
                    "rgba(127, 127, 127, 0.8)"]

colors_unique=[]
for color in colors_all:
    if color not in colors_unique:
        colors_unique.append(color)


print(len(colors_unique))


# Load the data from the Excel file
df = pd.read_excel('bayern-bvb-fichajes-filtro@2.xlsx')

# Filter the data by Club_destino
df_bayern = df[df['Club_destino'] == 'Bayern Múnich']
df_bvb = df[df['Club_destino'] == 'Borussia Dortmund']
colores_nodes=[]
colores_links=[]

for torneo in df_bayern['Torneo']:
    color=f"rgba({(torneo - 2000) * 10 % 256}, {(torneo - 2000) * 15 % 256}, {(torneo - 2000) * 20 % 256}, 0.8)"


# Define the nodes for each club
nodes_bayern = []
for torneo in df_bayern['Torneo'].unique():
    nodes_bayern.append({'label': str(torneo)})
for liga in sorted(df_bayern['Liga_origen'].unique()):  # Sort leagues alphabetically
    nodes_bayern.append({'label': liga})

#print(nodes_bayern)
links_bayern = []
colors_bayern = []
years = sorted(df_bayern['Torneo'].unique())
for i, row in df_bayern.iterrows():
    year_colors = f"rgba({(torneo - 2000) * 10 % 256}, {(torneo - 2000) * 15 % 256}, {(torneo - 2000) * 20 % 256}, 0.8)"
    source_index = nodes_bayern.index({'label': str(row['Torneo'])})
    target_index = nodes_bayern.index({'label': row['Liga_origen']})
    links_bayern.append({'source': source_index, 'target': target_index, 'value': 1})
    colors_bayern.append(year_colors)

#print(colors_bayern)


nodes_bvb = []
for torneo in df_bvb['Torneo'].unique():
    color_bvb= f"rgba({(torneo - 2000) * 10 % 256}, {(torneo - 2000) * 15 % 256}, {(torneo - 2000) * 20 % 256}, 0.8)"
    nodes_bvb.append({'label': str(torneo)})
for liga in sorted(df_bvb['Liga_origen'].unique()):  # Sort leagues alphabetically
    nodes_bvb.append({'label': liga})

# Define the links and colors for each club


links_bvb = []
colors_bvb = []
years = sorted(df_bvb['Torneo'].unique())
#year_colors = f"rgba({(torneo - 2000) * 10 % 256}, {(torneo - 2000) * 15 % 256}, {(torneo - 2000) * 20 % 256}, 0.8)"
for i, row in df_bvb.iterrows():
    year_colors = f"rgba({(torneo - 2000) * 10 % 256}, {(torneo - 2000) * 15 % 256}, {(torneo - 2000) * 20 % 256}, 0.8)"
    source_index = nodes_bvb.index({'label': str(row['Torneo'])})
    target_index = nodes_bvb.index({'label': row['Liga_origen']})
    links_bvb.append({'source': source_index, 'target': target_index, 'value': 1})
    colors_bvb.append(year_colors)

# Create the Sankey graphs for each club

# Sankey graph for Bayern Munich
fig_bayern = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=[node['label'] for node in nodes_bayern],
        color=[colors_bayern]
    ),
    link=dict(
        source=[link['source'] for link in links_bayern],
        target=[link['target'] for link in links_bayern],
        value=[link['value'] for link in links_bayern],
        color=[colors_bayern]
    )
)])


fig_bayern.show()


# Sankey graph for Borussia Dortmund
fig_bvb = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=[node['label'] for node in nodes_bvb],
        color=[colors_bvb]
    ),
    link=dict(
        source=[link['source'] for link in links_bvb],
        target=[link['target'] for link in links_bvb],
        value=[link['value'] for link in links_bvb],
        color=[colors_bvb]
    )
)])

fig_bvb.show()