
import java.util.*; 
class Connection{
    String node1;
    String node2;
    int cost;
    public Connection(String a, String b, int c){
        node1 = a;
        node2 = b;
        cost = c;
    }
}
public class Solution {
	public static ArrayList<Connection> getLowCost(ArrayList<Connection> connections) {		
		//Output arraylist
		ArrayList<Connection> result=new ArrayList<>();
		//Edge case
		if(connections==null||connections.size()==0) return result;
		//Copy the given list to make sure it invariable during the operation 
		//Linked list also has better performance on 'remove' function
		LinkedList<Connection> connectionsList = new LinkedList<>(connections);
		//Current MST
		HashSet<String> nodesInMST=new HashSet<>();
		
		//sort the list by the costs of the connections
		Collections.sort(connectionsList,new Comparator<Connection>(){
			@Override
			public int compare(Connection A, Connection B) {
				return Integer.compare(A.cost,B.cost);
			}
		});		
		//After removing a connection from the list, break and check if it is empty
		while(!connectionsList.isEmpty()){
			int length=connectionsList.size();
			//this loop can make sure lower cost connection go first since the list is sorted
			for(Connection connection:connectionsList){
				String nodeA=connection.node1;
				String nodeB=connection.node2;
			
				//first connection(MST is empty)
				if(nodesInMST.isEmpty()){
					nodesInMST.add(nodeA);
					nodesInMST.add(nodeB);
					result.add(connection);
					connectionsList.remove(connection);
					break;
				}					
				//If both cities of a connection are already in the MST, drop it
				if(nodesInMST.contains(nodeA)&&nodesInMST.contains(nodeB)){
					connectionsList.remove(connection);
					break;
				}
				//If only one city of a connection is in the MST, take it
				if(nodesInMST.contains(nodeA)){
					result.add(connection);
					nodesInMST.add(nodeB);
					connectionsList.remove(connection);
					break;
				}else if(nodesInMST.contains(nodeB)){
					result.add(connection);
					nodesInMST.add(nodeA);
					connectionsList.remove(connection);
					break;
				}	
			}
			//if the list is not empty and no connections can be removed, the solution is not exist
			if(length==connectionsList.size())return null;
		}
		
		//sort the result alphabetically 	
		Collections.sort(result,new Comparator<Connection>(){
			@Override
			public int compare(Connection A,Connection B){
				if(A.node1.equals(B.node1)) return A.node2.compareTo(B.node2);
				return A.node1.compareTo(B.node1);
			}
		});
		
		return result;
	}
	
	public static void main(String[] args) {

	 ArrayList<Connection> connections = new ArrayList<>();
	    //test case 1
     	System.out.println("TEST 1");
	    System.out.println("");

	    connections.add(new Connection("A","B",6));
	    connections.add(new Connection("B","C",4));
	    connections.add(new Connection("C","D",5));
	    connections.add(new Connection("D","E",8));
	    connections.add(new Connection("E","F",1));
	    connections.add(new Connection("B","F",10));
	    connections.add(new Connection("E","C",9));
	    connections.add(new Connection("F","C",7));
	    connections.add(new Connection("B","E",3));
	    connections.add(new Connection("A","F",1));

	    ArrayList<Connection> result = getLowCost(connections);
	    
	    if(result==null||result.isEmpty()) 
	    	System.out.println(result);
	    else{
	    	for (Connection c : result){
	    		System.out.println(c.node1 + " -> " + c.node2 + " Cost : " + c.cost);
	    	}
	    }
	  //test case 2
	    
	    System.out.println("");
     	    System.out.println("TEST 2");
	    connections = new ArrayList<>();

	    connections.add(new Connection("A","B",6));
	    connections.add(new Connection("C","D",5));
	    connections.add(new Connection("E","F",1));
	    connections.add(new Connection("B","F",10));
	    connections.add(new Connection("B","E",3));
	    connections.add(new Connection("A","F",1));

	    result = getLowCost(connections);
	    
	    if(result==null||result.isEmpty()) 
	    	System.out.println(result);
	    else{
	    	for (Connection c : result){
	    		System.out.println(c.node1 + " -> " + c.node2 + " Cost : " + c.cost);
	    	}
	    }
	
	    //test case 3
	    System.out.println("");
     	System.out.println("TEST 3");
	    connections = new ArrayList<>();

	    connections.add(new Connection("A","B",1));
	    connections.add(new Connection("B","C",5));
	    connections.add(new Connection("C","D",1));
	    result = getLowCost(connections);
	    
	    if(result==null||result.isEmpty()) 
	    	System.out.println(result);
	    else{
	    	for (Connection c : result){
	    		System.out.println(c.node1 + " -> " + c.node2 + " Cost : " + c.cost);
	    	}
	    }
	}
}
