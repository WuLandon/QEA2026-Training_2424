package todo;

import java.util.ArrayList;
import java.util.List;

public class TodoListManager {
    private final List<String> tasks = new ArrayList<>();

    public void addTask(String task) {
        tasks.add(task);
    }

    public String getTask(int index) {
        if (index < 0 || index >= tasks.size()) {
            throw new IndexOutOfBoundsException("Invalid task index: " + index);
        }
        
        return tasks.get(index);
    }

    public void completeTask(int index) {
        if (index < 0 || index >= tasks.size()) {
            throw new IndexOutOfBoundsException("Invalid task index: " + index);
        }

        tasks.remove(index);
    }

    public List<String> listTasks() {
        return new ArrayList<>(tasks);
    }

    public int size() {
        return tasks.size();
    }
}
