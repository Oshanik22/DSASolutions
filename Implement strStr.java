class Solution {
    public int strStr(String haystack, String needle) {
        if(haystack.length()<needle.length()) return -1;
        if(needle.length()==0) return 0;
        
        //Naive Approach
        
        for(int i =0; i<=haystack.length()-needle.length(); i++){
            boolean found = true;
            for(int j=0; j<needle.length(); j++){
                if(haystack.charAt(i+j)!=needle.charAt(j)){
                    found = false;
                    break;
                }
            }
            if(found){
                return i;
            }
        }
        return -1;
    }
}
/*
needle=2
haystack.length()-needle.length()=3
i=0, sub(0,2)=he
i=1, sub(1,3)=el
i=2, sub(2,3)=ll (match)
i=3, sub(3,4)=lo


*/
