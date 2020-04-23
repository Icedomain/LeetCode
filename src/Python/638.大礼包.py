#
# @lc app=leetcode.cn id=638 lang=python3
#
# [638] 大礼包
#
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.dic = {}
        return self.dfs(price , special , needs)

    def dfs(self,price , special , needs):
        # 买完了
        if sum(needs) == 0:
            return 0
        # 避免重复
        if tuple(needs) in self.dic:
            return self.dic[tuple(needs)]

        res = 0
        # 没有优惠的价格
        # 单个买
        for i in range(len(needs)):
            res += needs[i]*price[i]
        
        # 买套装
        for sp in special:
            for i in range(len(needs)):
                needs[i] -= sp[i]
            if all(needs[i] >= 0 for i in range(len(needs))):
                res = min(res, self.dfs(price , special , needs) + sp[-1])
            for i in range(len(needs)):
                needs[i] += sp[i]

        self.dic[tuple(needs)] = res
        return res

