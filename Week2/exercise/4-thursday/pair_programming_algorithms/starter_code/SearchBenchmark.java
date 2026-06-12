/**
 * Pair exercise — build sorted array, pick target, time both searches.
 * TODO: complete main after SearchLib is implemented.
 */
import java.util.Random;

public class SearchBenchmark {

    public static void main(String[] args) {
        int n = 1_000_000;
        int[] arr = buildSortedEvens(n);

        Random rand = new Random();
        int targetIndex = rand.nextInt(n);
        int target = arr[targetIndex];

        long startLinear = System.nanoTime();
        int linearResult = SearchLib.linearSearch(arr, target);
        long endLinear = System.nanoTime();

        long startBinary = System.nanoTime();
        int binaryResult = SearchLib.binarySearch(arr, target);
        long endBinary = System.nanoTime();

        double linearMs = (endLinear - startLinear) / 1_000_000.0;
        double binaryMs = (endBinary - startBinary) / 1_000_000.0;

        System.out.println("N: " + n);
        System.out.println("Target: " + target);
        System.out.println("Expected index: " + targetIndex);

        System.out.println("Linear search index: " + linearResult);
        System.out.println("Linear search time: " + linearMs + " ms");

        System.out.println("Binary search index: " + binaryResult);
        System.out.println("Binary search time: " + binaryMs + " ms");
    }

    static int[] buildSortedEvens(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i * 2;
        }
        return arr;
    }
}
