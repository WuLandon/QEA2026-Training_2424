package com.revature.constructors;

public class PersonManager {
    public static void main(String[] args) {
        Person person = new Person("Landon", 23);
        System.out.println(person.displayPerson());

        Person p = new Person();
        p.setName("LW");
        p.setAge(23);
        System.out.println(p.displayPerson());


    }
}
