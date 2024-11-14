public class Main {
    public static void main(String[] args) {

        // To do: Buatlah sebuah Objek baru dari class Komputer
        Komputer komputer = new Komputer(50,"Warnet Gaming Z",50000);
        // To do: Panggillah Method Informasi dari class Komputer
        komputer.Informasi();

        // To do: Buatlah sebuah Objek baru dari class KomputerVIP 
        KomputerVIP komputerVIP = new KomputerVIP(10, "Warnet Gaming Z", 10000, true);
        // To do: Panggillah Method Informasi dari class KomputerVIP
        komputerVIP.Informasi();
        // To do: Panggillah Method Login
        komputerVIP.Login("Antoni");
        // To do: Panggillah Method Bermain 2x agar dapat melakukan polymorphism overloading
        komputerVIP.Bermain(8);
        komputerVIP.Bermain(1, 10);
        
        

        System.out.println();


        // To do: Buatlah sebuah Objek baru dari class KomputerPremium
        KomputerPremium komputerPremium = new KomputerPremium(25, "Warnet Gaming Z", 20000, true);

        // To do: Panggillah Method Informasi dari class KomputerPremium
        komputerPremium.Informasi();
        // To do: Panggillah Method Pesan
        komputerPremium.Pesan(2);
        // To do: Panggillah Method TambahLayanan 2x agar dapat melakukan polymorphism overloading
        komputerPremium.TambahLayanan("Takoyaki");
        komputerPremium.TambahLayanan("Takoyaki", "Thai Tea");
       
    }
}