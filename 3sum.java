class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<ArrayList<Integer>> triplets = new HashSet<>();
        Arrays.sort(nums);
        for(int i=0; i<nums.length; i++){
            int j=i+1;
            int k=nums.length-1;
            while(j<k){
                //System.out.println(i+" "+j+" "+k);
                int sum = nums[i]+nums[j]+nums[k];
                if(sum < 0){
                    j++;
                }
                else if(sum > 0){
                    k--;
                }
                else if(sum==0){

                    ArrayList<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[i]); triplet.add(nums[j]); triplet.add(nums[k]);
                    triplets.add(triplet);
                    j++; k--;
                }
            }
        }

        return new ArrayList<List<Integer>>(triplets);
    }
}
