class Solution {
    public String countAndSay(int n) {
        String digit = "11";
        
        if(n==1) return "1";
        if(n==2) return "11";
        
        for(int i=3; i<=n; i++){
            //looping through the sequence
            digit += '&';
            int count=1;
            String temp="";
            for(int j=1; j<digit.length(); j++){
                if(digit.charAt(j)==digit.charAt(j-1)){
                    count++;
                }
                else{
                    temp += String.valueOf(count) + String.valueOf(digit.charAt(j-1));
                    count=1;
                }
            }
            digit = temp;
            
            
        }
        return digit;
    }
}



/*




1
11
21
1211
111221
312211
13112221
1113213211




*/
