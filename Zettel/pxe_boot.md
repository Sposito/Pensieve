# PXE Boot Preboot Execution Environment

Protocolo que permite a um computador inicializar (boot) diretamente a partir de um servidor na rede, sem depender de um disco local. A funcionalidade "Network Stack" na [[bios|BIOS]] geralmente se refere à habilitação da pilha de rede necessária para o PXE Boot.

## Status e Implicacoes

Configuração que habilita ou desabilita a pilha de rede para boot via PXE na [[huananzhi_x99_f8d_plus]].

- Status: `[Disabled]`
- Justificativa: O boot pela rede não era um requisito para o sistema [[nixos|NixOS]] em questão.
- Impacto no [[Wake-on-LAN|Wake on Lan]]: Nenhum. O WoL depende da opção `LAN Wake Up Control` estar ativa e da placa de rede receber energia em estados de baixo consumo, não da habilitação da pilha de boot PXE. É possível ter WoL funcionando com o Network Stack/PXE desabilitado.