class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        # Approach: count for where we can plant a flower that should be greater or equal to n.
        # 1. loop over flowerbed
        # 2. check for left if we can plat or not
        # 3. check for right if we can plant or not
        # 4. if we get yes in both then increase count and update in given flowerbed position
        # 5. if count>= n then true or false.
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                leftCheck = False
                rightCheck = False
                if (i == 0 or flowerbed[i-1] == 0):
                    leftCheck = True
                if (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                    rightCheck = True

                if leftCheck and rightCheck:
                    flowerbed[i] = 1
                    count += 1
        if count >= n:
            return True
        return False
