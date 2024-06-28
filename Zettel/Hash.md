### _

A hash [[Algorithm]] is a function that returns a constant sized value from a given arbitrary input . It is useful for assigning, for examples, identifier numbers for data. Since the output is a finite number, but the input is potentially infinite, one common issue with hashing algorithms is that, depending on the implementation two distinct inputs could output the same value, we call those not singular results "collisions". With that in mind it is fair to assume that an optimal hashing algorithm is one that minimizes computational time while maxing the range of possible outputs (minimize collisions).

---
## Examples:

![[C#djb2]]

