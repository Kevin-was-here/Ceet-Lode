#include <iostream>
#include <vector>

using namespace std;

//Initial 40% solution
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> sum (nums.size());
        for(int i = 0; i < nums.size(); i++){
            if(i==0){
                sum[i] = nums[i];
            }else{
                sum[i] = sum[i-1] + nums[i];
            }
        }
        return sum;
    }
};

//WTF 0ms solution
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> rs = nums;
        for(int i=1; i<nums.size();i++){
            rs[i] = rs[i-1] + nums[i];                
        }
        return rs;
    }
};
