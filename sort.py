def BubbleSort(ar):
    n = len(ar)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if ar[j] > ar[j + 1]:
                ar[j], ar[j + 1] = ar[j + 1], ar[j] 

def InsertionSort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        j = i-1
        while j >= 0 and key < ar[j]:
                ar[j + 1] = ar[j]
                j -= 1
        ar[j + 1] = key

def SelectionSort(ar):
    for i in range(len(ar)):
        min_idx = i
        for j in range(i+1, len(ar)):
            if ar[min_idx] > ar[j]:
                min_idx = j
        ar[i], ar[min_idx] = ar[min_idx], ar[i]
 
def MergeSort(ar):
    if len(ar) > 1:
        mid = len(ar)//2
        L = ar[:mid]
        R = ar[mid:]

        MergeSort(L)
        MergeSort(R)
  
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                ar[k] = L[i]
                i += 1
            else:
                ar[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            ar[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            ar[k] = R[j]
            j += 1
            k += 1

def partition(start, end, array):
    
    pivot_index = start 
    pivot = array[pivot_index]
      
    while start < end:
          
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        while array[end] > pivot:
            end -= 1
          
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    return end
      
def QuickSort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
          
        QuickSort(start, p - 1, array)
        QuickSort(p + 1, end, array)

def countSort(arr):
    output = [0 for i in range(len(arr))]
 
    count = [0 for i in range(256)]
 
    ans = ["" for _ in arr]
 
    for i in arr:
        count[ord(i)] += 1
 
    for i in range(256):
        count[i] += count[i-1]
 
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
 
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

def radixSort(arr):
 
    max1 = max(arr)
    exp = 1
    while max1 / exp > 1:
        countSort(arr, exp)
        exp *= 10

def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    
             
def bucketSort(x):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])
         
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
         
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
