package org.example;

public class launcher {
    public static void main(String[] args) {
            DemoClassesObjects.Student a = new DemoClassesObjects.Student("Asha");
            DemoClassesObjects.Student b = new DemoClassesObjects.Student("Ben");
            System.out.println(a);
            System.out.println(b);

            System.out.println("totalStudents (static):" + DemoClassesObjects.Student.getTotalStudents());
            DemoClassesObjects.Student c = new DemoClassesObjects.Student("Chen");
            System.out.println("identity a==c ? " + a.equals(c));
        }
    }

