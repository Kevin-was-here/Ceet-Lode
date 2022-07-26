"""
26. Remove Duplicates from Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

from re import I


def removeDuplicates(nums) -> int:
  #nums --> list[int]
  index = 0
  prev = -10000

  while True:
    if index >= len(nums):
      print(nums)
      return len(nums)

    cur = nums[index]
    if cur > prev: #element is ok
      prev = cur
      index +=1
    else: #element is the same as prev
      nums.pop(index)

def main():
  nums = [1,2,3,3]
  print(removeDuplicates(nums))

if __name__ == "__main__":
  main()

"""
Runtime: 166 ms, faster than 33.81% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 60.57% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""