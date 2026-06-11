package com.revature;

public class StringDemo {
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = new String("Hello");

        String s11 = s1.concat(" World");
        
        System.out.println(s11);
        System.out.println(s11.length());

        StringBuffer sBuffer = new StringBuffer("Hello");
        sBuffer.append("World");
        sBuffer.insert(2, "abcd");

    }
}
