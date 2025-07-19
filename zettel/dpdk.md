# DPDK

The data plane development kit is a tool developed by intel engineer Venky Venkatesan to facilitate development of packet processors  in user space, today it is maintained by the [[linux]] Foudantion. It is one of the main tools for working with exokernels on linux.

The project be found in: https://github.com/DPDK/dpdk


### Compiling examples:


https://stackoverflow.com/questions/62513785/need-help-on-compiling-dpdk-hello-world

Based on the error logs, it looks like you have not built dpdk libraries in the desired target folder. To do it correctly

```
cd dpdk-main-folder

export RTE_SDK=$PWD &&
export RTE_TARGET=x86_64-native-linuxapp-gcc &&
make config T=$RTE_TARGET O=$RTE_TARGET &&
cd $RTE_TARGET &&
make -j 16
```

```
sudo chsh -s /bin/bash sposito
```
With these done go to your desired example and execute 'make'

```
echo 1024 | sudo tee /sys/devices/system/node/node0/hugepages/hugepages-2048kB/nr_hugepages
```
