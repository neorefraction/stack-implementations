class Node:
    def __init__(self, value: any = None, parent: Node = None):
        '''
        Constructs a new node with a value and a pointer to a parent

        Args:
            value: The object to be stored by the node
            parent: Pointer to the parent node
        '''
        self._value = value
        self._parent = parent

    def set_value(self, value: any) -> None:
        '''
        Sets the node value

        Args:
            value: The object to be stored by the node
        
        Raises:
            TypeError: If value is None it can't be setted
        '''
        if value is None:
            raise TypeError('None is not a valid type for the value of the node')
        
        self._value = value

    def get_value(self) -> any:
        '''
        Gets the object stored on the node

        Returns:
            The value of the node
        '''
        return self._value
    
