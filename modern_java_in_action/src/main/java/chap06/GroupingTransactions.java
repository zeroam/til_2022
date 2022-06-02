package chap06;

import java.util.*;
import java.util.stream.Collectors.*;

import static java.util.stream.Collectors.*;

public class GroupingTransactions {

    public static List<Transaction> transactions = Arrays.asList(
            new Transaction(Currency.EUR, 1500.0),
            new Transaction(Currency.USD, 2300.0),
            new Transaction(Currency.GBP, 9900.0),
            new Transaction(Currency.EUR, 1100.0),
            new Transaction(Currency.JPY, 7800.0),
            new Transaction(Currency.CHF, 6700.0),
            new Transaction(Currency.EUR, 5600.0),
            new Transaction(Currency.USD, 4500.0),
            new Transaction(Currency.CHF, 3400.0),
            new Transaction(Currency.GBP, 3200.0),
            new Transaction(Currency.USD, 4600.0),
            new Transaction(Currency.JPY, 5700.0),
            new Transaction(Currency.EUR, 6800.0)
    );

    public static void main(String[] args) {
//        groupImperatively();
//        groupFunctionally();
        example1();
    }

    private static void groupImperatively() {
        Map<Currency, List<Transaction>> transactionByCurrencies = new HashMap<>();
        for (Transaction transaction : transactions) {
            Currency currency = transaction.getCurrency();
            List<Transaction> transactionsForCurrency = transactionByCurrencies.get(currency);
            if (transactionsForCurrency == null) {
                transactionsForCurrency = new ArrayList<>();
                transactionByCurrencies.put(currency, transactionsForCurrency);
            }
            transactionsForCurrency.add(transaction);
        }

        System.out.println(transactionByCurrencies);
    }

    private static void groupFunctionally() {
        Map<Currency, List<Transaction>> transactionByCurrencies = transactions.stream().collect(groupingBy(Transaction::getCurrency));
        System.out.println(transactionByCurrencies);
    }

    private static void example1() {
        // 통화별로 트랜잭션을 그룹화한 다음에 해당 통화로 일어난 모든 트랜잭션 합계를 계산
        Map<Currency, Double> result = transactions.stream().collect(
                groupingBy(Transaction::getCurrency,
                        summingDouble(Transaction::getValue)));
        System.out.println(result);
    }

    private static void example2() {
        // 트랜잭션을 비싼 트랜잭션과 저렴한 트랜잭션 두 그룹으로 분류
    }

    private static void example3() {
        // 트랜잭션을 도시 등 다 수준으로 그룹화, 각 트랜잭션이 비싼지 저렴한지 구분
    }


    public static class Transaction {
        private final Currency currency;
        private final double value;

        public Transaction(Currency currency, double value) {
            this.currency = currency;
            this.value = value;
        }

        public Currency getCurrency() {
            return currency;
        }

        public double getValue() {
            return value;
        }

        @Override
        public String toString() {
            return "Transaction{" +
                    "currency=" + currency +
                    ", value=" + value +
                    '}';
        }
    }

    public enum Currency {
        EUR, USD, JPY, GBP, CHF
    }
}

