from instance import *


def improvedGreedy(instance: Instance, sequence=None, cost=0):
    if sequence is None:
        sequence = [random.randint(0, instance.k)]
        cost = instance.l

    while cost < instance.n:
        candidates = [p for p in range(instance.k) if p not in sequence]
        if len(candidates) == 0:
            candidates = range(instance.k)
        predecessor, predecessorCost = choosePredecessor(
            instance, sequence[0], candidates)
        successor, successorCost = chooseSuccessor(
            instance, sequence[-1], candidates)
        if predecessorCost < successorCost:
            sequence.insert(0, predecessor)
            cost += predecessorCost
        else:
            sequence.append(successor)
            cost += successorCost

    return sequence


def choosePredecessor(instance, v, candidates):
    bestOverlap = 0
    bestCandidate = candidates[0]
    for p in candidates:
        for q in [x for x in candidates if x != p]:
            candidateOverlap = instance.matrix[q][p] + instance.matrix[p][v]
            if candidateOverlap > bestOverlap:
                bestCandidate = p
                bestOverlap = candidateOverlap
    return bestCandidate, instance. l - instance.matrix[bestCandidate][v]


def chooseSuccessor(instance, v, candidates):
    bestOverlap = 0
    bestCandidate = candidates[0]
    for p in candidates:
        for q in [x for x in candidates if x != p]:
            candidateOverlap = instance.matrix[v][p] + instance.matrix[p][q]
            if candidateOverlap > bestOverlap:
                bestCandidate = p
                bestOverlap = candidateOverlap
    return bestCandidate, instance.l - instance.matrix[v][bestCandidate]


def reconstructSequence(path, spectrum, matrix):
    sequence = spectrum[path[0]]
    l = len(sequence)
    for i in range(1, len(path)):
        offset = l - int(matrix[path[i-1]][path[i]])
        sequence = sequence + (spectrum[path[i]][-offset:])
    return sequence


if __name__ == '__main__':
    instance = Instance("53.500-200.txt", 509)
    wordSequence = improvedGreedy(instance)
    result = reconstructSequence(
        wordSequence, instance.spectrum, instance.matrix)
    usedWords = len(set(wordSequence))
    print("% Wykorzystanych słów: {}".format(
        usedWords/instance.k))
