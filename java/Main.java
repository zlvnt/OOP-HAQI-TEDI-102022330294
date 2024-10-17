import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Masukkan panjang sisi kubus: ");
        int sisi = input.nextInt();

        int volume = sisi * sisi * sisi;

        System.out.println("Volume kubus dengan sisi " + volume);

        input.close();
    }
}
