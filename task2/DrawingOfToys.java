package ToyStore;

import java.util.Iterator;
import java.util.List;

public class DrawingOfToys {

    private final int presentToy = 0;
    private final int smallToy = 20;
    private final int mediumToy = 50;
    private final int bigToy = 70;


    public void drawToy(List<Toy> toys, List<Toy> prizeToy) {
        int max = 100;
        int rnd = (int) (Math.random() * ++max);
        System.out.println(rnd);
        for (int i = 0; i < toys.size(); i++) {
            if (toys.get(i).getWeight() == presentToy && rnd < smallToy) {
                int count = toys.get(i).getCount();
                System.out.print("\033[H\033[J");
                System.out.println("вам достался презент");
                prizeToy.add(toys.get(i));
                if (toys.get(i).getCount() == 1) {
                    toys.get(i).setCount(count - 1);
                    toys.remove(toys.get(i));
                    i--;
                }else toys.get(i).setCount(count - 1);
            }
            else if (toys.get(i).getWeight() == smallToy && rnd >= smallToy && rnd < mediumToy) {
                int count = toys.get(i).getCount();
                System.out.print("\033[H\033[J");
                System.out.println("вам достался маленьткий приз");
                prizeToy.add(toys.get(i));
                if (toys.get(i).getCount() == 1) {
                    toys.get(i).setCount(count-1);
                    toys.remove(toys.get(i));
                    i--;
                }else toys.get(i).setCount(count-1);
            }
            else if (toys.get(i).getWeight() == mediumToy && rnd >= mediumToy && rnd < bigToy) {
                int count = toys.get(i).getCount();
                System.out.print("\033[H\033[J");
                System.out.println("вам достался средний приз");
                prizeToy.add(toys.get(i));
                
                if (toys.get(i).getCount() == 1) {
                    toys.get(i).setCount(count-1);
                    toys.remove(toys.get(i));
                    i--;
                }else toys.get(i).setCount(count-1);
            }
            else if (toys.get(i).getWeight() == bigToy && rnd >= bigToy) {
                int count = toys.get(i).getCount();
                System.out.print("\033[H\033[J");
                System.out.println("вам достался большой приз");
                prizeToy.add(toys.get(i));
                if (toys.get(i).getCount() == 1) {
                    toys.get(i).setCount(count-1);
                    toys.remove(toys.get(i));
                    i--;
                }else toys.get(i).setCount(count-1);
            }
        }
    }
}

