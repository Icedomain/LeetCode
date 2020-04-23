/*
 * @lc app=leetcode.cn id=69 lang=cpp
 *
 * [69] x 的平方根
 */
#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        /*
        long r = x;
        while (r*r > x)
            r = (r + x/r) / 2;
        return (int) r;
        */
    
        int l = 0, r = x ;
        long mid ,ret ;
        while (l <= r){
            mid = (l + r) >> 1 ;
            if ( mid * mid <= x & x < (mid+1)*(mid+1) )
            {
                ret = mid;
                break ;
            }
            else if (x < mid*mid )
                r = mid ;
            else 
                l = mid + 1;
        }
        return (int) mid;
    }
};
/*
int main() {
    Solution s;
    std::cout << s.mySqrt(8) << std::endl;
    std::cout << s.mySqrt(19) << std::endl;
	return 0;
}
*/
