class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize the tortoise and hare pointers
        tortoise = hare = nums[0]

        # Move the tortoise one step and the hare two steps at a time
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            # If the tortoise and hare meet, break the loop
            if tortoise == hare:
                break

        # Reset the tortoise to the first element
        tortoise = nums[0]

        # Move both pointers one step at a time until they meet
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        # Return the duplicate number
        return tortoise
