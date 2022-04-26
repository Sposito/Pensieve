#paper #OS
# IX A Protected Dataplane Operating System for High Throughput and Low Latency Review

## Analysis
On a conventional Linux server, it is common to use a user-level network stack in order to bypass the kernel and gain performance by context switch overheads avoidance. IX \cite{belay2014ix}proposes a solution for this problem by making a separation of the regular kernel responsible for scheduling and system control from a virtualized network stacks called by the author of the "dataplanes". It uses the Dune \cite{belay2012dune} Linux module to be able to run those dataplanes in hardware ring 0 while maintaining full protection.

That said, raw virtualization is not enough to provide satisfactory performance boots; in order to diminish latency, the authors describe some techniques used by IX; it does pass incoming network input as pointers avoiding the neep of copies altogether; it implements a timeout to the incoming batch, not necessarily waiting it to fill before dispatching it. It also locks correlated flows in the same physical core to avoid inter-core communication overheads; finally, it does use a congestion monitor to decide when to allocate and deallocate cores for dataplanes.

## Conclusion
IX proved itself a success and showed much better use of Dune than the benchmark test applications described in \cite{belay2012dune}. Using a single processor socket, it was capable of saturating 4x10GB configurations. Also, the paper authors mention that porting memcached a key-value store\cite{jose2011memcached} to IX, they were able to see more than 3x throughput and drop tail latency in half.

```
@inproceedings{belay2014ix,

title={$\{$IX$\}$: a protected dataplane operating system for high throughput and low latency},

author={Belay, Adam and Prekas, George and Klimovic, Ana and Grossman, Samuel and Kozyrakis, Christos and Bugnion, Edouard},

booktitle={11th USENIX Symposium on Operating Systems Design and Implementation (OSDI 14)},

pages={49--65},

year={2014}

}

```