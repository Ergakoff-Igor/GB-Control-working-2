package ToyStore;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ToyStorage {
    ArrayList<Toy> toys = new ArrayList<>();
    ArrayList<Toy> prizeToys = new ArrayList<>();


    public void addToy(Toy toy) {
        toys.add(toy);
    }

    public void changeWeight(Scanner scanner) {
        int id = scanner.nextInt();
        int weight = scanner.nextInt();
        for (Toy toy : toys) {
            if (toy.getId() == id) {
                toy.setWeight(weight);
            }
        }
    }



    public void saveToyToFile(Toy toy, String filename) {
        try {
            FileWriter writer = new FileWriter(filename, true);
            writer.write(toy.toString() + "\n");
            writer.close();
        } catch (IOException e) {
            System.out.println("Ошибка записи в файл");
        }
    }


}
