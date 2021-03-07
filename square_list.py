# Author: Paul Quaife
# Date: 3/4/2021
# Description: Squares a list of numbers given.

def square_list(nums):
    """definition squares list of numbers given"""
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
