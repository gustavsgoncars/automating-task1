// 231RDB029 Gustavs Gončars 

import java.util.Scanner;

abstract class Figura {
    abstract double getArea();
    abstract double getPerimeter();
}

class Rectangle extends Figura {
    double width;
    double height;

    public Rectangle(double inputWidth, double inputHeight) {
        width = inputWidth;
        height = inputHeight;
    }

    public double getArea() {
        return width*height;
    }

    public double getPerimeter() {
        return (width+height)*2;
    }
}

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        Figura[] figuras = new Figura[count];
        
        for (int i = 0; i < count; i++) {;
            double width = scanner.nextDouble();
            double height = scanner.nextDouble();
            figuras[i] = new Rectangle(width, height);
        }
        
        for (int i = 0; i < figuras.length; i++) {
            System.out.printf("%.2f %.2f%n", figuras[i].getArea(), figuras[i].getPerimeter());
        }
        
        scanner.close();
    }
}
