import java.util.PriorityQueue;
import java.util.Queue;

/** Partner B — drain PriorityQueue in priority order. */
public class TaskQueueApp {
    public static void main(String[] args) {
        Queue<Task> q = new PriorityQueue<>();
        
        // Offer tasks out of order
        q.offer(new Task(4, "Do laundry"));
        q.offer(new Task(1, "Finish project"));
        q.offer(new Task(3, "Buy groceries"));
        q.offer(new Task(2, "Study for exam"));
        q.offer(new Task(5, "Watch TV"));

        // Peek demo (does not remove)
        System.out.println("Peek: " + q.peek());
        System.out.println("Queue size after peek: " + q.size());
        
        System.out.println("\nPolling tasks:");

        // Drain queue in priority order
        while (!q.isEmpty()) {
            System.out.println(q.poll());
        }

        System.out.println("\nQueue empty? " + q.isEmpty());
    }
}
