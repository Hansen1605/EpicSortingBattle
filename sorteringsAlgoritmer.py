import random, copy

def insertionSort(items):
    items = items.copy()

    for i in range(1,len(items)):
        x = i-1
        while i > 0:
            if items[i] < items[x]:
                temp = items[x]
                items[x] = items[i]
                items[i] = temp
                i -=1
                x -=1
            else:

                break

    return items

def bubbleSort(items):
    items = items.copy()  # laver kopi af items
    n = len(items)
    swapped = False
    for i in range(n - 1):  # lykken gentager sig selv, sidste tal i listen vender sig om

        for j in range(0, n - i - 1):  # krydser array fra 0 til n-i-1
            if items[j] > items[j + 1]:  # for lykke bytter tal hvis det er større end næste tal
                swapped = True
                items[j], items[j + 1] = items[j + 1], items[j]  # Bytter tal rundt

        if not swapped:
            break
    return items

if __name__ == '__main__':
    l = list(range(0, 20))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = insertionSort(lb)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
        elif ls == l:
            print('Succes! Algoritmen sorterer korrekt.')
            break
    print('blandet: ', lb)
    print('sorteret:', ls)
