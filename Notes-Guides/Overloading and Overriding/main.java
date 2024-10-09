public class main{
    public static void main (String[] Args){
        Car moe = new Car("ginger", "Bugatti", "Moetown", 2008);

        System.out.println(moe);
        System.out.println(moe.getOwner());

        moe.setOwner("Self");

        System.out.println(moe.getOwner());

        moe.updateCarData("Self", "Brunette");

        System.out.println(moe.getOwner());
        System.out.println(moe.getColor());

        moe.updateCarData("Nolan's Land of Cars");
        System.out.println(moe.getOwner());
    }
}