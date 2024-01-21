import networkx as nx
import matplotlib.pyplot as plt

def kharkiv_metro_graph():

    DG = nx.DiGraph()

    # Creating nodes for Kharkiv metro (stations names)
    red_nodes = ["Kholodna Hora", "Pivdennyy Vokzal", "Tsentralnyy Rynok", "Maydan Konst", "Gagarina Ave", "Sportyvna", "Zavod Malysheva",
                    "Turboatom", "Sport Palace", "Armiyska", "Maselskogo", "Traktornyy Zavod", "Industrial"]
    blue_nodes = ["Istorychnyy Muzey", "University", "Pushkinska", "Kyivska", "Barabashova", "Pavlova", "Studentska", "Heroiv Pratsi"]
    green_nodes = ["Metrobudivnykiv", "Zakhysnykiv Ukrainy", "Beketova", "Derzhprom", "Naukova", "Botanichnyy Sad", "23 Serpnya", "Oleksiivska", "Peremoga"]

    nodes_list = red_nodes + blue_nodes + green_nodes
    DG.add_nodes_from(nodes_list)

    # Creating edges (red, blue, green lines)
    red_edges = [(red_nodes[i], red_nodes[i + 1]) for i in range(len(red_nodes) - 1)]
    red_edges += [(red_nodes[i + 1], red_nodes[i]) for i in range(len(red_nodes) - 1)]

    blue_edges = [(blue_nodes[i], blue_nodes[i + 1]) for i in range(len(blue_nodes) - 1)]
    blue_edges += [(blue_nodes[i + 1], blue_nodes[i]) for i in range(len(blue_nodes) - 1)]

    green_edges = [(green_nodes[i], green_nodes[i + 1]) for i in range(len(green_nodes) - 1)]
    green_edges += [(green_nodes[i + 1], green_nodes[i]) for i in range(len(green_nodes) - 1)]

    # Additional edges for transfer stations
    transfer_edges = [("Maydan Konst", "Istorychnyy Muzey"), ("Istorychnyy Muzey", "Maydan Konst"),
                    ("Derzhprom", "University"), ("University", "Derzhprom"),
                    ("Sportyvna", "Metrobudivnykiv"), ("Metrobudivnykiv", "Sportyvna"),]

    edges_list = red_edges + blue_edges + green_edges + transfer_edges
    DG.add_edges_from(edges_list)

    DG.red_nodes, DG.blue_nodes, DG.green_nodes = red_nodes, blue_nodes, green_nodes
    DG.red_edges, DG.blue_edges, DG.green_edges, DG.transfer_edges = red_edges, blue_edges, green_edges, transfer_edges

    # Adding weights to the edges which reflect the estimated travel time between stations
    DG["Kholodna Hora"]["Pivdennyy Vokzal"]["weight"] = 3
    DG["Pivdennyy Vokzal"]["Tsentralnyy Rynok"]["weight"] = 3
    DG["Tsentralnyy Rynok"]["Maydan Konst"]["weight"] = 3
    DG["Maydan Konst"]["Gagarina Ave"]["weight"] = 2
    DG["Gagarina Ave"]["Sportyvna"]["weight"] = 2
    DG["Sportyvna"]["Zavod Malysheva"]["weight"] = 2
    DG["Zavod Malysheva"]["Turboatom"]["weight"] = 2
    DG["Turboatom"]["Sport Palace"]["weight"] = 2
    DG["Sport Palace"]["Armiyska"]["weight"] = 2
    DG["Armiyska"]["Maselskogo"]["weight"] = 2
    DG["Maselskogo"]["Traktornyy Zavod"]["weight"] = 2
    DG["Traktornyy Zavod"]["Industrial"]["weight"] = 2
    DG["Istorychnyy Muzey"]["University"]["weight"] = 3
    DG["University"]["Pushkinska"]["weight"] = 3
    DG["Pushkinska"]["Kyivska"]["weight"] = 3
    DG["Kyivska"]["Barabashova"]["weight"] = 4
    DG["Barabashova"]["Pavlova"]["weight"] = 3
    DG["Pavlova"]["Studentska"]["weight"] = 3
    DG["Studentska"]["Heroiv Pratsi"]["weight"] = 3
    DG["Metrobudivnykiv"]["Zakhysnykiv Ukrainy"]["weight"] = 3
    DG["Zakhysnykiv Ukrainy"]["Beketova"]["weight"] = 3
    DG["Beketova"]["Derzhprom"]["weight"] = 1
    DG["Derzhprom"]["Naukova"]["weight"] = 3
    DG["Naukova"]["Botanichnyy Sad"]["weight"] = 1
    DG["Botanichnyy Sad"]["23 Serpnya"]["weight"] = 3
    DG["23 Serpnya"]["Oleksiivska"]["weight"] = 3
    DG["Oleksiivska"]["Peremoga"]["weight"] = 3

    return DG

def draw_metro_graph(graph):
    options = {
        "node_color": ["red" if node in graph.red_nodes else "blue" if node in graph.blue_nodes else "green" for node in graph.nodes],
        "edge_color": ["purple" if edge in graph.transfer_edges else "red" if edge in graph.red_edges else "blue" if edge in graph.blue_edges else "green" for edge in graph.edges],
        "style": "solid",
        "node_size": 500,
        "width": [4 if edge in graph.transfer_edges else 1 for edge in graph.edges], 
        "with_labels": True,
        "font_size": 6,
    }

    edge_colors_legend = {
        "purple": "Transfer Station",
        "red": "Red Line",
        "blue": "Blue Line",
        "green": "Green Line",
    }

    legend_labels = []
    for color, label in edge_colors_legend.items():
        legend_labels.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=8, label=label))

    plt.legend(handles=legend_labels, loc="upper right", fontsize=10, frameon=True, fancybox=True, shadow=True)

    layout = nx.kamada_kawai_layout(graph)
    nx.draw(graph, pos=layout, **options)

    plt.title("Kharkiv metro", fontsize=15, fontweight="bold", pad=20, loc="center", fontstyle="italic")
    plt.show()

def find_shortest_path(graph, start_node, target_node):
    start_node = "Kholodna Hora"
    target_node = "Studentska"

    entire_shortest_path = nx.single_source_dijkstra_path(graph, source=start_node)
    entire_shortest_length = nx.single_source_dijkstra_path_length(graph, source=start_node)

    shortest_path = entire_shortest_path[target_node]
    travel_time = entire_shortest_length[target_node]

    return shortest_path, travel_time    

if __name__ == "__main__":

    metro_graph = kharkiv_metro_graph()
    draw_metro_graph(metro_graph)

    start_node = "Kholodna Hora"
    target_node = "Studentska"
    
    shortest_path, travel_time = find_shortest_path(metro_graph, start_node, target_node)

    print(f"\nShortest path from {start_node} to {target_node}: {shortest_path}")
    print(f"\nTravel time: {travel_time} minutes\n")
