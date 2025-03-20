public class reverseString {
    public static String stringReverse(String string){
        if(string.length() <= 0){
            return string; 
        }
        if(string.length() ==1){
            return string.substring(string.length()-1);
        }
        else{
            return stringReverse((string.substring(1))) + string.substring(0, 1);
        }
    }
    public static void main(String[] Args){
        String test = "Karel";

        System.out.println(reverseString.stringReverse(test));
    }
    
}
