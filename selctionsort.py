def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        min_idx = i
        
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
my_array = [5, 2, 8, 12, 1, 6]
selection_sort(my_array)
print(my_array)
