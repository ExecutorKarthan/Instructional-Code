public class countLetter {
    public static int cl(String phrase, String letter){
        if(phrase.length() == 0){
            return 0; 
        }
        if(phrase.substring(0,1).equals(letter)){
            return 1 + cl(phrase.substring(1, phrase.length()-1), letter);
        }
        else{
            return 0 + cl(phrase.substring(1, phrase.length()-1), letter);
        }
    }
    public static void main(String[] Args){
        String test = "Horses are good!";

        System.out.println(countLetter.cl(test, "s"));
    }
    
}
