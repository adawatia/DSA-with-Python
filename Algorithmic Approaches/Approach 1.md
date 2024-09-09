# Problem Staement:
 ### To solve the problem of finding the missing element from an array of size \( n-1 \) that contains distinct integers from the range 1 to \( n \), you can apply various techniques. Here are some common approaches:

---

### 1. **Sum Formula Method**
   - **Technique**: Use the formula for the sum of the first \( n \) natural numbers \( \text{sum}(1 \text{ to } n) = \frac{n(n+1)}{2} \), then subtract the sum of elements in the array.
   - **Steps**:
     1. Calculate the expected sum of numbers from 1 to \( n \).
     2. Calculate the actual sum of elements in the array.
     3. The missing number is the difference between the expected sum and the actual sum.
   - **Time Complexity**: \( O(n) \)
   - **Space Complexity**: \( O(1) \)

   **Example**:
   ```python
   def find_missing_number_sum_formula(n, arr):
       total_sum = n * (n + 1) // 2
       arr_sum = sum(arr)
       return total_sum - arr_sum
   ```

### 2. **XOR Method**
   - **Technique**: The XOR operator has a useful property: \( a \oplus a = 0 \) and \( a \oplus 0 = a \). By XOR-ing all numbers from 1 to \( n \) and then XOR-ing with all elements in the array, all numbers except the missing one will cancel out.
   - **Steps**:
     1. XOR all numbers from 1 to \( n \).
     2. XOR the result with the XOR of all elements in the array.
     3. The remaining value is the missing number.
   - **Time Complexity**: \( O(n) \)
   - **Space Complexity**: \( O(1) \)

   **Example**:
   ```python
   def find_missing_number_xor(n, arr):
       xor_all = 0
       for i in range(1, n + 1):
           xor_all ^= i
       for num in arr:
           xor_all ^= num
       return xor_all
   ```

### 3. **Hashing (Set or Dictionary)**
   - **Technique**: Use a set to track all numbers from 1 to \( n \). Then, remove elements that are in the array. The remaining number in the set is the missing number.
   - **Steps**:
     1. Create a set of numbers from 1 to \( n \).
     2. Remove elements in the array from the set.
     3. The remaining element is the missing number.
   - **Time Complexity**: \( O(n) \)
   - **Space Complexity**: \( O(n) \)

   **Example**:
   ```python
   def find_missing_number_hashing(n, arr):
       num_set = set(range(1, n + 1))
       for num in arr:
           num_set.remove(num)
       return num_set.pop()
   ```

### 4. **Mathematical Difference Method**
   - **Technique**: This is similar to the sum formula, but instead of directly calculating the sum using a formula, you incrementally subtract the array's values from the expected sum.
   - **Steps**:
     1. Start with the sum of numbers from 1 to \( n \).
     2. Subtract each element in the array from this sum.
     3. The remaining value is the missing number.
   - **Time Complexity**: \( O(n) \)
   - **Space Complexity**: \( O(1) \)

   **Example**:
   ```python
   def find_missing_number_difference(n, arr):
       missing_number = n
       for i in range(1, n):
           missing_number += i - arr[i-1]
       return missing_number
   ```

### 5. **Binary Search (for sorted array)**
   - **Technique**: If the array is sorted, you can apply binary search. The missing element will cause a discrepancy between the expected value at each index and the actual value.
   - **Steps**:
     1. Sort the array (if not already sorted).
     2. Use binary search to identify where the missing element should be.
   - **Time Complexity**: \( O(n \log n) \) for sorting or \( O(\log n) \) if the array is already sorted.
   - **Space Complexity**: \( O(1) \)

   **Example**:
   ```python
   def find_missing_number_binary_search(n, arr):
       arr.sort()
       left, right = 0, n - 2
       while left <= right:
           mid = left + (right - left) // 2
           if arr[mid] == mid + 1:
               left = mid + 1
           else:
               right = mid - 1
       return left + 1
   ```

### 6. **Counting Method**
   - **Technique**: Create a count array or a boolean array to track which elements between 1 to \( n \) appear in the input array.
   - **Steps**:
     1. Create an array of size \( n \) initialized to `False`.
     2. Mark the indices corresponding to the elements in the input array as `True`.
     3. The index which remains `False` corresponds to the missing number.
   - **Time Complexity**: \( O(n) \)
   - **Space Complexity**: \( O(n) \)

   **Example**:
   ```python
   def find_missing_number_count(n, arr):
       count = [False] * n
       for num in arr:
           count[num - 1] = True
       for i in range(n):
           if not count[i]:
               return i + 1
   ```

### Summary
- **Sum Formula Method** and **XOR Method** are both efficient with \( O(n) \) time and \( O(1) \) space.
- **Hashing** or **Counting** can also solve the problem but require \( O(n) \) additional space.
- **Binary Search** is useful if the array is sorted or can be sorted efficiently.

Each of these techniques works well depending on the constraints and whether you need to prioritize time or space efficiency.