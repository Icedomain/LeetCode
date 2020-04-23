#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = [[] for _ in range(numCourses)]

        flags = [0 for _ in range(numCourses)]
        #(cur,pre)对
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not self.dfs(i, adjacency, flags): 
                return False
        return True

    def dfs(self,i, adjacency, flags):
        # flag标志
        # 0:未访问 
        # 1:已被当前节点启动的访问
        #-1:已被其他节点启动的访问
        if flags[i] == -1: 
            return True
        if flags[i] == 1: 
            return False
        flags[i] = 1
        for j in adjacency[i]:
            if not self.dfs(j, adjacency, flags): 
                return False
        flags[i] = -1
        return True
