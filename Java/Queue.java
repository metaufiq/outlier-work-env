public class Queue<T> {
  private T[] elements;
  private int front;
  private int rear;
  private int size;
  public Queue(int capacity) {
      elements = (T[]) new Object[capacity];
      front = 0;
      rear = -1;
      size = 0;
  }

  public void enqueue(T element) {
      if (size == elements.length) {
          throw new RuntimeException("Queue is full");
      }
      rear = (rear + 1) % elements.length;
      elements[rear] = element;
      size++;
  }

  public T dequeue() {
      if (isEmpty()) {
          throw new RuntimeException("Queue is empty");
      }
      T removed = elements[front];
      front = (front + 1) % elements.length;
      size--;
      return removed;
  }

  public boolean isEmpty() {
      return size == 0;
  }

  public int size() {
      return size;
  }

  @Override
  public String toString() {
      if (isEmpty()) {
          return "Empty";
      }
      String str = "";
      int i = front;
      while (i != rear) {
          str += elements[i] + " ";
          i = (i + 1) % elements.length;
      }
      str += elements[rear];
      return str;
  }
}