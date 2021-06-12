import java.util.*;

class Program {
  public static int getNthFib(int n) {
		if(n==1) return 0;
		if(n==2) return 1;
		
		int n1Value =1;
		int n2Value =0;
		
		for(int i=3; i<=n; i++){
			if(i==n) return n1Value + n2Value;
			int temp = n1Value;
			n1Value = n1Value+n2Value;
			n2Value = temp;
		}
		return 0;
  }
}

