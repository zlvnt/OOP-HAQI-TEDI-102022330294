import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;

public class LoginController {

    @FXML
    private TextField usernameField;

    @FXML
    private PasswordField passwordField;

    @FXML
    private Button loginButton;

    @FXML
    private void handleLogin(ActionEvent event) {
        String username = usernameField.getText();
        String password = passwordField.getText();

        if ("admin".equals(username) && "panjul123".equals(password)) {
            try {
                FXMLLoader loader = new FXMLLoader(getClass().getResource("/Inventory.fxml"));
                Stage stage = (Stage) loginButton.getScene().getWindow();
                stage.setScene(new Scene(loader.load()));
            } catch (Exception e) {
                e.printStackTrace();
                tampilkanPesan("Kesalahan", "Tidak dapat memuat layar inventaris.");
            }
        } else {
            tampilkanPesan("Login Gagal", "Nama pengguna atau kata sandi salah.");
        }
    }

    private void tampilkanPesan(String judul, String pesan) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle(judul);
        alert.setHeaderText(null);
        alert.setContentText(pesan);
        alert.showAndWait();
    }
}