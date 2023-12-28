public class Calculator {

    // Method to add two numbers
    public static int add(int a, int b) {
        return a + b;
    }

    // Method to subtract two numbers
    public static int subtract(int a, int b) {
        return a - b;
    }

    // Method to multiply two numbers
    public static int multiply(int a, int b) {
        return a * b;
    }

    // Method to divide two numbers
    public static double divide(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Divider cannot be 0");
        }
        return (double) a / b;
    }

    public static void main(String[] args) {
        // Test the divide and subtract methods
        divide(2, 1);
        subtract(7, 6);
    }
}