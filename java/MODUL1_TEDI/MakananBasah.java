// Don't delete any comments below!!!
public class MakananBasah {
    // Todo : Create private attribute of MakananKering (nama, jumlah, harga, and bahan)
    private String nama;
    private int jumlah;
    private double harga;
    private String bahan;

    // Todo : Create Constructor of MakananBasah
    public MakananBasah(String nama, int jumlah, double harga, String bahan){
        this.nama = nama;
        this.jumlah = jumlah;
        this.harga = harga;
        this.bahan = bahan;
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
    public String getbahan(){
        return bahan;
    }

    // Todo : Create Method ShowData
    public void tampilkanData(){
        System.out.println("Nama Makanan: " + getnama());
        System.out.println("Jumlah: " + getjumlah());
        System.out.println("Harga: " + getharga());
        System.out.println("bahan: " + getbahan());
    }

}
