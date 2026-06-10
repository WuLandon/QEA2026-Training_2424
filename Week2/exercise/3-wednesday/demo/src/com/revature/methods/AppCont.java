package com.revature.methods;

public class AppCont {
    public static void main(String[] args) {
        System.out.println("Sum = " + sum(2, 3));
        System.out.println("Sum = " + sum(2, 3, 4));
        
        AppCont appCont = new AppCont();
        System.out.println(appCont.sayHello("Landon"));
    }

    // variable arguments accepts any number of arguments
    public static int sum(int ...numbers) {
        int total = 0;
        for (int num: numbers) {
            total += num;
        }
        return total;
    }

    public String sayHello(String name) {
        return "Hello " + name;
    }
}
