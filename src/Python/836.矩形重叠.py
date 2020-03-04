#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or  # rec1的右边在rec2的左边
                    rec1[3] <= rec2[1] or  # rec1的上边在rec2的下边
                    rec1[0] >= rec2[2] or  # rec1的左边在rec2的右边
                    rec1[1] >= rec2[3])    # rec1的下边在rec2的上边

