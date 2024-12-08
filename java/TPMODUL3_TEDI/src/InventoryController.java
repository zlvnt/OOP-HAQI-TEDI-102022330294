import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;

public class InventoryController {

    @FXML
    private TableView<Album> albumTable;
    @FXML
    private TableColumn<Album, String> albumNameColumn;
    @FXML
    private TableColumn<Album, String> artistColumn;
    @FXML
    private TableColumn<Album, Integer> totalColumn;
    @FXML
    private TableColumn<Album, Integer> availableColumn;
    @FXML
    private TableColumn<Album, Integer> rentedColumn;

    @FXML
    private TextField albumNameField;
    @FXML
    private TextField artistField;
    @FXML
    private TextField totalField;
    @FXML
    private TextField availableField;

    private ObservableList<Album> albumList = FXCollections.observableArrayList();

    @FXML
    private void initialize() {
        albumNameColumn.setCellValueFactory(data -> data.getValue().albumNameProperty());
        artistColumn.setCellValueFactory(data -> data.getValue().artistProperty());
        totalColumn.setCellValueFactory(data -> data.getValue().totalProperty().asObject());
        availableColumn.setCellValueFactory(data -> data.getValue().availableProperty().asObject());
        rentedColumn.setCellValueFactory(data -> data.getValue().rentedProperty().asObject());

        albumTable.setItems(albumList);
        albumTable.setOnMouseClicked(this::handleRowSelect);
    }

    @FXML
    private void handleAdd() {
        try {
            String albumName = albumNameField.getText().trim();
            String artist = artistField.getText().trim();
            int total = Integer.parseInt(totalField.getText().trim());
            int available = Integer.parseInt(availableField.getText().trim());

            if (albumName.isEmpty() || artist.isEmpty()) {
                showAlert("Input Error", "Fields cannot be empty!");
                return;
            }
            if (total < available) {
                showAlert("Input Error", "Total cannot be less than available!");
                return;
            }

            albumList.add(new Album(albumName, artist, total, available, 0));
            clearFields();
        } catch (NumberFormatException e) {
            showAlert("Input Error", "Total and Available must be numbers!");
        }
    }

    @FXML
    private void handleDelete() {
        Album selectedAlbum = albumTable.getSelectionModel().getSelectedItem();
        if (selectedAlbum != null) {
            albumList.remove(selectedAlbum);
            clearFields();
        } else {
            showAlert("Selection Error", "No album selected!");
        }
    }

    @FXML
    private void handleUpdate() {
        Album selectedAlbum = albumTable.getSelectionModel().getSelectedItem();
        if (selectedAlbum != null) {
            try {
                String albumName = albumNameField.getText().trim();
                String artist = artistField.getText().trim();
                int total = Integer.parseInt(totalField.getText().trim());
                int available = Integer.parseInt(availableField.getText().trim());

                if (albumName.isEmpty() || artist.isEmpty()) {
                    showAlert("Input Error", "Fields cannot be empty!");
                    return;
                }
                if (total < available) {
                    showAlert("Input Error", "Total cannot be less than available!");
                    return;
                }

                selectedAlbum.setAlbumName(albumName);
                selectedAlbum.setArtist(artist);
                selectedAlbum.setTotal(total);
                selectedAlbum.setAvailable(available);
                albumTable.refresh();
                clearFields();
            } catch (NumberFormatException e) {
                showAlert("Input Error", "Total and Available must be numbers!");
            }
        } else {
            showAlert("Selection Error", "No album selected!");
        }
    }

    @FXML
    private void handleRowSelect(MouseEvent event) {
        Album selectedAlbum = albumTable.getSelectionModel().getSelectedItem();
        if (selectedAlbum != null) {
            albumNameField.setText(selectedAlbum.getAlbumName());
            artistField.setText(selectedAlbum.getArtist());
            totalField.setText(String.valueOf(selectedAlbum.getTotal()));
            availableField.setText(String.valueOf(selectedAlbum.getAvailable()));
        }
    }

    private void clearFields() {
        albumNameField.clear();
        artistField.clear();
        totalField.clear();
        availableField.clear();
    }

    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle(title);
        alert.setContentText(message);
        alert.showAndWait();
    }
}
