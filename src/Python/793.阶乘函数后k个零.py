#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后K个零
#

class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        #  k = zeta(x) = int(x/5) + int(x/25) + ... <= x/5 + x/25 + ... = 4x/5 
        # 故有 x >= 5K/4 >= K 
        # x <=10*K+1是个很宽泛的的上界，事实上这一题x <= 5*K+1 也是过
        l , r = K , 5 * K + 1
        while l <= r:
            mid = (l + r) // 2
            cnt = self.trailingZeroes(mid)
            if cnt == K: 
                return 5
            elif cnt < K:
                l = mid + 1
            else: 
                r = mid - 1
        return 0

    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count


