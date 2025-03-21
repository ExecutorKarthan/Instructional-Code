public class sumOfNumbers {
    public static int sum(int num){
        if(num == 0){
            return 0;
        }
        return num + sum(num-1);
    }
    public static void main (String [] Args){
        System.out.println(sum(5));
    }
}
