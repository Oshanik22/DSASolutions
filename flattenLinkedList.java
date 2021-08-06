class GfG
{
    Node flatten(Node root)
    {
        if(root==null) return null;
        if(root.next==null) return root;
        return merge(root, flatten(root.next));
    }

    Node merge(Node n1, Node n2){

        Node dummy = new Node(0);
        Node head = dummy;
        while(n1!=null && n2!=null){
            if(n1.data<n2.data){
                dummy.bottom = n1;
                n1 = n1.bottom;
            }
            else{
                dummy.bottom = n2;
                n2 = n2.bottom;
            }
            dummy = dummy.bottom;
        }

        if(n1!=null) dummy.bottom = n1;
        if(n2!=null) dummy.bottom = n2;

        return head.bottom;
    }
}
