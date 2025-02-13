elements = [4, 7, 9 , 33, 47, 99, 103, 106, 111, 145, 176, 189]

def binary_search(elements: list, item: int) -> int:
    low = 0
    high = len(elements) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = elements[mid]
        if item == guess:
            return mid
        elif item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    item = int(input("Please enter an element to find in list: "))
    result = binary_search(elements, item)
    if result == -1:
        print(f"The element {item} was not found in the list")
    else:
        print(f"The element {item} was found at position {result} in the list")
