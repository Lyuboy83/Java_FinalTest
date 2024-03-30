// Задание

// -Подумать над структурой класса Ноутбук для магазина техники - выделить поля и
// методы. Реализовать в java.
// -Создать множество ноутбуков.
// -Написать метод, который будет запрашивать у пользователя критерий (или критерии)
// фильтрации и выведет ноутбуки, отвечающие фильтру. Критерии фильтрации можно
// хранить в Map. Например:
// “Введите цифру, соответствующую необходимому критерию:
// 1 - ОЗУ
// 2 - Объем ЖД
// 3 - Операционная система
// 4 - Цвет …
// -Далее нужно запросить минимальные значения для указанных критериев - сохранить
// параметры фильтрации можно также в Map.
// -Отфильтровать ноутбуки их первоначального множества и вывести проходящие по
// условиям.

import java.util.*;
import java.util.stream.Collectors;

class Laptop {
    String brand;
    int ram;
    int hdd;
    String os;
    String color;

    public Laptop(String brand, int ram, int hdd, String os, String color) {
        this.brand = brand;
        this.ram = ram;
        this.hdd = hdd;
        this.os = os;
        this.color = color;
    }

    @Override
    public String toString() {
        return "марка = " + brand + '\'' +
                ", ОЗУ = " + ram +
                ", ЖД = " + hdd +
                ", ОС = " + os + '\'' +
                ", цвет = " + color + '\'';

    }
}

public class NotebookShop {
    public static void main(String[] args) {
        Set<Laptop> laptops = new HashSet<>();
        laptops.add(new Laptop("Dell", 16, 512, "Windows", "Black")); // Не получается сделать выбор цвета кириллицей.
        laptops.add(new Laptop("Apple", 8, 256, "MacOS", "Silver"));
        laptops.add(new Laptop("Lenovo", 32, 1024, "Windows", "Grey"));
        laptops.add(new Laptop("Aquarius", 32, 2048, "AltLinux", "Gold"));
        Map<String, Object> filters = new HashMap<>();

        Scanner scanner = new Scanner(System.in);

        System.out.println("Выберите критерии поиска:");
        System.out.println("1 - ОЗУ");
        System.out.println("2 - Объем HDD");
        System.out.println("3 - Операционная система");
        System.out.println("4 - Цвет");
        System.out.println("5 - Марка");
        System.out.println("0 - Завершить выбор");

        int choice;
        while (true) {
            choice = scanner.nextInt();
            if (choice == 0) {
                System.out.println("Попробуйте выбрать ещё раз.");
                break;
            }

            if (choice == 1) {
                System.out.println("Введите минимальный объём ОЗУ: ");
                filters.put("ram", scanner.nextInt());
            } else if (choice == 2) {
                System.out.println("Введите минимальный объем HDD: ");
                filters.put("hdd", scanner.nextInt());
            } else if (choice == 3) {
                System.out.println("Выберите операционную систему: ");
                filters.put("os", scanner.next());
            } else if (choice == 4) {
                System.out.println("Выберите цвет: ");
                filters.put("color", scanner.next());
            } else if (choice == 5) {
                System.out.println("Введите название марки: ");
                filters.put("brand", scanner.next());
            } else {
                System.out.println("Такого товара нет в наличии. Посмотрите другие товары.");
            }

        }

        Set<Laptop> filteredLaptops = laptops.stream()
                .filter(laptop -> filters.getOrDefault("ram", 0) instanceof Integer
                        && laptop.ram >= (int) filters.getOrDefault("ram", 0))
                .filter(laptop -> filters.getOrDefault("hdd", 0) instanceof Integer
                        && laptop.hdd >= (int) filters.getOrDefault("hdd", 0))
                .filter(laptop -> filters.getOrDefault("os", "").equals("")
                        || laptop.os.equalsIgnoreCase((String) filters.getOrDefault("os", "")))
                .filter(laptop -> filters.getOrDefault("color", "").equals("")
                        || laptop.color.equalsIgnoreCase((String) filters.getOrDefault("color", "")))
                .filter(laptop -> filters.getOrDefault("brand", "").equals("")
                        || laptop.brand.equalsIgnoreCase((String) filters.getOrDefault("brand", "")))
                .collect(Collectors.toSet());

        System.out.println("Результат поиска:");
        for (Laptop laptop : filteredLaptops) {
            System.out.println(laptop);
        }
    }
}