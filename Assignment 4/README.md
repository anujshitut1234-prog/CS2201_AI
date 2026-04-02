# AI Assignment: Constraint Satisfaction Problems (CSP)

## Overview

This project contains implementations of multiple problems using **Constraint Satisfaction Problems (CSP)** in Python.
Each problem is solved using **backtracking and constraint-based reasoning**, as studied in Artificial Intelligence.

---

## 🔹 Bit 1: Map Coloring (Australia)

### Problem

Assign colors to Australian states such that no two adjacent states share the same color.

### Approach

* Variables: States
* Domain: {Red, Green, Blue}
* Constraints: Neighboring states must have different colors
* Solved using **backtracking**

---

## 🔹 Bit 2: Telangana Map Coloring

### Problem

Assign colors to Telangana districts so that adjacent districts do not share the same color.

### Approach

* CSP formulation with districts as variables
* Backtracking algorithm used
* Ensures all constraints are satisfied

### Visualization

* Implemented using **NetworkX and Matplotlib**
* Districts represented as nodes
* Adjacency represented as edges
* Colors visually displayed

---

## 🔹 Bit 3: Sudoku Solver

### Problem

Solve a 9×9 Sudoku puzzle.

### CSP Formulation

* Variables: Each cell
* Domain: {1–9}
* Constraints:

  * No repetition in rows
  * No repetition in columns
  * No repetition in 3×3 subgrids

### Approach

* Solved using **backtracking search**
* Finds a valid complete solution

---

## 🔹 Bit 4: Cryptarithmetic (SEND + MORE = MONEY)

### Problem

Assign digits to letters such that:

SEND + MORE = MONEY

### CSP Formulation

* Variables: Letters (S, E, N, D, M, O, R, Y)
* Domain: {0–9}
* Constraints:

  * All digits must be unique
  * No leading zero (S ≠ 0, M ≠ 0)
  * Arithmetic equation must be satisfied

### Approach

* Implemented using **backtracking CSP**
* Assigns digits step-by-step and checks constraints

---

## Concepts Used

* Constraint Satisfaction Problems (CSP)
* Backtracking Algorithm
* Constraint Checking
* Recursion
* Graph Representation (for visualization)

---

## How to Run

### Install dependencies (for Bit 2 visualization)

pip install networkx matplotlib

---

## Conclusion

This project demonstrates how various problems such as map coloring, Sudoku, and cryptarithmetic can be modeled and solved using CSP techniques. Backtracking ensures that all constraints are satisfied efficiently.


