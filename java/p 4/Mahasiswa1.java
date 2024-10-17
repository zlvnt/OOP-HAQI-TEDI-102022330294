
    
public class Mahasiswa1 {
    // Atribut
    private String nama;
    private double tugas;
    private double kuis;
    private double uts;
    private double uas;

    // Konstruktor
    public Mahasiswa1(String nama, double tugas, double kuis, double uts, double uas) {
        this.nama = nama;
        this.tugas = tugas;
        this.kuis = kuis;
        this.uts = uts;
        this.uas = uas;
    }

    // Metode untuk menghitung nilai akhir
    public double hitungNilaiAkhir() {
        // Misalkan bobot: Tugas 20%, Kuis 10%, UTS 30%, UAS 40%
        double nilaiAkhir = (tugas * 0.2) + (kuis * 0.1) + (uts * 0.3) + (uas * 0.4);
        return nilaiAkhir;
    }

    // Getter untuk nama
    public String getNama() {
        return nama;
    }
}

    
