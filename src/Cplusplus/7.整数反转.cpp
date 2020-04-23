/*
 * @lc app=leetcode.cn id=7 lang=cpp
 *
 * [7] 整数反转
 */
#include <climits>
#include <iostream>

class Solution {
public:
    int reverse(int x) {
        long result = 0;
        while(x != 0)
        {
            result = result*10 + x % 10;
            std::cout << result;
            x /= 10;
        }
        return (result > INT_MAX || result < INT_MIN)? 0 : result;
        }
};
/*
int main()
{
    Solution s;
    std::cout << s.reverse(123) << std::endl;
    std::cout << s.reverse(-123) << std::endl;
    std::cout << s.reverse(10100) << std::endl;
    std::cout << s.reverse(1000000003) << std::endl;

    return 0;
}
*/
