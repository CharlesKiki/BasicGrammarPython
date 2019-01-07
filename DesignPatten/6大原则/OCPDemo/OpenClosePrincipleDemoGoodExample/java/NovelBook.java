
public class NovelBook implements IBook {
    //书籍名称
    private String name;
    //书籍价格
    private int price;
    //书籍作者
    private String author;

    //通过构造函数传递书籍数据
    public NovelBook(String name, int price, String author) {
        this.name = name;
        this.price = price;
        this.author = author;
    }

    //获取作者名字
    @Override
    public String getAuthor() {
        return author;
    }

    //获取书籍名字
    @Override
    public String getName() {
        return name;
    }

    //获取书籍价格
    @Override
    public int getPrice() {
        return price;
    }
}
