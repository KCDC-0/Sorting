### Bubble Sort, Insertion Sort, Merge Sort, Quick Sort

def bubble_sort(lst, order = 'ascending'):
    count = 1
    while count != len(lst):
        count = 1
        for i in range(len(lst)):
            if i == 0:
                a = 1
            else:
                if lst[i] < lst[i - 1]:
                    lst[i], lst[i - 1] = lst[i - 1], lst[i]
                else:
                    count += 1
    o = 0
    if order == 'descending':
        lst.reverse()
        o = 1
    if type(lst[0]) == str:
        maxlen = 0
        for i in lst:
            if len(i) > maxlen:
                maxlen = len(i)
        lis =[]
        for i in range(maxlen + 1):
            if o == 1:
                for e in lst:
                    if len(e) == (maxlen + 1) - i:
                        lis.append(e)
            else:
                for e in lst:
                    if len(e) == i:
                        lis.append(e)
        lst = lis
    return lst

def insertion_sort(lst, order = 'ascending'):
    ls = []
    ls.append(lst[0])
    lst = lst[1:]
    for i in range(len(lst)):
        done = 0
        for e in range(len(ls)):
            if lst[i] <= ls[e] and done == 0:
                ls.insert(e, lst[i])
                done = 1
            else:
                if e == len(ls) - 1 and done == 0:
                    ls.append(lst[i])
                    done = 1
    if order == 'descending':
        ls.reverse()
    return ls

def mergeSort(lst, order = 'ascending'):
    res = []
    if len(lst) > 1:
        front = mergeSort(lst[:len(lst) // 2])
        back = mergeSort(lst[len(lst) // 2:])
    elif len(lst) == 1:
        return lst
    while len(front) != 0 or len(back) != 0:
        if len(front) == 0:
            res.append(back[0])
            back.remove(back[0])
        elif len(back) == 0:
            res.append(front[0])
            front.remove(front[0])
        elif front[0] > back[0]:
            res.append(back[0])
            back.remove(back[0])
        else:
            res.append(front[0])
            front.remove(front[0])
    if order == 'descending':
        res.reverse()
    return res

def quickSort(lst):
    res = []
    if len(lst) == 1 or len(lst) == 0:
        return lst
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            lst.reverse()
        return lst
    pdecide = [lst[0], lst[len(lst) // 2], lst[-1]]
    pdecide.remove(max(pdecide))
    pdecide.remove(min(pdecide))
    pivot = pdecide[0]
    lst.remove(pivot)
    fro =[]
    bac = []
    for i in range(len(lst)):
        if lst[i] < pivot:
            fro.append(lst[i])
        else:
            bac.append(lst[i])
    front = quickSort(fro)
    back = quickSort(bac)
    front.append(pivot)
    return front + back
            




