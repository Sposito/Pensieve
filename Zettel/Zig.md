##### Zig
Zig is general purpose systems [[Programming Languages|programming language]] that embraces simplicity and safety. It was conceived as better [[C]] and builds upon its shortcomings. It aims for code clarity and avoidance of hidden "magic code" i does not support macros, having its meta-programming based on the concept of "comp time", where plain sig code can be marked as code to be executed at compile time. 

###### Pointers
Pointers in zigs are similar to C pointers, with the diference that they are tagged and the compilers forces the programmer to validate it before accessing. Zig pointers can point to location 0 and also cannot have null as value.

They follow the `*T` syntax, where T is the child type. Referencing is done by `&variable` and dereferencing is done `with variable.*`

Example:
``` zig
```
