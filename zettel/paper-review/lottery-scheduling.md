#paper #OS
# Lottery Scheduling Review

## Introduction
Lottery Scheduling: Flexible Proportional-Share Resource Management explores stochastic alternatives for multithreaded process management\cite{waldspurger1994lottery}.


## Analysis
This paper addresses the starvation problem. In multithreaded systems that manage their scheduling using a priority list, it is possible that low priority processes end up virtually never scheduled because higher priority ones would never yield.

The proposed solution is a lottery system, where every process holds a given number of tickets, and inside every interval window a draw is called, and the chance of each process running is the ratio of its own ticks by the total sum of tickets of all other processes, this concept extends all the way up to tasks and users.

The lottery proposed in the paper is based on the Park-Miller algorithm \cite{park1988random} and is able to determine the next process; the author's implementation is said to take 10 RISK instructions.

Finally, it is important to mention that a process is compensated if not fully utilizing its scheduled time and that it is also possible for a client to transfer its own tickets for someone else holding a dependency of their own. 


## Conclusion
From a micro-kernel perspective, where modularity is key, the lottery system seemed to thrive, as demonstrated by their results. It seems that this method has minimal overhead for the systems of the time. This paper shows a clever and fair way of managing system resources.

```
@inproceedings{waldspurger1994lottery,
  title={Lottery scheduling: Flexible proportional-share resource management},
  author={Waldspurger, Carl A and Weihl, William E},
  booktitle={Proceedings of the 1st USENIX conference on Operating Systems Design and Implementation},
  pages={1--es},
  year={1994}
}
```
