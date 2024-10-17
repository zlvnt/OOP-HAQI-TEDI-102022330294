package java;
import java.util.Scanner;

public class main3 {
    public static void main(String[] args) {
        Scanner put = new Scanner(System.in);

        System.out.print("angka pertama: ");
        int angka1 = put.nextInt();

        System.out.print("angka kedua: ");
        int angka2 = put.nextInt();

        if (angka1 > angka2) {
            System.out.println("Angka pertama > angka kedua.");
        } else if (angka1 < angka2) {
            System.out.println("Angka kedua > angka pertama.");
        } else {
            System.out.println("Kedua angka sama.");
        }

        put.close();
    }
}