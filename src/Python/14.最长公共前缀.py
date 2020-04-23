#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        sz = zip(*strs)
        ret = ""
        for char in sz:
            if len(set(char)) > 1:
                break
            ret +=char[0]
        return ret
        '''
        if not strs:
            return ''
        strs.sort(key = lambda x : len(x))
        for idx in range(len(strs[0])):
            # 最大的可能长度就是第一个的长度
            for i in range(1,len(strs)):
                # 对每个元素都要遍历
                if strs[i][idx] != strs[0][idx]:
                    return strs[0][:idx]
        return strs[0]

