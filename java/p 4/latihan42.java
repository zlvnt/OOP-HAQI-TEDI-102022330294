public class latihan42 {
    private String nama;
    private int nik;
    private String status;
    private String jk;

    public latihan42(String nama, int nik, String status, String jk) {
        this.nama = nama;
        this.nik = nik;
        this.status = status;
        this.jk = jk;
    }

    public int hitungTunjangan() {
        if (status.equalsIgnoreCase("menikah") && jk.equalsIgnoreCase("Laki-laki")) {
            return 25000;
        } else if (status.equalsIgnoreCase("menikah") && jk.equalsIgnoreCase("Perempuan")) {
            return 20000;
        } else {
            return 15000;
        }
    }

    public int hitungPendapatanTotal() {
        int tunjangan = hitungTunjangan();
        int pendapatanPokok = jk.equalsIgnoreCase("Perempuan") ? 5000 : 6000;
        return tunjangan + pendapatanPokok;
    }
    
    public String getNama() {
        return nama;
    }
    public int getNik() {
        return nik;
    }
    public String getJenisKelamin() {
        return jk;
    }
}
