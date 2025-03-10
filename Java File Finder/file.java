
import java.lang.reflect.Array;
import java.util.ArrayList;

public class file {
    private String fileName = "";
    private ArrayList<String> nextFile = new ArrayList<String>();
    private ArrayList<String> previousFiles = new ArrayList<String>();
    public file(String nameOfFile){
        this.fileName = nameOfFile;
    }

    public file(String nameOfFile, ArrayList<String> nextList, ArrayList<String> previousList){
        this.fileName = nameOfFile;
        this.nextFile = nextList;
        this.previousFiles = previousList;
    }

    public ArrayList<String> getNext(){
        return this.nextFile;
    }

    public ArrayList<String> getPrevious(){
        return this.previousFiles;
    }

    public void printObject(){
        String output = this.fileName + " is preceded by "; 
        if(this.previousFiles.size() == 0){
            for (String previousFileName : previousFiles) {
                output += previousFileName + " ";
            }
        }
        else{
            for (int index = 0; index < previousFiles.size(); index++){
                if(index == previousFiles.size()-1){
                    output += previousFiles.get(index);
                }
                else{
                    output += previousFiles.get(index) + ", ";
                }
            }       
        }
        output += " and is followed by ";
        if(this.nextFile.size() == 0){
            for (String nextFileName : nextFile) {
                output += nextFileName + " ";
            }
        }
        else{
            for (int index = 0; index < nextFile.size(); index++){
                if(index == nextFile.size()-1){
                    output += nextFile.get(index);
                }
                else{
                    output += nextFile.get(index) + ", ";
                }
            }   
        }
        System.out.println(output);
    }
}
