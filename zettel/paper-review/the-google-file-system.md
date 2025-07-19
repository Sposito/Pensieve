#incomplete
\section{Introduction}

The Google File System is an article written in 2003 by Sanjay Ghemawat, Howard Gobioff, and Shun-Tak Leung \cite{ghemawat2003google}. The three of them were Google's employees back in the time.

By the time of publication, google was a five years old company with around 800 permanent employees \cite{google_coorp_info} and annual revenue of around 1 billion dollars. 2003 was the year prior to the company's IPO\cite{katje_2020}. Therefore, it was in their best interest to promote how this company was growth capable without significant scale frictions. This article proposes a distributed file system designed to serve the company internally.

\section{Summary} 
The first couple sections of the paper are a general description of the problem and their take on tackling it, including their assumptions and proposed architecture. The third section is all about how the system's different components and stakeholders interact with each other. It presents the control/data flows and responsibilities. The following section is a more in-depth description of Master/Workers architectures, presenting the design choices for dealing with their forecast bottlenecks in scalability. Section 5 presents the reader on system reliability and mechanisms to enforce it. The following two sections are respectively objective and subjective observations and analyses of the system. The final sections are comparisons with related works conclusions and acknowledgements. 


\section{Analysis}
The GFS was designed with a few main points in mind. 1: servers were built over commodity hard drives; constant instance failures were expected. 2: They knew their file system use case: big files where writes are mostly appendages. 3: they were serving a system to themselves, so clients could be trusted and they could optimise for this.

What they had was a single master server with several chunk (worker) servers actually handling data storage and transmission. The master job was facilitating communication between clients and the data they were after, guaranteeing consistency by keeping a lock on name mutation (that were always atomic) and keeping log of its own works. Systems (both master and chunks) were designed for fast recovery by storing their state periodically. They even mention not differentiating normal from abnormal termination when restarting.

The file system kept chunk consistency by versioning those and marking inconsistent old ones as "stale", being ignored mutations and apt for garbage collection. For reliability and availability, chucks were replicated among different servers and hack, where more critical or used chunks were bumped to be more often replicated. Master periodically broadcast chunk checksums requests, being able to spot corruption and swiftly handle it. Google claims GFS fully met their need at the time and signalise that entities with similar use cases could make good use of the technology.


\section{Conclusion}

A few considerations about reading this article today; We live under the shadow of "The Cloud" in the third decade of this century \cite{kazmi2016impact}. Talking about a centralised master/workers architecture sounds like an outcry for trouble; that is why it is important to emphasise that we must read it in the early '00s timeframe, at the dawn of commercial internet future\cite{leiner2009brief}.

The year of 2003 was the worse point of the dot-com bubble-burst aftermatch\cite{delong2006short} and also the year prior its IPO. We can assume this is related to the clever way they enforce reliability over commodity and fail prone hard drives. They had to move fast, and they could not spare the work hours required for maintaining a complex system.

We see a young company trying to prove itself in this expanding new world that was the web, a company growing at a manifold speed at the brink of an IPO \cite{fleischer2006branding} proposing a solution for its own internal data store and serving. Google was not looking for scaleability or maintenance or cost optimal solutions but a balance between all of those that could fulfill their own needs.

```
@inproceedings{ghemawat2003google,
    title={The Google file system},
    author={Ghemawat, Sanjay and Gobioff, Howard and Leung, Shun-Tak},
    booktitle={Proceedings of the nineteenth ACM symposium on Operating systems principles},
    pages={29--43},
    year={2003}
}
```