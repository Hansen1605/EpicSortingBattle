import random, copy






def insertionSort(items):
    items = items.copy()

    for i in range(1,len(items)):

        x = i-1
        while i < x:
            temp = items[i]
            if items[i] < items[x]:
                items[x] = items[i]
                items[i] = temp
                i =-1
                x =-1
            else:
                break

    return items












if __name__ == '__main__':
    l = list(range(0, 20))
    lb = l.copy()
    for i in range(50):
        random.shuffle(lb)
        ls = insertionSort(l)
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
