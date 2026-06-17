package banking;

public class BankingDemo {
    public static void main(String[] args) throws Exception {
        
        Bank bank = new Bank();

        try {
             // Success path
            bank.openAccount("A1", 500.0);
            bank.openAccount("A2", 100.0);

            bank.transfer("A1", "A2", 200.0);

            System.out.println("Transfer successful.");
            System.out.println(
                "A1 balance: " +
                bank.getAccount("A1").getBalance()
            );
            System.out.println(
                "A2 balance: " +
                bank.getAccount("A2").getBalance()
            );
            
            // Checked exception: insufficient funds
            bank.transfer("A1", "A2", 1000.0);      

        } catch (InsufficientFundsException e) {

            System.out.println(
                "Insufficient funds. Shortfall: $" +
                e.getShortfall()
            );

        } catch (InvalidAccountException e) {

            System.out.println(
                "Account error: " +
                e.getMessage()
            );
        }

        try {
            // Checked exception: invalid account
            bank.getAccount("DOES_NOT_EXIST");

        } catch (InvalidAccountException e) {

            System.out.println(
                "Caught invalid account: " +
                e.getMessage()
            );
        }

        // Unchecked exception: negative amount deposit
        try {
            bank.getAccount("A1").deposit(-50.0);
        } catch (IllegalArgumentException e) {

            System.out.println(
                "Caught unchecked exception: " +
                e.getMessage()
            );
        }
    }
}
