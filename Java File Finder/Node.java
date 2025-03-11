
import java.util.ArrayList;

public class Node {
    private String fileName = "";
    private ArrayList<Node> childNodes = new ArrayList<Node>();
    private Node parentNode = null;

    public Node(String nameOfFile){
        this.fileName = nameOfFile;
    }

    public String getName(){
        return this.fileName;
    }   

    public void addChild(Node child){
        if(this.childNodes.isEmpty() == false){
            boolean uniqueChild = true;
            for(int index = 0; index < childNodes.size(); index++){
                if(childNodes.get(index).getName().equals(child.fileName)){
                    uniqueChild = false;   
                    break;             
                }
            }
            if(uniqueChild){
                this.childNodes.add(child);
            }
        }   
        if(child.parentNode == null){
            child.addParent(this);
        }
    }

    public void addParent(Node parent){
        this.parentNode = parent;
    }

    public void getChildren(){
        String response = this.fileName + " has the following children: " + "\n";
        for(Node child: this.childNodes){
            response += child.getName() + ", ";
        }
        System.out.println(response);
    }

    public void getParent(){
        if(this.parentNode != null){
            System.out.println(this.fileName + " has the following parent: " + this.parentNode.getName() + "\n");
        }
    }

    public void printObject(){
        System.out.println(this.fileName);
        this.getChildren();
        this.getParent();
    }
}
