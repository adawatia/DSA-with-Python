---

# Bubble Sort Algorithm

## Overview

Bubble Sort is a simple comparison-based sorting algorithm. It works by repeatedly stepping through the list, comparing adjacent pairs of elements, and swapping them if they are in the wrong order. This process is repeated until the entire list is sorted. Bubble Sort is easy to understand but is inefficient for large datasets due to its time complexity.

### Why is it called Bubble Sort?

The algorithm is called "Bubble Sort" because the larger elements "bubble up" to the top of the list as the algorithm progresses. During each pass through the list, larger elements move towards the end, similar to how bubbles rise to the surface of water.

## How It Works

The Bubble Sort algorithm works by comparing adjacent elements and swapping them if they are in the wrong order. This process is repeated for each element in the list until the list is completely sorted.

Steps:
1. **Compare Adjacent Elements**: Compare the first two elements in the list. If the first element is greater than the second, swap them.
2. **Move Forward**: Move to the next pair of adjacent elements and repeat the comparison and swapping process.
3. **Repeat Passes**: Continue this process for each element in the list, making multiple passes through the list until no more swaps are needed.
4. **Stop Condition**: If no swaps are performed during a pass, the list is already sorted, and the algorithm stops.

## Algorithm

1. Start with the first element.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next element and repeat the comparison.
5. After completing one pass through the list, the largest element will have "bubbled up" to its correct position.
6. Repeat the process for the rest of the list, excluding the sorted elements at the end.
7. Continue until the entire list is sorted.

### Example

Consider an array: `[64, 34, 25, 12, 22, 11, 90]`

- **First Pass**:
  - Compare `64` and `34`, swap them. `[34, 64, 25, 12, 22, 11, 90]`
  - Compare `64` and `25`, swap them. `[34, 25, 64, 12, 22, 11, 90]`
  - Continue this process for the entire array. After the first pass, the largest element `90` is in its correct position.

- **Second Pass**:
  - Start from the beginning again. After this pass, the second largest element will be in its correct position.

- **Subsequent Passes**:
  - Repeat the process until all elements are sorted.

## Time Complexity

- **Best Case**: O(n) - occurs when the list is already sorted. In this case, Bubble Sort can detect this condition and stop early (with an optimized implementation).
- **Average Case**: O(n²)
- **Worst Case**: O(n²)

Bubble Sort has a worst-case time complexity of O(n²) because it requires multiple passes through the list, comparing and potentially swapping elements.

## Space Complexity

- **Space Complexity**: O(1)

Like Selection Sort, Bubble Sort is an in-place sorting algorithm, meaning it requires a constant amount of additional space.

## Uses

Bubble Sort is primarily used for educational purposes to illustrate basic sorting algorithms. Due to its inefficiency, it is rarely used for practical applications involving large datasets. However, it can be used for small datasets or when simplicity is prioritized over performance.

### How to Use Bubble Sort to Find k Greatest Elements

Although Bubble Sort is not efficient for full sorting of large arrays, it can be adapted to find the **k greatest elements** efficiently for small values of `k`. This can be done by performing only the first `k` passes of the Bubble Sort, as these will ensure that the `k` largest elements "bubble up" to the end of the list.

#### Steps to Find k Greatest Elements:
1. Perform Bubble Sort, but only up to the `k` passes through the array.
2. After `k` passes, the last `k` elements in the array will be the `k` greatest elements, though they might not be in sorted order.
3. Optionally, sort the last `k` elements if you need them in ascending or descending order.

#### Example:
Consider the array `[5, 1, 9, 3, 7, 2]` and let's find the 3 greatest elements (`k = 3`).

- **First Pass**:
  - Largest element `9` will "bubble" to the end of the array.

- **Second Pass**:
  - The second-largest element `7` will move to its correct position just before `9`.

- **Third Pass**:
  - The third-largest element `5` will move to its position.

After 3 passes, the largest three elements (`9, 7, 5`) will be in the last three positions of the array.

## Advantages

- Simple to implement and understand.
- The optimized version can stop early if the list is already sorted, making it slightly better in practice than Selection Sort for some cases.

## Disadvantages

- **Inefficient**: Bubble Sort has a time complexity of O(n²), making it impractical for large datasets.
- **Not Adaptive**: Without optimization, Bubble Sort doesn't take advantage of already sorted portions of the array.
- **Not Stable**: While it can be made stable, the basic implementation may not preserve the relative order of equal elements.

## Conclusion

Bubble Sort is one of the simplest sorting algorithms, often used as an introductory example of sorting in computer science education. Although inefficient for large datasets, its simplicity makes it an excellent tool for teaching sorting principles. Its inefficiency and lack of adaptability limit its use in real-world applications, where more efficient algorithms are typically preferred. However, it can be useful for finding the `k` greatest elements with minimal sorting effort.

---