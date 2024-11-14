class Komputer {

    // To do: Buatlah 3 variable sesuai ketentuan
    protected int jumlahkomputer;
    protected String namaWarnet;
    protected float hargaperJam;
    // To do: Buatlah constructor pada class Komputer
    public Komputer(int jumlahkomputer, String namaWarnet, float hargaperJam) {
        this.jumlahkomputer = jumlahkomputer;
        this.namaWarnet = namaWarnet;
        this.hargaperJam = hargaperJam;
    }
    // To do: Buatlah Method Informasi dengan isi yang sesuai dengan ketentuan 
    public void Informasi(){
        System.out.println("Jumlah Kompurter: "+ jumlahkomputer);
        System.out.println("Nama Warnet : "+ namaWarnet);
        System.out.println("Harga per jam: "+ hargaperJam);
    }
}
    // (boleh berbeda dengan output jurnal tetapi dengan cangkupan masih sesuai oleh materi modul!)
