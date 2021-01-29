class Solution {
    public int maxSubArray(int[] nums) {
        int max_sum = nums[0];
        int current_sum = nums[0];
        
        for(int i=1; i<nums.length; i++){
             current_sum = Math.max(current_sum+nums[i], nums[i]);
             max_sum = Math.max(current_sum, max_sum);
        }
        return max_sum;
    }
}
/*
-contiguous
-largest sum
-O(n)

max_sum
current_sum

current_sum = max(nums[i], nums[i]+max_sum)
max_sum = max(current_sum, max_sum)
     . 
[-2, 1, -3, 4, -1, 2, 1, -5, 4]



*/
