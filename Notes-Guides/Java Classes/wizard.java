public class wizard {
    private String robeColor = "grey";
    private String[] spells = new String[10];
    private int beardLength = 0;

    public wizard(String enteredRobeColor, String[] enteredSpells, int enteredBeardLength){
        this.robeColor = enteredRobeColor;
        this.spells = enteredSpells;
        this.beardLength = enteredBeardLength;
    }

    public String getRobeColor(){
        return this.robeColor;
    }

    public void setRobeColor(String newColor){
        this.robeColor = newColor;
    }

    public int getBeardLength(){
        return this.beardLength;
    }

    public void setBeardLength(){
        this.beardLength += 1;
    }

    public int damage(){
        int result = (int) Math.floor(Math.random()*20);
        return result;
    }

}
