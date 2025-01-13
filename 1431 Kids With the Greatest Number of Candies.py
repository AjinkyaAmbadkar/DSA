class Solution:
    # 1.find highestCandy in candies
    # 2.loop over candies
    # 3.if current candy + extra candy >= highestCandy Return true
    # 4. Else Return False
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        high = candies[0]

        def highestCandies(candies):
            for i in range(0, len(candies)):
                if candies[i] >= high:
                    high = candies[i]
            return high
        print(high)
        for candy in candies:
            if candy + extraCandies >= high:
                result.append(True)
            else:
                result.append(False)

        return result
