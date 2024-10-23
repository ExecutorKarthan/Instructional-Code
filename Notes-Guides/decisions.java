public class decisions {
    public static void main(String Args[]){
        boolean dehydrated = false;
        boolean waterAvailable = false;
        boolean waterDrinkable = false;

        double dehydratedValue = Math.random();
        if(dehydratedValue < 0.5){
            dehydrated = true;
        }

        double waterValue = Math.random();
        if(waterValue > 0.5){
            waterAvailable = true;
        }

        if (waterAvailable){
            double waterSanitation = Math.random();
            if(waterSanitation > 0.5){
                waterDrinkable = true;
            }
        }

        System.out.println((false && false));

        System.out.println("Thirsty is: " + dehydrated);

        System.out.println("Water nearby is: " + waterAvailable);

        if(dehydrated && waterAvailable && waterDrinkable){
            System.out.println("Drink up homie!");
        }
        // else if(dehydrated && (!waterAvailable || !waterDrinkable)){
           else if(dehydrated && !(waterAvailable && waterDrinkable)){
            System.out.print("No water to quench yo thirst. RIP!");
        }
        else if(!dehydrated && waterAvailable){
            System.out.print("Not thristy bro? Thats cool");
        }
        else{
            System.out.print("You either don't need to or cannot get water to drink. That sucks!");
        }


    }
}
