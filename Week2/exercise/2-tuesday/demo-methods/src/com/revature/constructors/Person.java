package com.revature.constructors;

public class Person {

    // Instance variables
    private String name;
    private int age;

    // Default Constructor
    public Person() {

    }

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String displayPerson() {
        return  "name: " + this.name + ", Age: " + this.age;
    }
}
