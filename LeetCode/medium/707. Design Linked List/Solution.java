
class MyLinkedList {

    class ListNode {

        int val;
        ListNode next;
        ListNode prev;

        public ListNode(int val) {
            this.val = val;
        }

    }

    private ListNode head = null;
    private ListNode tail = null;
    private int size = 0;

    public MyLinkedList() {

    }

    public int get(int index) {

        if (index > size - 1) {
            return -1;
        }

        ListNode curr = head;
        int c = 0;

        while (curr != null) {

            if (c == index) {
                return curr.val;
            }

            curr = curr.next;
            c++;
        }

        return -1;
    }

    public void addAtHead(int val) {

        ListNode node = new ListNode(val);

        if (head == null) {
            tail = node;
        }
        else {
            head.prev = node;
            node.next = head;
        }
        head = node;

        size++;

    }

    public void addAtTail(int val) {

        ListNode node = new ListNode(val);

        if (tail == null) {
            head = node;
        }
        else {
            tail.next = node;
            node.prev = tail;
        }
        tail = node;

        size++;

    }

    public void addAtIndex(int index, int val) {

        if (index == 0) {
            addAtHead(val);
        }
        else if (index == size) {
            addAtTail(val);
        }
        else if (index < size) {

            int c = 0;
            ListNode curr = head;
            ListNode node = new ListNode(val);

            while (curr != null) {

                if (c == index) {
                    ListNode prev = curr.prev;
                    prev.next = node;
                    node.prev = prev;
                    curr.prev = node;
                    node.next = curr;
                }

                curr = curr.next;
                c++;
            }

            size++;
        }


    }

    public void deleteAtIndex(int index) {

        if (size > 0 && index == 0) {
            head = head.next;

            if (size == 1) {
                tail = null;
            }

            size--;
        }
        else if (index == size - 1) {
            ListNode newTail = tail.prev;
            newTail.next = null;
            tail = newTail;
            size--;
        }
        else if (index >= 0 && index < size) {

            int c = 0;
            ListNode curr = head;

            while (curr != null) {

                if (c == index) {
                    ListNode prev = curr.prev;
                    ListNode next = curr.next;
                    prev.next = next;
                    next.prev = prev;
                }

                c++;
                curr = curr.next;
            }

            size--;
        }

    }
    
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */