# SR IOV Single Root IO Virtualization

Especificação que permite a um único dispositivo [[pci_express|PCIe]], como uma placa de rede ou [[gpu|GPU]], aparentar ser múltiplos dispositivos físicos separados. Isso é usado em cenários de [[virtualizacao|virtualização]] para permitir que máquinas virtuais tenham acesso direto e de alta performance a porções do hardware físico, sem sobrecarga do hypervisor.

## Status de Ativacao na BIOS

Define se o suporte a SR-IOV está habilitado na [[bios|BIOS]] para dispositivos PCIe compatíveis na [[huananzhi_x99_f8d_plus]].

- Status: `[Enabled]`
- Justificativa: O usuário utiliza a [[gpu|GPU]] em cenários de [[virtualizacao|virtualização]], tornando o SR-IOV potencialmente útil.
- Nota: A funcionalidade também depende de suporte no hypervisor, no sistema operacional guest e no próprio dispositivo PCIe. Habilitar na BIOS é apenas o primeiro passo.