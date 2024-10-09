import java.util.Scanner;

public class main{
    public static void main(String[] Args){
        Scanner scanObj = new Scanner(System.in);
        System.out.println("What is your x2 value? ");
        String x2ValueRaw = scanObj.nextLine();
        System.out.println(x2ValueRaw);
        Integer x2Value = Integer.valueOf(x2ValueRaw);
        System.out.println(x2Value);
        // D = square.root.of(x2 - x1)^2 + (y2 - y1)^2
    }
}