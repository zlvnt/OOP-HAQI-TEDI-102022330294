public class Burung extends Hewan {
    private String warnaBulu;

    public Burung(String nama, int umur, String warnaBulu) {
        super(nama, umur);
        this.warnaBulu = warnaBulu;
    }
    public void suara() {
        System.out.println(nama + " berkicau seperti: Cuit-cuit-cuit");
    }
    public void infoHewan() {
        super.infoHewan();
        System.out.println("Warna bulu:" + warnaBulu);
    }
    public void halo() {
        System.out.println("\nCuit! Aku burung berwarna " + warnaBulu + " yang bernama " + nama);
    }
}