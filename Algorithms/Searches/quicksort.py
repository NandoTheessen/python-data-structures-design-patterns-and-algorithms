from sys import argv
from random import randint


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[-1]
        left = []
        right = []
        for x in range(0, len(nums)-1):
            if nums[x] < pivot:
                left.append(nums[x])
            else:
                right.append(nums[x])
        return quicksort(left) + [pivot] + quicksort(right)


def main(list):
    """executes all functions in this script

    Args:
        list given by the user
    """
    print(quicksort(list))


def random_list():
    """Random List generator
    Returns:
        List with len of 500 including random ints between 0 and 3000"""
    random_list = []
    for i in range(500):
        random_list.append(randint(0, 3000))
    return random_list


if __name__ == '__main__':
    list = list(map(int, argv[1].split(','))) if len(
        argv) == 2 else random_list()
    main(list)
