import java.util.ArrayList;
import java.util.List;

public class Survivor {
	// Initial amount of chairs
	static int MAX = 100;
	static String USAGE = "Usage: java Survivor <max number of chairs>";
    public static void main(String[] args) {
		// reads in parameter from command line for a general
		// solution
		if(args.length==1){
			try{
				MAX = Integer.parseInt(args[0]);
				// no negative values for chairs
				if (MAX<=0){
					error();
				}
			}catch(NumberFormatException e){
				error();
			}
		}
		// exit if there are more than one comand line parameters
		if(args.length>1){
			error();
		}
		
		// init list [1..100] or [1..MAX]
    	List<Integer> chairs = new ArrayList<Integer>();
    	for(int i=1;i<MAX+1; i++){
    		chairs.add(i);
    	}
		//System.out.println("all: "+chairs.toString());
		
		List<Integer> answer = getSurvivor(chairs,true);
		
    	// print answer
        System.out.println("Survivor: "+answer);
    }

	public static List<Integer> getSurvivor(List<Integer> chairs, boolean delete){
		if (chairs.size()==1){
			return chairs;
		} else{
			// temporary array
			List<Integer> newArray=new ArrayList<Integer>();
			// loop over chairs
			for (Integer i: chairs){
				// add every other to a new array
				if (!delete){
					newArray.add(i);
				}
				// flip delete
				delete=!delete;
			}
				//System.out.println(newArray);
				return getSurvivor(newArray, delete);
			 }
	}

	
	// print message if an error occures
	public static void error(){
		System.out.println(USAGE);
		System.exit(0);
	}
}
