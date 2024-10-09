public class Car {
    private String color;
    private String make;
    private String model;
    private String owner;
    private int year;

    public Car(String enteredColor, String enteredMake, String enteredModel, int enteredYear){
        this.color = enteredColor;
        this.make = enteredMake;
        this.model = enteredModel;
        this.year = enteredYear;
    }

    public void updateCarData(String newOwner){
        this.owner = newOwner;
    }

    public void updateCarData(String newOwner, String newColor){
        this.color = newColor;
        this.owner = newOwner;
    }

    public void setColor(String newColor){
        this.color = newColor;
    }

    public void setOwner(String newOwner){
        this.owner = newOwner;
    }

    public void setYear(int newYear){
        this.year = newYear;
    }

    public String getOwner(){
        return this.owner;
    }

    public String getColor(){
        return this.color;
    }

    public int getYear(){
        return this.year;
    }

}
