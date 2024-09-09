def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_idx = i
        # Check the rest of the array to find the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    user = input("Enter array elements (separated by spaces): ")
    array = list(map(int, user.split()))  # Convert input to list of integers
    print("Array before sort:", array)
    
    selection_sort(array)  # Sort the array
    
    print("Array after sort:", array)
    
if __name__ == "__main__":
    main()
