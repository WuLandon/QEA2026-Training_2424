import java.util.Objects;

/**
 * Lab 2 — Student. Replace UnsupportedOperationException bodies with real logic.
 * See ../README.md
 */
public class Student {
    private static int nextId = 0;
    private static int enrollmentCount = 0;
    private final int id;
    private String name;
    private String program;

    public Student(String name, String program) {
        this.id = ++nextId;
        this.name = name;
        this.program = program;
        enrollmentCount++;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getProgram() {
        return program;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setProgram(String program) {
        this.program = program;
    }

    public static int getEnrollmentCount() {
        return enrollmentCount;
    }

    @Override
    public String toString() {
        return "Student{id=" + id + ", name='" + name + "', program='" + program + "'}";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Student)) {
            return false;
        }
        Student student = (Student) o;
        return id == student.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
