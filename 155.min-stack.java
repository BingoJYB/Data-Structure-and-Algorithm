import java.util.Stack;

/*
 * @lc app=leetcode id=155 lang=java
 *
 * [155] Min Stack
 *
 * https://leetcode.com/problems/min-stack/description/
 *
 * algorithms
 * Easy (41.10%)
 * Likes:    2721
 * Dislikes: 279
 * Total Accepted:    423.5K
 * Total Submissions: 1M
 * Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum
 * element in constant time.
 * 
 * 
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 * 
 * 
 * 
 * 
 * Example:
 * 
 * 
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin();   --> Returns -3.
 * minStack.pop();
 * minStack.top();      --> Returns 0.
 * minStack.getMin();   --> Returns -2.
 * 
 * 
 * 
 * 
 */

// @lc code=start
class MinStack {
    Stack<Integer> main_stack;
    Stack<Integer> minor_stack;

    /** initialize your data structure here. */
    public MinStack() {
        main_stack = new Stack<Integer>();
        minor_stack = new Stack<Integer>();
    }
    
    public void push(int x) {
        main_stack.push(x);

        if (minor_stack.isEmpty())
            minor_stack.push(x);
        else if (minor_stack.peek() >= x)
            minor_stack.push(x);
    }
    
    public void pop() {
        int popped = 0;

        if (main_stack.size() > 0)
            popped = main_stack.pop();

        if (popped == minor_stack.peek())
            minor_stack.pop();
    }
    
    public int top() {
        if (main_stack.size() > 0)
            return main_stack.peek();
        return 0;
    }
    
    public int getMin() {
        if (minor_stack.size() > 0)
            return minor_stack.peek();
        return 0;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
// @lc code=end

