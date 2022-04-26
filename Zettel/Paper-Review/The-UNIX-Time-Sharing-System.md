#paper #OS

# The UNIX Time-Sharing System Review

## Introduction
The [[Unix]] Time-Sharing System written in 1974 about 4 or 5 years down the first functional version of Unix is a nice and fair reflection from Dennis Richie Ken Thompson about the system key strengths and capabilities namely its file system, process management and the shell. It is a very fortunate reading at the beginning of an Operational Systems discipline as time has proved it so fundamental for the field in the years to come.


## Summary
The article begins with a historical contextualization of the OS path down to that point in time, the hardware it was designed around, and its main use cases (Sections 1 and 2). From there it jumps straight on discussion and presentation about its file system on Section 3 . Section 4 is about more technical tidbits of the FS implementation. Just after this, we are presented with how the system handle process in section 5, with that in mind we are naturally exposed to the shell in the next section. Section 7 is an acknowledgement of the influences it had. Finally, the last two sections present more objective data about system performance and reliability. 


## Analysis
As someone who used Posix like OS for most of my life it's fascinating reading on section 3.3 the original description of concepts we always took as granted such as "On Linux everything is a file", it became clear how this choice attempted to simplify how the system organizes itself as a whole, not needing too many handling cases for its different aspects. Another highlight of the file system is the efficiency of its tree-like structure (not considering  . and ..) and the ingenuity of i-numbers, a  numeric file reference used in system tables to retrieve its descriptor. This simplicity permits the construction of notions such as i-lists where Unix can handle FS consistency cheaply. 

Although the authors elect the file system as the most important job of Unix, I can't neglect to mention the peculiarity of how Unix handles its process: except by the very process of its initialization, Unix processes are always created by a clone of the parent process followed by straight on wipe of the new process image to replaced by its own. This counter-intuitive behaviour creates a concise parent-child relationship that allows easy implementation of certain features like Piping (an inter-process communication channel). The Shell exploits this feature very well:  where it leverages those links by allowing very explicit chaining of different programs. That, in my opinion, give rise to the most powerful capability of Unix: its versatility.


## Conclusion

This is a very interesting reading of an early view of the System by its creators. It is a somewhat comfortable read for us today, when those concepts are broadly adopted in many of the systems we interact with daily, but I imagine it was necessary some work of imagination by its readers back in the day. It is a very descriptive text, and for that, it serves its purpose. If anything one could expect a deeper objective analysis of system performance and reliability numbers. Also, there is a noticeable lack of acknowledgement of system downsides, which is somewhat understandable when we take into account the difficulties the team had with Bell Labs concerning lack of trust in the new system.

---


```
@article{ritchie1978unix,
  title={The UNIX time-sharing system},
  author={Ritchie, Dennis M and Thompson, Ken},
  journal={Bell System Technical Journal},
  volume={57},
  number={6},
  pages={1905--1929},
  year={1978},
  publisher={Wiley Online Library}
}
```