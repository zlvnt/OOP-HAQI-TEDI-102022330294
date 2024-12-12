public class Car extends Vehicle {
    private String fuelType;
    private int seatingCapacity;

    // Constructor
    public Car(String brand, String model, int price, int stockQuantity, String fuelType, int seatingCapacity) {
        super(brand, model, price, stockQuantity);
        this.fuelType = fuelType;
        this.seatingCapacity = seatingCapacity;
    }

    // Getter and Setter
    public String getFuelType() {
        return fuelType;
    }

    public int getSeatingCapacity() {
        return seatingCapacity;
    }

    // Override toString to include Car-specific attributes
    @Override
    public String toString() {
        return super.toString() + ", Fuel Type: " + fuelType + ", Seats: " + seatingCapacity;
    }
}