[[Linux]] is a modular system and certain parts of its kernel (aka drivers) can be blocked at start up for doing do we edit the `/etc/modprobe.d/pve-blacklist.conf` 

```pve-blacklist.conf

blacklist amdgpu

```


