def bubble_sort(array):
    n = len(array)  # Get the length of the array
    # Traverse through all elements in the array
    for i in range(n):
        swapped = False  # To check if any swapping occurred during the pass
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):  # Last i elements are already in place
            if array[j] > array[j + 1]:
                # Swap if the element is greater than the next element
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True  # A swap occurred
        # If no elements were swapped during this pass, array is sorted
        if not swapped:
            break  # Exit early if no swapping happened, array is sorted

def main():
    # User input to get the array elements
    user = input("Enter array elements (separated by spaces): ")
    array = list(map(int, user.split()))  # Convert input to a list of integers
    print("Array before sort:", array)
    
    bubble_sort(array)  # Call the sorting function
    
    print("Array after sort:", array)  # Print the sorted array

# Standard Python convention to run the main function
if __name__ == "__main__":
    main()
