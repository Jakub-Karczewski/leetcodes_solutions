class Solution:
    def longestValidParentheses(self, s: str) -> int:  # Complexity O(n), first converted every consistent sequence of parenthesis into numbers, then used stack to compress the adjecent closed sequences ( XD ? )
        if len(s) == 0:
            return 0
        arr = []
        stack = []
        prev = s[0]
        temp = 1 if s[0] == "(" else -1
        for x in s[1:]:
            if x == prev:
                temp += (1 if x == "(" else -1 )
            else:
                arr.append(temp)
                temp = (1 if x == "(" else -1 )
            prev = x
        arr.append(temp)

        maxi = 0
        for i in range(len(arr)):
            x = arr[i]
            if x < 0:
                count = 0
                x *= -1
                while len(stack):
                    remain = x - count
                    if remain <= 0 or stack[-1][0] == 0:
                        break

                    if stack[-1][0] > remain:
                        stack[-1][1] += 2 * remain
                        maxi = max(maxi, stack[-1][1])
                        stack[-1][0] -= remain
                        break
                    else:
                        temp, temp_res = stack[-1]
                        count += temp
                        stack.pop()
                        if len(stack):
                            stack[-1][1] += temp * 2 + temp_res
                            maxi = max(maxi, stack[-1][1])
                            if stack[-1][0] == 0 and count < x:
                                maxi = max(maxi, stack[-1][1])
                                stack.pop()
                                break
                        else:
                            maxi = max(maxi, temp * 2 + temp_res)
                            if count < x:
                                break
                            stack.append([0, temp * 2 + temp_res])
                            break
            else:
                stack.append([x, 0])

        return maxi
