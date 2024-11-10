public class Kucing extends Hewan {
    private String ras;

    public Kucing(String nama, int umur, String ras) {
        super(nama, umur);
        this.ras = ras;
    }
    public void suara() {
        System.out.println(nama + " mengeong: Miau miau");
    }
    public void infoHewan() {
        super.infoHewan();
        System.out.println("Ras nya adalah: " + ras);
    }
    public void halo() {
        System.out.println("\nmiaw Hai, aku kucing lucu bernama " + nama + ". Ras ku adalah " + ras);
    }
}
