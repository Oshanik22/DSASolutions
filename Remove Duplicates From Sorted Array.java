class Solution {
    public int removeDuplicates(int[] nums) {
        int len = nums.length;
        
        if(len>1){
            for(int i=0; i<len-1; i++){
                if(i!=len-1){           
                    while(nums[i]==nums[i+1]){
                        System.out.println("basd");
                    if(i+1==len-1){
                        len--;
                        break;
                    }
                    else{
                        for(int j=i; j<len-1; j++){
                        nums[j]=nums[j+1];
                    }
                    len--;
                    }
                }
                }
            }
        }
        return len;
    }
}
