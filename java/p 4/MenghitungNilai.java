


import java.util.Scanner;
public class MenghitungNilai {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input data mahasiswa
        System.out.print("Masukkan nama mahasiswa: ");
        String nama = scanner.nextLine();

        System.out.print("Masukkan nilai tugas (0-100): ");
        double tugas = scanner.nextDouble();

        System.out.print("Masukkan nilai kuis (0-100): ");
        double kuis = scanner.nextDouble();

        System.out.print("Masukkan nilai UTS (0-100): ");
        double uts = scanner.nextDouble();

        System.out.print("Masukkan nilai UAS (0-100): ");
        double uas = scanner.nextDouble();

        // Membuat objek Mahasiswa
        Mahasiswa1 mahasiswa = new Mahasiswa1(nama, tugas, kuis, uts, uas);

        // Menghitung nilai akhir
        double nilaiAkhir = mahasiswa.hitungNilaiAkhir();

        // Menampilkan hasil
        System.out.println("\n--- Hasil Perhitungan Nilai Akhir ---");
        System.out.println("Nama Mahasiswa: " + mahasiswa.getNama());
        System.out.printf("Nilai Akhir: %.2f\n", nilaiAkhir);

        // Menentukan grade
        String grade;
        if (nilaiAkhir >= 85) {
            grade = "A";
        } else if (nilaiAkhir >= 70) {
            grade = "B";
        } else if (nilaiAkhir >= 55) {
            grade = "C";
        } else if (nilaiAkhir >= 40) {
            grade = "D";
        } else {
            grade = "E";
        }

        System.out.println("Grade: " + grade);

        scanner.close();
    }
}


