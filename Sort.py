### Comparison sorts: Bubble Sort, Insertion Sort, Merge Sort, Quick Sort
### Non-comparison sorts: Count Sort, Radix Sort

def bubble_sort(lst, order = 'ascending'):
    '''Bubble Sort'''
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
    '''Insertion Sort'''
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
    '''Merge Sort'''
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
    '''Quick Sort'''
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
    return front + pivot + back


def countSort(lst):
    '''Count Sort'''
    if not lst:
        return []

    maxval = max(lst)

    count = [0] * (maxval + 1)

    for v in lst:
        count[v] += 1

    for i in range(1, maxval + 1):
        count[i] += count[i - 1]

    ans = [0] * len(lst)

    for i in range(len(lst) - 1, -1, -1):
        v = lst[i]
        ans[count[v] - 1] = v
        count[v] -= 1

    return ans


def radixSort(lst):
    '''Radix Sort'''
    max_element = max(lst)

    place = 1
    while max_element // place > 0:
        size = len(lst)
        output = [0] * size
        count = [0] * 10

        for i in range(0, size):
            index = lst[i] // place
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            index = lst[i] // place
            output[count[index % 10] - 1] = lst[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            lst[i] = output[i]

        place *= 10
            




