# PythonDSA

Welcome to the Python Data Structures and Algorithms (DSA) repository! This repository contains implementations of various data structures and algorithms in Python.

## Table of Contents

- [Graphs](#graphs)
  - [Adjacency Matrix](#adjacency-matrix)
  - [Adjacency List](#adjacency-list)
- [Linked Lists](#linked-lists)
  - [Singly Linked List](#singly-linked-list)
  - [Doubly Linked List](#doubly-linked-list)
- [Algorithms](#algorithms)
  - [Depth-First Search (DFS)](#depth-first-search-dfs)

## Graphs

### Adjacency Matrix

Graphs can be represented in adjacency matrix form with vertices (V) and edges (E). An adjacency matrix is a 2D array made of V x V. Both row and column represent vertices, and 1 represents an edge between the vertices.

![Adjacency Matrix](https://cdn.programiz.com/sites/tutorial2program/files/adjacency-matrix_1.png)

### Adjacency List

Graphs can also be represented using an adjacency list where the relationship between vertices is shown with the help of a linked list.

![Adjacency List](https://cdn.programiz.com/sites/tutorial2program/files/adjacency-list.png)

For more details, check the [Graph Readme](Graph/Readme.md).

## Linked Lists

### Singly Linked List

A singly linked list is a linear data structure where each element is a separate object. Each element (node) of a list is comprising two items - the data and a reference to the next node.

```python
# Example usage of LinkedList
ll = LinkedList()
ll.addNode(10)
ll.addNode(20)
ll.display()
```
