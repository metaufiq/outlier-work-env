public class QueueTest {
  public static void main(String[] args) {
      // Test with Integer queue
      testIntegerQueue();
      
      // Test with String queue
      testStringQueue();
      
      // Test edge cases
      testEdgeCases();
  }
  
  public static void testIntegerQueue() {
    Queue<Integer> queue = new Queue(5);
    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    System.out.println(queue); // prints "1 2 3"
    queue.dequeue();
    System.out.println(queue); // prints "2 3"
    System.out.println(queue.size()); // prints 2
    System.out.println(queue.isEmpty()); // prints false
  }
  
  public static void testStringQueue() {
      System.out.println("\nTesting String Queue:");
      Queue<String> stringQueue = new Queue<>(4);
      
      // Test enqueue
      try {
          stringQueue.enqueue("Hello");
          stringQueue.enqueue("World");
          stringQueue.enqueue("Java");
          
          // Print current queue state
          System.out.println("Queue after enqueuing: " + stringQueue);
          
          // Test size
          System.out.println("Queue size: " + stringQueue.size());
          
          // Test dequeue
          String removed = stringQueue.dequeue();
          System.out.println("Dequeued element: " + removed);
          System.out.println("Queue after dequeue: " + stringQueue);
      } catch (Exception e) {
          System.out.println("Error in String Queue test: " + e.getMessage());
      }
  }
  
  public static void testEdgeCases() {
      System.out.println("\nTesting Edge Cases:");
      
      // Test empty queue
      Queue<Double> emptyQueue = new Queue<>(3);
      System.out.println("Empty queue: " + emptyQueue);
      System.out.println("Is empty queue empty? " + emptyQueue.isEmpty());
      
      // Test full queue and overflow
      Queue<Integer> fullQueue = new Queue<>(3);
      try {
          fullQueue.enqueue(1);
          fullQueue.enqueue(2);
          fullQueue.enqueue(3);
          
          System.out.println("Full queue: " + fullQueue);
          
          // This should throw an exception
          fullQueue.enqueue(4);
      } catch (RuntimeException e) {
          System.out.println("Expected exception when queue is full: " + e.getMessage());
      }
      
      // Test dequeue to empty
      Queue<Character> charQueue = new Queue<>(2);
      try {
          charQueue.enqueue('A');
          charQueue.enqueue('B');
          
          System.out.println("Char queue: " + charQueue);
          
          charQueue.dequeue();
          charQueue.dequeue();
          
          // This should throw an exception
          charQueue.dequeue();
      } catch (RuntimeException e) {
          System.out.println("Expected exception when dequeuing from empty queue: " + e.getMessage());
      }
  }
}