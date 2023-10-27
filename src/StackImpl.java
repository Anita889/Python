public class StackImpl {
     StackNode front;
    static class StackNode{
        private final Object data;
        private StackNode next;
        StackNode(Object data)
        {
            this.data=data;
        }
    }
   public void push(StackImpl stack,Object pushData)
   {
       StackNode node=new StackNode(pushData);
       node.next=stack.front;
       front=node;
   }
   public Object peek()
   {
   try {
       return front.data;
   }
   catch (Exception e)
   {
       System.out.println("Your stack is empty(((((");
       return null;
   }
   }
   public void delete()
   {
       try {
           front= front.next;
       }
       catch (Exception e)
       {
           System.out.println("Your stack is empty,can not delete anything(((((");
       }
   }

   public static void main(String[] args) {
       int i=0,count=0;
       StackImpl stack=new StackImpl();
       String string="[{()}]";
       while (string.length()!=i){
           stack.push(stack,string.charAt(i));
           i++;
       }
       while (stack!=null){
           if (stack.peek()== "[") {
               count += 3;
           } else if (stack.peek()=="{") {
               count += 2;
           } else if (stack.peek()=="(") {
               count += 1;
           } else if (stack.peek()=="]") {
               count -= 3;
           } else if (stack.peek()=="}") {
               count -= 2;
           } else if (stack.peek()==")") {
               count -= 1;
           }
           stack.delete();
       }
       System.out.println(count == 0);
    }
}
