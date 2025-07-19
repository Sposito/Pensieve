# Placa mae HUANANZHI X99 F8D PLUS

Placa-mãe de soquete duplo (dual socket) padrão E-ATX, baseada no chipset Intel C612 (frequentemente referido como X99 em placas chinesas), projetada para processadores [[intel_xeon_e5_v3_v4|Intel Xeon E5 26xx v3 e v4]] no soquete LGA2011-3. Não suporta processadores Core ou Xeon E5-16xx v3.

## Características Principais

Especificações e funcionalidades gerais da placa:

- Soquete CPU: 2x LGA2011-3
- Chipset: Intel C612
- Memória:
    - 8x slots DDR4 [[ram|RAM]]
    - Suporta [[ecc_memory|REG ECC]] e non-ECC
    - Arquitetura Quad-Channel (por CPU, se populado corretamente)
    - Frequências suportadas: 1866/2133/2400 MHz (oficialmente)
    - Capacidade Máxima: Varia conforme a fonte, com reports de até 256GB ou 512GB (8x 64GB).
- Slots de Expansão [[pci_express|PCIe]]:
    - 3x PCIe 3.0 x16
    - 3x PCIe 3.0 x8
- Armazenamento:
    - 10x portas SATA 3.0 (6Gb/s) (Algumas podem ser designadas como SSATA)
    - 2x M.2 22110 [[nvme|NVMe]] PCIe 3.0 x4
    - 1x M.2 2280 que pode operar como [[nvme|NVMe]] PCIe (possivelmente 2.0 x4) ou SATA 3.0 (NGFF). O uso deste slot em modo SATA pode desabilitar uma das portas SATA convencionais.
- Rede:
    - 1x ou 2x portas LAN Gigabit ou 2.5 Gigabit (chipset Realtek, modelo exato como RTL8125BG pode variar). Suporta [[Wake-on-LAN|Wake on Lan]].
- Áudio:
    - Codec de áudio Realtek 7.1 (ex: ALC887 ou ALC892).
- USB:
    - Portas USB 3.0 e USB 2.0 no painel traseiro e conectores internos.
- BIOS:
    - [[ami_bios|American Megatrends (AMI)]] [[uefi|UEFI]] BIOS.

## Considerações e Quirks Comuns

Pontos a observar ao usar esta placa:

- BIOS: Pode beneficiar-se de atualizações ou modificações para melhor compatibilidade, performance ou habilitar recursos como [[pcie_resizable_bar|Resizable BAR]].
- VRM e Refrigeração: Sendo uma placa dual-socket, é crucial garantir boa refrigeração nos VRMs, especialmente ao usar CPUs com TDP elevado. Um bom fluxo de ar no gabinete é recomendado.
- Tempo de Boot: Pode apresentar tempos de inicialização (POST) mais longos em comparação com placas consumer.
- Slots M.2: Verificar a especificação exata do terceiro slot M.2 (NVMe PCIe 2.0 ou SATA) e o compartilhamento de recursos com portas SATA.
- Fonte de Alimentação: Requer uma fonte robusta (PSU) com conectores de energia adequados (2x 8-pin CPU + 24-pin ATX).
- Formato E-ATX: Exige um gabinete compatível com o formato E-ATX (30.5cm x 33cm).