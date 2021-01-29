class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int arr1=m-1;
        int arr2=n-1;
        int i=m+n-1;
        
        while(i>=0){
            //System.out.println(i+"  arr1 : "+arr1+" arr2 : "+arr2);
            if(arr1<0){
                //System.out.println("nums1 finished");
                nums1[i]=nums2[arr2--];
                i--;
            }
            else if(arr2<0){
                //System.out.println("nums2 finished");
                nums1[i]=nums1[arr1--];
                i--;
                
            }
            else {
                
                if(nums2[arr2]>=nums1[arr1]){
                    nums1[i]=nums2[arr2];
                    //System.out.println("put from 2");
                    i--;
                    arr2--;
                }
                
                else{
                nums1[i]=nums1[arr1];
                //System.out.println("put from 1");
                i--;
                arr1--;
                }
            }     
        }
    }
}
/*
[1,2,3,0,0,0]

[2,5,6]


*/
