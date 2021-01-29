class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        String x = "";
        boolean isCommon = true;
        
        if(strs.length!=0){
            for (int i = 0; i<strs[0].length(); i++)//Iterating through every character in first element
        {
            for (int j = 1; j<strs.length; j++) //Iterating through all elements after 1st
            {   
                if(i<strs[j].length()) //checking for index overflow
                {
                    if(strs[j].charAt(i)!=strs[0].charAt(i))
                    {
                        isCommon = false;                        
                    }
                } else{
                    isCommon = false;
                }
            }
            if(isCommon){
                x += String.valueOf(strs[0].charAt(i));            
            }
        }
        }
        
        return x;
    }
}
