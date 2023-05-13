import cProfile
import math
def getFile(dosya):
    values,weights=[],[]
    txt = open(dosya, "r")
    item=txt.readline().split(" ")
    capacity=int(item[1])
    item=int(item[0])
    for line in txt:
        line=(line.strip()).split(" ")
        values.append(int(line[0]))
        weights.append(int(line[1]))
    maxsel,maxvalue,maxweight=greedyKnapsack(values, weights, capacity,item)
    print("Optimal value değeri: ",maxvalue)
    print("Optimal çözüme dahil edilen itemler: ",end="")
    for i in range(len(maxsel)-1):
        print (maxsel[i],". ve ",end="")
    print(maxsel[len(maxsel)-1]," item")
def greedyKnapsack(values,weights,capacity,item):
    def score(i) :return values[i]/weights[i]
    items = sorted(range(item)  , key=score , reverse = True)
    sel,value,weight,maxsel,maxvalue,maxweight=knapsack(values,weights,capacity,items)
    for i in range(len(items),0,-1):
        items.pop(0)
        sel,value,weight,maxsel,maxvalue,maxweight=knapsack(values,weights,capacity,items,maxsel,maxvalue,maxweight)
    return maxsel, maxvalue, maxweight
def knapsack(values,weights,capacity,items, maxsel=[],maxvalue=0,maxweight=0):
    selweights,sel, value,weight,count = [],[],0,0,0
    for i in items:        
        if weight +weights[i] <= capacity:
            weight += weights[i]
            count+=1
            sel += [i]
            value += values [i]
    if maxvalue<value:
        maxsel=sel
        maxvalue=value
        maxweight=weight
    return sel, value, weight,maxsel,maxvalue,maxweight
getFile('ks_10000_0.txt')
