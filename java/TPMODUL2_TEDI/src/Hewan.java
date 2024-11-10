public class Hewan {
    protected String nama;
    protected int umur;

    public Hewan(String nama, int umur) {
        this.nama = nama;
        this.umur = umur;
    }
    public void suara() {
        System.out.println(nama + " mengeluarkan suara yang khas.");
    }
    public void makan() {
        System.out.println(nama + " sedang menikmati makanannya.");
    }
    public void makan(String makanan) {
        System.out.println(nama + " sedang menikmati " + makanan + ".");
    }
    public void infoHewan() {
        System.out.println("Nama: " + nama + ", Umur: " + umur + " tahun.");
    }
    public void halo() {
        System.out.println("\nHalo! Aku adalah hewan bernama " + nama + ".");
    }
}