#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        # 方法一
        uf = []
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    x = self.findIndex(i,uf)
                    y = self.findIndex(j,uf)
                    # 两个都不在里面
                    if (x == -1) and (y == -1):
                        uf.append(set([i, j]))
                    # y在里面
                    elif x == -1:
                        uf[y].add(i)
                    elif y == -1:
                        uf[x].add(j)
                    # 两个都在里面
                    elif x == y :
                        pass
                    # 合并掉
                    else:
                        uf[x] = uf[x].union(uf[y])
                        del uf[y]
                    print(uf)
        return len(uf)
        '''
        # 方法二
        # 遍历每个人,遍历到过置1
        visited = [0 for _ in range(len(M))]
        # 圈数
        count = 0
        for i in range(len(M)):
            # 等于1表示被别的圈包进去了,等于0表示再开一个圈
            if visited[i] == 0:
                visited[i] = 1
                self.dfs(M, visited, i)
                count += 1
        return count
        '''

    def findIndex(self,target, uf):
        for idx, comp in enumerate(uf):
            if target in comp:
                return idx
        return -1
    
    # 判断和i认识的都是哪些人
    def dfs(self, M, visited, i):
        # 不需要终止条件
        for j in range(len(M)):
            if j != i and visited[j] == 0 and M[i][j] == 1 :
                visited[j] = 1
                self.dfs(M, visited, j)
