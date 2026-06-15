import java.util.Arrays;

/**
 * Lab 1 — Arrays & loops. Implement the bodies.
 * See ../README.md
 */
public class ArrayLoopsLab {

    /** Reverse array in place. */
    public static void reverse(int[] data) {
        int l = 0;
        int r = data.length - 1;
        int temp;

        while (l < r) {
            temp = data[l];
            data[l] = data[r];
            data[r] = temp;

            l++;
            r --;
        }
    }

    /** Smallest element; illegal if null or empty. */
    public static int min(int[] data) {
        if (data.length == 0 || data == null) {
            throw new IllegalArgumentException();
        }

        int min_num = data[0];

        for (int num : data) {
            if (num < min_num) {
                min_num = num;
            }
        }
        return min_num;
    }

    /** Largest element; illegal if null or empty. */
    public static int max(int[] data) {
        if (data.length == 0 || data == null) {
            throw new IllegalArgumentException();
        }

        int max_num = data[0];

        for (int num : data) {
            if (num > max_num) {
                max_num = num;
            }
        }
        return max_num;
    }

    /** In-place ascending sort using nested loops only (no Arrays.sort). */
    public static void sortAscending(int[] data) {
        for (int i = 0; i < data.length - 1; i++) {
            for (int j = i + 1; j < data.length; j++) {
                if (data[j] < data[i]) {
                    int temp = data[j];
                    data[j] = data[i];
                    data[i] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] data = {5, 2, 8, 1, 3};

        System.out.println("Original: " + Arrays.toString(data));

        reverse(data);
        System.out.println("Reversed: " + Arrays.toString(data));

        sortAscending(data);
        System.out.println("Sorted:   " + Arrays.toString(data));

        System.out.println("Min: " + min(data));
    }
}
