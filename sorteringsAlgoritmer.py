import random, copy


def merge(items, l, m, r):
    #items = items.copy()


    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range (0, n1):
        L[i] = items[l + i]

    for j in range (0, n2):
        R[j] = items[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 & j < n2:
        if L[i] <= R[j]:
            items[k] = L[i]
            i += 1
        else:
            items[k] = R[j]
            j += 1
        k += 1

    print(L, R) # Skriv om til nye sublister i memory

    while i < n1:
        items[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        items[k] = R[j]
        j += 1
        k += 1

def mergeSort(items, l = None, r = None):
    if l == None and r == None:
        l = 0
        r = len(items) - 1
    if l < r:
        m = l + (r - l)//2
        mergeSort(items, l, m)
        mergeSort(items, m + 1, r)
        merge(items, l, m, r)
        #print(items)
        return items






def insertionSort(items):
    items = items.copy() # kopier listen givet
    for i in range(1,len(items)): # Løkke der kører listen igennem der starter ved 1
        x = i-1         # Sætter x til 1 mindre end i som bruges til at tjekke index til venstre for i
        while i > 0:
            if items[i] < items[x]: # Bytter om på index i og x i listen hvis i er mindre end x så længe i > 0
                temp = items[x]
                items[x] = items[i]
                items[i] = temp
                i -= 1
                x -= 1
            else:
                break
    return items

def bubbleSort (items):
    items = items.copy()#laver kopi af items
    n = len(items)
    swapped = False

    for i in range(n-1):#lykken gentager sig selv, sidste tal i listen vender sig oms

        for j in range(0,n-i-1):#krydser array fra 0 til n-i-1

            if items[j] > items[j+1]:#for lykke bytter tal hvis det er større end næste tal
                swapped = True
                items[j], items[j+1] = items[j+1], items[j]#Bytter tal rundt

            if not swapped:
                break
    return items



if __name__ == '__main__':
    l = list(range(0, 3 ))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = mergeSort(lb,0, 4)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
