### _
Zig is general purpose systems [[Programming Languages|programming language]] that embraces simplicity and safety. It was conceived as better [[C]] and builds upon its shortcomings. It aims for code clarity and avoidance of hidden "magic code" i does not support macros, having its meta-programming based on the concept of "comp time", where plain sig code can be marked as code to be executed at compile time. 

---
### Assignments
In zig a value can be a constant or variable, it has an identifier(its name) and a type. Types can be inferred or explicitly annotated.

```zig title="values.zig"
const some_const : i32 = -5;
var   some_var   : u32 = 5;

const inf_const = @as(u32, 9);
var  inf_var.  = @as(i32, -22);

const idk : i32 = undefined;
```

### Pointers
Pointers in Zig are similar to C pointers, with the diference that they are tagged and the compilers forces the programmer to validate it before accessing. Zig pointers can point to location 0 and also cannot have null as value.

They follow the `*T` syntax, where T is the child type. Referencing is done by `&variable` and dereferencing is done with `variable.*`

Example:
```zig fold title=pointers.zig
fn double(number: *u16) void {
    number.* *= 2;
}

test "pointer test" {
 var n: u16 = 2;
 double (&n);
 try expect(n == 4);
}
```
