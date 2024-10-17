// Don't delete any comments below!!!
// Todo : Import Arraylist and Scanner
import java.util.ArrayList;
import java.util.Scanner;

public class ManajemenInventaris {
    // Todo : Create ArrayList of MakananKering (daftarMakananKering) and MakananBasah (daftarMakananBasah) to store items
    private ArrayList<MakananKering> daftarMakananKering = new ArrayList<>();
    private ArrayList<MakananBasah> daftarMakananBasah = new ArrayList<>();
    private Scanner sc = new Scanner(System.in);

    public void tambahMakananKering() {
        
        // Todo : Create input for Nama Makanan, Jumlah Makanan, Harga Makanan, and Brand Makanan
        System.out.print("Masukkan Nama Makanan: ");
        String nama = sc.nextLine();
        System.out.print("Masukkan Jumlah Makanan: ");
        int jumlah = sc.nextInt();
        System.out.print("Masukkan Harga Makanan: ");
        Double harga = sc.nextDouble();
        System.out.print("Masukkan Brand Makanan: ");
        String brand = sc.nextLine();

        // Todo : Create a new object for MakananKering
        MakananKering maker = new MakananKering(nama, jumlah, jumlah, brand);
        daftarMakananKering.add(maker);
        // Todo : Create Print Notifitaction "Makanan kering berhasil ditambahkan"
        System.out.println("=======================================");
        System.out.println("Makanan kering berhasil ditambahkan");
    }

    public void tambahMakananBasah() {
        // Todo : Create input for Nama Makanan, Jumlah Makanan, Harga Makanan, and Bahan Makanan
        System.out.print("Masukkan Nama Makanan: ");
        String nama = sc.nextLine();
        System.out.print("Masukkan Jumlah Makanan: ");
        int jumlah = sc.nextInt();
        System.out.print("Masukkan Harga Makanan: ");
        Double harga = sc.nextDouble();
        System.out.print("Masukkan Bahan Makanan: ");
        String bahan = sc.nextLine();

        // Todo : Create a new object for MakananBasah
        MakananBasah maksah = new MakananBasah(nama, jumlah, jumlah, bahan);
        daftarMakananBasah.add(maksah);
        
        // Todo :Create Print Notifitaction "Makanan Basah berhasil ditambahkan"
        System.out.println("=======================================");
        System.out.println("Makanan Basah berhasil ditambahkan");
    }

    public void tampilkanSemuaMakanan() {
        if (daftarMakananKering.isEmpty() && daftarMakananBasah.isEmpty()) {
            // Todo : Create Print Notification "Tidak ada makanan disini"
        } else{
            // Todo : Create print notification for Makanan Kering  
            for(MakananKering maker : daftarMakananKering){
                maker.tampilkanData();
                System.out.println("=======================================");
            }
            // Todo : Create print notification for  Makanan Basah
            for (MakananBasah maksah : daftarMakananBasah){
                maksah.tampilkanData();
                System.out.println("=======================================");
            }
        }
    }
}
