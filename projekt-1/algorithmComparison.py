import random, time
from quicksort import quicksort, partition
from heapsort import build_max_heap
from mergesort import sort_merge
from insertionsort import insertionSort


if __name__ == "__main__":
    random = [random.randint(1, 400000) for x in range(400000)]
    ascending = list(range(400000))
    descending = list(range(400001, 1, -1))

    # QUICKSORT
    # random

    A = list(random)
    t0 =time.time()
    quicksort(A, 0, 399999)
    t1 = time.time()
    print("Quicksort on random array: ", t1 - t0)

    # sorted in ascending order

    # B = ascending
    # t0 =time.time()
    # quicksort(B, 0, 399999)
    # t1 = time.time()
    # print(t1 - t0)

    # sorted in descending order

    # C = descending
    # t0 =time.time()
    # quicksort(C, 0, 399999)
    # t1 = time.time()
    # print(t1 - t0)

    # HEAPSORT
    # random

    A = list(random)
    t0 =time.time()
    build_max_heap(A)
    t1 = time.time()
    print("\nHeapsort on random array: ", t1 - t0)

    # sorted in ascending order

    B = list(ascending)
    t0 =time.time()
    build_max_heap(B)
    t1 = time.time()
    print("Heapsort on ascending array: ", t1 - t0)

    # sorted in descending order

    C = list(descending)
    t0 =time.time()
    build_max_heap(C)
    t1 = time.time()
    print("Heapsort on descending array: ", t1 - t0)

    # MERGESORT
    #random

    A = list(random)
    t0 =time.time()
    sort_merge(A)
    t1 = time.time()
    print("\nMergesort on random array: ", t1 - t0)

    # sorted in ascending order

    B = list(ascending)
    t0 =time.time()
    sort_merge(B)
    t1 = time.time()
    print("Mergesort on ascending array: ", t1 - t0)

    # sorted in descending order

    C = list(descending)
    t0 =time.time()
    sort_merge(C)
    t1 = time.time()
    print("Mergesort on descending array: ", t1 - t0)

    # INSERTION SORT
    #random

    # A = list(random)
    # t0 =time.time()
    # insertionSort(A)
    # t1 = time.time()
    # print("\nInsertionsort on random array: ", t1 - t0)

    # sorted in ascending order

    B = list(ascending)
    t0 =time.time()
    insertionSort(B)
    t1 = time.time()
    print("Insertionsort on ascending array: ", t1 - t0)

    # sorted in descending order

    # C = list(descending)
    # t0 =time.time()
    # insertionSort(C)
    # t1 = time.time()
    # print("Insertionsort on descending array: ", t1 - t0)