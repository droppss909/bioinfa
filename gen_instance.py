import random
import math
sequences=[]
oligo=[]


def gen_seq():
    for i in range(509):
        ran=int(random.random()*1000)%4
        if ran==0:
            sequences.append("A")
        elif ran==1:
            sequences.append("C")
        elif ran==2:
            sequences.append("G")
        elif ran==3:
            sequences.append("T")

    print(sequences)

def do_oligometers():
    for i in range(len(sequences)-9):
        tmp=[sequences[i]]
        for x in range(1,10):
            tmp.append(sequences[i+x])
        oligo.append(tmp)
    print(len(oligo),oligo)


def do_negative():
    tab_of_deleted=[]
    l=int(random.random()*10000)%100

    for i in range(l):
        ind=int(random.random()*1000)%len(oligo)
        while (ind in tab_of_deleted) or (ind-1 in tab_of_deleted) or (ind+1 in tab_of_deleted) or ind==0:
            ind=int(random.random()*1000)%len(oligo)
        tab_of_deleted.append(ind)
        oligo.pop(ind)

def gen_10():
    tens=[]
    for _ in range(10):
        i =int(random.random()*10000)%4
        if i==0:
            tens.append("A")
        elif i==1:
            tens.append("C")
        elif i==2:
            tens.append("G")
        elif i==3:
            tens.append("T")
    return tens

def do_positive():
    l=int(random.random()*10000)%100

    for i in range(l):
        oligo.append(gen_10())


def to_file():
    file=open("plik.txt", "w")
    file.write(str(509)+"\n")
    to_add=[]
    for i in oligo:
        tmp="".join(i)
        to_add.append(tmp)
    to_add.sort()
    for x in range(len(to_add)):
        if x==len(to_add)-1:
            file.write(to_add[x])
        else:
            file.write(to_add[x]+"\n")






if __name__=="__main__":
    gen_seq()
    do_oligometers()
    #do_negative()
    do_positive()
    to_file()
