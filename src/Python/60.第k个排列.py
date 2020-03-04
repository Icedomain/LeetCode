#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 待选择的字符串
        nums = [str(i) for i in range(1,n+1)]
        # 0!, 1!, ..., (n - 1)!
        factorials = [1]
        for i in range(1, n):            
            factorials.append(factorials[i - 1] * i)
        
        # 第几个转化为第几个的索引(减1)
        k -= 1
        
        res = []
        for i in range(n - 1, -1, -1):
            # 计算第几个区间,首位所在的区间 k//(n-1)! 
            # 第一个区间首位是1,第二个区间首位是2
            idx = k // factorials[i]
            # 减去多个区间对应的值
            k -= idx * factorials[i]
            # 结果值添加对应的数字
            res.append(nums[idx])
            # 因为排列不重复,nums需要去掉对应元素 
            nums.pop(idx)
        
        return ''.join(res)
