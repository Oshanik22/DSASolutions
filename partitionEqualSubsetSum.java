class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for(int i : nums){
            sum+=i;

        }
        int[][] memoise = new int[nums.length][sum/2+1];
        if(sum%2!=0) return false;
        return maxHalfSum(nums.length-1, nums, memoise, sum/2)==sum/2;
    }

    public int maxHalfSum(int idx, int[] nums, int[][] memoise, int sumLeft){
        if(idx < 0) return 0;
        if(sumLeft <= 0) return 0;
        if(memoise[idx][sumLeft]>0) return memoise[idx][sumLeft];
        if(nums[idx]>sumLeft) return memoise[idx][sumLeft] = maxHalfSum(idx-1, nums, memoise, sumLeft);

        return  memoise[idx][sumLeft] = Math.max(nums[idx] + maxHalfSum(idx-1, nums, memoise, sumLeft-nums[idx]),
                            maxHalfSum(idx-1, nums, memoise, sumLeft));
    }
}
