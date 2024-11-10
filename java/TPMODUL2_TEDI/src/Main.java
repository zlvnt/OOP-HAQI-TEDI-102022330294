public class Main {
    public static void main(String[] args) {
        System.out.println("\nDetail hewan");
        Kucing kucing = new Kucing("Tara", 3, "Persia");
        kucing.halo();
        kucing.suara();
        kucing.makan();
        kucing.makan("wiskas");
        Burung burung = new Burung("Faris", 2, "Hijau");
        burung.halo();
        burung.suara();
        burung.makan();
        burung.makan("buah");
        System.out.println("");
        kucing.infoHewan();
        burung.infoHewan();
    }
}
