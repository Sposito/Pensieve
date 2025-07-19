O kernel [[linux]], criado por [[linus-torvalds]] é a parte mais básica do sistema que conhecemos com Linux (GNU/Linux) e é responsável for gerenciar e orquestrar os diferentes componente de hardware que compõe um computador moderno.
## Módulos
[[linux]] is a modular system and certain parts of its kernel (aka drivers) can be blocked at start up for doing do we edit the `/etc/modprobe.d/pve-blacklist.conf` 

```pve-blacklist.conf

blacklist amdgpu

```
