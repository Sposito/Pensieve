#  Nixstation

Workstation/servidor pessoal customizado, utilizando a distribuição [[nixos|NixOS]]. O nome "Nixstation" refere-se a esta máquina específica.

## Componentes de Hardware

Lista dos principais componentes que formam esta máquina:

- Placa-mãe: [[huananzhi_x99_f8d_plus|HUANANZHI X99-F8D PLUS]]
- Processadores: 2x [[intel_xeon_e5_v3_v4|Intel Xeon E5-2650 v4 @ 2.20GHz]]
- Memória: 128GB DDR4 [[ecc_memory|REG ECC]] [[ram|RAM]] (4x 32GB @ 2400 MHz)
- Placas de Vídeo: 2x NVIDIA RTX 3090 [[gpu|GPU]]
- Armazenamento:
    - 1x WD Green SN350 2TB [[nvme|NVMe]] SSD (Sistema operacional em partição [[btrfs|Btrfs]])
    - 1x Volume [[btrfs|Btrfs]] adicional montado em `/mnt/hdd0` (Dispositivo físico a confirmar)
- Fonte de Alimentação (PSU): (Especificar modelo e potência, se conhecido)
- Gabinete e Refrigeração: (Especificar modelo do gabinete e sistema de refrigeração da CPU/GPU)

## Sistema Operacional e Configuracao

Detalhes sobre o software base e os objetivos da configuração:

- Sistema Operacional: [[nixos|NixOS]] (stateVersion `24.05`)
- Gerenciador de Boot: [[systemd|Systemd-boot]]
- Modo de Boot: [[uefi|UEFI]] (com [[csm_support|CSM]] desabilitado)
- Configuração da BIOS: Ajustada conforme documentado em [[bios-energy-wol.md]], com foco em:
    - Suporte estável a [[acpi_sleep_states|hibernação (S4)]] e [[acpi_sleep_states|suspensão (S3)]].
    - Funcionalidade de [[Wake-on-LAN|Wake on Lan]].
    - Uso das [[gpu|GPUs]] para [[virtualizacao|virtualização]] (com [[sr-iov|SR-IOV]] ativado na BIOS).
    - Garantir [[pcie_above_4g_decoding|Above 4G Decoding]] para as RTX 3090s.
- Virtualização: Suporte via [[kvm|KVM]]/[[qemu|QEMU]] e [[vmware|VMware]] habilitado.

## Status Atual ou Notas

- (Espaço para adicionar problemas encontrados, como a dificuldade inicial em fazer a máquina hibernar/suspender corretamente que motivou a revisão da BIOS).
- (Espaço para próximos passos ou otimizações planejadas).
## Docker e GPUS Nvidia
```--device nvidia.com/gpu=all```


### Config Files
[Github: Nixstation/default.nix](https://github.com/Sposito/nix-conf/blob/master/hosts/Nixstation/default.nix)
[Github: Nixstation/hardware-configuration.nix](https://github.com/Sposito/nix-conf/blob/master/hosts/Nixstation/hardware-configuration.nix)
