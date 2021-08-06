class Solution {
    public int trap(int[] height) {
        int[][] talls = new int[height.length][2];

        int tallestLeft = 0;
        for(int i=0; i<height.length; i++){
            talls[i][0] = tallestLeft;
            tallestLeft = Math.max(tallestLeft, height[i]);
        }

        int tallestRight = 0;
        for(int i=height.length-1; i>=0; i--){
            talls[i][1] = tallestRight;
            tallestRight = Math.max(tallestRight, height[i]);
        }

        int totalWater = 0;
        for(int i=0; i<talls.length; i++){
            int currentWater = Math.min(talls[i][0], talls[i][1])-height[i];
            totalWater += currentWater>0? currentWater : 0;
        }

        return totalWater;
    }
}
