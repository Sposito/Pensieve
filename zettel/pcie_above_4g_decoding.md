# PCIe Above 4G Decoding

Configuração da [[bios|BIOS]] que permite ao sistema mapear espaços de endereços de [[pci_express|PCIe]] acima do limite de 4 Gigabytes. Essencial para dispositivos que requerem grandes Base Address Registers (BARs), como [[gpu|GPUs]] modernas com muita VRAM.

## Status e Necessidade

Estado da configuração `Above 4G Decoding` na [[huananzhi-x99-f8d-plus]].

- Status: `[Enabled]`
- Justificativa: Necessário para o correto funcionamento de [[gpu|GPUs]] como a NVIDIA RTX 3090 (com 24GB de VRAM). Sem isso, o sistema pode não conseguir alocar todo o espaço de memória da GPU, levando a problemas de performance ou instabilidade. É também um pré-requisito para habilitar [[pcie_resizable_bar|Resizable BAR]].