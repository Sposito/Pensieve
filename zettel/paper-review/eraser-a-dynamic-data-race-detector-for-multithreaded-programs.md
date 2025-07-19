#paper #OS
# Eraser A Dynamic Data Race Detector for Multithreaded Programs Review 

## Introduction
Multithreading is hard today, and one can only imagine how terrifying back when it was something new. This paper describes Eraser, a tool for detecting racing conditions on multithreaded programs\cite{savage1997eraser}


## Analysis
A data race is a condition where a program running in parallel fails due to the difference between the observed and the expected execution order.

In order to avoid this condition, programmers use locks that are nothing more than semaphores indicating when some thread can read/write on some portion of the memory.

When programmers find themselves debugging this kind of situation, it could take a considerable amount of time to detect precisely what is going on since the more complex the system, the harder it may become to reproduce the problem.

Eraser is a tool based on group theory based algorithm named the lockset. It consists in taking notes of reads and writes during program execution and later checking the intersection of unexpected intersections of unprotected reads and writes.

It needs to go a bit further by relaxing these algorithm constraints to cater to common false positives. Still, the authors mention that false positives are expected to happen,


## Conclusion
Reading this article, one can get somewhat uncomfortable, maybe because it depends on runtime execution with no guarantee of total coverage. It feels more natural to expect some sort of static checking, although it is not always possible to do so.

For non-mission-critical programs Eraser, back on its time probably was a handy tool for avoiding unforseen races conditions.

```
@article{savage1997eraser,
  title={Eraser: A dynamic data race detector for multithreaded programs},
  author={Savage, Stefan and Burrows, Michael and Nelson, Greg and Sobalvarro, Patrick and Anderson, Thomas},
  journal={ACM Transactions on Computer Systems (TOCS)},
  volume={15},
  number={4},
  pages={391--411},
  year={1997},
  publisher={ACM New York, NY, USA}
}

```
