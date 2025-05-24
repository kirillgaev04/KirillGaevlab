package org.example;

public class JapaneseCarFactory implements CarFactory {
    public Sedan createSedan() {
        return new JapaneseSedan();
    }

    public SUV createSUV() {
        return new JapaneseSUV();
    }
}
