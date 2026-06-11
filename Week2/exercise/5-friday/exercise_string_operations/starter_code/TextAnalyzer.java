import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * Week 2 Exercise — String analysis (implement TODO methods).
 *
 * Compile: javac TextAnalyzer.java
 * Run:     java TextAnalyzer
 */
public class TextAnalyzer {

    public static int wordCount(String text) {
        if (text == null || text.trim().isEmpty()) {
            return 0;
        }

        // Remove leading/trailing whitespace
        // Split the string into an array of strings wherever there is one or more whitespace characters.
        // Gets the number of elements in the array.
        return text.trim().split("//s+").length;
    }

    public static boolean isPalindrome(String token) {
        if (token == null) {
            return false;
        }

        token = token.trim().toLowerCase();

        for (int i = 0; i < token.length() / 2; i++) {
            int left = i;
            int right = token.length() - 1 - i;
            if (token.charAt(left) != token.charAt(right)) {
                return false;
            }
        }
        return true;
    }

    public static int countOccurrences(String haystack, String needle) {
        if (haystack == null || needle == null || needle.isEmpty()) {
            return 0;
        }

        int count = 0;
        int idx = 0;

        while ((idx = haystack.indexOf(needle, idx)) != -1) {
            count++;
            idx += needle.length();
        }

        return count;
    }

    public static void main(String[] args) throws IOException {
        Path p = Path.of("sample.txt");
        String body = Files.readString(p);
        System.out.println("words=" + wordCount(body));
        System.out.println("palindrome(Radar)=" + isPalindrome("Radar"));
        System.out.println("occurrences of 'QA'=" + countOccurrences(body, "QA"));
    }
}
