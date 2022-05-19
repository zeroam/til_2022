package chap02;

import java.util.Arrays;
import java.util.List;

public class PrettyPrintApple {
    public static void main(String[] args) {
        List<Apple> inventory = Arrays.asList(
                new Apple(80, FilteringApples.Color.GREEN),
                new Apple(155, FilteringApples.Color.GREEN),
                new Apple(120, FilteringApples.Color.RED)
        );

        prettyPrintApple(inventory, new AppleFancyFormatter());
        prettyPrintApple(inventory, new AppleSimpleFormatter());
    }

    public static void prettyPrintApple(List<Apple> inventory, AppleFormatter formatter) {
        for (Apple apple : inventory) {
            String output = formatter.accept(apple);
            System.out.println(output);
        }
    }

    interface AppleFormatter {
        String accept(Apple apple);
    }

    public static class AppleFancyFormatter implements AppleFormatter {
        @Override
        public String accept(Apple apple) {
            String characteristic = apple.getWeight() > 150 ? "heavy" : "light";
            return "A " + characteristic + " " + apple.getColor() + " apple";
        }
    }

    public static class AppleSimpleFormatter implements AppleFormatter {
        @Override
        public String accept(Apple apple) {
            return "An apple of " + apple.getWeight() + "g";
        }
    }

}
