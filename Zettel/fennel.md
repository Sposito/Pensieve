# _
Fennel is a [[programming language]] from [[lisp]] family syntax and [[Lua]] semantics
# Getting Started with Fennel

## Overview

- OK, so how do you do things?
  - Functions and lambdas  
  - Locals and variables  
  - Numbers and strings  
  - Tables  
  - Sequential Tables  
  - Iteration  
  - Looping  
  - Conditionals  
- Back to tables just for a bit  
- Error handling  
- Variadic Functions  
- Strict global checking  
- Gotchas  
- Other stuff just works  
- Modules and multiple files  
  - Relative require  
  - Compile-time relative include  
  - Requiring modules from modules other than init.fnl  

## A programming language is made up of syntax and semantics

The semantics of Fennel vary only in small ways from Lua (all noted below). The syntax of Fennel comes from the lisp family of languages. Lisps have syntax which is very uniform and predictable, which makes it easier to write code that operates on code as well as structured editing.

If you know Lua and a lisp already, you'll feel **right at home** in Fennel. Even if not, Lua is one of the simplest programming languages in existence, so if you've programmed before you should be able to pick it up without too much trouble, especially if you've used another dynamic imperative language with closures. The Lua reference manual is a fine place to look for details, but Fennel's own Lua Primer is shorter and covers the highlights.

If you've already got some Lua example code and you just want to see how it would look in Fennel, you can learn a lot from putting it in **antifennel**.

---

# OK, so how do you do things?

## Functions and lambdas

Use `fn` to make functions. If you provide an optional name, the function will be bound to that name in local scope; otherwise it is simply an anonymous value.

> A brief note on naming: identifiers are typically lowercase separated by dashes (aka "kebab-case"). They may contain digits too, as long as they're not at the start. You can also use the question mark (typically for functions that return a true or false, ex., at-max-velocity?). Underscores (`_`) are often used to name a variable that we don't plan on using.

The argument list is provided in square brackets. The final value in the body is returned.

**If you've never used a lisp before, the main thing to note is that the function or macro being called goes inside the parens, not outside.**

```lisp
(fn print-and-add [a b c]
  (print a)
  (+ b c))
```

Functions can take an optional docstring in the form of a string that immediately follows the argument list. Under normal compilation, this is removed from the emitted Lua, but during development in the REPL the docstring and function usage can be viewed with the `,doc` command:

```lisp
(fn print-sep [sep ...]
  "Prints args as a string, delimited by sep"
  (print (table.concat [...] sep)))

,doc print-sep ; -> outputs:
;; (print-sep sep ...)
;;   Prints args as a string, delimited by sep
```

Like other lisps, Fennel uses semicolons for comments.

Functions defined with `fn` are fast; they have no runtime overhead compared to Lua. However, they also have no arity checking. (That is, calling a function with the wrong number of arguments does not cause an error.) For safer code you can use `lambda` which ensures you will get at least as many arguments as you define, unless you signify that one may be omitted by beginning its name with a **?**:

```lisp
(lambda print-calculation [x ?y z]
  (print (- x (* (or ?y 1) z))))
```

```lisp
(print-calculation 5) ; -> error: Missing argument z
(print-calculation 5 nil 3) ; -> 2
```

Like `fn`, lambdas accept an optional docstring after the argument list.

---

## Locals and variables

Locals are introduced using `let` with the names and values wrapped in a single set of square brackets:

```lisp
(let [x (+ 89 5.2)
      f (fn [abc] (print (* 2 abc)))]
  (f x))
```

Here `x` is bound to the result of adding 89 and 5.2, while `f` is bound to a function that prints twice its argument. These bindings are only valid inside the body of the `let` call.

You can also introduce locals with `local`, which is nice when they'll be used across the whole file, but in general `let` is preferred inside functions because it's clearer at a glance where the value can be used:

```lisp
(local tau-approx 6.28318)
```

Locals set this way cannot be given new values, but you can introduce new locals that shadow the outer names:

```lisp
(let [x 19]
  ;; (set x 88) <- not allowed!
  (let [x 88]
    (print (+ x 2))) ; -> 90
  (print x)) ; -> 19
```

