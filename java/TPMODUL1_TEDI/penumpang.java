public class penumpang {
    private String NIK;
    private String namaDepan;
    private String namaBelakang;

    // konsetruktor
    public penumpang(String NIK, String namaDepan, String namaBelakang) {
        this.NIK = NIK;
        this.namaDepan = namaDepan;
        this.namaBelakang = namaBelakang;
    }

    public String getNIK() { return NIK; }
    public String getNamaDepan() { return namaDepan; }
    public String getNamaBelakang() { return namaBelakang; }

    public void lihatpenumpang() {
        System.out.println("NIK: " + NIK);
        System.out.println("Nama: " + namaDepan + " " + namaBelakang);
    }
}
