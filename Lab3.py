SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(arr, sorting_order):
    # Check if all elements in arr are integers
    if not all(isinstance(x, int) for x in arr):
        return 2  # Return 2 if any element is not an integer

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = []

    elif n >= 10:
        arr_result = 1
    
    elif n == 0:
        arr_result = 0

    return arr_result

def main():
    
    print("Lab 3 - Software Unit Testing with PyTest")

    arr = []
    while True:
        item = input("Enter an item (or type '1' to finish): ")
        if item == "1":  # Stop if the user types '1'
            break
        try:
            arr.append(int(item))  # Convert to integer and append
        except ValueError:
            print("Invalid input, please enter an integer.")

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    if result == 2:
        print("\nError: Array contains non-integer values.")
    else:
        print("\nSorted array in ascending order: ")
        print(result)

    # Sort in descending order
    result = bubble_sort(arr, SORT_DESCENDING)
    if result == 2:
        print("\nError: Array contains non-integer values.")
    else:
        print("Sorted array in descending order: ")
        print(result)

if __name__ == "__main__":
    main()

    #initial commit