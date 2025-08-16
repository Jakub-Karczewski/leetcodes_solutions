class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_unique = {}
        for x in nums:
            nums_unique[x] = nums_unique.get(x, 0) + 1
        arr = []
        for num, count in zip(list(nums_unique.keys()), list(nums_unique.values())):
            arr.append([num, count])
        arr.sort()
        n = len(arr)
        DP = [[0, 0] for _ in range(n)]
        DP[n-1][1] = arr[n-1][1] * arr[n-1][0]
        for i in range(n-2, -1, -1):
            if arr[i+1][0] == arr[i][0] + 1:
                DP[i][0] = max(DP[i+1][1], DP[i+1][0])
                DP[i][1] = DP[i+1][0] + arr[i][1] * arr[i][0]
            else:
                DP[i][1] = max(DP[i+1][1], DP[i+1][0]) + arr[i][1] * arr[i][0]
                DP[i][0] = max(DP[i+1][1], DP[i+1][0])
        return max(DP[0])
