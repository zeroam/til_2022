package chap02;

public class Apple {

    private int weight = 0;
    private FilteringApples.Color color;

    public Apple(int weight, FilteringApples.Color color) {
        this.weight = weight;
        this.color = color;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public FilteringApples.Color getColor() {
        return color;
    }

    public void setColor(FilteringApples.Color color) {
        this.color = color;
    }

    @SuppressWarnings("boxing")
    @Override
    public String toString() {
        return String.format("Apple{color=%s, weight=%d}", color, weight);
    }
}
