import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        
        // Take input
        Scanner sc = new Scanner(System.in);
        String name = sc.next();

        // Call/invoke method
        String result = greet(name);
        System.out.println(result);
    }

    static String greet(String name) {
        return "Hello " + name;
    }
}
