# find the sum of subarry of size k=4 
array = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
result = []
def max_sum_subarray(k, arr):
    window_sum = sum(arr[:k])
    result.append(window_sum)
                                    # use this example array = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    for i in range(k, len(arr)):      # range(4, 9)- does this include the 4th index or it starts from the 5th? does it becomes [10, 2 3,1, 0, 20]
        window_sum += arr[i]          # add the value at the array index arr[i] to the existing value in the window sum
        window_sum -= arr[i - k]      # subtract.... 
        result.append(window_sum)
        max_sum = max(result)
    return result, f"The maximum sum is: {max_sum}"



print(max_sum_subarray(k, array))