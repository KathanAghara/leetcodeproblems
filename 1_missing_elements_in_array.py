"""given an array nums contain n distinct numbers in the range [0, n] return the only number in the range that is missing from the array."""


class solution_array(object):

  def missing_array(self, nums):
    for i in range(len(nums) + 1):
      if i not in nums:
        return i

  # def missing_array(self, nums):
  #   x0=0
  #   x1=0
  #   for i in range(len(nums)+1):
  #       x0=x0^i
  #   for i in range(len(nums)):
  #       x1=x1^nums[i]

  #   return x0^x1
  # def missing_array(self, nums):
  #   n = len(nums)
  #   x1 = 0
  #   for i in range(n):
  #     x1 ^= nums[i]
  #   x2 = 0
  #   for i in range(n + 1):
  #     x2 ^= i
  #   return x1 ^ x2


# nums = [0,3,4,5]
UI = input("enter the number in array: Note: saperated by space: ")
# nums = (UI.split())
nums = [int(num) for num in UI.split()]
Solution = solution_array()
missing_number = Solution.missing_array(nums)
print("The missing number is:", missing_number)
