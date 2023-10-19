class MinStack:
    def __init__(self):
        # Initialize stack
        self.stack = []

    def push(self, val):
        # Push the value to the list
        self.stack.append(val)

    def pop(self):
        # Remove the last element and return it
        value = self.stack.pop()

    def top(self):
        # Return the last element
        value = self.stack[-1]
        return value

    def getMin(self):
        # Copy the stack and sort it in reverse order (to not change the original stack)
        stack_copy = list(self.stack)
        stack_copy.sort(reverse=True)

        # Return the first element (already reverse sorted, minimum is the last element)
        min_value = stack_copy[-1]
        return min_value
