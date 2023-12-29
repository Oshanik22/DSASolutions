import java.util.*;

class Program {
  public static List<Integer[]> diskStacking(List<Integer[]> disks) {
		disks.sort((a,b) -> a[2].compareTo(b[2]));
    int[] stackHeights = new int[disks.size()+1];
		HashMap<Integer, List<Integer[]>> stacks = new HashMap<Integer, List<Integer[]>>();
		int maxHeight = Integer.MIN_VALUE; int maxHeightIdx = 0;
		for(int i=0; i<disks.size(); i++){
			stackHeights[i] = disks.get(i)[2];
			List<Integer[]> temp = new ArrayList<Integer[]>();
			temp.add(disks.get(i));
			stacks.put(i, temp);
		}
		for(int diskIdx=0; diskIdx<disks.size(); diskIdx++){
			int maxStackIdx = -1; int maxStackHeight = 0;
			int currentHeight = disks.get(diskIdx)[2];
			int currentWidth = disks.get(diskIdx)[0];
			int currentDepth = disks.get(diskIdx)[1];
			
			for(int i=0; i<disks.size(); i++){
				int prevHeight = disks.get(i)[2];
				int prevWidth = disks.get(i)[0];
				int prevDepth = disks.get(i)[1];
				if(currentHeight>prevHeight && currentWidth>prevWidth && currentDepth>prevDepth){
					if(stackHeights[i]>=maxStackHeight){
						maxStackHeight = stackHeights[i];
						maxStackIdx = i;
					}
				}
			}
			
			List<Integer[]> currentStack = new ArrayList<Integer[]>();
			if(maxStackHeight != 0){
				currentStack.addAll(stacks.get(maxStackIdx));
			}
			
			currentStack.add(disks.get(diskIdx));
			stacks.put(diskIdx, currentStack);
			int newHeight = maxStackIdx!=-1? stackHeights[maxStackIdx] + currentHeight : currentHeight;
			stackHeights[diskIdx] = newHeight;
			if(newHeight>maxHeight){
				maxHeight = newHeight;
				maxHeightIdx = diskIdx;
			}
		}
		
    return stacks.get(maxHeightIdx);
  }
}

