/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 哈希表
        unordered_map<int, int>dict;
        vector<int> res ;
        for(int i = 0 ; i <nums.size();i++ ){
            // 找不到
            if (dict.find(target - nums[i]) == dict.end()){
                dict[nums[i]] = i;
            }
            else{
                res.push_back(dict[target-nums[i]]);
                res.push_back(i);
            }                     
        }
        return res; 
    }
};
/*
int main(){
    Solution s;

    std::vector<int> v1{2, 7, 11, 15};
    for(const int& k : s.twoSum(v1, 9))
        cout << k << " "; // 0, 1
    cout << endl;
    
    std::vector<int> v2{0, 4, 3, 0};
    for(const int& k : s.twoSum(v2, 0))
        cout << k << " "; // 0, 3
    cout << endl;

    std::vector<int> v3{-3, 4, 3, 90};
    for(const int& k : s.twoSum(v3, 0))
        cout << k << " "; // 0, 2
    cout << endl;

    return 0;
}
*/
