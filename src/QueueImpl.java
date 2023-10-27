public class QueueImpl {
   private QueueNode front;
    private QueueNode back;
    static class QueueNode{
      private   Object data;
       private QueueNode next;
        QueueNode(Object data)
        {
            this.data=data;
        }
    }
    public int countLength(QueueImpl queue)
    {
        QueueNode node=queue.back;
        int count=0;
        while(node!=queue.front){
            node=node.next;
            count++;
        }
        return count;
    }
    public  Object peek(QueueImpl queue)
    {
        return queue.front.data;
    }
    public void add(QueueImpl queue, Object data)
    {
        QueueNode newLast=new QueueNode(data);
        if(queue.front==null) {
            queue.front =newLast;
            queue.back=newLast;
        }
        else if(queue.back==queue.front)
        {
            newLast.next=front;
            queue.back=newLast;
        }
        else
        {
            newLast.next=queue.back;
            queue.back=newLast;
        }
    }
    public void delete(QueueImpl queue,Object removeData)
    {
         QueueNode node=queue.back;
         int count=0,i=0;
         while(node!=queue.front)
         {
             if(node.data==removeData)
             {
                 //for back
                 if(count==0) {
                     queue.back= node.next;
                 }
                 //for middle
                 else  {
                     QueueNode nodeBefore = queue.back;
                     while (i < count - 1) {
                         nodeBefore = nodeBefore.next;
                         i++;
                     }
                     QueueNode nodeAfter=node.next;
                     nodeBefore.next=nodeAfter;
                     break;
                 }
             }
             count++;
             node=node.next;
         }
         //for front
         i=0;
         if(node==queue.front) {
             QueueNode nodeBefore = queue.back;
             while (i < count - 1) {
                 nodeBefore = nodeBefore.next;
                 i++;
             }
             queue.front = nodeBefore;
         }
    }
    public void print(QueueImpl queue)
    {
        QueueNode node1=queue.front;
        QueueNode node2=queue.back;
        while(node2!=node1)
        {
            System.out.println(node2.data);
            node2=node2.next;
        }
        System.out.println(node2.data);
    }
    public static void main(String[] args) {
        QueueImpl queue=new QueueImpl();
        queue.add(queue,5);
        queue.add(queue,1);
        queue.add(queue,3);
        queue.add(queue,1);
        queue.add(queue,1);
        queue.add(queue,6);
        queue.delete(queue,1);
        queue.print(queue);

    }
}
