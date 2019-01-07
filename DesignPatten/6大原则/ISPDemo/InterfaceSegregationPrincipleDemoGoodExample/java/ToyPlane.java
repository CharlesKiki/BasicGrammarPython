
public class ToyPlane implements Toy, Movable, Flyable {
    double price;
    String color;

    public void setPrice(double price) {
        this.price = price;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void move() {
        System.out.println("ToyPlane: Start moving plane.");
    }

    public void fly() {
        System.out.println("ToyPlane: Start flying plane.");
    }

    @Override
    public String toString() {
        return "ToyPlane: Movable and flyable toy plane - Price: " + price + " Color: " + color;
    }
}
