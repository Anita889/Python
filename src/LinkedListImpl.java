import java.util.LinkedList;
import java.util.Stack;

public class LinkedListImpl {
    Node head;
    static class Node{
        Object data;
        Node next;
        Node(Object data)
        {
            this.data=data;
        }
    }
    public void insert(Object data){
        if(head==null)
            head=new Node(data);
        else
        {
            Node finish=head;
            while(finish.next!=null){
                finish=finish.next;
            }
            finish.next=new Node(data);
        }
    }
    public LinkedListImpl delete(LinkedListImpl list,Object removeData)
    {
        Node nodeRemove=list.head;
        Node BeforeNodeRemove=nodeRemove;
        Node AfterNodeRemove=nodeRemove;
        int count=0,i=0;
        while(nodeRemove.data!=removeData){
            nodeRemove=nodeRemove.next;
            count++;
        }
        while(i!=count-1){
            BeforeNodeRemove=BeforeNodeRemove.next;
            i++;
        }
        AfterNodeRemove=nodeRemove.next;
        BeforeNodeRemove.next=AfterNodeRemove;
        return list;
    }
    public void print(LinkedListImpl list)
    {
        Node node=list.head;
        System.out.print("[");
        System.out.print(node.data);
        node=node.next;
        while(node!=null)
        {
            System.out.print(","+node.data);
            node=node.next;
        }
        System.out.print("]");
    }
    public  Object middleMember(LinkedListImpl list) {
        Node oneStep=list.head;
        Node twoStep=list.head;
        while(twoStep.next!=null && twoStep.next.next!=null){
            oneStep=oneStep.next;
            twoStep=twoStep.next.next;
        }
        return oneStep.data;
    }
    public Boolean findCycle(LinkedListImpl list)
    {
        if (list.head == null) {
            return false;
        }
        Node oneStep=list.head;
        Node twoStep=list.head;
        while(twoStep.next!=null&& twoStep.next.next!=null){
            twoStep=twoStep.next.next;
            if(oneStep==twoStep) {
                System.out.println(oneStep+" "+twoStep+" "+oneStep.data.getClass());
                return true;
            }
            else {
                oneStep = oneStep.next;
                twoStep = twoStep.next.next;
            }
        }
        return false;
    }
    public Boolean palindrome(LinkedListImpl list)
    {
        Node nodeOne=list.head;
        Node nodeTwo=list.head;
        Stack<Object> stack=new Stack<>();
        LinkedListImpl list1=new LinkedListImpl();

        while (nodeTwo.next!=null&&nodeTwo.next.next!=null)
        {
            nodeTwo=nodeTwo.next.next;
            stack.add(nodeOne.data);
            nodeOne=nodeOne.next;
        }
        if(nodeOne.data!=stack.peek()) {
            stack.add(nodeOne.data);nodeOne=nodeOne.next;
        }
        while (nodeOne!=null)
        {
            list1.insert(nodeOne.data);
            nodeOne=nodeOne.next;
        }
    //    list1.insert(nodeOne.data);
       list1.print(list1);
        Node node=list1.head;
        while (!stack.isEmpty()){
           System.out.println(stack.peek());
           // System.out.println(node.data);
            if(node.data!=stack.peek())
                return false;
            node=node.next;
            stack.pop();
        }
        return true;
    }
    public static void main(String[] args) {

        LinkedListImpl list=new LinkedListImpl();
         Integer node1=1;
        Integer node2=2;
        Integer node3=3;
        Integer node4=4;
       Integer node5=4;
        Integer node6=3;
        Integer node7=2;
        Integer node8=1;
        list.insert(node1);
        list.insert(node2);
        list.insert(node3);
        list.insert(node4);
       list.insert(node5);
        list.insert(node6);list.insert(node7);
        list.insert(node8);
   //     list.print(list);
        System.out.println(list.palindrome(list));
    }
}
