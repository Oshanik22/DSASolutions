class Solution {
    public int searchInsert(int[] nums, int target) {
        int index = -1;
        for(int i=0; i<nums.length; i++){
            if(nums[i]<=target){
                if(nums[i]==target){
                    index=i;
                    break;
                }
            }else{
                index = i;
                break;
            }
        }
        return index==-1? nums.length : index;
    }
}
