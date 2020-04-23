/*
 * @lc app=leetcode.cn id=70 lang=cpp
 *
 * [70] 爬楼梯
 */
#include <iostream>
#include <vector>
#include <functional>
using namespace std;

class Solution {
public:
    int climbStairs2(int n) {
        if (n < 0) 
            return 0;
        else if (n < 3) 
            return n;
        int res = 0;
        int a = 1, b = 2;
        for (int i = 2; i < n; i++ )
        {
            res = a + b ;
            a = b ;
            b = res ;
        }
        return b;
    }

    int climbStairs(int n) {
        if (n < 0) return 0;
        vector<int> vec = {1,1};
        if (n > 1) vec.resize(n+1, -1);
        int res = fib(vec , n) ;
        return res;
    }
    int fib(vector<int>& vec, int n){
            if (vec[n] == -1)
                vec[n] = fib(vec ,n-1) + fib(vec ,n-2);
            return vec[n];
        }
};

/*
int main() {
    Solution s;
    std::cout << s.climbStairs(4) << std::endl;
	return 0;
}
*/
