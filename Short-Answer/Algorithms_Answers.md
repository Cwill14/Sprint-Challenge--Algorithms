#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(n), because we are in a loop that will run a variable amount of times, increasing the amount of times directly compared to the value of n

b)
    <!-- O(n^2) because we have a loop inside of a loop -->
    <!-- O(n), because the n is the dominant part ? -->
    O(n log n), because the first loop is O(n), and the nested loop runs proportionally less the higher n becomes, which would be O(log n).
    O(n) * O(log n) == O(n log n)

c)
    <!-- O(n) I think, because everything inside the recursion is an O(1)? -->
    <!-- O(n^2) because there is recursion? -->
    O(n), each recursion only increases the number of operations by 1. so the higher the number, the more operations

## Exercise II

<!-- how are ever supposed to figure out f without more information given than just the height of building??? does f change with every building?? if this was realistic, wouldn't f be the same no matter the building height? 
^^^^^^^^^^^^^^^^ -->

To figure out what floor the egg breaks at given that the variable n could be a large building, the best way to minimize the number of dropped/broken eggs would be to use a binary search. Binary search would start at floor n/2, and if the egg breaks, then try it at (n/2)/2. if not, try dropping it at (n/2) + (n/2)/2. This pattern would repeat till the floor f is found.

