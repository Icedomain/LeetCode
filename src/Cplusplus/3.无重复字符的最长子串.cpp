/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 */
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 记录表 256个字符 填-1
        vector<int> charmap (256,-1);
        
        int start = 0;
        int maxlen = 0;
        // 遍历 滑动窗 [start,j ] j往右边移动 若遇到重复的 start又移一位
        for(int j = 0;j<s.size();j++){
            // 如果这个字符出现过了,又移动 最左边那个踢出滑动窗 
            if(charmap[s[j]] >= start)
                start = charmap[s[j]] + 1;
            // 如果这个字符在滑动窗中没出现过,位置给它(出现过也要给它)
            charmap[s[j]] = j;
            maxlen = max(maxlen , j - start +1);
        }
        return maxlen;
    }
};
/*
int main(){
    Solution s ;
    cout << s.lengthOfLongestSubstring("abcabcbb"); // 3

}
*/

