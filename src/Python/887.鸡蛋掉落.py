#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        self.memo = {}
        return self.dp(K, N)

    def dp(self,k, n):
        if (k, n) not in self.memo:
            if n == 0:
                count = 0
            elif k == 1:
                count = n
            else:
                lo, hi = 1, n
                # 二分缩小区间
                while lo + 1 < hi:
                    x = (lo + hi) // 2
                    t1 = self.dp(k-1, x-1)
                    t2 = self.dp(k, n-x)

                    if t1 < t2:
                        lo = x
                    elif t1 > t2:
                        hi = x
                    else:
                        lo = hi = x

                count = 1 + min(
                    max(self.dp(k-1, x-1), self.dp(k, n-x)) for x in (lo, hi)
                                )

            self.memo[k, n] = count
        return self.memo[k, n]

