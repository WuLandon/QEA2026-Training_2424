/**
 * Week 2 Exercise — Calculator with static methods and overloads.
 *
 * Division by zero strategy (TODO — choose and implement):
 *   Option A: print error message and return Double.NaN
 *   Option B: return 0.0 and document why (not ideal for production)
 *
 * Compile: javac Calculator.java
 * Run:     java Calculator
 */
public class Calculator {

    /** Adds two double values. */
    public static double add(double a, double b) {
        return a + b;
    }

    /** Adds three double values. */
    public static double add(double a, double b, double c) {
        return a + b + c;
    }

    /** Subtracts {@code b} from {@code a}. */
    public static double subtract(double a, double b) {
        return a - b;
    }

    /** Multiplies two double values. */
    public static double multiply(double a, double b) {
        return a * b;
    }

    /**
     * Divides {@code a} by {@code b}.
     * Returns {@link Double#NaN} when {@code b} is zero to avoid an exception.
     */
    public static double divide(double a, double b) {
        if (b == 0) {
            System.out.println("Cannot divide by zero. Returning NaN.");
            return Double.NaN;
        }
        return a / b;
    }

    public static void main(String[] args) {
        System.out.println("add(2.0, 3.5) = " + add(2.0, 3.5));
        System.out.println("add(1.0, 2.0, 3.0) = " + add(1.0, 2.0, 3.0));
        System.out.println("subtract(10.0, 4.0) = " + subtract(10.0, 4.0));
        System.out.println("multiply(6.0, 7.0) = " + multiply(6.0, 7.0));
        System.out.println("divide(20.0, 5.0) = " + divide(20.0, 5.0));
        System.out.println("divide(5.0, 0.0) = " + divide(5.0, 0.0));
    }
}
