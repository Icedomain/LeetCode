#
# @lc app=leetcode.cn id=393 lang=python3
#
# [393] UTF-8 编码验证
#
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # cnt表示后面接几个字节字符
        # cnt 从0到0表示一个字符
        cnt = 0
        for d in data:
            if cnt == 0:
                if (d >> 5) == 0b110:
                    cnt = 1
                elif (d >> 4) == 0b1110:
                    cnt = 2
                elif (d >> 3) == 0b11110:
                    cnt = 3
                # 0xxxxxxx 后面不接
                # 这种情况首位不是0就错
                elif (d >> 7): 
                    return False
            else:
                # 如果不接10xxxxxx
                if (d >> 6) != 0b10:
                    return False
                cnt -= 1
        return cnt == 0

