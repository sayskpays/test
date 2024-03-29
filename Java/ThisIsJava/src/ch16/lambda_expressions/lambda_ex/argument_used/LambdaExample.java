package ch16.lambda_expressions.lambda_ex.argument_used;

public class LambdaExample {
    public static void main(String[] args) {
        Person person = new Person();

        //매개변수가 두 개일 경우
        person.action1((name, job) -> {
            System.out.println(name);
            System.out.println(job);
        });
        person.action1((name, job) -> System.out.println(name));

        // 매개변수가 한 개일 경우
        person.action2(word->{
            System.out.println(word);
            System.out.println("라고 말합니다.");
        });
        person.action2(word-> System.out.println(word+""));
    }
}
