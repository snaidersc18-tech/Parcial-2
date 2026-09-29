#Snaider Santiago Castro Ruiz

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

centro = "Snaider(Snicker)"
G.add_node(centro, comunidad="Centro")

familia = ["Yorleny", "Guillermo", "Alba", "Alejandro"]
amigos = ["Sofia(Picaku)", "Andres", "Paula", "Pencue", "JP", "Diego"]
companeros = ["Carlos", "Bayona", "Cerere", "Ana"]

for persona in familia:
    G.add_node(persona, comunidad="Familia")

for persona in amigos:
    G.add_node(persona, comunidad="Amigos")

for persona in companeros:
    G.add_node(persona, comunidad="Companeros")

for persona in familia + amigos + companeros:
    G.add_edge(centro, persona)

G.add_edge("Yorleny", "Guillermo")
G.add_edge("Yorleny", "Alba")
G.add_edge("Alba", "Guillermo")
G.add_edge("Yorleny", "Alejandro")

G.add_edge("Sofia(Picaku)", "Andres")
G.add_edge("Sofia(Picaku)", "Paula")
G.add_edge("Sofia(Picaku)", "Pencue")
G.add_edge("Sofia(Picaku)", "JP")
G.add_edge("Sofia(Picaku)", "Diego")
G.add_edge("Andres", "Paula")
G.add_edge("Andres", "Pencue")
G.add_edge("Andres", "JP")
G.add_edge("Andres", "Diego")
G.add_edge("Paula", "Pencue")
G.add_edge("Paula", "JP")
G.add_edge("Paula", "Diego")
G.add_edge("Pencue", "JP")
G.add_edge("Pencue", "Diego")
G.add_edge("JP", "Diego")

G.add_edge("Carlos", "Bayona")
G.add_edge("Cerere", "Ana")

pos = {
    "Snaider(Snicker)": (0, 0),
    
    "Yorleny": (-2.5, 3.5),
    "Guillermo": (-0.8, 4.2),
    "Alba": (0.8, 4.2),
    "Alejandro": (2.5, 3.5),
    
    "Sofia(Picaku)": (3.5, 2.0),
    "Andres": (4.5, 0.7),
    "Paula": (4.8, -0.8),
    "Pencue": (4.2, -2.3),
    "JP": (3.0, -3.5),
    "Diego": (1.2, -4.2),
    
    "Carlos": (-3.5, -1.0),
    "Bayona": (-4.5, -2.2),
    "Cerere": (-3.2, -3.5),
    "Ana": (-1.5, -4.2)
}

colores = []
for nodo in G.nodes():
    com = G.nodes[nodo]["comunidad"]
    if com == "Centro":
        colores.append("#ff4d4d")
    elif com == "Familia":
        colores.append("#72bcd4")
    elif com == "Amigos":
        colores.append("#7cd97c")
    elif com == "Companeros":
        colores.append("#ffdd53")

plt.figure(figsize=(14, 10))

nx.draw_networkx_nodes(G, pos, node_color=colores, node_size=3400, edgecolors="black", linewidths=1.5)

nx.draw_networkx_edges(G, pos, width=1.2, alpha=0.45, edge_color="gray", arrows=False)

nx.draw_networkx_labels(G, pos, font_size=7.5, font_family="sans-serif", font_weight="bold")

plt.axis("off")
plt.tight_layout()
plt.show()