"""Lesson 3: Understanding Big O Notation

What does Big O mean?
Big O is a way to describe how an algorithm's work grows as the input gets bigger.

Don't worry about memorizing the notation yet. Understand the idea first.
List size	Worst-case checks for linear search
5 numbers	5 checks
10 numbers	10 checks
100 numbers	100 checks
1,000 numbers	1,000 checks

We call this \(O(n)\) — “Big O of n.”

Here, n means the number of items.

Big O: Describes how an algorithm's work grows as the input grows.
\(O(1)\) — Constant time: The work stays the same.
\(O(n)\) — Linear time: The work grows with the number of items.
Linear search: Its worst case is \(O(n)\), because it may check every item.
"""