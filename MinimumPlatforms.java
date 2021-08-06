class Solution
{
    //Function to find the minimum number of platforms required at the
    //railway station such that no train waits.
    public static int findPlatform(int arr[], int dep[], int n)
    {
        int count = 0;

        PriorityQueue<Train> trains = getTrainInfo(arr, dep, n);
        PriorityQueue<Integer> platforms = new PriorityQueue<Integer>();


        while(!trains.isEmpty()){
           Train current = trains.poll();
           int requiredAt = current.arr;
           int requiredTill = current.dep;

           if(platforms.isEmpty() || platforms.peek() >= requiredAt){
               count++;
           }else{
               platforms.poll();
           }
           platforms.offer(requiredTill);
        }

        return count;
    }

    public static PriorityQueue<Train> getTrainInfo(int[] arr, int[] dep, int n){
        PriorityQueue<Train> trains = new PriorityQueue<Train>((a,b)->Integer.compare(a.arr, b.arr));

        for(int i=0; i<n; i++){
            trains.offer(new Train(arr[i], dep[i]));
        }

        return trains;
    }


    public static class Train{
        int arr; int dep;
        public Train(int arr, int dep){
            this.arr = arr;
            this.dep = dep;
        }
    }

}
