#paper #OS 
# Scheduler Activations
## Introduction
The kernel/userspace barrier is costly; this makes user-level threads inherently more efficiently. This creates a problem since information about kernel threading is opaque to the user.\cite{anderson1992scheduler}

## Analysis
After convincing the user of the issue, this paper proposes a solution involving a new kernel interface and a user-level thread package.

When implementing user-spaces threads on top of kernel threads, we incur a hiccup situation; despite user-level threads being more efficient if no kernel calls are required, the user threads have no idea how many processors they have available them. On the other hand, the kernel is also blind and do not know the amount of parallelism needed from it, and it is also in the dark to allocate the correct number of resources to it.

The proposed solution gives each application a virtual multi-processor, so it knows precisely how many physical cores it has access to. The kernel in this scenario holds control of the allocation of processors among address spaces and can change the number of physical cores assigned to an application during execution.

## Conclusion
Authors mention that the effects of their modifications are more easily observed when more cores are available. Also, no significant degradation could be found in most scenarios where improvements were not observed.

The kernel mechanism used to implement this active communication with applications is called scheduler activations. Authors mention that despite it being used in this example to facilitate the abstraction of user threads, it could also be used in any other concurrency abstraction at the user level.


```
@article{anderson1992scheduler,
  title={Scheduler activations: Effective kernel support for the user-level management of parallelism},
  author={Anderson, Thomas E and Bershad, Brian N and Lazowska, Edward D and Levy, Henry M},
  journal={ACM Transactions on Computer Systems (TOCS)},
  volume={10},
  number={1},
  pages={53--79},
  year={1992},
  publisher={ACM New York, NY, USA}
}
```