class Solution {
    public int reverse(int x) {
        boolean isNegative = false;
        
        if(x<0){
            x = x *-1;
            isNegative = true;
        }
        long reversed = 0;
        while(x>0){
            reversed = (reversed*10) + (x%10);
            //System.out.println("reversed is "+ reversed);
            x /=10;
        }
        //System.out.println("max value is : " + Integer.MAX_VALUE);
        
        if(reversed > Integer.MAX_VALUE){
            return 0;
        }
        if(isNegative){
            reversed = reversed* -1;
        }
        return (int)reversed;
        
        
        
        
    }
}
