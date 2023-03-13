def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """

    # create and initialize a total_sum to 0
    total_sum = 0
    # loop over each num in nums list
    for num in nums:
        # add the current num to total_sum and store the result to total_sum
        total_sum += num

    # return total_sum
    return total_sum


print("sum_nums returned", sum_nums([1, 2, 3, 4]))
