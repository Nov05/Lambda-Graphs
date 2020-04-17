from collections import defaultdict
# local import
import sys
sys.path.insert(0, 'd:/github/Lambda-Graphs/projects/graph')
from graph import Graph


class WordLadder(object):
    def __init__(self, path='words.txt'):
        self.words = defaultdict(set)
        self.graphs = dict()

        # read words from text file
        with open(path, 'r') as f:
            text = f.read().split('\n')
        for word in text:
            self.words[len(word)].add(word)


    def find_ladder(self, begin_word, end_word):
        length = len(begin_word)
        words = self.words[length]

        # check both words are in the word list
        if begin_word not in words:
            print(f'"{begin_word}" is not in the list.')
            return
        if end_word not in words:
            print(f'"{end_word}" is not in the list.')
            return 

        # search graph
        if length in self.graphs:
            print('graph exists.')
            graph = self.graphs[length]
        else:
            print('building a graph...')
            graph = self.build_graph(length) 
        path = graph.bfs_shortest(begin_word, end_word)
        print(path)


    def build_graph(self, length):
        graph = Graph()
        buckets = defaultdict(list)

        # add vertices and group words
        for word in self.words[length]:
            graph.add_vertex(word)
            for i in range(length):
                buckets[word[:i]+'_'+word[i+1:]].append(word)
        
        # add edges
        for vertices in buckets.values():
            for i in range(len(vertices)):
                for j in range(i+1, len(vertices)):
                    graph.add_edge(vertices[i], vertices[j])
                    graph.add_edge(vertices[j], vertices[i])
        # print(graph.vertices)
        self.graphs[length] = graph
        return graph


# https://bradfieldcs.com/algos/graphs/word-ladder/

if __name__ == '__main__':

    wordladder = WordLadder()
    wordladder.find_ladder('hit', 'cog') 
    wordladder.find_ladder('hit', 'cat') 
    wordladder.find_ladder('sail', 'boat') 
    wordladder.find_ladder('happy', 'hungry') 