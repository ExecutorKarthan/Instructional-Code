public class greatestCommonDivisor {
    public static int gcd(int num1, int num2){
        if(num1 > num2){
            int largerValue = num1;
            num1 = num2;
            num2 = largerValue;
        }
        if(num1 % 2 == 0 && num2 % 2 == 0){
            return 2 * gcd((num1/2), (num2/2));
        }
        if(num1 % 3 == 0 && num2 % 3 == 0){
            return 3 * gcd((num1/3), (num2/3));
        }
        if(num1 % 5 == 0 && num2 % 5 == 0){
            return 5 * gcd((num1/5), (num2/5));
        }
        if(num1 % 7 == 0 && num2 % 7 == 0){
            return 7 * gcd((num1/7), (num2/7));
        }
        if(num1 % 11 == 0 && num2 % 11 == 0){
            return 11 * gcd((num1/11), (num2/11));
        }
        return 1;
    }
    public static void main (String [] Args){
        System.out.println(greatestCommonDivisor.gcd(80,56));
    }
}
