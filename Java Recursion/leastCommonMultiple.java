public class leastCommonMultiple {
    public static int lcm(int num1, int num2, int multiple){
        if(num1 > num2){
            int largerValue = num1;
            num1 = num2;
            num2 = largerValue;
        }
        if(num2*multiple % num1 == 0){
            return num2*multiple;
        }
        if(num2*multiple % num1 != 0){
            multiple++;
            return lcm(num1, num2, multiple);
        }
        return num1 * num2;
    }
    public static void main (String [] Args){
        System.out.println(leastCommonMultiple.lcm(20,8, 1));
    }
}
