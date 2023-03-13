def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # loop the nums list
    for num in nums:
        # check if current num is less than or equal to lowest and highest
        if num >= lowest and num <= highest:
            # if current num passes the condition print the num
            print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 30)
