package com.static_study;

public class StaticAlonePractice {

    private static int studentNum = 0;
    int studentCardNum;
    final int NUM = 100;

    // Constructor
    StaticAlonePractice(){
        studentNum++;

        this.studentCardNum = NUM + studentNum;
    }

    // getter
    public int getStudentCardNum() {
        return studentCardNum;
    }

    void showInfo(){
        // System.out.println("STUDENT CARD NUMBER : " + studentCardNum);
    }

}
