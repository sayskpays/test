package ch18.data_io.binary_io_stream.output_stream;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class WriteExample3 {
    public static void main(String[] args) {
        try {
            OutputStream os = new FileOutputStream("C:/Temp/test2.db");

            byte[] array = {10, 20, 30, 40, 50};

            os.write(array, 1, 3); // 1번 인덱스부터 3개까지만 출력

            os.flush(); // 내부 버퍼에 잔류하는 바이트를 출력하고 버퍼를 비움
            os.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}