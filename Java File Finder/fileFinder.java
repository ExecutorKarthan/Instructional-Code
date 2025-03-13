import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class fileFinder{
    public static String path_creator(String path, String targetFileName, String currentFileName, Map <String, Node> nameToObj) {
        String result = "";
        if (currentFileName.equals(targetFileName)) {
            return path + currentFileName;
        }
        else{
            ArrayList<Node> currentChildren = nameToObj.get(currentFileName).getChildNodes();
            for(Node childNode: currentChildren){
                String newPath = path + currentFileName + "/";
                result = path_creator(newPath, targetFileName, childNode.getName(), nameToObj); 
                if(result != null && result.substring(result.lastIndexOf("/")+1).equals(targetFileName)){
                    return result;
                }
            }
            return null;
        }
    }
    public static void main(String Args []){
        Map <String, Node> nameToObj = new HashMap<>();
       try {
        File myObj = new File("fileHierarchy.txt");
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            String nodeName = data.substring(data.indexOf("\"")+1, data.indexOf("\"", data.indexOf("\"")+1));
            if(!nameToObj.containsKey(nodeName)){
                nameToObj.put(nodeName, new Node(nodeName));            
            }        
            if(data.indexOf("[") > -1){
                for(int index = 0; index < data.length()-2; index++){
                    if(data.indexOf("[", index) == -1){
                        break;
                    }
                    String childName = data.substring(data.indexOf("[", index)+1, data.indexOf("]", data.indexOf("[", index)));
                    if(!nameToObj.containsKey(childName)){
                        nameToObj.put(childName, new Node(childName));            
                    }
                    nameToObj.get(nodeName).addChild(nameToObj.get(childName));
                    index = data.indexOf("]", data.indexOf("[", index));
                }
            }
        }
        myReader.close();
        } 
        catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        } 
    }
}
