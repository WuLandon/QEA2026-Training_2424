package banking;

import java.util.HashMap;
import java.util.Map;

public class Bank {

    private Map<String, Account> accounts = new HashMap<>();

    public void openAccount(String id, double initialDeposit) throws InvalidAccountException {
        if (id == null || id.isBlank()) {
            throw new InvalidAccountException("Account id cannot be blank.");
        }

        if (accounts.containsKey(id)) {
            String msg = String.format("Account with id %s already exists", id);
            throw new InvalidAccountException(msg);
        }

        accounts.put(id, new Account(id, initialDeposit));
    }

    public Account getAccount(String id) throws InvalidAccountException {
        if (!accounts.containsKey(id)) {
            String msg = String.format("Account with id %s not found.", id);
            throw new InvalidAccountException(msg);
        }

        return accounts.get(id);
    }

    public void transfer(String fromId, String toId, double amount)
            throws InvalidAccountException, InsufficientFundsException {
        
        Account fromAccount = getAccount(fromId);
        Account toAccount = getAccount(toId);

        fromAccount.withdraw(amount);
        toAccount.deposit(amount);
    }
}
