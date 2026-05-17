
#Fonte: GeeksForGeeks (https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/)
def bubble_sort(target:list[str]):
    n = len(target)
    for i in range(n-1):
        swap = False

        for j in range(0, n - i - 1):
            if target[j] > target[j+1]:
                target [j], target[j+1] = target[j+1], target[j]
                swap = True
        
        if not swap: break

#Fonte: GeeksForGeeks (https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/)
def insertion_sort(target:list[str]):
    for i in range(1, len(target)):
        key = target[i]
        j = i - 1

        while j >= 0 and key < target[j]:
            target[j + 1] = target[j]
            j -= 1
        target[j + 1] = key

#Fonte: GeeksForGeeks (https://www.geeksforgeeks.org/dsa/selection-sort-algorithm-2/)
def selection_sort(target:list[str]):
    n = len(target)
    
    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if target[j] < target[min_idx]:
                min_idx = j

        target[i], target[min_idx] = target[min_idx], target[i]

#Fonte: GeeksForGeeks (https://www.geeksforgeeks.org/dsa/shell-sort/)
def shell_sort(target:list[str]):
    n = len(target)

    gap = n // 2
    while gap > 0:
        
        for i in range(gap, n):
            temp = target[i]   
            j = i

            while j >= gap and target[j - gap] > temp:
                target[j] = target[j - gap]
                j -= gap
            
            target[j] = temp
      
        gap //= 2

#=======================heap sort==================================
#Fonte: GeeksForGeeks (https://www.geeksforgeeks.org/dsa/heap-sort/)
def heapify(target:list[str], n:int, i:int):

    largest = i

    l = 2 * i + 1

    r = 2 * i + 2

    if l < n and target[l] > target[largest]:
        largest = l

    if r < n and target[r] > target[largest]:
        largest = r

    if largest != i:
        target[i], target[largest] = target[largest], target[i]

        heapify(target, n, largest)

def heap_sort(target:list[str]):
    n = len(target)

    for i in range(n // 2 - 1, -1, -1):
        heapify(target, n, i)

    for i in range(n - 1, 0, -1):

        target[0], target[i] = target[i], target[0]

        heapify(target, i, 0)

#============merge sort===================
#Fonte: GeeksForGeeks (https://www.geeksforgeeks.org/dsa/merge-sort/)
def merge(target:list[str], left:int, mid:int, right:int):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = target[left + i]
    for j in range(n2):
        R[j] = target[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            target[k] = L[i]
            i += 1
        else:
            target[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        target[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        target[k] = R[j]
        j += 1
        k += 1

def merge_sort(target:list[str], left:int, right:int):
    if left < right:
        mid = (left + right) // 2

        merge_sort(target, left, mid)
        merge_sort(target, mid + 1, right)
        merge(target, left, mid, right)

def true_merge_sort(target:list[str]):
    merge_sort(target, 0, len(target)-1)

#==============quick sort===================
#Fonte: GeeksForGeeks (https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/)
def partition(target:list[str], low:int, high:int):
    
    pivot = target[high]
    
    i = low - 1

    for j in range(low, high):
        if target[j] < pivot:
            i += 1
            swap(target, i, j)

    swap(target, i + 1, high)
    return i + 1

def swap(target:list[str], i, j):
    target[i], target[j] = target[j], target[i]

def quick_sort(target, low, high):
    if low < high:
        
        pi = partition(target, low, high)

        quick_sort(target, low, pi - 1)
        quick_sort(target, pi + 1, high)

def true_quick_sort(target):
    quick_sort(target, 0, len(target)-1);

