package todo;

public class TodoDemo {
    public static void main(String[] args) {

        TodoListManager todoList = new TodoListManager();

        todoList.addTask("Buy groceries");
        todoList.addTask("Finish Lab 2");
        todoList.addTask("Go to the gym");

        System.out.println("Tasks:");
        System.out.println(todoList.listTasks());

        todoList.completeTask(1);

        System.out.println("\nAfter completing task 1:");
        System.out.println(todoList.listTasks());

        System.out.println("\nTotal tasks: " + todoList.size());
    }
}