#
# @lc app=leetcode.cn id=1293 lang=python3
#
# [1293] 网格中的最短路径
#
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        # 极限情况就是走四边 最多 m+n+3 个障碍物
        k = min(k, m + n - 3)
        # 记录
        visited = set((0, 0, k))
        q = [(0, 0, k) ]

        step = 0
        while q:
            step += 1
            tmp = []
            for _ in range(len(q)):
                x, y, rest = q.pop(0)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        # 无障碍
                        if grid[nx][ny] == 0 and \
                            (nx, ny, rest) not in visited:
                            if nx == m - 1 and ny == n - 1:
                                return step
                            tmp.append((nx, ny, rest))
                            visited.add((nx, ny, rest))
                        # 有障碍
                        elif grid[nx][ny] == 1 and rest > 0 \
                            and (nx, ny, rest - 1) not in visited:
                            tmp.append((nx, ny, rest - 1))
                            visited.add((nx, ny, rest - 1))
            q = tmp
        return -1
