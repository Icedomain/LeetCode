#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        flags = [0 for _ in range(numCourses)]
        inverse_adj = [[] for _ in range(numCourses)]
        for second, first in prerequisites:
            inverse_adj[second].append(first)

        res = []
        for i in range(numCourses):
            if self.dfs(i,inverse_adj, flags, res):
                return []
        return res

    def dfs(self, i, inverse_adj, flags, res):
        """
        :param i: 结点的索引
        :param inverse_adj: 逆邻接表，记录的是当前结点的前驱结点的集合
        :param flags: 记录了结点是否被访问过，2 表示当前正在 DFS 这个结点
        :return: 是否有环
        """
        if flags[i] == 2:
            return True
        if flags[i] == 1:
            return False

        flags[i] = 2
        for precursor in inverse_adj[i]:
            if self.dfs(precursor, inverse_adj, flags, res):
                return True

        flags[i] = 1
        res.append(i)
        return False
