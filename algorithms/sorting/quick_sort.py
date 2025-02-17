def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = [arr[0]]
        less = [item for item in arr[1:] if item < pivot[0]]
        greater = [item for item in arr[1:] if item > pivot[0]]

        return qsort(less) + pivot + qsort(greater)

if __name__ == "__main__":
    arr = [3,5,2,1,4]
    sarr = qsort(arr)
    print(f"The array after sorting is {sarr}")