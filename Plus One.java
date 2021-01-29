class Solution {
    public int[] plusOne(int[] digits) {
        
        int last=digits.length-1;
        if(digits[last]!=9){
            digits[last]++;
            return digits;
        }
        
        else if(digits[last]==9){
            //System.out.println("last :"+last+" d: "+ digits[last]);
            for(int j=last; j>=0; j--){
                if(digits[j]==9){
                    
                    if(j==0){
                        //System.out.println("entered j=0 condition");
                        int temp[] = new int[digits.length+1];
                        temp[0]=1;
                        for (int k=1; k<temp.length; k++){
                            temp[k]=0;
                        }
                        return temp;
                    }
                    else if(j!=0){
                        //System.out.println("entered making digit zero condition");
                        digits[j]=0;
                    }
                }else if(digits[j]!=9){
                    digits[j]++;
                    break;
                }
            }
        }
        return digits;
    }
}
/*
[1,2,3,4,9]
[9,9,9]
Solution-
if last element is not 9{
add 1 to last element
}


if last element is 9{
    loop through digits from r2l{
    if element is 9{
        if index is 0{
            make a new array
            
            
            
            int temp[] = new int[digits.length+1];
                    temp[0]=1;
                    for (int j=1; j<temp.length; j++){
                        temp[j]=0;
                    }
                    return temp;
                    
                    
                    
                    
        }
    }
    }
    
}


*/
