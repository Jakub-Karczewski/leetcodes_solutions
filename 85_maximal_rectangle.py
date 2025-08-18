class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        global_res = 0
        
        one_tower = [[0 for _ in range(cols)] for _ in range(rows)]
        for j in range(cols): # Complexity O(n^2)
            count = 0
            for i in range(rows):
                if matrix[i][j] == "0" and count > 0:
                    temp_i = i-1
                    for k in range(temp_i, -1, -1):
                        if matrix[k][j] == "0":
                            break
                        one_tower[k][j] = count
                        count -= 1
                elif matrix[i][j] == "1":
                    count += 1
            if count > 0:
                for k in range(rows-1, -1, -1):
                    if matrix[k][j] == "0":
                        break
                    one_tower[k][j] = count
                    count -= 1

        def rect_in_histogram(row_idx, start_index, end_index):  # Complexity O(n)
            heights = []
            stack = []
            for k in range(start_index, end_index+1):
                heights.append(one_tower[row_idx][k])
            heights.append(0)
            res = 0
            for h in heights:
                count = 0
                while len(stack) and stack[-1][0] > h:
                    count += stack[-1][1]
                    res = max(res, count * stack[-1][0])
                    stack.pop()
                stack.append([h, count+1])
            return res

        for i in range(rows): # complexity O(n^2)
            start_idx = 0
            new_began = False
            for j in range(cols):
                if matrix[i][j] == "0":
                    if new_began:
                        global_res = max(global_res, rect_in_histogram(i, start_idx, j-1)) # Complexity O(n)
                        new_began = False
                else:
                    if not new_began:
                        new_began = True
                        start_idx = j
                    if j == cols-1:
                        global_res = max(global_res, rect_in_histogram(i, start_idx, j))
        
        return global_res
