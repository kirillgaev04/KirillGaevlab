package org.example;

public class Main {
    public static void main(String[] args) {
        CarFactory japaneseFactory = new JapaneseCarFactory();
        Sedan japaneseSedan = japaneseFactory.createSedan();
        SUV japaneseSUV = japaneseFactory.createSUV();

        japaneseSedan.drive();
        japaneseSUV.offRoad();

        System.out.println("-------------");


        CarFactory germanFactory = new GermanCarFactory();
        Sedan germanSedan = germanFactory.createSedan();
        SUV germanSUV = germanFactory.createSUV();

        germanSedan.drive();
        germanSUV.offRoad();
    }
}