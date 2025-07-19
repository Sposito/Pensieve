Rust variables are immutable by default. they are defined using the keyword `let`. They can be explicitly made mutable buy the use of the key word  `mut`. There is also the keyword `const` that is similar with a non-mutable let but it is so by enforcing and it does require a type anotation.

#### Rust Data types
Intagers can be signed or unsigned and range in sizes from 8-bit to 128-bit, like in `i8`, or `i64` or `u16` or `u32`.
```
let dec = 98_100;
let hex = 0xfff;
let octal = 0o77;
let binary = 0b111_00
```

Floats default precision is 64bits
```
let x = 2.0; // f64
let y: f32 = 3.0; // f32

```

Tuples
tuples are a coolection of items no necessarily of the same time
```
let tup = (5,2.0,'a')

```

Array
arrays are similiar to tuples but they do require a single type. invalid acess in arrays are caught by default at runtime raising a panic.
```
let arr = [0, 2, 4, 5]
```

