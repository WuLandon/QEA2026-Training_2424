/** Lab 2 driver — run after Student is implemented. */
public class StudentDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Ava", "Computer Science");
        Student s2 = new Student("Ben", "Mathematics");
        Student s3 = new Student("Cara", "Data Analytics");

        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
        System.out.println("Enrollment count: " + Student.getEnrollmentCount());

        Student sameReference = s1;
        System.out.println("s1 == sameReference: " + (s1 == sameReference));
        System.out.println("s1.equals(sameReference): " + s1.equals(sameReference));

        System.out.println("s1 == s2: " + (s1 == s2));
        System.out.println("s1.equals(s2): " + s1.equals(s2));
    }
}
