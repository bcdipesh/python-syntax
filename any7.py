def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # loop over each num in nums list
    for num in nums:
        # check if current num is equal to 7
        if num == 7:
            # if num passes the condition return True
            return True

    # if the code makes it way out of the loop then return False
    return False


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
