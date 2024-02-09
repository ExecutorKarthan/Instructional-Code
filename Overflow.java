public class Overflow {
    public static void main(String[] args){
        int count = 0;
        int value = 2147483643;
        System.out.println(value);
        while (count < 10){
            count = count +1;
            value = value + 1;
            System.out.println(value);
        }
    }    
}