If you need to change the value of a local, you can use `var` which works like `local` except it allows `set` to work on it. There is no nested `let`-like equivalent of `var`.

```lisp
(var x 19)
(set x (+ x 8))
(print x) ; -> 27
```

---

## Numbers and strings

All standard arithmetic operators like `+`, `-`, `*`, and `/` work in **prefix** form. Note that numbers are double-precision floats in all Lua versions prior to 5.3, which introduced integers. On 5.3 and up, integer division uses `//` and bitwise operations use `lshift`, `rshift`, `bor`, `band`, `bnot` and `xor`. These bitwise operators and integer division won't work on older Lua versions.

You may also use underscores to separate sections of long numbers. The underscores have no effect on the value.

```lisp
(let [x (+ 1 99)
      y (- x 12)
      z 100_000]
  (+ z (/ y 10)))
```

Strings are essentially immutable byte arrays. UTF-8 support is provided in the `utf8` table in Lua 5.3+ or from a 3rd-party library in earlier versions. Strings are concatenated with `..`:

```lisp
(.. "hello" " world")
```

---

## Tables

In Lua (and thus in Fennel), tables are the only data structure. The main syntax for tables uses curly braces with key/value pairs in them:

```lisp
{"key" value
 "number" 531
 "f" (fn [x] (+ x 2))}
```

Use `.` to get values out of tables:

```lisp
(let [tbl (function-which-returns-a-table)
      key "a certain key"]
  (. tbl key))
```

And `tset` to put them in:

```lisp
(let [tbl {}
      key1 "a long string"
      key2 12]
  (tset tbl key1 "the first value")
  (tset tbl key2 "the second one")
  tbl)
; -> {"a long string" "the first value" 12 "the second one"}
```

---

## Sequential Tables

Some tables are used to store data that's used sequentially; the keys in this case are just numbers starting with 1 and going up. Fennel provides alternate syntax for these tables with square brackets:

```lisp
["abc" "def" "xyz"] ; equivalent to {1 "abc" 2 "def" 3 "xyz"}
```

Lua's built-in `table.insert` function is meant to be used with sequential tables; all values after the inserted value are shifted up by one index. If you don't provide an index to `table.insert` it will append to the end of the table.

The `table.remove` function works similarly; it takes a table and an index (which defaults to the end of the table) and removes the value at that index, returning it.

```lisp
(local ltrs ["a" "b" "c" "d"])

(table.remove ltrs)       ; Removes "d"
(table.remove ltrs 1)     ; Removes "a"
(table.insert ltrs "d")   ; Appends "d"
(table.insert ltrs 1 "a") ; Prepends "a"

(. ltrs 2) ; -> "b"
;; ltrs is back to its original value ["a" "b" "c" "d"]
```

The `length` form returns the length of sequential tables and strings:

```lisp
(let [tbl ["abc" "def" "xyz"]]
  (+ (length tbl)
     (length (. tbl 1)))) ; -> 6
```

Note that the length of a table with gaps in it is undefined. Lua's standard library is very small, and thus several functions you might expect (e.g. map, reduce, filter) are absent. In Fennel macros are used for this instead; see `icollect`, `collect`, and `accumulate`.

---

## Iteration

Looping over table elements is done with `each` and an iterator like `pairs` (used for general tables) or `ipairs` (for sequential tables):

```lisp
(each [key value (pairs {"key1" 52 "key2" 99})]
  (print key value))

(each [index value (ipairs ["abc" "def" "xyz"])]
  (print index value))
```

Whether a table is sequential or not depends on which iterator is used with it. You can call `ipairs` on any table, and it will only iterate over numeric keys starting with 1 until it hits a nil.

You can use any Lua iterator with `each`, but these are the most common. Here's an example that walks through matches in a string:

```lisp
(var sum 0)
(each [digits (string.gmatch "244 127 163" "%d+")]
  (set sum (+ sum (tonumber digits))))
```

If you want to get a table back, try `icollect` (for a sequential table) or `collect` (for a key/value table). A body which returns `nil` will cause that to be omitted from the resulting table.

