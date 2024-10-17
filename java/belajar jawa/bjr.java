import java.util.Scanner;

public class bjr {
    public static void main(String[] args) {
        Scanner put = new Scanner(System.in);

        System.out.print("Masukkan nama: ");
        String nama = put.nextLine();

        System.out.print("Masukkan nim: ");
        int nim = put.nextInt();

        int tugas, quiz, uts, uas;
        System.out.print("Masukkan nilai tugas: ");
        tugas = put.nextInt();
        System.out.print("Masukkan nilai quiz: ");
        quiz = put.nextInt();
        System.out.print("Masukkan nilai uts: ");
        uts = put.nextInt();
        System.out.print("Masukkan nilai uas: ");
        uas = put.nextInt();

        double rata_rata = (tugas + quiz + uts + uas) / 4;

        System.out.printf("Nilai rata-rata MK PBO milik %s dengan NIM %s adalah: %f%n", nama, nim, rata_rata);
    }
    
}
