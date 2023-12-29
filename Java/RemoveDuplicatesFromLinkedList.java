import java.util.*;

class Program {
  // This is an input class. Do not edit.
  public static class LinkedList {
    public int value;
    public LinkedList next;

    public LinkedList(int value) {
      this.value = value;
      this.next = null;
    }
  }

  public LinkedList removeDuplicatesFromLinkedList(LinkedList linkedList) {
    LinkedList node = linkedList;
		while(linkedList != null){
			while(linkedList.next!=null && linkedList.next.value==linkedList.value){
				linkedList.next=linkedList.next.next;
			}
			linkedList = linkedList.next;
		}
    return node;
  }
}

