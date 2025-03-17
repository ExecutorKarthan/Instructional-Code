//Import needed utilities
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class fileFinder{
    //Create callable function
    public static String path_creator(String path, String targetFileName, String currentFileName, Map <String, Node> nameToObj) {
        //Define a result string to be returned
        String result = "";
        //Create a base-case to return if the node name is indeed the same as the name of the file being searched
        if (currentFileName.equals(targetFileName)) {
            return path + currentFileName;
        }
        //Create an alternate case to handle not finding the target file
        else{
            //Create an arrayList of the children nodes to iterate over
            ArrayList<Node> currentChildren = nameToObj.get(currentFileName).getChildNodes();
            //Iterate over the children, recalling the function so the search continues
            for(Node childNode: currentChildren){
                String newPath = path + currentFileName + "/";
                result = path_creator(newPath, targetFileName, childNode.getName(), nameToObj); 
                if(result != null && result.substring(result.lastIndexOf("/")+1).equals(targetFileName)){
                    return result;
                }
            }
            // If the file cannot be found, return a string that says "File not found"
            return "File not found";
        }
    }
    public static void main(String Args []){
        //Create a hashmap to hold all the objects
        Map <String, Node> nameToObj = new HashMap<>();
       try {
        //Create a fileObject to read
        File myObj = new File("fileHierarchy.txt");
        Scanner myReader = new Scanner(myObj);
        //Iterate over the fileObject to read each line, making objects from the data
        while (myReader.hasNextLine()) {
            //Read the file name and detect the filename
            String data = myReader.nextLine();
            String nodeName = data.substring(data.indexOf("\"")+1, data.indexOf("\"", data.indexOf("\"")+1));
            //If the name is not in the hashmap, then add it as an object
            if(!nameToObj.containsKey(nodeName)){
                nameToObj.put(nodeName, new Node(nodeName));            
            }        
            //Continue to read the data, adding child nodes
            if(data.indexOf("[") > -1){
                for(int index = 0; index < data.length()-2; index++){
                    //If there are no children, break the loop
                    if(data.indexOf("[", index) == -1){
                        break;
                    }
                    //If a child is found, make a new object and add it to the map if it doesn't already exist
                    String childName = data.substring(data.indexOf("[", index)+1, data.indexOf("]", data.indexOf("[", index)));
                    if(!nameToObj.containsKey(childName)){
                        nameToObj.put(childName, new Node(childName));            
                    }
                    //Add the child to the parent node
                    nameToObj.get(nodeName).addChild(nameToObj.get(childName));
                    index = data.indexOf("]", data.indexOf("[", index));
                }
            }
        }
        myReader.close();
        }
        //Throw and error if the txt file is missing 
        catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        } 
        //Create strings and execute the function
        String targetFilePath = "/";
        String targetFile = "Trees.png";
        System.out.println(fileFinder.path_creator(targetFilePath, targetFile, "User", nameToObj));
    }
}
