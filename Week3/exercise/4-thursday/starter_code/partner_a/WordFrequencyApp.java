import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;

/**
 * Partner A — word counts + sorted unique words.
 * See ../../README.md
 */
public class WordFrequencyApp {

    static final String SAMPLE =
        "Java collections maps sets queues lambdas\n"
        + "Java maps and sets and more Java\n";

    public static void main(String[] args) {

        // Change to false to run the original implementation
        boolean useRefactored = true;

        // Tokenize SAMPLE, convert to lower-case, and count words
        Map<String, Integer> counts = new HashMap<>();

        String lower = SAMPLE.toLowerCase();
        String[] words = lower.split("[^a-zA-Z]+");

        for (String w : words) {
            if (!w.isEmpty()) {
                counts.put(w, counts.getOrDefault(w, 0) + 1);
            }
        }

        // Add all distinct words to vocabulary
        TreeSet<String> vocabulary = new TreeSet<>();
        vocabulary.addAll(counts.keySet());

        System.out.println("Word Counts:");

        if (useRefactored) {

            // ==================== REFACTORED ====================
            counts.forEach((word, count) ->
                System.out.println(word + " = " + count));

        } else {

            // ==================== ORIGINAL ====================
            for (Map.Entry<String, Integer> entry : counts.entrySet()) {
                System.out.println(entry.getKey() + " = " + entry.getValue());
            }
        }

        // Print top N frequent words
        int n = 3;

        List<Map.Entry<String, Integer>> entries =
            new ArrayList<>(counts.entrySet());

        System.out.println("\nTop " + n + " Words:");

        if (useRefactored) {

            // Sort entries by frequency, highest count first
            Comparator<Map.Entry<String, Integer>> byFrequencyDesc =
                Comparator.comparing(Map.Entry<String, Integer>::getValue)
                          .reversed();

            entries.sort(byFrequencyDesc);

            // Print top N using stream + lambda
            entries.stream()
                   .limit(n)
                   .forEach(entry ->
                       System.out.println(
                           entry.getKey() + " = " + entry.getValue()));

        } else {

            // ==================== ORIGINAL ====================
            entries.sort((e1, e2) ->
                Integer.compare(e2.getValue(), e1.getValue()));

            for (int i = 0; i < Math.min(entries.size(), n); i++) {
                Map.Entry<String, Integer> entry = entries.get(i);
                System.out.println(
                    entry.getKey() + " = " + entry.getValue());
            }
        }

        System.out.println("\nVocabulary: " + vocabulary);
        System.out.println("First word: " + vocabulary.first());
        System.out.println("Last word: " + vocabulary.last());
    }
}