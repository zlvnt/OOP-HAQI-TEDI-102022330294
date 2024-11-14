class KomputerPremium extends Komputer {
    // To do: Buatlah 1 variable sesuai ketentuan
    protected boolean ruangPrivat;
    // To do: Buatlah constructor pada class KomputerPremium

    public KomputerPremium(int jumlahKomputer, String namaWarnet, float hargaPerJam, boolean ruangPrivat) {
        super(jumlahKomputer, namaWarnet, hargaPerJam);
        this.ruangPrivat = ruangPrivat;
    }
    // To do: Buatlah Method Informasi memakai Polymorphism Override dengan isi yang sesuai dengan ketentuan 
    // (boleh berbeda dengan output jurnal tetapi dengan cangkupan masih sesuai oleh materi modul!)
    @Override
    public void Informasi(){
        super.Informasi();
        if(ruangPrivat) {
            System.out.println("Status ruangan: Privat");
            System.out.println("fasiitas ruangan: ");
            System.out.println("Ruangan ber AC pribadi");
            System.out.println("Sofa gaming exclusive");
            System.out.println("komputer spesifikasi tinggi");
            System.out.println("konekis internet dedicate 100Mbps");
        }
        else{
            System.out.println("Status: ruangan standar");
            System.out.println("Fasilitas ruangan standar: ");
            System.out.println("biasa saja");
            System.out.println("berdiri");
            System.out.println("gratis minum");  
        }
    }
    // To do: Buatlah method Pesan sesuai dengan ketentuan
    public void Pesan(int nomorKomputer){
        System.out.println("memesan komputer no: " + nomorKomputer);
    // To do: Buatlah method TambahLayanan sesuai dengan ketentuan
    }
    public void TambahLayanan(String makanan){
        System.out.println("memesan makanan:  " + makanan);

    }

    // To do: Buatlah method TambahLayanan memakai Polymorphism Overloading sesuai dengan ketentuan
    public void TambahLayanan(String makanan, String minuman){
        System.out.println("tambah minum:  " + makanan + "dan minuman: " + minuman);
    }
    
}