

public class User {
    public String userName;
    public int id;
    public Socket socket;
    public void disconnect() throws Exception {
        socket.close();
    }
    // 其它处理socket的方法
}
