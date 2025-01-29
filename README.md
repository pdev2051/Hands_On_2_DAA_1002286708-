# Arguing the Correctness of Selection Sort
To prove the correctness of Selection Sort, we can use the loop invariant method. This method involves showing that a certain condition holds before and after each iteration of the algorithm.

# Proof by Loop Invariant Method 
At the beginning of each iteration 
𝑖
i of the outer loop, the subarray arr[0] to arr[i-1] contains the smallest 
𝑖
i elements in sorted order.
# Loop Invariant Statement
At the beginning of each iteration i of the outer loop, the subarray arr[0] to arr[i-1] contains the smallest i elements in sorted order.

# Step 1: Initialization (Base Case)
Before the first iteration (𝑖 = 0), the sorted portion of the array is empty.
This trivially satisfies the loop invariant because an empty subarray is always sorted.

# Step 2: Maintenance (Inductive Step)
During each iteration:

The algorithm finds the smallest element in the unsorted portion of the array (arr[i] to arr[n-1]).
It swaps this smallest element with arr[i].
As a result, the subarray arr[0] to arr[i] remains sorted and contains the smallest 
𝑖
+
1
i+1 elements in the correct order.
By induction, if the invariant holds at the start of iteration 
𝑖
i, it will hold for iteration 
𝑖
+
1
i+1 as well.

Step 3: Termination
At the end of the last iteration (
𝑖
=
𝑛
−
1
i=n−1), the entire array is sorted because:

The sorted portion extends to the whole array.
Every element is in its correct position.
Since the loop invariant holds for all iterations, Selection Sort correctly sorts the array.

# Time Complexity Analysis
## Best Case: 
𝑂
(
𝑛
2
)
O(n 
2
 )
## Worst Case: 
𝑂
(
𝑛
2
)
O(n 
2
 )
## Average Case: 
𝑂
(
𝑛
2
)
O(n 
2
 )
Even in the best case (already sorted array), Selection Sort still performs 
𝑂
(
𝑛
2
)
O(n 
2
 ) comparisons because it always scans the entire remaining array to find the minimum.

 # Conclusion
 **Selection Sort is correct** because its loop invariant guarantees that the sorted portion of the array grows correctly.

However, it is inefficient for large arrays due to its 
𝑂
(
𝑛
2
)
O(n 
2
 ) complexity.

It is useful for small datasets or cases where memory swaps are costly (since it makes at most 
𝑛
n swaps).




