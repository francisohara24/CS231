/*
File Name:   DumbShuffle.java
Authors:     Francis O'Hara
Date:        02/20/2024
Description: Contains multiple implementations of shuffling algorithms.
How to Run:  java -ea DumbShuffle
*/
package project_1.lab_1;

import java.util.ArrayList;
import java.util.Random;

public class DumbShuffle {
    /**
     * "Shuffles" an ArrayList by reversing the order of elements.
     * @param integerArray The ArrayList to be shuffled.
     * @return The shuffled ArrayList.
     */
    public static ArrayList<Integer> dumbShuffle( ArrayList<Integer> integerArray ) {
        // ArrayList for storing shuffled output
        ArrayList<Integer> newIntegerArray = new ArrayList<>();

        // Add the last to the new list and remove it until the end
        for ( int i = integerArray.size() - 1 ; i >= 0 ; i -- )
            newIntegerArray.add( integerArray.get( i ) );

        return newIntegerArray ;
    }

    /**
     * Doesn't shuffle the arraylist, just returns a copy
     */
    public static ArrayList<Integer> noShuffle( ArrayList<Integer> integerArray ) {

        ArrayList<Integer> newIntegerArray = new ArrayList<>() ;

        // Add the last to the new list and remove it until the end
        for (Integer integer : integerArray) {
            newIntegerArray.add(integer);
        }

        return newIntegerArray ;
    }

    /**
     * Shuffles an ArrayList. Based on the Fisher-Yates shuffling algorithm.
     * @param integerArray The ArrayList of integers to be shuffled.
     * @return The shuffled ArrayList.
     */
    public static ArrayList<Integer> smartShuffle (ArrayList<Integer> integerArray) {
        ArrayList<Integer> oldArray = new ArrayList<>();
        ArrayList<Integer> newArray = new ArrayList<>();

        // copy contents of integerArray to prevent deletion
        for (int value: integerArray)
            oldArray.add(value);

        // remove random values from oldArray and append to newArray
        Random random = new Random();

        for (int i = 0; i < integerArray.size(); i++) {
            // add randomly selected value from oldArray to newArray
            int randomIndex = random.nextInt(oldArray.size());
            newArray.add(oldArray.get(randomIndex));

            // remove selected value from oldArray
            oldArray.remove(randomIndex);
        }
        return newArray;
    }

    /**
     * The main entry point into the program.
     * @param args Array of Strings representing the command-line arguments passed to the program.
     */
    public static void main(String[] args){
        // LAB INSTRUCTION 10: REMOVE THE VALUES IN RANDOM ORDER.
        // create ArrayList of Integers with numbers 1 to 10 in order
        ArrayList<Integer> integerArray = new ArrayList<>();
        for (int i = 1; i <= 10; i ++)
            integerArray.add(i);

        // randomly remove values from ArrayList and print order in which values were removed.
        System.out.print("Removed values: ");

        for (int i = 0; i < 10; i ++) {
            // select a valid random index for removing elements
            int removedElement;
            Random random = new Random();
            int randomIndex = random.nextInt(integerArray.size());

            // print out element to be removed at randomIndex
            removedElement = integerArray.get(randomIndex);
            System.out.print(removedElement + " ");

            // remove element at randomIndex
            integerArray.remove(randomIndex);
        }
    }
}