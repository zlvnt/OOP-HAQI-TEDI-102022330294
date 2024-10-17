package java;
import java.util.Scanner;

public class main2 {
    public static void main(String[] args) {
        Scanner masukkan = new Scanner(System.in);
        int tinggi, alas, luas;

        System.out.print("Masukkan Tinggi Segitiganya: ");
        tinggi = masukkan.nextInt();

        System.out.print("Masukkan Alas Segitiganya: ");
        alas = masukkan.nextInt();

        luas = alas * tinggi / 2;
        System.out.print("Luas Segitiganya adalah: " + luas);
    }
}
