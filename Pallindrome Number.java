class Solution {
    public boolean isPalindrome(int x) {
        
        boolean isNegative=false;
        if(x<0){
           return false;
        }
        long original = x;
        long reversed = 0;
        while(x>0){
            reversed = (reversed*10)+(x%10);
            x /= 10;
        }
        if(original==reversed){
            return true;
        }
        else{
            return false;
        }
    }
}
