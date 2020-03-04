/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */
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


