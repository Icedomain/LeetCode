#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 遍历每个人,遍历到过置1
        visited = [0 for _ in range(len(M))]
        # 圈数
        count = 0
        for i in range(len(M)):
            # 等于1表示被别的圈包进去了,等于0表示再开一个圈
            if visited[i] == 0:
                self.dfs(M, visited, i)
                count += 1
        return count
    
    # 判断和i认识的都是哪些人
    def dfs(self, M, visited, i):
        # 全1了
        if sum(visited) == len(M):
            return 
        for j in range(len(M)):
            if j != i and visited[j] == 0 and M[i][j] == 1 :
                visited[j] = 1
                self.dfs(M, visited, j)

