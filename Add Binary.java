class Solution {    
    public String addBinary(String a, String b) {
        
        //Making the two strings the same length
        while(a.length()<b.length()){
            a = "0"+a;
        }
        while(b.length()<a.length()){
            b="0"+b;
        }
        System.out.println("a; "+a+" b: "+b);
        
        
        a="0"+a;
        b="0"+b;
        //System.out.println(a.charAt(4));
        
        int carry=0;
        String result="";
        for(int j=a.length()-1; j>=0; j--){
            
            int aCh= Character.getNumericValue(a.charAt(j));
            int bCh= Character.getNumericValue(b.charAt(j));
            
            int check = carry+aCh+bCh;
            
            if(check==0){
                System.out.println("check: "+check);
                
                result = "0" + result;
                System.out.println(" res: "+result);
                carry=0;
            }
            if(check==1){
                System.out.println("check: "+check);
                
                result = "1" + result;
                System.out.println(" res: "+result);
                carry=0;
            }
            if(check==2){
                System.out.println("check: "+check);
                
                result = "0" + result;
                System.out.println(" res: "+result);
                carry=1;
            }
            if(check==3){
                System.out.println("check: "+check);
                
                result = "1" + result;
                System.out.println(" res: "+result);
                carry = 1;
            }
        }
        
        if(result.charAt(0)=='0') result=result.substring(1);
        
        return result;
        
    }
}
/*

"1010"
"0010"





make both same length
iterate through each binary r2l

0- {
c=0,a=0,b=0
}

1- {

}


if  sum=0 => 0
    sum=1 => 1
    sum=2 => 0, carry=1
    sum=3 => 1, carry=1

carry= , result=


*/
