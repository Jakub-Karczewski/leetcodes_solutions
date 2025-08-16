class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        global_res = 0

        def rect_in_histogram(row_idx, start_index, end_index):  # Complexity O(n^2)
            heights = []
            stack = []
            for k in range(start_index, end_index+1):
                last_idx = -1
                for l in range(row_idx, rows):
                    if matrix[l][k] == "0":
                        last_idx = l
                        break
                if last_idx == -1:
                    heights.append(rows-row_idx)
                else:
                    heights.append(last_idx - row_idx)
            heights.append(0)
            print(heights)
            res = 0
            for h in heights:
                count = 0
                while len(stack) and stack[-1][0] > h:
                    count += stack[-1][1]
                    res = max(res, count * stack[-1][0])
                    stack.pop()
                stack.append([h, count+1])
            return res

        for i in range(rows):
            start_idx = 0
            new_began = False
            for j in range(cols): #complexity O(n^2)
                if matrix[i][j] == "0":
                    if new_began:
                        global_res = max(global_res, rect_in_histogram(i, start_idx, j-1))
                        new_began = False
                else:
                    if not new_began:
                        new_began = True
                        start_idx = j
                    if j == cols-1:
                        global_res = max(global_res, rect_in_histogram(i, start_idx, j))
        return global_res
