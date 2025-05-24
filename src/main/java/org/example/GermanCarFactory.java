package org.example;

public class GermanCarFactory implements CarFactory {
    public Sedan createSedan() {
        return new GermanSedan();
    }

    public SUV createSUV() {
        return new GermanSUV();
    }
}
