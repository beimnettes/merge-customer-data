def merge_customers(customerData1, m, customerData2, n):
    # Initialize pointers for customerData1, customerData2, and the merged array
    i, j, k = m - 1, n - 1, m + n - 1
    
    # Merge arrays from the end to the beginning
    while i >= 0 and j >= 0:
        if customerData1[i] > customerData2[j]:
            customerData1[k] = customerData1[i]
            i -= 1
        else:
            customerData1[k] = customerData2[j]
            j -= 1
        k -= 1
    
    # Copy remaining elements from customerData2, if any
    while j >= 0:
        customerData1[k] = customerData2[j]
        j -= 1
        k -= 1

# Unit tests
def test_merge_customers():
    # Normal case 1
    customerData1 = [101, 104, 107, 0, 0, 0]
    m = 3
    customerData2 = [102, 105, 108]
    n = 3
    merge_customers(customerData1, m, customerData2, n)
    assert customerData1 == [101, 102, 104, 105, 107, 108], "Test Case 1 Failed"

    # Normal case 2
    customerData1 = [103, 106, 109, 0, 0, 0]
    m = 3
    customerData2 = [104, 105, 110]
    n = 3
    merge_customers(customerData1, m, customerData2, n)
    assert customerData1 == [103, 104, 105, 106, 109, 110], "Test Case 2 Failed"

    # Edge case: Empty customerData2
    customerData1 = [103]
    m = 1
    customerData2 = []
    n = 0
    merge_customers(customerData1, m, customerData2, n)
    assert customerData1 == [103], "Edge Case 1 Failed"

    # Edge case: Empty customerData1
    customerData1 = [0]
    m = 0
    customerData2 = [101]
    n = 1
    merge_customers(customerData1, m, customerData2, n)
    assert customerData1 == [101], "Edge Case 2 Failed"

    # Edge case: Both arrays empty
    customerData1 = []
    m = 0
    customerData2 = []
    n = 0
    merge_customers(customerData1, m, customerData2, n)
    assert customerData1 == [], "Edge Case 3 Failed"

    print("All test cases passed!")

# Run the tests
if __name__ == "__main__":
    print("Running test cases...")
    test_merge_customers()
