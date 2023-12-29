import java.util.*;

class Program {
  public static OrgChart getLowestCommonManager(
      OrgChart topManager, OrgChart reportOne, OrgChart reportTwo) {
    HashMap<OrgChart, OrgChart> managers = new HashMap<OrgChart, OrgChart>();
		HashMap<OrgChart, Integer> depths = new HashMap<OrgChart, Integer>();
		getManagersAndDepth(null, managers, topManager, 0, depths);
		
		int depth1 = depths.get(reportOne);
		int depth2 = depths.get(reportTwo);
		if(depth1!=depth2){
			if(depth1>depth2){
				while(depth1!=depth2){
					reportOne = managers.get(reportOne);
					depth1 = depths.get(reportOne);
				}
			}else{
				while(depth2!=depth1){
					reportTwo = managers.get(reportTwo);
					depth2 = depths.get(reportTwo);
				}
			}
		}
		while(reportOne != null && reportTwo != null){
			if(reportOne == reportTwo) return reportOne;
			else{
				reportOne = managers.get(reportOne);
				reportTwo = managers.get(reportTwo);
			}
		}
		
    return reportOne; // Replace this line.
  }
	
	public static void getManagersAndDepth(OrgChart parent, HashMap<OrgChart, OrgChart> managers, OrgChart current, int depth, HashMap<OrgChart, Integer> depths){
		if(current!=null){
			depths.put(current,depth);
			managers.put(current, parent);
			for(OrgChart child : current.directReports){
				getManagersAndDepth(current, managers, child, depth + 1, depths);
			}
		}
	}
	/*
	O(n)|O(n)
	->create a hashmap of managers
	->create a hashmap of depth
	-> if depth is not same, go up until depth of both is same
	-> go up in both simultaneously until you reach a common manager
	*/

  static class OrgChart {
    public char name;
    public List<OrgChart> directReports;

    OrgChart(char name) {
      this.name = name;
      this.directReports = new ArrayList<OrgChart>();
    }

    // This method is for testing only.
    public void addDirectReports(OrgChart[] directReports) {
      for (OrgChart directReport : directReports) {
        this.directReports.add(directReport);
      }
    }
  }
}