```lisp
(icollect [_ s (ipairs [:greetings :my :darling])]
  (if (not= :my s)
      (s:upper)))
;; -> ["GREETINGS" "DARLING"]

(collect [_ s (ipairs [:greetings :my :darling])]
  s (length s))
;; -> {:darling 7 :greetings 9 :my 2}
```

A lower-level iteration construct is `for`, which iterates numerically from the provided start value to the inclusive finish value:

```lisp
(for [i 1 10]
  (print i))
```

You can specify an optional step value; this loop will only print odd numbers under ten:

```lisp
(for [i 1 10 2]
  (print i))
```

---

## Looping

If you need to loop but don't know how many times, you can use `while`:

```lisp
(while (keep-looping?)
  (do-something))
```

---

## Conditionals

Fennel's `if` form can be used the same way as in other lisps, but it can also be used as **cond** for multiple conditions compiling into `elseif` branches:

```lisp
(let [x (math.random 64)]
  (if (= 0 (% x 2))
      "even"
      (= 0 (% x 9))
      "multiple of nine"
      "I dunno, something else"))
```

With an odd number of arguments, the final clause is interpreted as "else". Being a lisp, Fennel has no statements, so `if` returns a value as an expression. Lua programmers will be glad to know there's no need to construct precarious chains of `and/or` just to get a value!

The other conditional is `when`, used for an arbitrary number of side-effects with no else clause:

```lisp
(when (currently-raining?)
  (wear "boots")
  (deploy-umbrella))
```

---

# Back to tables just for a bit

Strings that don't have spaces or reserved characters can use the **`:shorthand`** syntax, often for table keys:

```lisp
{:key value :number 531}
```

If a table has string keys like this, you can pull values out of it easily with a dot if the keys are known up front:

```lisp
(let [tbl {:x 52 :y 91}]
  (+ tbl.x tbl.y)) ; -> 143
```

You can also use this syntax with `set`:

```lisp
(let [tbl {}]
  (set tbl.one 1)
  (set tbl.two 2)
  tbl) ; -> {:one 1 :two 2}
```

If a table key has the same name as the variable you're setting it to, you can omit the key name and use `:` instead:

```lisp
(let [one 1 two 2
      tbl {: one : two}]
  tbl) ; -> {:one 1 :two 2}
```

Finally, `let` can destructure a table into multiple locals:

- **Positional destructuring**:

```lisp
(let [data [1 2 3]
      [fst snd thrd] data]
  (print fst snd thrd)) ; -> 1       2       3
```

- **Destructuring of tables via key**:

```lisp
(let [pos {:x 23 :y 42}
      {:x x-pos :y y-pos} pos]
  (print x-pos y-pos)) ; -> 23      42
```

As above, if a table key has the same name as the variable you're destructuring it to, you can omit the key name and use `:`:

```lisp
(let [pos {:x 23 :y 42}
      {: x : y} pos]
  (print x y)) ; -> 23      42
```

This can nest and mix and match:

```lisp
(let [f (fn [] ["abc" "def" {:x "xyz" :y "abc"}])
      [a d {:x x : y}] (f)]
  (print a d)
  (print x y))
```

If the size of the table doesn't match the number of binding locals, missing values are filled with **nil** and extra values are discarded. Note that unlike many languages, **nil** in Lua actually represents the absence of a value, and thus tables cannot contain nil. It is an error to try to use nil as a key, and using nil as a value removes whatever entry was at that key before.

---

# Error handling

Errors in Lua have two forms they can take. Functions in Lua can return any number of values, and most functions which can fail will indicate failure by using two return values: **nil** followed by a failure message string. You can interact with this style of function in Fennel by destructuring with parens instead of square brackets:

```lisp
(case (io.open "file")
  f (do (use-file-contents (f:read :*all))
         (f:close))
  (nil err-msg) (print "Could not open file:" err-msg))
```

You can write your own function which returns multiple values with `values`.

```lisp
(fn use-file [filename]
  (if (valid-file-name? filename)
      (open-file filename)
      (values nil (.. "Invalid filename: " filename))))
```

The problem with this type of error is that it does not compose well; the error status must be propagated all the way along the call chain from inner to outer. To address this, you can use **error**. This will terminate the whole process unless it's within a protected call, similar to throwing an exception in other languages. You can make a protected call with `pcall`:

