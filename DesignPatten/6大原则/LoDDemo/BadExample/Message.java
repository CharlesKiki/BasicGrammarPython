

public class Message {
    //给用户发送"Hello..."消息
    public void sayHello(User user) {
        Socket s = user.socket;
        try {
            OutputStream outputStream = s.getOutputStream();
            PrintWriter out = new PrintWriter(outputStream);
            out.println("Hello...");
        } catch (Exception e) {
            //处理异常
        }
    }
}
