#paper #OS
# The Evolution of the Unix Time-sharing System Review

## Introduction

The following review from "The Evolution of the Unix Time-sharing System"\cite{ritchie1979evolution} is a posterior revisiting in the early years of the Unix system. Unlike the previously read article that presented the system formally, we have here a quick peek at the early days of the [[Unix]] system, particularly the social and material circumstances around its creation and how it impacted the system we know today.

 
## Summary

After a short introduction to the article, we are presented to Unix origins and its ill-fated predecessor, Multics. After that, we are exposed to how the file system designed for the PDP-7 machine moulded Unix's future iterations in that regard. This is followed by some explanations on the process control system IO redirection. The following section discusses the acquisition of the mini-computer PDP-11 and its impact on Unix development. Continuing, the author talks about Pipes origins just before an excellent overview on how higher-level languages changed the way they developed Unix(higher than assembly, in that case). The article now concludes and finish with some Acknowledgements.

 
## Analysis

Although simple, this was the article that most brought me joy reading. It is fascinating to have a firsthand witness description of the first steps on an operating system that impacted the computing world in the decades to come. It is pretty nice to see the small team around the project. Their previous unsuccessful incursions on operating systems almost obliterated the project and moulded it into what it became.

There was a funding situation, where due to the failure of the Multics system, it was pretty hard for the team to have access to the PDP-7 and PDP-11 machines they used during development. Also, it is interesting to see how they had to find a specific and strong motivation for the work and makes us wonder how "word processing oriented" this system really is.

Unix is very praised for the simplicity of some of its concepts, like the file system; it is mentioned on the paper how it came to be almost as we know it, with only directories paths being made what we know very early on. Another distinguishing characteristics of it were pretty crude or inexistent and changed and appeared as the system matured, the process control system, and the way piping works, namely.

Finally, it is great to see how the need to provide a Fortran compiler led to the development of the B language and culminated in the [[C]] programming language that would take a central part in the Unix development\cite{kernighan1988c}.

  
## Conclusion

This paper brings a quite historical and social perspective in some of the hidden forces behind private research; from a more technical perspective like the one presented in [[The-UNIX-Time-Sharing-System]] we usually have the impression that complex systems come to be out of thin air as imagined by their designer. Nevertheless, more importantly, it gives us a better understanding of the "how", or in other words, the chain of events that enabled the Unix system to become what it became.

---

```
@inproceedings{ritchie1979evolution,
  title={The evolution of the Unix time-sharing system},
  author={Ritchie, Dennis M},
  booktitle={Symposium on Language Design and Programming Methodology},
  pages={25--35},
  year={1979},
  organization={Springer}
}
```