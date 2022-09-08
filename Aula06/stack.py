from typing import List, Any
from copy import deepcopy


class Stack:
    """Uma classe representando uma pilha"""

    def __init__(self) -> None:
        # Essa stack é genérica, por isso
        # a lista poderá receber qualquer
        # tipo de dados
        self.__data: List[Any] = []

        # Representa o índice para iterações
        # com for
        self.__index = 0

    def append(self, item: Any) -> None:
        """Representa o append da lista"""
        self.__data.append(item)

    def pop(self) -> Any:
        """Representa o pop da lista sem parâmetros"""
        if not self.__data:
            return

        return self.__data.pop()

    def peek(self) -> Any:
        """Mostra o último elemento adicionado à pilha"""
        if not self.__data:
            return

        return self.__data[-1]

    def __repr__(self) -> str:
        """Representação dos dados"""
        return str(self.__data)

    def __iter__(self):
        """Para iteração com for"""
        self.__index = len(self.__data)
        return self

    def __next__(self):
        """Para iteração com for (next item)"""
        if self.__index == 0:
            raise StopIteration

        self.__index -= 1
        return self.__data[self.__index]

    def __bool__(self):
        """Para iteração com while"""
        return bool(self.__data)


if __name__ == "__main__":
    stack = Stack()

    stack.append('A')
    stack.append('B')
    stack.append('C')

    print('FOR:')
    for item in stack:
        print(item)
    print()

    print('POP:')
    last_item = stack.pop()
    print(stack, last_item)
    print()

    print('WHILE:')
    stack_copy = deepcopy(stack)
    while stack_copy:
        print(stack_copy.pop())
    print()

    print('ORIGINAL STACK:')
    print(stack)