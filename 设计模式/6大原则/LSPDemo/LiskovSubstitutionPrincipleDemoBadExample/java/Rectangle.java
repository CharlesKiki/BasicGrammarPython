

public class Rectangle {
    private int mWidth;
    private int mLength;

    public void setLength(int length) {
        mLength = length;
    }

    public void setWidth(int width) {
        mWidth = width;
    }

    public int getLength() {
        return mLength;
    }

    public int getWidth() {
        return mWidth;
    }

    public int getArea() {
        return mLength * mWidth;
    }
}
