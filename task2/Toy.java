package ToyStore;

public class Toy {
    private int id;
    private String title;
    private int count;
    private int weight;
    private static int idCount = 0;

    Toy(String title, int count, int weight) {
        this.id = ++ idCount;
        this.title = title;
        this.count = count;
        this.weight = weight;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public int getCount() {
        return count;
    }

    public int getWeight() {
        return weight;
    }

    public String toString() {
        int id = this.getId();
        return "ID: " + id + ", Название игрушки: " + this.getTitle() + ", количество: " + this.getCount() + ", вес " + this.getWeight();
    }
}
