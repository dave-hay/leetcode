class Solution:
    """
    dp? could iterate n times
    find the two most common numbers
    ok it is sliding window
    one pass
    """

    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        l = 0

        for r, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            if len(basket) > 2:
                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
        return r - l + 1
