import java.util.*;

class Program {
	
  public String tournamentWinner(
      ArrayList<ArrayList<String>> competitions, ArrayList<Integer> results) {
    //Done in 23:58, without using hint or seeing solution
		String team, winning_team="";
		int max_score=0;
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		
		for(int i=0; i<results.size(); i++){
			if(results.get(i)==1){
				team = competitions.get(i).get(0);
			}
			else{
				team = competitions.get(i).get(1);
			}
			
			if(map.containsKey(team)){
					map.replace(team, map.get(team)+1);
				}
				else{
					map.put(team,1);
				}
				if(map.get(team)>max_score){
					max_score=map.get(team);
					winning_team=team;
				}
			
		}
    return winning_team;
  }
}

