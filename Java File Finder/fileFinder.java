import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner; 

class fileFinder{
    public static void main(String Args []){
        ArrayList<file> masterFileList = new ArrayList<file>();
        int masterIndex = 0;
       try {
        File myObj = new File("fileHierarchy.txt");
        Scanner myReader = new Scanner(myObj);
        while (myReader.hasNextLine()) {
            String data = myReader.nextLine();
            String fileName = data.substring(data.indexOf("\"")+1, data.indexOf("\"", data.indexOf("\"")+1));
            ArrayList<String> next = new ArrayList<String>();
            if(data.indexOf("[") > -1){
                for(int index = 0; index < data.length()-2; index++){
                    if(data.indexOf("[", index) == -1){
                        break;
                    }
                    String nextEntry = data.substring(data.indexOf("[", index)+1, data.indexOf("]", data.indexOf("[", index)));
                    next.add(nextEntry);
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
            if(next.size() > 0 && previous.size() >0){
                masterFileList.add(new file(fileName, next, previous));    
            }
            else if (next.size() > 0 && previous.size() == 0) {
                previous.add("root");
                masterFileList.add(new file(fileName, next, previous));
            }
            else{
                next.add("base");
                masterFileList.add(new file(fileName, next, previous));
            }
            masterIndex += 1;
        }
        myReader.close();
        } 
        catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }   

        

    }
}
