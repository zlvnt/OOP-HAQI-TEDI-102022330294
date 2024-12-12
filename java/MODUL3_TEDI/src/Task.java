import java.time.LocalDate;

public class Task {
    // TO DO: Lengkapi atribut-atribut private kelas Task
    private final StringProperty title;
    private final StringProperty Priority;
    private final StringProperty dueDate;
    private final StringProperty status;

    // TO DO: Buat constructor untuk kelas Task
    public Task(String title, String Priority, int dueDate, String status) {
        this.title = new SimpleStringProperty(title);
        this.Priority = new SimpleStringProperty(Priority);
        this.dueDate = new SimpleIntegerProperty(dueDate);
        this.status = new SimpleIntegerProperty(status);
    }
    // TO DO: Buat getter untuk title
    public String gettitle() {
        return title.get();
    }
    // TO DO: Buat getter untuk priority
    public String getPriority() {
        return Priority.get();
    }
    // TO DO: Buat getter untuk dueDate

    // TO DO: Buat getter untuk status
    
    // TO DO: Buat setter untuk status
    public String getstatus() {
        return status.get();
    }

    public void setstatus(String status) {
        this.status.set(status);
    }

    public StringProperty statuStringProperty() {
        return status;
    }
}
