import networkx as nx
from string import ascii_lowercase

def edit_dist(w1, w2):
	dist = abs(len(w1) - len(w2))
	for i in range(0, min(len(w1), len(w2))):
		if w1[i] != w2[i]:
			dist = dist + 1
	return dist

def edit_dist2(w1, w2):
	return len(w1) - len(set(w1) & set(w2))

def create_graph(words, part):
	graph = nx.Graph(name="words")
	for word in words:
		graph.add_node(word)
	nodes = graph.nodes()

	for i in range(0, nx.number_of_nodes(graph)):
		for j in range(i+1, nx.number_of_nodes(graph)):
			if part == 1 and edit_dist(nodes[i], nodes[j]) == 1:
				graph.add_edge(nodes[i], nodes[j])
			if part == 2 and edit_dist(nodes[i], nodes[j]) == 1:
				graph.add_edge(nodes[i], nodes[j])
	return graph

def read_words(filename, length):
	f = open(filename, 'r')
	words = set()
	for line in f.readlines():
		line = line.decode()
		if line.startswith('*'):
			continue
		words.add(str(line[0:length]))
	return words


def main():
	words = read_words('words4.txt', 4)
	graph = create_graph(words, part=1)
	print nx.shortest_path(graph, 'cold', 'warm')
	print nx.shortest_path(graph, 'love', 'hate')

	print ""
	words = read_words('words5.txt', 5)
	graph = create_graph(words, part=1)
	print nx.shortest_path(graph, 'chaos', 'order')
	print nx.shortest_path(graph, 'nodes', 'graph')
	print nx.shortest_path(graph, 'moron', 'smart')
	#print nx.shortest_path(graph, 'pound', 'marks')

	print ""
	graph = create_graph(words, part=2)
	print nx.shortest_path(graph, 'chaos', 'order')
	print nx.shortest_path(graph, 'nodes', 'graph')
	print nx.shortest_path(graph, 'moron', 'smart')


if __name__ == '__main__' : main()