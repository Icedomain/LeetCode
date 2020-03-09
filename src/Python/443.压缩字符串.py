#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#
class Solution:
    def compress(self, chars: List[str]) -> int:
        # count 几个一样
        # walker 写入的位置
        # runner 往后跑的
        walker, runner = 0, 0

        while runner < len(chars):
            # 写字符
            chars[walker] = chars[runner]
            count = 1
			
            while runner + 1 < len(chars) and \
            chars[runner] == chars[runner+1] :
                runner += 1
                count += 1
			
            if count > 1:
                for c in str(count):
                    # 写数字
                    walker += 1
                    chars[walker] = c
            
            runner += 1
            walker += 1
        
        return walker



