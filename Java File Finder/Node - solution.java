
//Import needed information
import java.util.ArrayList;

//Create a node class to organize the data
public class Node {
    //Give the oject a name, arrayList to track children and a parent node
    private String fileName = "";
    private ArrayList<Node> childNodes = new ArrayList<Node>(); // Broke this line by making it an array
    private Node parentNode = null;

    //Assign the Node's name
    public Node(String nameOfFile){
        this.fileName = nameOfFile;
    }

    //Get the Node's name
    public String getName(){
        return this.fileName;
    }   

    //Add a child to the node
    public void addChild(Node child){
        if(this.childNodes.isEmpty() == false){
            //Add a test to ensure the child node is unique before adding it
            boolean uniqueChild = true;
            for(int index = 0; index < childNodes.size(); index++){ // broke this by introducing a 1 off error
                if(childNodes.get(index).getName().equals(child.fileName)){
                    uniqueChild = false;   
                    break;             
                }
            }
            //If the node did not exist before, add it
            if(uniqueChild){
                this.childNodes.add(child); // Broke this by removing "child" so it doesn't add anything
            }
        }
        //If the parent node has no children, add the child node
        else{
            this.childNodes.add(child);
        }   
        //Update the parent node of the child
        if(child.parentNode == null){
            child.addParent(this);
        }
    }

    //Get the arrayList of child nodes
    public ArrayList<Node> getChildNodes(){
        return this.childNodes; // Broke this by only calling the first node
    }

    //Get the parent node value
    public Node getParentNode(){
        if(parentNode != null){
            return this.parentNode;
        }
        else{
            return null;
        }
    }

    //Add a parent node to a child
    public void addParent(Node parent){
        this.parentNode = parent; // Broke this by removing "this"
    }

    public void printChildren(){
        String response = this.fileName + " has the following children: " + "\n";
        for(Node child: this.childNodes){
            response += child.getName() + ", ";
        }
        System.out.println(response.substring(0, response.length()-2));
    }

    public void printParent(){
        if(this.parentNode != null){
            System.out.println(this.fileName + " has the following parent: " + this.parentNode.getName() + "\n");
        }
    }

    public void printObject(){
        System.out.println(this.fileName);
        this.printChildren();
        this.printParent();
    }
}