```lisp
(let [(ok? val-or-msg) (pcall potentially-disastrous-call filename)]
  (if ok?
      (print "Got value" val-or-msg)
      (print "Could not get value:" val-or-msg)))
```

`pcall` returns a boolean (`ok?`) to let you know if the call succeeded or not, and a second value (`val-or-msg`) which is the actual value if it succeeded or an error message if it didn't.

The `assert` function takes a value and an error message; it calls `error` if the value is **nil** and returns it otherwise. This can be used to turn multiple-value failures into errors (kind of the inverse of `pcall` which turns errors into multiple-value failures):

```lisp
(let [f (assert (io.open filename))
      contents (f.read f "*all")]
  (f.close f)
  contents)
```

---

## Variadic Functions

Fennel supports variadic functions (functions that take any number of arguments). The syntax for taking a variable number of arguments to a function is the **`...`** symbol, which must be the last parameter to a function. This syntax is inherited from Lua rather than Lisp.

The `...` form is **not** a list or first class value; it expands to multiple values inline. To access individual elements of the vararg, you can destructure with parentheses, wrap it in a table literal (`[...]`), or use the `select` function from Lua's core library. Often, the vararg can be passed directly to another function.

```lisp
(fn print-each [...]
  (each [i v (ipairs [...])]
    (print (.. "Argument " i " is " v))))

(print-each :a :b :c)
```

```lisp
(fn myprint [prefix ...]
  (io.write prefix)
  (io.write (.. (select "#" ...) " arguments given: "))
  (print ...))

(myprint ":D " :d :e :f)
```

Varargs are scoped differently than other variables—they are only accessible to the function in which they are created. Functions cannot close over them. The following example **will not work**, because the varargs in the inner function are out of scope:

```lisp
(fn badcode [...]
  (fn []
    (print ...)))
```

---

## Strict global checking

If you get an error that says **unknown global in strict mode** it means that you're trying to compile code that uses a global which the Fennel compiler doesn't know about. Most of the time, this is due to a coding mistake. However, in some cases you may get this error with a legitimate global reference.

You can use `_G.myglobal` to refer to it in a way that works around this check and calls attention to the fact that this is in fact a global.

Another possible cause for this error is a modified function environment. The solution depends on how you're using Fennel:

- **Embedded Fennel** can have its searcher modified to ignore certain (or all) globals via the `allowedGlobals` parameter. See the Lua API page for instructions.  
- **Fennel's CLI** has the `--globals` parameter, which accepts a comma-separated list of globals to ignore. For example, to disable strict mode for globals `x`, `y`, and `z`:

  ```
  fennel --globals x,y,z yourfennelscript.fnl
  ```

---

## Gotchas

There are a few surprises that might bite seasoned lispers. Most of these result necessarily from Fennel's insistence upon imposing zero runtime overhead over Lua.

- The arithmetic, comparison, and boolean operators are **not** first-class functions. They can behave in surprising ways with multiple-return-valued functions, because the number of arguments to them must be known at compile-time.

- There is **no** `apply` function; instead use `table.unpack` or `unpack` (depending on your Lua version):
  ```lisp
  (f 1 3 (table.unpack [4 9]))
  ```

- Tables are compared for equality by identity, **not** based on the value of their contents.

- Return values in the repl will get pretty-printed, but calling `(print tbl)` will emit output like `table: 0x55a3a8749ef0`. For debugging, you might define a printer function which calls `fennel.view` on its argument before printing it:
  ```lisp
  (local fennel (require :fennel))
  (fn _G.pp [x] (print (fennel.view x)))
  ```
  If you add this definition to your `~/.fennelrc` file it will be available in the standard repl.

- Lua programmers should note Fennel functions cannot do **early returns**.

---

## Other stuff just works

Built-in functions in Lua's standard library can be called with no fuss and no overhead. This includes features like **coroutines**, which are often implemented using special syntax in other languages. Coroutines let you express non-blocking operations without callbacks.

Tables in Lua may seem a bit limited, but **metatables** allow a great deal more flexibility. All metatable features are accessible from Fennel code just the same as from Lua.

---

# Modules and multiple files

