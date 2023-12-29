class Solution {
    public int removeDuplicates(int[] nums) {
        int pos = 0;
        int val = Integer.MIN_VALUE;

        for(int i=0; i<nums.length; i++){
            if(nums[i] != val){
                nums[pos] = nums[i];
                val = nums[i];
                pos++;
            }
        }
        return pos;
    }
}
