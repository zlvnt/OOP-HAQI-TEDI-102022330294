public class bmm extends nk {

    private String bahan;

    public bmm(String nama, int jumlah, double harga, String bahan) {
        super(nama, jumlah, harga);
        this.bahan = bahan;
    }

    public void tampilkanData(){
        System.out.println("Nama Makanan: " + getnama());
        System.out.println("Jumlah: " + getjumlah());
        System.out.println("Harga: " + getharga());
        System.out.println("bahan: " + bahan);
    }

}
