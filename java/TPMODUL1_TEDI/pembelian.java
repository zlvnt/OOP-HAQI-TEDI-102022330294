import java.util.ArrayList;
import java.util.Scanner;

public class pembelian {
    private ArrayList<penerbangan> simpanP = new ArrayList<>();
    private ArrayList<penumpang> daftarP = new ArrayList<>();

    public static void main(String[] args) {
        Scanner put = new Scanner(System.in);
        pembelian pembelian = new pembelian();

        pembelian.tambahPenerbangan(new penerbangan("AB100", "Lampung, Jakarta", "IATA, CGK", "06:30", "12:00", 500000.0f));
        pembelian.tambahPenerbangan(new penerbangan("WR200", "Jakarta, Makasar", "CGK, UPG", "09:00", "03:00", 1200000.0f));

        while (true) {
            System.out.println("====== EAD Ticket Booking System ======");
            System.out.println("1. Tampilkan Daftar Penerbangan");
            System.out.println("2. Beli Tiket");
            System.out.println("3. Tampilkan Pesanan Tiket");
            System.out.println("4. Exit");
            System.out.print("Silahkan pilih menu: ");
            int pilihan = put.nextInt();

            switch (pilihan) {
                case 1:
                    pembelian.catatpenerbangan();
                    break;
                case 2:
                    pembelian.beliTiket(put);
                    break;
                case 3:
                    pembelian.lihattiket();
                    break;
                case 4:
                    System.out.println("Terima kasih!");
                    return;
                default:
                    System.out.println("Pilihan tidak ada");
            }
        }
    }

    public void tambahPenerbangan(penerbangan penerbangan) {
        simpanP.add(penerbangan);
    }

    public void catatpenerbangan() {
        if (simpanP.isEmpty()) {
            System.out.println("Tidak ada penerbangan tersedia.");
        } else {
            for (int i = 0; i < simpanP.size(); i++) {
                System.out.print((i + 1) + ". ");
                simpanP.get(i).catatpenerbangan();
            }
        }
    }

    public void beliTiket(Scanner put) {
        put.nextLine();
        System.out.println("Silahkan isi data diri Anda terlebih dahulu");
        System.out.print("Masukan NIK: ");
        String NIK = put.nextLine();
        System.out.print("Masukkan Nama Depan: ");
        String namaDepan = put.nextLine();
        System.out.print("Masukkan Nama Belakang: ");
        String namaBelakang = put.nextLine();

        penumpang penumpang = new penumpang(NIK, namaDepan, namaBelakang);
        daftarP.add(penumpang);

        System.out.println("Terima kasih telah mengisi data pelanggan. Silahkan pilih tiket penerbangan yang tersedia.");
        catatpenerbangan();

        System.out.print("Pilih nomor penerbangan (ex: 1): ");
        int pilihanPenerbangan = put.nextInt();

        if (pilihanPenerbangan > 0 && pilihanPenerbangan <= simpanP.size()) {
            System.out.println("Pemesanan tiket berhasil dilakukan.");
        } else {
            System.out.println("Penerbangan tidak valid.");
        }
    }

    public void lihattiket() {
        if (daftarP.isEmpty()) {
            System.out.println("Pembelian tiket tidak ada.");
        } else {
            for (penumpang penumpang : daftarP) {
                penumpang.lihatpenumpang();
            }
        }
    }
}
