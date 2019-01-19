
public class BookStore {
    private final static ArrayList<IBook> bookList = new ArrayList<IBook>();
    //手动添加数据
    static {
        bookList.add(new OffNovelBook("天龙八部", 4500, "金庸"));
        bookList.add(new OffNovelBook("射雕英雄传", 4000, "金庸"));
        bookList.add(new OffNovelBook("The Lord of the Rings", 6000, "Tolkien"));
        bookList.add(new OffNovelBook("The Hobbit", 5000, "Tolkien"));
    }
    public static void main(String[] args) {
        NumberFormat formatter = NumberFormat.getCurrencyInstance();
        formatter.setMaximumFractionDigits(2);
        System.out.println("-----------书店卖出去的书籍记录如下-----------");
        for (IBook book : bookList) {
            System.out.println("书籍名称: " + book.getName() + "\t书籍作者: " + book.getAuthor() + "\t书籍价格: " + formatter.format(book.getPrice() /
                    100.0) + "元");
        }
    }
}
