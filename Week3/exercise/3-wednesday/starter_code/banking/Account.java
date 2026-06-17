package banking;

public class Account {
    private String id;
    private double balance;

    public Account(String id, double balance) {
        this.id = id;
        this.balance = balance;
    }

    public String getId() {
        return id;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("Deposit amount cannot be negative.");
        }

        balance += amount;
    }

    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount < 0) {
            throw new IllegalArgumentException("Withdrawal amount cannot be negative.");
        }

        if (amount > balance) {
            double shortfall = amount - balance;
            throw new InsufficientFundsException("Insufficient funds.", shortfall);
        }
        
        balance -= amount;
    }
}
