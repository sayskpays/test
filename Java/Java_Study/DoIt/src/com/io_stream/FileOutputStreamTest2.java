package com.io_stream;


import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputStreamTest2 {
    public static void main(String[] args) throws IOException {

        FileOutputStream fos = new FileOutputStream("output2.txt", true);

        try(fos){
           byte[] bs = new byte[26];
           byte data = 65; // 'A'의 아스키 값
            for(int i=0; i<bs.length;i++){
                bs[i] = data;
                data++;
            }// A부터 Z까지 배열에 넣기
            fos.write(bs); // 배열을 한꺼번에 출력
        }
    }
}
