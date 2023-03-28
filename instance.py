import numpy as np
import random


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
        random.shuffle(self.spectrum)
        K = len(self.spectrum)
        self.matrix = np.zeros((K, K), dtype=int)
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
                        self.matrix[first_word][second_word] = self.l - i
                        break
