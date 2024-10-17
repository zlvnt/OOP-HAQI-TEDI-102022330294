public class km extends nk{

    private String brand;

    public km(String nama, int jumlah, double harga, String brand) {
        super(nama, jumlah, harga);
        this.brand = brand;
    }

    public void tampilkanData(){
        System.out.println("Nama Makanan: " + getnama());
        System.out.println("Jumlah: " + getjumlah());
        System.out.println("Harga: " + getharga());
        System.out.println("brand: " + brand);
    }
}
