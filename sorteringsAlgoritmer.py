import random, copy


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
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = bubbleSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)



