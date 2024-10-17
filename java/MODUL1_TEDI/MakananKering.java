// Don't delete any comments below!!!
public class MakananKering {
    // Todo : Create private attribute of MakananKering (nama, jumlah, harga, and brand)
    private String nama;
    private int jumlah;
    private double harga;
    private String brand;

    // Todo : Create Constructor of MakananKering
    public MakananKering(String nama, int jumlah, double harga, String brand){
        this.nama = nama;
        this.jumlah = jumlah;
        this.harga = harga;
        this.brand = brand;
    }

    // Todo : Create Getter and Setter
    public String getnama(){
        return nama;
    }
    public int getjumlah(){
        return jumlah;
    }
    public double getharga(){
        return harga;
    }
    public String getbrand(){
        return brand;
    }

    // Todo : Create Method ShowData
    public void tampilkanData(){
        System.out.println("Nama Makanan: " + getnama());
        System.out.println("Jumlah: " + getjumlah());
        System.out.println("Harga: " + getharga());
        System.out.println("brand: " + getbrand());
    }

}
