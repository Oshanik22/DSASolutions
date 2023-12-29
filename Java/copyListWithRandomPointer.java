class Solution {
    HashMap<Node, Node> map = new HashMap<>();
    public Node copyRandomList(Node head) {


        Node ptr = head;
        while(ptr!=null)
        {
            map.put(ptr, new Node(ptr.val));
            ptr = ptr.next;
        }

        ptr = head;
        while(ptr!=null)
        {
            if(ptr.next!=null)
            {
                map.get(ptr).next = map.get(ptr.next);
            }
            if(ptr.random!=null)
            {
                map.get(ptr).random = map.get(ptr.random);
            }
            ptr = ptr.next;
        }


        return map.get(head);
    }
}
