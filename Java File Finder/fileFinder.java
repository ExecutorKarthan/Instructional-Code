import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class fileFinder{
    public static void main(String Args []){
        //Import data from txt and make files from it. 
        Map <Node, String> objToName = new HashMap<>();
        Map <String, Node> nameToObj = new HashMap<>();
       try {
        File myObj = new File("fileHierarchy.txt");
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            String fileName = data.substring(data.indexOf("\"")+1, data.indexOf("\"", data.indexOf("\"")+1));
            if(!objToName.containsValue(data)){
                objToName.put(new Node(fileName), fileName);
                nameToObj.put(fileName, new Node(fileName));            
            }        
            if(data.indexOf("[") > -1){
                for(int index = 0; index < data.length()-2; index++){
                    if(data.indexOf("[", index) == -1){
                        break;
                    }
                    String childName = data.substring(data.indexOf("[", index)+1, data.indexOf("]", data.indexOf("[", index)));
                    if(!objToName.containsValue(data)){
                        objToName.put(new Node(childName), childName);
                        nameToObj.put(childName, new Node(childName));            
                    }
                    Node test = new Node("Goats");

                    test.getChildren();
                    // .addChild(nameToObj.get(childName));
                    index = data.indexOf("]", data.indexOf("[", index));
                }
            }
            ArrayList<String> previous = new ArrayList<String>();
            if(data.indexOf("{") > -1){
                for(int index = 0; index < data.length()-1; index++){
                    if(data.indexOf("{", index) == -1){
                        break;
                    }
                    String previousEntry = data.substring(data.indexOf("{", index)+1, data.indexOf("}", index));
                    previous.add(previousEntry);
                    index = data.indexOf("{", index);
                }
            }
            // if(next.size() > 0 && previous.size() >0){
            //     masterFileList.add(new file(fileName, next, previous));    
            // }
            // else if (next.size() > 0 && previous.size() == 0) {
            //     previous.add("root");
            //     masterFileList.add(new file(fileName, next, previous));
            // }
            // else{
            //     next.add("base");
            //     masterFileList.add(new file(fileName, next, previous));
            // }
        }
        myReader.close();
        } 
        catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }   
    }
}
