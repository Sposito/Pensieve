#paper #OS
# Xen and the Art of Virtualization Review

## Introduction
Xen is a virtual machine monitor, vmm, projected to maximize the number of guest OS capable of running on commodity hardware, claiming to be able to run up to 100 virtual machine instances in the early 00s .

## Analysis
Xen is a vmm built to work on architectures that were not yet designed with virtualization in mind. So the virtualization must be carried out mainly through software. For being able to work around the performance and stability issues caused by shared hardware access, Xen goes to the stent of creating a virtual layer on top of every hardware interaction, not fully emulating it thought, by changes on the Guest OS, Xen was able to optimize the number of guest OSes highly.

The most interesting solution is the I/O ring, used for carrying data transference between host and guest OS; it is a circular queue that does not contain data itself but data buffer references. It is asynchronous and allows the hypervisor to easily relocate pointers facilitating scheduling. It also overcomes the need for copying data without compromising security.

## Conclusion
By blurring the limits between host and guest, Xen can provide low-cost transient virtual machines on commodity hardware with minimal overhead.

---


```
@article{barham2003xen,
  title={Xen and the art of virtualization},
  author={Barham, Paul and Dragovic, Boris and Fraser, Keir and Hand, Steven and Harris, Tim and Ho, Alex and Neugebauer, Rolf and Pratt, Ian and Warfield, Andrew},
  journal={ACM SIGOPS operating systems review},
  volume={37},
  number={5},
  pages={164--177},
  year={2003},
  publisher={ACM New York, NY, USA}
}
```