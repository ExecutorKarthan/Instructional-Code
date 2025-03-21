public class countLetter {
    public static int cl(String phrase, String letter){
        if(phrase.length() == 0){
            return 0; 
        }
        if(phrase.substring(0,1).equals(letter)){
            return 1 + cl(phrase.substring(1, phrase.length()), letter);
        }
        else{
            return 0 + cl(phrase.substring(1, phrase.length()), letter);
        }
    }
    public static void main(String[] Args){
        String test = "hellow world";

        System.out.println(countLetter.cl(test, "l"));
    }
    
}
