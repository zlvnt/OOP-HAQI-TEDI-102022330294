import java.util.ArrayList;
import java.util.Scanner;

public class Pembelian {
    private static final ArrayList<Penerbangan> daftarPenerbangan = new ArrayList<>();
    private static Penumpang penumpang = null;
    private static Penerbangan penerbanganDipilih = null;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        daftarPenerbangan.add(new Penerbangan("GA404", "CGK, Jakarta", "DPS, Bali", "12:00", "14:15", 1100000));
        daftarPenerbangan.add(new Penerbangan("QZ708", "PAD, Padang", "CGK, Jakarta", "06:00", "08:00", 1400000));

        int pilihan;
        do {
            System.out.println("===== EAD Ticket Booking System =====");
            System.out.println("1. Tampilkan Daftar Penerbangan");
            System.out.println("2. Beli Tiket");
            System.out.println("3. Tampilkan Pesanan Tiket");
            System.out.println("4. Exit");
            System.out.print("Silahkan pilih menu: ");
            pilihan = scanner.nextInt();

            switch (pilihan) {
                case 1 -> tampilkanDaftarPenerbangan();
                case 2 -> beliTiket(scanner);
                case 3 -> tampilkanPesanan();
                case 4 -> System.out.println("Terima kasih!");
                default -> System.out.println("Pilihan tidak valid.");
            }
        } while (pilihan != 4);
    }
    private static void tampilkanDaftarPenerbangan() {
        System.out.println("Daftar Penerbangan:");
        for (int i = 0; i < daftarPenerbangan.size(); i++) {
            System.out.println((i + 1) + ".");
            daftarPenerbangan.get(i).tampilDaftarPenerbangan();
            System.out.println();
        }
    }
    private static void beliTiket(Scanner scanner) {
        if (penumpang == null) {
            System.out.println("Silahkan isi data diri Anda terlebih dahulu!");
            System.out.print("Masukkan NIK: ");
            String NIK = scanner.next();
            System.out.print("Masukkan Nama Depan: ");
            String namaDepan = scanner.next();
            System.out.print("Masukkan Nama Belakang: ");
            String namaBelakang = scanner.next();

            penumpang = new Penumpang(NIK, namaDepan, namaBelakang);
        }
        System.out.println("Terima kasih telah mengisi data diri.");
        tampilkanDaftarPenerbangan();
        System.out.print("Pilih nomor penerbangan (ex: 1): ");
        int pilihanPenerbangan = scanner.nextInt();
        if (pilihanPenerbangan > 0 && pilihanPenerbangan <= daftarPenerbangan.size()) {
            penerbanganDipilih = daftarPenerbangan.get(pilihanPenerbangan - 1);
            System.out.println("Pemesanan tiket berhasil!");
        } else {
            System.out.println("Pilihan penerbangan tidak valid.");
        }
    }

    private static void tampilkanPesanan() {
        if (penumpang != null && penerbanganDipilih != null) {
            System.out.println("===== Detail Tiket Penerbangan =====");
            penumpang.tampilDaftarPenumpang();
            penerbanganDipilih.tampilDaftarPenerbangan();
        } else {
            System.out.println("Pembelian tiket tidak ada.");
        }
    }
}