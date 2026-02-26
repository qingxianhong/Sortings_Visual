import matplotlib.pyplot as plt
import random   #generate permutation of 50 numbers
import time     #random seed
import copy     #copy lists

#random numbers from 1~50
lower_bound = 1
upper_bound = 50

#generate permutation
def random_numbers(a = lower_bound, b = upper_bound):
    random.seed(time.time())
    numbers = list(range(a, b+1))
    random.shuffle(numbers)
    return numbers

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-2):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield

#insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
            yield
        arr[j+1] = key
        yield

#merge sort
def merge_sort(arr,lb=0,ub=upper_bound-1):
    if lb >= ub:
        return
    else:
        mid = (lb+ub)//2
        yield from merge_sort(arr,lb,mid)
        yield from merge_sort(arr,mid+1,ub)
        yield from merge(arr,lb,mid,ub)
    yield

def merge(arr,lb,mid,ub):
    new = []
    i = lb
    j = mid+1
    while(i<=mid and j<=ub):
        if(arr[i]<arr[j]):
            new.append(arr[i])
            i+=1
        else:
            new.append(arr[j])
            j+=1
    num_of_comparisons = len(new)
    if(i>mid):
        while(j<=ub):
            new.append(arr[j])
            j+=1
    else:
        while(i<=mid):
            new.append(arr[i])
            i+=1
    for i,val in enumerate(new):
        arr[lb+i] = val
        if i < num_of_comparisons:
            yield

#quick sort
def quick_sort(arr, l=0, r=upper_bound-1):
    if l>=r:
        return
    x = arr[l]
    j = l
    for i in range(l + 1, r + 1):
        if arr[i] <= x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
        yield
    arr[l], arr[j]= arr[j], arr[l]
    yield
    #pivot is already at the correct position (arr[j])
    yield from quick_sort(arr, l, j-1)
    yield from quick_sort(arr, j + 1, r)
    yield

#heap sort
def heap_sort(arr):
    n = len(arr)
    yield from heapify(arr, len(arr))    
    for i in range(n, 1, -1):
        arr[i-1], arr[0] = arr[0], arr[i-1]
        yield from adjust(arr, 1, i-1)
    yield

def heapify(arr, n):
    for i in range(int(n//2), 0, -1):
        yield from adjust(arr, i, len(arr))

def adjust(arr, i, n):
    child = 2 * i
    item = arr[i-1]
    while child <= n:
        if child < n and arr[child-1] < arr[child]:
            child += 1
        yield
        if item >= arr[child-1]:
            yield
            break
        yield
        arr[(child // 2)-1] = arr[child-1]
        child *= 2
    arr[int(child // 2)-1] = item

## Main function starts from here

title_A = "Bubble sort"
A = random_numbers()
title_B = "Insertion sort"
B = copy.deepcopy(A)
title_C = "Merge sort"
C = copy.deepcopy(A)
title_D = "Quick sort"
D = copy.deepcopy(A)
title_E = "Heap sort"
E = copy.deepcopy(A)

fig, ax = plt.subplots(1,5)
ax[0].set_title(title_A)
ax[1].set_title(title_B)
ax[2].set_title(title_C)
ax[3].set_title(title_D)
ax[4].set_title(title_E)
bar_rects_A = ax[0].bar(range(len(A)), A, align="edge")
bar_rects_B = ax[1].bar(range(len(B)), B, align="edge")
bar_rects_C = ax[2].bar(range(len(C)), C, align="edge")
bar_rects_D = ax[3].bar(range(len(D)), D, align="edge")
bar_rects_E = ax[4].bar(range(len(E)), E, align="edge")

text = [0 for _ in range(5)]
text[0] = ax[0].text(0.02, 0.95, "", transform=ax[0].transAxes)
text[1] = ax[1].text(0.02, 0.95, "", transform=ax[1].transAxes)
text[2] = ax[2].text(0.02, 0.95, "", transform=ax[2].transAxes)
text[3] = ax[3].text(0.02, 0.95, "", transform=ax[3].transAxes)
text[4] = ax[4].text(0.02, 0.95, "", transform=ax[4].transAxes)

#result (completely sorted numbers)
sorted_list = list(range(lower_bound, upper_bound+1))

generator_A = bubble_sort(A)
generator_B = insertion_sort(B)
generator_C = merge_sort(C)
generator_D = quick_sort(D)
generator_E = heap_sort(E)

iteration = 0
def update_fig_A():
    for rect, val in zip(bar_rects_A, A):
        rect.set_height(val)
    text[0].set_text("compare count: {}".format(iteration))

def update_fig_B():
    for rect, val in zip(bar_rects_B, B):
        rect.set_height(val)
    text[1].set_text("compare count: {}".format(iteration))

def update_fig_C():
    for rect, val in zip(bar_rects_C, C):
        rect.set_height(val)
    text[2].set_text("compare count: {}".format(iteration))

def update_fig_D():
    for rect, val in zip(bar_rects_D, D):
        rect.set_height(val)
    text[3].set_text("compare count: {}".format(iteration))

def update_fig_E():
    for rect, val in zip(bar_rects_E, E):
        rect.set_height(val)
    text[4].set_text("compare count: {}".format(iteration))

plt.ion()
plt.show()

# big loop (in each loop, one comparison is performed)
while (not A == sorted_list) or (not B == sorted_list) or (not C == sorted_list) or (not D == sorted_list) or (not E == sorted_list):
    iteration += 1
    if not A == sorted_list:
        next(generator_A)
        update_fig_A()
    if not B == sorted_list:
        next(generator_B)
        update_fig_B()
    if not C == sorted_list:
        next(generator_C)
        update_fig_C()
    if not D == sorted_list:
        next(generator_D)
        update_fig_D()
    if not E == sorted_list:
        next(generator_E)
        update_fig_E()
    fig.canvas.draw()
    time.sleep(0.1)
    fig.canvas.flush_events()

print("Done sorting.")
time.sleep(5)