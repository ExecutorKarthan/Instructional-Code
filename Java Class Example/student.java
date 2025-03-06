public class student {
 
    String firstName = "";
    String lastName = "";
    int grade;
    String [] courses = new String[8];
    // Creating constructor
    student(String firstName, String lastName, int grade, String [] inputedCourses)
    {
        for(int index = 0; index < inputedCourses.length; index++){
            this.courses[index] = inputedCourses[index];
        }

    }
    // Function to add the members of the class

}