#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        if not matrix or not matrix[0]:
            return 0
        m , n = len(matrix),len(matrix[0])
        # height 的尾部多了一个0,防止递增错误
        height = [0] * (n+1)
        max_area = 0        
        for i in range(m):
            # 计算h
            for j in range(n):
                # 遍历到的每行的h
                height[j] = height[j]+1 if matrix[i][j]=='1' else 0
            # 找出所有h和w的组合 
            # 同84题
            stack = [-1]
            for k in range(n + 1):
                while height[k] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = k - stack[-1] - 1
                    max_area = max(max_area, h * w)                
                stack.append(k)            
        return max_area
        '''
        if not matrix or not matrix[0]:
            return 0
        m , n = len(matrix),len(matrix[0])
        # 申请辅助数组并初始化       
        # 向上、向左、向右能延伸到的最远的地方
        left, right, height = [0]*n, [n]*n, [0]*n
        max_A = 0
        # 从第一行开始遍历
        for i in range(m):
            # 用来记录下标
            cur_left, cur_right = 0, n
            # 从第一个元素开始遍历
            for j in range(n):
                # 如果矩阵中当前坐标为1时， 我们将height对应的下标加一
                # left取cur_left和left[i]中取最大的
                if matrix[i][j] == "1":
                    height[j] = height[j] + 1
                    left[j] = max(left[j], cur_left)
                else: # 否则赋值位0
                    height[j], left[j] = 0, 0
                    cur_left = j+1
            # right数组从末尾开始遍历
            for j in range(n-1, -1, -1): 
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                # 计算到前行为止最大的面积
                max_A = max(max_A,(right[j]-left[j])*height[j])
        return max_A

