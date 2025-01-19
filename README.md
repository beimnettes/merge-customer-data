Merging Two-Sorted Arrays for Data Analytics
Problem Description
This project involves merging two sorted arrays, customerData1 and customerData2, into a single sorted array in-place. This task simulates a common scenario in data analytics where customer records from multiple databases need to be consolidated efficiently.

Input
customerData1: A sorted array with additional space to accommodate customerData2.
customerData2: A sorted array to be merged into customerData1.
m: Number of valid elements in customerData1.
n: Number of elements in customerData2.
Output
A single sorted array is stored in customerData1.

Example
Input:
Python
Copy
Edit
customerData1 = [101, 104, 107, 0, 0, 0]
m = 3
customerData2 = [102, 105, 108]
n = 3
Output:
python
Copy
Edit
[101, 102, 104, 105, 107, 108]
Approach
The algorithm works by merging the arrays from the back to avoid overwriting existing values in customerData1. It uses three pointers:

i: Tracks the last valid element in customerData1.
j: Tracks the last element in customerData2.
k: Tracks the current position for merging in customerData1.
Steps:
Initialize the pointers i, j, and k.
Compare the elements at customerData1[i] and customerData2[j].
Place the larger element in the position k of customerData1 and move the respective pointer.
Handle any remaining elements in customerData2.
Return the merged array.
Complexity Analysis
Time Complexity: 
𝑂
(
𝑚
+
𝑛
)
O(m+n), where 
𝑚
m and 
𝑛
n are the sizes of the two input arrays.
Each element is processed exactly once.
Space Complexity: 
𝑂
(
1
)
O(1).
The merging is done in-place without using extra memory.
Flowchart
The following flowchart illustrates the algorithm:


How to Run
Clone the repository:
bash
Copy
Edit
git clone https://github.com/your-username/merge-customer-data.git
Navigate to the project directory:
bash
Copy
Edit
cd merge-customer-data
Run the Python script:
bash
Copy
Edit
python merge_customer_data.py
Test Cases
The code has been tested with the following cases:

Normal Cases
Input:

python
Copy
Edit
customerData1 = [101, 104, 107, 0, 0, 0]
m = 3
customerData2 = [102, 105, 108]
n = 3
Output:

python
Copy
Edit
[101, 102, 104, 105, 107, 108]
Input:

python
Copy
Edit
customerData1 = [103, 106, 109, 0, 0, 0]
m = 3
customerData2 = [104, 105, 110]
n = 3
Output:

python
Copy
Edit
[103, 104, 105, 106, 109, 110]
Edge Cases
Empty customerData2:

python
Copy
Edit
customerData1 = [103]
m = 1
customerData2 = []
n = 0
Output:

python
Copy
Edit
[103]
Empty customerData1:

python
Copy
Edit
customerData1 = [0]
m = 0
customerData2 = [101]
n = 1
Output:

python
Copy
Edit
[101]
Both arrays empty:

python
Copy
Edit
customerData1 = []
m = 0
customerData2 = []
n = 0
Output:

python
Copy
Edit
[]
Video Explanation
A detailed explanation of the solution and its implementation is available in the following video: YouTube Video Explanation

Clarifying Questions
What should happen if both arrays are empty?
The merged array should also be empty.
Can the input arrays have duplicate customer IDs?
Yes, duplicates should be preserved in the merged array.
