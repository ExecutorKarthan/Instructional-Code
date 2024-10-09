public class Strings{
    public static void main(String[] Args){
        String word = new String("Bird is the word");
        String otherWord = new String("Horse is the Borse");
        String lastWord = new String("Bird is the word");
        int first = 5;
        int second = 5;
        Integer third = 5;
        Integer fourth = 5;
        String num = "5";
        Integer newNum = Integer.parseInt(num);
        // for(int index = 0; index < word.length(); index++){
        //     System.out.println(word.substring(index, index+1));
        // }
        System.out.println(word);
        // word = word + otherWord;
        // System.out.println(word);
        System.out.println(word == lastWord);
        System.out.println(word.equals(lastWord));
        System.out.println(first == newNum);
        System.out.println(first == third);
        System.out.println(newNum);
        System.out.println(fourth.equals(newNum));
    }
}