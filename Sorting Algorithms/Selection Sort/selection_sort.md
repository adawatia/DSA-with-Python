# Selection Sort Algorithm

## Overview

Selection Sort is a simple and intuitive sorting algorithm. It works by repeatedly finding the minimum element from the unsorted portion of the list and moving it to the beginning. This algorithm is not the most efficient for large datasets but is useful for its simplicity and ease of implementation.

## How It Works

The Selection Sort algorithm divides the list into two parts:
1. **Sorted portion**: The portion of the list that has already been sorted.
2. **Unsorted portion**: The portion of the list that remains to be sorted.

The algorithm proceeds as follows:
1. **Find the Minimum**: Scan the unsorted portion to find the minimum element.
2. **Swap**: Swap the found minimum element with the first unsorted element.
3. **Move Boundary**: Move the boundary between the sorted and unsorted portions one element forward.
4. **Repeat**: Repeat the process for the remaining unsorted portion until the entire list is sorted.

## Algorithm

1. Start with the first element as the minimum.
2. Compare this minimum with the rest of the elements.
3. If a smaller element is found, update the minimum.
4. Swap the minimum element found with the first element of the unsorted portion.
5. Move the boundary of the sorted portion one position ahead.
6. Repeat until the list is sorted.

### Example

Consider an array: `[64, 25, 12, 22, 11]`

- **First Pass**:
  - Find the smallest element (11) and swap it with the first element (64).
  - Array becomes: `[11, 25, 12, 22, 64]`

- **Second Pass**:
  - Find the smallest element (12) in the remaining array `[25, 12, 22, 64]` and swap it with the first element of this sub-array (25).
  - Array becomes: `[11, 12, 25, 22, 64]`

- **Third Pass**:
  - Find the smallest element (22) in the remaining array `[25, 22, 64]` and swap it with the first element of this sub-array (25).
  - Array becomes: `[11, 12, 22, 25, 64]`

- **Fourth Pass**:
  - The remaining elements `[25, 64]` are already sorted.

## Time Complexity

- **Best Case**: O(n²)
- **Average Case**: O(n²)
- **Worst Case**: O(n²)

The time complexity of Selection Sort is O(n²) because it involves a nested loop: one to select the minimum element and another to perform the comparisons.

## Space Complexity

- **Space Complexity**: O(1)

Selection Sort is an in-place sorting algorithm, which means it requires only a constant amount of additional space.

## Uses

Selection Sort is primarily used in educational contexts to illustrate sorting algorithms due to its simplicity. It is rarely used in practical applications for large datasets due to its inefficiency compared to more advanced sorting algorithms like Merge Sort or Quick Sort. However, it can be useful in scenarios where memory space is limited, and simplicity is a priority.

## Advantages

- Simple to understand and implement.
- Does not require additional memory beyond the input list (in-place sorting).

## Disadvantages

- Inefficient for large lists (O(n²) time complexity).
- Performance does not improve with partially sorted arrays.

## Conclusion

Selection Sort is a fundamental algorithm in computer science that provides a clear example of sorting techniques. Although not suitable for large datasets, its straightforward approach and in-place nature make it an excellent educational tool.

