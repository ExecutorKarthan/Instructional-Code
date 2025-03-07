
import java.lang.reflect.Array;
import java.util.ArrayList;

public class file {
    private String fileName = "";
    private ArrayList<String> nextFile = new ArrayList<String>();
    private ArrayList<String> previousFiles = new ArrayList<String>();
    public file(String nameOfFile){
        this.fileName = nameOfFile;
    }
    private void adjustNext(ArrayList<String> nextList){
        this.nextFile = nextList;
    }
    private void adjustPrevious(ArrayList<String> previousList){
        this.previousFiles = previousList;
    }
}
