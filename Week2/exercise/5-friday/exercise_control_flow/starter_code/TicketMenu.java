import java.util.Scanner;

/**
 * Week 2 Exercise — menu-driven console (implement the menu loop).
 *
 * Compile: javac TicketMenu.java
 * Run:     java TicketMenu
 */
public class TicketMenu {

    public static void main(String[] args) {
        String[] tickets = {"BUG-101 Login timeout", "BUG-102 CSV import", "BUG-103 flaky assertion"};
        int[] priorities = {2, 2, 2}; // stretch: update in menu option 2

        try (Scanner in = new Scanner(System.in)) {
            boolean running = true;

            while (running) {
                System.out.println();
                System.out.println("QA Ticket Console");
                System.out.println("1. List tickets");
                System.out.println("2. Set priority");
                System.out.println("3. Summary");
                System.out.println("4. Quit");
                System.out.print("Choose an option: ");

                String choiceText = in.nextLine().trim();
                int choice;

                try {
                    choice = Integer.parseInt(choiceText);
                } catch (NumberFormatException ex) {
                    System.out.println("Invalid menu choice. Enter 1, 2, 3, or 4.");
                    continue;
                }

                switch (choice) {
                    case 1:
                        System.out.println("Tickets:");
                        for (int i = 0; i < tickets.length; i++) {
                            System.out.println((i + 1) + ". " + tickets[i] + " [priority " + priorities[i] + "]");
                        }
                        break;
                    case 2:
                        int ticketIndex = readIntInRange(in, "Enter ticket number (1-" + tickets.length + "): ", 1, tickets.length);
                        int priority = readIntInRange(in, "Enter priority (1-3): ", 1, 3);
                        priorities[ticketIndex - 1] = priority;
                        System.out.println("Updated " + tickets[ticketIndex - 1] + " to priority " + priority + ".");
                        break;
                    case 3:
                        int count = tickets.length;
                        System.out.println("There " + (count == 1 ? "is " : "are ") + count + " ticket" + (count == 1 ? "" : "s") + " in the queue.");
                        break;
                    case 4:
                        running = false;
                        System.out.println("Goodbye.");
                        break;
                    default:
                        System.out.println("Unknown option. Please choose 1, 2, 3, or 4.");
                        break;
                }
            }
        }
    }

    private static int readIntInRange(Scanner in, String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);

            if (!in.hasNextInt()) {
                System.out.println("Please enter a number.");
                in.nextLine();
                continue;
            }

            int value = in.nextInt();
            in.nextLine(); // consume newline after nextInt()

            if (value < min || value > max) {
                System.out.println("Enter a value from " + min + " to " + max + ".");
                continue;
            }

            return value;
        }
    }
}
