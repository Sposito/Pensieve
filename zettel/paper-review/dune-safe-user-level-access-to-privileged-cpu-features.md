---
doi: 10.5555/2387880.2387913
---

#incomplete 
# Dune- Safe User-level Access to Privileged CPU Features [[dune-safe-user-level-access-to-privileged-cpu-features#Refs|¹]]

Dune is a small kernel module that cleverly uses system virtualization capabilities to safely expose privileged hardware at user level without incurring the most common penalties when virtualizing whole systems instead of processes .

# Summary
In the first section, we are introduced to Dune. The second section is a broad overview of hardware virtualization. Section three presents how Dune interacts with the Kernel. The following section is a description of user mode. Section 5 describes the three Applications they built as use cases: SandeBox, Wedge and GC. Section 6 is a more objective analysis evaluating their benchmarks. Before the conclusion, we have a few remarks on hardware changes that could improve solutions like Dune. We also have a few comparisons with a similar concept explored elsewhere, the exokernel, where their similarities and differences are exposed.

# Analysis
Dune answers a quite interesting question: "What could we leverage by using virtualization capabilities at the process level?". The barriers between user and kernel spaces usually imposed to guarantee safety and protection always come at a price. We got in contact with some solutions ranging from small changes or circumventions on the Kernel to radical changes. Dune comes with a less intrusive proposal; by using a small library and a kernel module, applications could benefit from hardware functionality exposed and managed by the hypervisor.  

The keyword here is "process" by acting at the process level; Dune gains a couple of advantages over traditional vmms. It is leaner since it does not need to run a whole new system. It has better overall communications with the rest of the system being just another part of it, capable of communicating more straightforwardly.

For testing those ideas, they write three applications that they believe would represent the more common uses for Dune: a SandBox: where they evaluated the loads by running SPEC2000 and lighthttpd, the last being benchmarked with Apache ab over a gigabit ethernet module. They noted a significant performance advantage over the same load run in a VM running on the VMware player. The second application consisted of running benchmarks comparing forks and Dune's threads. Finally, they benchmarked their Garbage collector implementation that leverages Dune to increase performance by directly reading the dirty bits and faster fault handling. Also, it was capable of better catering for TLB invalidations.

  
# Conclusion
Since virtualization is no longer an expensive server feature, it has become increasingly prevalent. Dune is a great example of that. Creativity could leverage virtualization features to improve performance in applications that needed more direct hardware control at minimal changes to Kernel and system stability.

# Refs
1. https://www.usenix.org/system/files/conference/osdi12/osdi12-final-117.pdf