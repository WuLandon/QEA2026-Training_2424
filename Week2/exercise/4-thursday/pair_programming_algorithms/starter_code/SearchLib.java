/**
 * Pair exercise — implement linearSearch and binarySearch.
 * Precondition: sorted ascending, may contain duplicates; return any matching index.
 */
public class SearchLib {

    public static int linearSearch(int[] sorted, int target) {
        for (int i = 0; i < sorted.length; i++) {
            if (sorted[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static int binarySearch(int[] sorted, int target) {
        int l = 0;
        int r = sorted.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (sorted[m] == target) {
                return m;
            }
            if (sorted[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return -1;
    }
}
