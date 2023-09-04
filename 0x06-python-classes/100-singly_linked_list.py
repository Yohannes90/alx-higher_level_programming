#!/usr/bin/python3

"""Defining classes for singly linked list"""

class Node:
    """ Represent a Node in a Singly linked list"""

    def __init__(self, data, next_node=None):
        """Initalize new node
        
        Args:
            data (int): data of new node
            next_node: next node of new node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defining a class Singly linked list"""

    def __init__(self):
        """Initalize new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        node = self.__head
        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)

    def __str__(self):
        """Define the print representation of a singly linked list"""
        sll_str = ""
        node = self.__head
        if node is not None:
            while node is not None:
                sll_str += str(node.data) + '\n'
                node = node.next_node
        return sll_str[:-1]
