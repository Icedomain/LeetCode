/*
 * @lc app=leetcode.cn id=9 lang=cpp
 *
 * [9] 回文数
 */
#include<iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        // 最高位的位数
        int d = 1;
        while (x / d >= 10){
            d *= 10;
        }
        int p , q;
        while (x > 0){
            // p q 对应最高位和最低位
            p = x / d ;
            q = x % 10;
            if (p != q) return false;
            // x 去掉最高位,去掉最低位
            x = x % d / 10 ;
            // x 去掉了两位,d也减两位
            d /= 100;
        }
        return true;
    }

    bool isPalindrome2(int x) {
        if (x < 0) return false;
        long rev = 0, origin = x;
        while (x > 0){
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        return rev == origin;
    }
};
/*
int main(){
    Solution s;
    cout << s.isPalindrome(2002) << endl;
    cout << s.isPalindrome2(2102) << endl;
    return 0;
}
*/
