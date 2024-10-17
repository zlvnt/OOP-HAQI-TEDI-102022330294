import java.util.Arrays;
import java.util.Scanner;
public class ElectronicsShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String pertama = scanner.nextLine();
        String[] arrayPertama = pertama.split(" ");
        int uang = Integer.parseInt(arrayPertama[0]);

        String keyboard = scanner.nextLine();
        String[] arrayKeyboard = keyboard.split(" ");
        Arrays.sort(arrayKeyboard);
        int keyboardMurah = Integer.parseInt(arrayKeyboard[0]);

        String usb = scanner.nextLine();
        String[] arrayUsb = usb.split(" ");
        Arrays.sort(arrayUsb);
        int usbMurah = Integer.parseInt(arrayUsb[0]);

        int a = uang - keyboardMurah - usbMurah;
        System.out.println(a);
        // int usbMurah = arrayUsb[0];
        // System.out.println(usbMurah);
    }
}
