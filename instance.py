import numpy as np


class Instance:
    spectrum = []
    matrix = []
    l = 0
    n = 0
    k = 0

    def __init__(self, file_path, n):
        file = open(file_path, "r")
        for line in file:
            self.spectrum.append(line[:-1])
        K = len(self.spectrum)
        self.matrix = np.zeros((K, K))
        self.l = len(self.spectrum[0])
        self.n = n
        self.k = len(self.spectrum)
        self.populate_adjacency_matrix()

    def populate_adjacency_matrix(self):
        for first_word in range(len(self.spectrum)):
            for second_word in range(len(self.spectrum)):
                if first_word == second_word:
                    continue
                for i in range(1, self.l):
                    if self.spectrum[first_word][i:] == self.spectrum[second_word][:-i]:
                        self.matrix[first_word][second_word] = i
                        break

    def get_adj(self, i, j):
        if i < 0 or j < 0:
            return None
        if i >= len(self.matrix) or j >= len(self.matrix[i]):
            return None
        return self.matrix[i][j]
