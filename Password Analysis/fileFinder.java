import java.util.ArrayList;
import java.util.Arrays;

class fileFinder{
    public static void main(String Args []){
        ArrayList<String> masterStringList= new ArrayList<String>(Arrays.asList(
            "User",
            "Downloads",
            "HappyImage.jpeg",
            "Screenshot--25252.gif",
            "Documents",
            "Homework.doc",
            "Financials.doc",
            "Reports",
            "BankStatement1.doc",
            "BankStatement2.doc",
            "BankStatement3.doc",
            "BankStatement4.doc",
            "Pictures",
            "Vacation.png",
            "House.png",
            "Trees.gif",
            "Music",
            "Dave Matthews Band",
            "Under the table and dreaming",
            "The Best of What's Around.mp3",
            "What Would You Say.mp3",
            "Satellite.mp3",
            "Rhyme & Reason.mp3",
            "Typical Situation.mp3",
            "Dancing Nancies.mp3", 
            "Ants Marching.mp3",
            "Lover Lay Down.mp3",
            "Jimi Thing.mp3", 
            "Warehouse.mp3",
            "Pay for What You Get.mp3",
            "#34.mp3"
        ));

        ArrayList<file> masterFileList = new ArrayList<file>();

       for (String fileName :  masterStringList ){
        masterFileList.add(new file(fileName));
       };
       System.out.print("I made it!");
    }
}
