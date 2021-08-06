class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxStreak = 0;
        int currentStreak = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i]==1) currentStreak++;
            else{
                maxStreak = Math.max(currentStreak, maxStreak);
                currentStreak=0;
            }
        }
        return Math.max(currentStreak, maxStreak);
    }
}
