from instance import *
import os
import time
import matplotlib.pyplot as plt

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



def show_graph(times, acc):
    x_label=list(range(208,509,100))
    x = list(range(5, 12))
    fig, axs = plt.subplots(2)
    fig.suptitle('instancje z błędami pozytywnymi')
    axs[0].plot(x_label, times)
    axs[1].plot(x_label, acc)
    axs[0].set_ylabel("czas wykonania [s]")

    axs[1].set_ylabel("wykorzystana część słów")
    axs[1].set_xlabel("długośc sekwencji")
    plt.show()

def check_results():
    tab_files=[]
    times=[]
    accuracy=[]
    how_many=[]
    file = open("zapis.txt", "w")
    for i in range(4):
        times.append(0)
        how_many.append(0)
        accuracy.append(0)

    for files in os.walk("D:\pythonProject4\data"):
        tab_files=files[2]

    for data in tab_files:
        print(data)
        if data=="25.500-100.txt" or data=="25.500-200.txt":
            continue
        instance = Instance("D:\pythonProject4\data"+"\\"+data)
        first=time.time()
        wordSequence = improvedGreedy(instance)
        result = reconstructSequence(
            wordSequence, instance.spectrum, instance.matrix)
        usedWords = len(set(wordSequence))
        end=time.time()-first
        file.write(data+" "+str(end)+" "+str(usedWords/instance.k))
        if instance.n==209:
            times[0]=times[0]+end
            how_many[0]+=1
            accuracy[0]+=usedWords/instance.k

        elif instance.n==309:
            times[1] = times[1] + end
            how_many[1] += 1
            accuracy[1] += usedWords / instance.k

        elif instance.n==409:
            times[2] = times[2] + end
            how_many[2] += 1
            accuracy[2] += usedWords / instance.k

        elif instance.n==509:
            times[3] = times[3] + end
            how_many[3] += 1
            accuracy[3] += usedWords / instance.k

    show_graph(times,accuracy)
    file.close()


def check_one():
    data="plik.txt"
    file = open("zapis2.txt", "a")
    instance = Instance("D:\pythonProject4\data" + "\\" + data)
    first = time.time()
    wordSequence = improvedGreedy(instance)
    result = reconstructSequence(
        wordSequence, instance.spectrum, instance.matrix)
    usedWords = len(set(wordSequence))
    end = time.time() - first
    print(data + " " + str(end) + " " + str(usedWords / instance.k))
    file.write(str(instance.n) + " " + str(end) + " " + str(usedWords / instance.k)+"\n")
    file.close()

def graphs():
    times=[]
    acc=[]
    lens=[]
    for x in range(4):
        times.append(0)
        acc.append(0)
        lens.append(0)
    file=open("zapis2.txt","r")
    for line in file:
        line_s=line.split()
        if line_s[0]=="209":
            times[0]+=float(line_s[1])
            lens[0]+=1
            acc[0]+=float(line_s[2])
        elif line_s[0]=="309":
            times[1]+=float(line_s[1])
            lens[1]+=1
            acc[1]+=float(line_s[2])
        elif line_s[0]=="409":
            times[2]+=float(line_s[1])
            lens[2]+=1
            acc[2]+=float(line_s[2])
        elif line_s[0]=="509":
            times[3]+=float(line_s[1])
            lens[3]+=1
            acc[3]+=float(line_s[2])

    for x in range(4):
        times[x]=times[x]/lens[x]
        acc[x]=acc[x]/lens[x]
    show_graph(times,acc)

if __name__ == '__main__':
    # instance = Instance("data\\53.500+200")
    # wordSequence = improvedGreedy(instance)
    # result = reconstructSequence(
    #     wordSequence, instance.spectrum, instance.matrix)
    # usedWords = len(set(wordSequence))
    # print("% Wykorzystanych słów: {}".format(
    #     usedWords / instance.k))
    #check_results()
    check_one()
    #graphs()