from node import Node

class Stack:
    '''
    TODO: generate the class pydoc
    '''

    def __init__(self, top: 'Node' = None):
        '''
        Constructs an empy stack

        Args:
            lenght: Lenght of the stack
        '''
        self.__top = top
        self.__lenght = 0
    
    def add_node(self, node: 'Node') -> None:
        '''
        Adds a node to the stack

        Args:
            node: The node to be added
        '''

        # It has no sense to a None node
        if not Node:
            raise TypeError('Null node is not valid')
        
        # Step 1: Set the top of the stack as the parent of the new node
        node.set_parent(self.__top)

        # Step 2: Set the new node as the new top of the stack
        self.__top = node

        # Step 3: Increment the lenght of the stack
        self.__lenght += 1
    
    def pop(self) -> 'Node':
        '''
        TODO: generate the pydoc
        '''

        # Step 1: Saves the pointer to the top
        node = self.__top

        # Step 2: Set the parent of the top as the new top
        self.__top = self.__top.get_parent()

        return node
    
    def __repr__(self) -> str:
        output = '['

        node = self.__top

        while node:
            output += str(node) + ', '
            node = node.get_parent()
        
        return output + ']'


if __name__ == '__main__':

    # Creates an empty stack
    stack = Stack()

    # Add some values to the stack
    for i in range(3):
        stack.add_node(Node(i))
    
    print(f'Stack before pop: {stack}')
    print(f'Pop value: {stack.pop()}')
    print(f'Stack after pop: {stack}')