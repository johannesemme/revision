# Belief revision engine

A Python implementation of an Artificial Intelligence (AI) engine that can revise an existing belief base when new beliefs are added.

### About the project
The project is part of the course [02180 Introduction to Artificial Intelligence] at DTU.

### Algorithms

* **Resolution**:  
  Based on the `PL-Resolution` algorithm in the book "[Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/)" by Stuart Russell and Peter Norvig. 

### Authors

* [Laura Marott](https://github.com/LauraMarott) (s152973)
* [Johannes](https://github.com/johannesemme) (s144003)

### Project structure
* `main.py`: The main class that executes
* `resolution.py`: Implementation of resolution algorithm.
* `revision.py`: Implementation of revision
* `logic.py`: Useful functions for operations on logic formulas
* `ui.py`: Functions for User Interface

### Example of usage
```
------- MENU -------
1. Add new belief
2. Print belief base
3. Empty belief base
4. Quit

Choose from the menu: 1

Write belief: P

Assign priority (real number betweeen 0 and 1): 0.3

Belief base: 
{P: 0.3}

------- MENU -------
1. Add new belief
2. Print belief base
3. Empty belief base
4. Quit

Choose from the menu: 1

Write belief: Q

Assign priority (real number betweeen 0 and 1): 0.7

Belief base: 
{P: 0.3, Q: 0.7}

------- MENU -------
1. Add new belief
2. Print belief base
3. Empty belief base
4. Quit

Choose from the menu: 1

Write belief: P >> Q

Assign priority (real number betweeen 0 and 1): 0.7

Belief base: 
{P: 0.3, Q: 0.7, Q | ~P: 0.7}

------- MENU -------
1. Add new belief
2. Print belief base
3. Empty belief base
4. Quit

Choose from the menu: 1

Write belief: ~Q

Assign priority (real number betweeen 0 and 1): 0.8

Belief base: 
{Q | ~P: 0.7, ~Q: 0.8}

```
