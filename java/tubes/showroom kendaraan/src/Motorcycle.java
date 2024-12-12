
public class Motorcycle extends Vehicle {
    private int engineCC;
    private String category;

    // Constructor
    public Motorcycle(String brand, String model, int price, int stockQuantity, int engineCC, String category) {
        super(brand, model, price, stockQuantity);
        this.engineCC = engineCC;
        this.category = category;
    }

    // Getter and Setter
    public int getEngineCC() {
        return engineCC;
    }

    public String getCategory() {
        return category;
    }

    // Override toString to include Motorcycle-specific attributes
    @Override
    public String toString() {
        return super.toString() + ", Engine CC: " + engineCC + ", Category: " + category;
    }
}
