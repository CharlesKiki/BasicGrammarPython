
public class ToyBuilder {
    public static ToyHouse buildToyHouse() {
        ToyHouse toyHouse = new ToyHouse();
        toyHouse.setPrice(100);
        toyHouse.setColor("yellow");
        return toyHouse;
    }

    public static ToyCar buildToyCar() {
        ToyCar toyCar = new ToyCar();
        toyCar.setPrice(25.00);
        toyCar.setColor("red");
        toyCar.move();
        return toyCar;
    }

    public static ToyPlane buildToyPlane() {
        ToyPlane toyPlane = new ToyPlane();
        toyPlane.setPrice(125.00);
        toyPlane.setColor("white");
        toyPlane.move();
        toyPlane.fly();
        return toyPlane;
    }
}
