class Solution {
    public boolean isValid(String s) {
        int j=1;
        Stack<Character> stk = new Stack();
        for(int i=0; i<s.length(); i++){
            //Iterating through the string
            char x=s.charAt(i);
            if(x=='('||x=='{'||x=='['){
                stk.push(x);
            }
            else if(stk.empty()==false &&(x==')'&&stk.peek()=='('||
                    x=='}'&&stk.peek()=='{'||
                    x==']'&&stk.peek()=='['
                   )){
                stk.pop();
            }
            else{
                return false;
            }
        }
        return stk.empty();
    }
}
