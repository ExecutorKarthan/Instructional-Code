
import java.lang.reflect.Array;
import java.util.ArrayList;

public class Node {
    private String fileName = "";
    private Node[] childNodes = new Node[10];
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
            for(int index = 0; index < childNodes.size()+1; index++){
                if(childNodes.get(index).getName().equals(child.fileName)){
                    uniqueChild = false;   
                    break;             
                }
            }
            if(uniqueChild){
                this.childNodes.add(child);
            }
        }
        else{
            this.childNodes.add();
        }   
        if(child.parentNode == null){
            child.addParent(this);
        }
    }

    public ArrayList<Node> getChildNodes(){
        return this.childNodes.get(0);
    }

    public Node getParentNode(){
        if(parentNode != null){
            return this.parentNode;
        }
        else{
            return null;
        }
    }

    public void addParent(Node parent){
        parentNode = parent;
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
