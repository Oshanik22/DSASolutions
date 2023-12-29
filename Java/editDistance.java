class Solution {
    public int editDistance(String s, String t) {
        int[][] memoise = new int[s.length()][t.length()];
        return minOperations(s,t, s.length()-1, t.length()-1, memoise);
    }
    public int minOperations(String s, String t, int idx1, int idx2, int[][] memoise){
        if(idx1==-1) return idx2+1;
        if(idx2==-1)return idx1+1;
        if(memoise[idx1][idx2]>0) return memoise[idx1][idx2];
        if(s.charAt(idx1) == t.charAt(idx2)){
            return memoise[idx1][idx2]=minOperations(s, t, idx1-1, idx2-1, memoise);
        }
        else{
            return memoise[idx1][idx2] = 1 + getMin(minOperations(s,t, idx1-1, idx2,memoise),
                                        minOperations(s,t, idx1, idx2-1 ,memoise),
                                        minOperations(s,t, idx1-1, idx2-1, memoise));
        }
    }
    public int getMin(int i, int j, int k){
        if(i<=j && i<=k) return i;
        if(j<=i && j<=k) return j;
        return k;
    }
}
