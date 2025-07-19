#### _
Go is a general purpose, compiled, typed, imperative, garbage collected language developed by [[Google]] as a fast and simple alternative to writing performant code for the web. It main goal is to cut the complexity and unsafeties of [[c-plus-plus|C++]] while keeping a somewhat familiar [[c]] syntax. It is specifically tailored towards concurrent programming


## The Language
### Control
#### Conditional Flow
```go
// basic case:
fun condition (x int) {
.  if x > 10 {
.     return x
.   } 
.   else {
.     return 0
.   }
}

// with a statement:
if a := b + c; a < 10{}

// Type assertion inside if
var val interface{} = "foo"
if str, ok := val.(string); ok {
.   fmt.Println(str)
}
```

#### Loops
```go
for { // or even better infinite loop:
	for ; i < 10{ // "while"
	
	}
	for i := 1; i < 10; i++{ // basic iterattion
		a := 1
		for i < 2 { // single contion you can ommit ;

		}
tag: // labes
		if False{
			continue tag: // labes
		}	
	}
}
```
### Language Keywords
```go
break        default      func         interface    select
case         defer        go           map          struct
chan         else         goto         package      switch
const        fallthrough  if           range        type
continue     for          import       return       var
```





### References
https://go.dev/ref/spec ^ref1
https://github.com/a8m/golang-cheat-sheet