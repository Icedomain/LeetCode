#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 摩尔投票法得到两个大多数
        result1 , result2 = -1, -1
        score1 , score2 = 0 , 0
        for i in range(len(nums)):
            if (result1==nums[i]): 
                score1+=1
            elif (result2==nums[i]):
                score2+=1
            elif (score1==0): 
                result1=nums[i]
                score1=1
            elif (score2==0): 
                result2=nums[i]
                score2=1
            else :
                score1 -= 1
                score2 -= 1

        # 统计两个大多数的出现次数
        time1,time2 = 0 , 0
        for i in range(len(nums)):
            if   (nums[i]==result1): time1+=1
            elif (nums[i]==result2): time2+= 1
        
        # 得到结果
        result = []
        if (time1>len(nums)/3): result.append(result1)
        if (time2>len(nums)/3): result.append(result2)
        return result

