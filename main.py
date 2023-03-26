from instance import *


def DFS(instance: Instance, v, used=None, currentPath=[], currentCost=0, currentLength=0):
    if used is None:
        used = set()
        currentLength = instance.l
    if currentLength >= instance.n:
        # print(currentPath)
        return
    used.add(v)
    currentPath.append(v)
    successors = [i for i in range(
        instance.k) if i not in used and instance.get_adj(v, i) > 0]
    successors = sorted(successors, key=lambda s: instance.get_adj(v, s))
    print(instance.spectrum[v])
    for successor in successors[:1]:
        edgeCost = int(instance.get_adj(v, successor))
        print(" "*(currentLength - instance.l + edgeCost), end="")
        DFS(instance, successor, used, currentPath,
            currentCost+edgeCost, currentLength+edgeCost)


if __name__ == '__main__':
    instance = Instance("9.200-40", 209)
    print(instance.matrix)
    DFS(instance, 7)
