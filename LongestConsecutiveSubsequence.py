class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict_min, dict_max = dict(), dict()
        res_max = 0
        for x in nums:
            if dict_min.get(x+1) is None and dict_max.get(x-1) is None:
                if dict_max.get(x) is None and dict_min.get(x) is None:
                    dict_min[x], dict_max[x] = 0, 0
                    res_max = max(res_max, 1)
                continue
            if dict_max.get(x-1) is not None:
                last = dict_max[x - 1]
                if dict_max.get(x) is None or  last + 1 > dict_max.get(x):
                    dict_max.pop(x-1)
                    dict_max[x] = last+1
                    res_max = max(res_max, last + 1 + 1)
                    dict_min[x-1-last] += 1
            if dict_min.get(x+1) is not None:
                last = dict_min[x+1]
                if dict_min.get(x) is None or last + 1 > dict_min.get(x):
                    dict_min.pop(x+1)
                    dict_min[x] = last+1
                    res_max = max(res_max, last + 1 + 1)
                    dict_max[x+1+last] += 1
            if(dict_max.get(x) is not None and dict_min.get(x) is not None):
                left, right = dict_max[x], dict_min[x]
                dict_min.pop(x)
                dict_max.pop(x)
                dict_max[x+right] = right + left
                dict_min[x-left] = left + right
                res_max = max(res_max, left + right + 1)
        return res_max
            
