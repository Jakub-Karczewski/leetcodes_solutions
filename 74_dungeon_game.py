class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[inf] * m for _ in range(n)]

        def get_min_health(currCol: int, nextRow: int, nextCol: int) -> float:
            if nextRow >= n or nextCol >= m:
                return inf

            nextVal = dp[nextRow][nextCol] 
            return max(1, nextVal - currCol)

        for row in reversed(range(n)):
            for col in reversed(range(m)):
                currCell = dungeon[row][col]

                right_health = get_min_health(currCell, row, col + 1)
                down_health = get_min_health(currCell, row + 1, col)
                next_health = min(right_health, down_health)

                if next_health != inf:
                    min_health = next_health
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)

                dp[row][col] = min_health

        return dp[0][0]
