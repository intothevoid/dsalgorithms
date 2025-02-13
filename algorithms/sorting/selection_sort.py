def get_smallest_item(arr):
    smallest = arr[0]
    smallest_idx = 0
    for idx in range(1, len(arr)):
        if arr[idx] < smallest:
            smallest = arr[idx]
            smallest_idx = idx
    return smallest_idx

def selection_sort(arr):
    new_arr = []
    for idx in range(len(arr)):
        smallest_idx = get_smallest_item(arr)
        new_arr.append(arr.pop(smallest_idx))
    return new_arr

if __name__ == "__main__":
    us_arr = [99,1,45,2,78,55,23,32,43,11]
    s_arr = selection_sort(us_arr)
    print(f"The sorted array is {s_arr}")