You can use the `require` function to load code from other files:

```lisp
(let [lume (require :lume)
      tbl [52 99 412 654]
      plus (fn [x y] (+ x y))]
  (lume.map tbl (partial plus 2))) ; -> [54 101 414 656]
```

Modules in Fennel and Lua are simply tables which contain functions and other values. The **last value** in a Fennel file is used as the value of the whole module. Technically this can be any value, but a table is most common.

To require a module that's in a subdirectory, take the file name, replace the slashes with dots, and remove the extension, then pass that to `require`. For instance, `lib/ui/menu.lua` would be read when loading the module `lib.ui.menu`.

When you run your program with the `fennel` command, you can call `require` to load Fennel or Lua modules. But in other contexts (such as compiling to Lua and then using the `lua` command, or in programs that embed Lua) it will not know about Fennel modules. You need to install the searcher that knows how to find `.fnl` files:

```lisp
require("fennel").install()
local mylib = require("mylib") -- will compile and load code in mylib.fnl
```

Once you add this, `require` will work on Fennel files just like Lua. For instance `(require :mylib.parser)` will look in `"mylib/parser.fnl"` on Fennel's search path, stored in `fennel.path`. The path usually includes an entry to let you load things relative to the current directory by default.

---

## Relative require

There are several ways to write a library which uses modules. One of them is to rely on something like LuaRocks to manage library installation and availability of its modules. Another way is to use the **relative require** style for loading nested modules, making the library not depend on the root directory name or its location.

For example, here's a small library with an `init.fnl` file and a module at the root directory:

```lisp
;; file example/init.fnl:
(local a (require :example.module-a))

{:hello-a a.hello}
```

Here, the main module requires additional `example.module-a` module, which holds the implementation:

```lisp
;; file example/module-a.fnl
(fn hello [] (print "hello from a"))
{:hello hello}
```

The main issue is that the path to the library must be **exactly** `example`. If the library were moved into `libs` directory and required as `(require :libs.example)`, there would be a runtime error because the code tries to require `:example.module-a`, which won't exist under the new path `:libs.example.module-a`.

LuaRocks addresses this by setting the `LUA_PATH` environment variable. In the Fennel ecosystem we often prefer a simpler approach: just drop a library into your project or use a git submodule, and let the library handle relative paths internally.

Here's how a **relative require path** can be specified in `libs/example/init.fnl` to make it name/path agnostic:

```lisp
;; file libs/example/init.fnl:
(local a (require (.. ... :.module-a)))

{:hello-a a.hello}
```

It works because, if we now require the library with `(require :libs.example)`, the first value in `...` will hold the string `"libs.example"`. That string is then concatenated with `".module-a"`, and `require` will properly find and load the nested module at runtime under the `"libs.example.module-a"` path. This is a **Lua** feature, not specific to Fennel.

---

## Compile-time relative include

Since Fennel v0.10.0, this also works at compile-time when using the **`include`** special or the **`--require-as-include`** flag, as long as the expression can be computed at compile time. This means it must not refer to locals or globals:

**Non-working example** (at compile time, because `current-module` is not known):
```lisp
(local current-module ...)
(require (.. current-module :.other-module))
```

**Working example**:
```lisp
(require (.. ... :.other-module))
```

The `...` module args are propagated during compilation, so when the application using this library is compiled, all library code is correctly included into the self-contained Lua file.  

---

## Requiring modules from modules other than init.fnl

To require a module from another module (not the `init` module), keep the path up to the current module but remove the module name. Suppose we add `greet.fnl` in `libs/example/utils/greet.fnl` and want to require it from `libs/example/module-a.fnl`:

```lisp
;; file libs/example/utils/greet.fnl:
(fn greet [who] (print (.. "hello " who)))
```

We can require it like this:

```lisp
;; file libs/example/module-a.fnl
(local greet (require (.. (: ... :match "(.+)%.[^.]+") :.utils.greet)))

(fn hello [] (print "hello from a"))

{:hello hello :greet greet}
```

Here we determine the **parent module name** by calling the `match` method on the current module name (`...`). That way, `module-a.fnl` can refer properly to `greet.fnl` in `utils` without relying on the entire path being named `libs.example...`.