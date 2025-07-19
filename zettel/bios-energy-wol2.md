# BIOS, Energia e Wake-on-LAN na HUANANZHI X99-F8D PLUS

Esta nota serve como um ponto central para as configurações da BIOS da placa-mãe [[huananzhi-x99-f8d-plus]] relacionadas a gerenciamento de energia (suspensão, hibernação) e [[Wake-on-LAN|Wake on Lan]]. O objetivo é garantir um comportamento estável e eficiente em [[nixos|nixos]].

## 🧭 Informações Básicas da Placa

Detalhes sobre o hardware e versões de firmware.
![[huananzhi-x99-f8d-plus#Specs]]

## ⚙️ Configurações de Boot e Compatibilidade

Ajustes que definem como o sistema inicializa e lida com dispositivos legados vs modernos.

### [[csm-support|CSM Support]]
Fundamental para operar em modo UEFI puro, necessário para hibernação S4 eficiente e outros recursos modernos.
![[csm-support#Configuração Recomendada para UEFI Puro]]

## ⚡ Gerenciamento de Energia da CPU

Configurações cruciais para permitir que a CPU entre em estados de baixo consumo (C-States) e ajuste sua performance dinamicamente (P-States), essenciais para suspensão (S3) e hibernação (S4) eficazes.

### [[cpu-hwpm|CPU HWPM State Control]]
Define como os estados de performance (P-States) são gerenciados. A configuração nativa permite ao hardware tomar decisões mais rápidas e eficientes.
![[cpu-hwpm#HWPM Native Mode - Configuração]]

### [[cpu-c-states|CPU C-State Control]]
Controla os níveis de "sleep" da CPU quando ociosa. Habilitar reports e limites adequados (como C6) é vital para economia de energia e funcionalidade de sleep/hibernate.
![[cpu-c-states#Package C State Limit - Configuração]]
![[cpu-c-states#CPU C3 e C6 Report - Configuração]]
![[cpu-c-states#Autonomous C-State - Configuração]]

## 🌐 [[Wake-on-LAN|Wake on Lan]] e Rede

Permite "acordar" o computador remotamente enviando um pacote mágico pela rede cabeada.

### Habilitação na BIOS (Onboard LAN)
A opção específica na BIOS que ativa o recurso para a placa de rede integrada.
![[huananzhi-x99-f8d-plus#LAN Wake Up Control]]

### [[pxe_boot|Network Stack (PXE Boot)]]
Funcionalidade para boot pela rede. Não é necessária para o funcionamento do [[Wake-on-LAN|Wake on Lan]] e foi mantida desativada.
![[pxe_boot#Status e Implicações]]

## 🧬 [[pci_express|PCI Express]]

Configurações relacionadas aos barramentos PCIe, importantes para a estabilidade de periféricos (especialmente [[gpu|GPUs]]) ao retornar de estados de suspensão/hibernação.

### [[pcie_above_4g_decoding|Above 4G Decoding]]
Necessário para sistemas com [[gpu|GPUs]] com grande quantidade de VRAM (como a RTX 3090) e para o funcionamento correto de tecnologias como Resizable BAR.
![[pcie_above_4g_decoding#Status e Necessidade]]

### [[sr-iov|SR-IOV Support]]
Relevante para cenários de [[virtualizacao|virtualização]] onde se deseja compartilhar uma única [[gpu|GPU]] física entre múltiplas máquinas virtuais.
![[sr-iov#Status de Ativação na BIOS]]

### [[pcie_restore_registers|Restore PCIe Registers on Wake]]
Pode solucionar problemas onde dispositivos PCIe não são detectados ou inicializados corretamente após o sistema retornar de S3/S4. Mantido desativado por padrão, ativar apenas se necessário.
![[pcie_restore_registers#Status e Quando Ativar]]

### Outras Configurações PCIe Relevantes
Detalhes sobre `Extended Tag`, `Latency Tolerance Reporting`, etc., que podem influenciar performance e compatibilidade.
![[pcie_configuration#Configurações Adicionais X99]]

## 🕹️ Outras Configurações Relevantes

### [[rtc-wake|RTC Wake system from S5]]
Permite ligar o computador automaticamente em um horário agendado, a partir do estado completamente desligado (S5). Não interfere com S3/S4 ou WoL.
![[rtc-wake#Status e Uso]]

## ✅ Resumo dos Objetivos Atingidos

As configurações documentadas e transcluídas aqui visam otimizar a placa [[huananzhi-x99-f8d-plus]] para:
- Suporte robusto aos estados de suspensão ([[acpi_sleep_states#S3 Suspend to RAM|S3]]) e hibernação ([[acpi_sleep_states#S4 Hibernate to Disk|S4]]).
- Funcionamento confiável do [[Wake-on-LAN|Wake on Lan]].
- Máxima compatibilidade e performance para [[gpu|GPUs]] modernas ([[pci_express|PCIe]]) no barramento X99, incluindo suporte a [[pcie_above_4g_decoding|Above 4G Decoding]].
- Suporte opcional para [[sr-iov|SR-IOV]] em cenários de [[virtualizacao|virtualização]].
- Operação estrita em modo [[uefi|UEFI]] puro, desabilitando o [[csm-support|CSM]].