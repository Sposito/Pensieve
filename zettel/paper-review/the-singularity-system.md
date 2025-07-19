#paper #OS
# The Singularity System

## Introduction
In The Singularity System Review \cite{larus2010singularity}, published in Communications of the ACM, a magazine directed for broader a public, we have a nice overview of an Operating System born to debunk C's dominance in the field.

  
## Summary
Because of the format, this was the less structured paper of all. The article begins with a description o key points and goals description. It further makes a case for using higher-level languages as it presents us their tailored solution addressing it. It then exposes the case about performance, advocating that higher-level languages are capable, in some specific cases, of having comparable or even superior performance. It continues on some discussion about safety before finally wrapping it all out with their conclusions and achievements with this project.


## Analysis
Not happy about cursing the world once with one operating system, Microsoft back in the late 00s was working in another, that time luckily with research purposes in mind. All jokes aside, Singularity seems to be an odd idea that worked quite well for what it was worth. The key idea was to investigate if using a safer language for systems programming was viable. It does follow the concept of a micro-kernel with any and everything responsibility in the system being very modular. The whole system was supposed to run on a lightweight version of Microsoft's runtime. More critical pieces would be written in Sing#, a dialect of C# tailored for fast execution, not compromising in type and memory safety. It manages its process differently, relying less on hardware enforce safety towards software managed isolation, what they call "SIPs" for the software-isolated processes. That said system is capable of using hardware security to give an extra layer of protection and isolation. Although Sing# for critical parts of the system can be compiled to native machine code, most of its applications run on top of given runtime, requiring it to be written with that target in mind using languages from "DotNet" family-like C# or Visual Basic. They seem to be very confident in their benchmarks and praise the system a lot at the paper's conclusion.
 

## Conclusion
Despite their claims of performance and safety, we so far have not heard of any commercial product that follows Singularioty's path. Microsoft is well-known for killing projects, and it might not be in their best interest to have any doubt cast upon Windows dominance. Also worth mentioning that around the time of publishing the said article, new systems capable languages like Rust\cite{matsakis2014rust} and later Swift\cite{goodwill2015swift} got much traction showing that it was possible to have zero cost safe abstractions, which might have impacted the impact any Sing# future. Either way, it is not everyday Microsoft gives me a good impression, and Singularity was one of those few moments. I do no doubt that even it never seeing the light of day as a fully matured OS, it did help improve the company's overall ecosystem.

---


```
@article{larus2010singularity,
  title={The singularity system},
  author={Larus, James and Hunt, Galen},
  journal={Communications of the ACM},
  volume={53},
  number={8},
  pages={72--79},
  year={2010},
  publisher={ACM New York, NY, USA}
}
```