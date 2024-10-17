public class nk {
    
    private String nama;
    private int jumlah;
    private double harga;

    public nk(String nama, int jumlah, double harga) {
        this.nama = nama;
        this.jumlah = jumlah;
        this.harga = harga;
    }

    public String getnama() {
        return nama;
    }

    public int getjumlah() {
        return jumlah;
    }

    public double getharga() {
        return harga;
    }
}
