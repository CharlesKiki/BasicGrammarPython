import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;


public class User {
    public String userName;
    public int id;
    //首先把域变成私有的，对外隐藏socket细节
    private Socket socket;

    public void sendMessage(String message) {
        try {
            OutputStream outputStream = socket.getOutputStream();
            PrintWriter out = new PrintWriter(outputStream);
            out.println(message);
        } catch (Exception e) {
            //处理异常
        }
    }

    // 其它处理socket的方法...
    public void disconnect() throws Exception {
        socket.close();
    }
}
