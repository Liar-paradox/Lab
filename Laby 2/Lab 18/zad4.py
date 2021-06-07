from heapq import heappush, heappop
import timeit

def heapsort(x):
    heap = []
    for i in x:
        heappush(heap,i)
    size = len(heap)
    return [heappop(heap) for i in range(size)]


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
        array[pivot], array[begin] = array[begin], array[pivot]
        return pivot

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quick_sort(array, begin, pivot - 1)
        _quick_sort(array, pivot + 1, end)

    return _quick_sort(array, begin, end)

x = [9, 2, 3, 0, 13, 14, 11, 10, 3]

print(heapsort(x))

x1 = [9, 2, 3, 0, 13, 14, 11, 10, 3]

quick_sort(x1, 0, len(x1) - 1)
print(x1)

a = '''
def heapsort(a):
    heap = []
    for i in a:
        heappush(heap, i)
    size = len(heap)
    return [heappop(heap) for i in range(size)]
'''

b = '''
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot
def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quick_sort(array, begin, pivot-1)
        _quick_sort(array, pivot+1, end)
    return _quick_sort(array, begin, end)
'''''

a_res = timeit.timeit(stmt=a)
b_res = timeit.timeit(stmt=b)
print(a_res)
print(b_res)

with open('res.txt','w') as f:
    f.writelines(f'a = {str(a_res)}')
    f.writelines(f'b = {str(b_res)}')