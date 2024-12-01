class Penerbangan {
    private final String kodePenerbangan;
    private final String asal;
    private final String tujuan;
    private final String jamBerangkat;
    private final String jamTiba;
    private final int harga;

    public Penerbangan(String kode, String asal, String tujuan, String berangkat, String tiba, int harga) {
        this.kodePenerbangan = kode;
        this.asal = asal;
        this.tujuan = tujuan;
        this.jamBerangkat = berangkat;
        this.jamTiba = tiba;
        this.harga = harga;
    }

    public void tampilDaftarPenerbangan() {
        System.out.println(kodePenerbangan + " | " + asal + " -> " + tujuan + " | " +
                jamBerangkat + " - " + jamTiba + " | Harga: Rp " + harga);
    }
}
