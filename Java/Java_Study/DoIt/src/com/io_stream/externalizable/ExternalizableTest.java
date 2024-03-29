package com.io_stream.externalizable;

import java.io.*;

class Dog implements Externalizable{
    String name;

    public Dog() {
    }

    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeUTF(name);
    }

    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {

        name = in.readUTF();
    } // 읽고 쓰는 내용을 직접 구현할 수 있다.
}



public class ExternalizableTest {
    public static void main(String[] args) throws IOException, ClassNotFoundException {

        Dog myDog = new Dog();
        myDog.name = "멍멍이";

        FileOutputStream fos = new FileOutputStream("external.out");
        ObjectOutputStream oos = new ObjectOutputStream(fos);

        try(fos; oos){
            oos.writeObject(myDog); // 직렬화
        }catch (Exception e){
            e.printStackTrace();
        }

        FileInputStream fis = new FileInputStream("external.out");
        ObjectInputStream ois = new ObjectInputStream(fis);

        Dog dog = (Dog)ois.readObject(); // 역직렬화
        System.out.println(dog);
    }
}
