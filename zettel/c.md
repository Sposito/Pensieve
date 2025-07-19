#article
#### _
**C** is a high-level, general-purpose [[programming-languages|programming language]] developed by Dennis Ritchie in the early 1970s at Bell Labs for the [[unix]] project. Key points are performance and control over system resources, C is extensively used in system programming, operating systems, and embedded systems. Key features include portability, low-level memory access, and the ability to generate efficient machine code. It supports structured programming and provides a rich standard library. 
C's influence extends to many modern programming languages, making it a foundational language in the field of computer science. Most inter communication between projects in different languages is done in the C ABI.

---
## The Language
### Pointers
- **Pointer** is a variable that stores the memory address of another variable.
#### Symbols
1. **`*`** (asterisk):

- **Declaration**: Used to declare a pointer variable.

```c
int *ptr; // ptr is a pointer to an integer
```
- **Dereference**: Used to access the value in the memory location pointed to by the pointer.
```c
int x = 10;
int *ptr = &x;
printf("%d", *ptr); // prints 10
```
2. **`&`** (ampersand):
- **Address**: Used to get the memory address of a variable.
```c
int x = 10;
int *ptr = &x; // ptr now stores the address of x
```

3. **`[]`** (brackets):
- **Arrays**: Used to access elements of an array.

```c
int arr[3] = {1, 2, 3};
printf("%d", arr[1]); // prints 2
```

- In pointer contexts, `arr[i]` is equivalent to `*(arr + i)`:
```c
int *ptr = arr;
printf("%d", *(ptr + 1)); // prints 2
```
#### Pointers in a nutshell
- **`*`**: Declares and dereferences pointers.
- **`&`**: Obtains the address of a variable.
- **`[]`**: Accesses elements of an array (shorthand syntax for pointer operations).
---

### Algorithms
#### Hashes 

![[hash#_]]

##### djb2
First reported in com.lang.c
```c
    unsigned long
    hash(unsigned char *str)
    {
        unsigned long hash = 5381;
        int c;

        while (c = *str++)
            hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

        return hash;
    }
```
---
[[c#^ref2|ref2]]

#### Learning Resources
[Harvard Lecture about C](https://www.youtube.com/watch?v=URrzmoIyqLw)  ^ref1
http://www.cse.yorku.ca/~oz/hash.html ^ref2

---
#### Projects of Interest:
- [Raylib](https://github.com/raysan5/raylib.git) Simple game dev libraries
- [RL Base](https://github.com/Sposito/raylib-base) Functionality written on top of Raylib for writing my own games
- [microui](https://github.com/rxi/microui) Very simple UI framework
- [Linux](https://kernel.org) Linux Kernel, most famous C project

