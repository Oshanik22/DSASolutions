import java.util.HashMap;
class Solution {    
    public int romanToInt(String s) {
        
        int num=0;

        //creating a hashmap to store int value for roman numerals
        HashMap<Character,Integer> romanValue= new HashMap<Character,Integer>();
        romanValue.put('I',1);
        romanValue.put('V',5);
        romanValue.put('X',10);
        romanValue.put('L',50);
        romanValue.put('C',100);
        romanValue.put('D',500);
        romanValue.put('M',1000);
        
        //69 
        
        for(int i=0; i<s.length(); i++){
            //Iterate through the roman string right to left
            
            if(i==s.length()-1){
                //if last character, add to sum
                num += romanValue.get(s.charAt(i));
            }
            else{
               if(romanValue.get(s.charAt(i))<romanValue.get(s.charAt(i+1))){
               //if i<=right
                 
                num -= romanValue.get(s.charAt(i));
                }
               else {
                   //if i>right
                   num += romanValue.get(s.charAt(i));
                                          
               }
           }
        }
        
        return num;
    }
}


















