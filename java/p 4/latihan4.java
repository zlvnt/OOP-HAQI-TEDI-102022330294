import java.util.Scanner;

public class latihan4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Masukkan data civitas akademik:");
        System.out.print("Nama: ");
        String nama = scanner.nextLine();

        System.out.print("NIK: ");
        int nik = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Masukkan status (sudah menikah/belum menikah): ");
        String status = scanner.nextLine();

        System.out.print("Masukkan jenis kelamin (Laki-laki/Perempuan): ");
        String jk = scanner.nextLine();

        latihan42 civitas = new latihan42(nama, nik, status, jk);

        int pendapatanTotal = civitas.hitungPendapatanTotal();

        System.out.println("\n--- Civitas Akademik ---");
        System.out.println("Nama\t\t: " + civitas.getNama());
        System.out.println("NIK\t\t: " + civitas.getNik());
        System.out.println("Jenis Kelamin\t: " + civitas.getJenisKelamin());
        System.out.println("Pendapatan\t: " + pendapatanTotal);

        scanner.close();
    }
}
