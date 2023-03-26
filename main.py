from instance import *


def DFS(instance: Instance, v, used=None, currentPath=[], currentCost=0, currentBestPath=[]):
    if used is None:
        used = set()
    used.add(v)
    currentPath.append(v)
    if currentCost >= instance.n - instance.l:
        return currentPath
    successors = [i for i in range(
        instance.k) if i not in used and instance.get_adj(v, i) > 0]
    successors = sorted(successors, key=lambda s: instance.get_adj(v, s))
    for successor in successors[-1:]:
        edgeCost = instance.l - int(instance.get_adj(v, successor))
        result = DFS(instance, successor, used.copy(), currentPath.copy(),
                     currentCost+edgeCost, currentBestPath.copy())
        if len(result) > len(currentBestPath):
            currentBestPath = result.copy()
    return currentBestPath


def reconstructSequence(path, spectrum, matrix):
    sequence = spectrum[path[0]]
    l = len(sequence)
    globalOffset = 0
    for i in range(1, len(path)):
        offset = l - int(matrix[path[i-1]][path[i]])
        sequence = sequence + (spectrum[path[i]][-offset:])
    return sequence


if __name__ == '__main__':
    instance = Instance("9.200-40", 209)
    longestPath = []
    for i in range(instance.k):
        path = DFS(instance, i, None, [], 0, [])
        print(len(path))
        if len(path) > len(longestPath):
            longestPath = path
    print(len(longestPath))
    sequence = reconstructSequence(
        longestPath, instance.spectrum, instance.matrix)
    print(sequence)
    print(len(sequence))
