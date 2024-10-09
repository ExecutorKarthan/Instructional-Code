public class loopsAndArrays{
    public static void main (String[] Args){
        String[] subjects = new String[]
        {"CSA", "ChEmIsTrY", "Math", "PE", "English with Ramsey", "Spanish", "Graphic Design", "Ceramics"};
        for(int index=0; index < subjects.length; index++){
            subjects[index] = "Goat";
            System.out.println(subjects[index]);
        }
        
    }
}