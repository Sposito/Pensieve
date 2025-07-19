# ACPI Sleep States Estados Globais de Energia

Estados de baixo consumo de energia definidos pela especificação ACPI (Advanced Configuration and Power Interface) que descrevem o estado geral do sistema. São diferentes dos [[cpu-c-states|C-States]] (que descrevem o estado da CPU) mas dependem deles.

## S3 Suspend to RAM

Também conhecido como "Sleep" ou "Standby".

- Descrição: A maior parte do hardware é desligada, mas o conteúdo da [[ram|RAM]] é mantido energizado com baixo consumo.
- Vantagem: Retorno muito rápido ao estado de trabalho anterior (poucos segundos).
- Desvantagem: Consome alguma energia para manter a RAM. Se a energia for cortada, o estado é perdido (equivalente a um desligamento forçado).
- Dependência: Requer que a [[cpu|CPU]] possa entrar em [[cpu-c-states|C-States]] apropriados e que a [[ram|RAM]] seja mantida energizada.

## S4 Hibernate to Disk

Também conhecido como "Hibernação".

- Descrição: Todo o conteúdo da [[ram|RAM]] é salvo em um arquivo ou partição no disco de armazenamento (SSD/HDD). O sistema então é completamente desligado (similar ao S5).
- Vantagem: Consumo de energia quase zero (ou zero, dependendo da implementação). O estado do sistema é preservado mesmo se a energia for cortada. Permite retomar exatamente de onde parou.
- Desvantagem: O tempo para entrar e sair da hibernação é maior que S3, pois depende da velocidade de leitura/escrita do disco. Requer espaço em disco igual ou maior que a quantidade de RAM.
- Dependência: Requer suporte da [[bios|BIOS]] ([[uefi|UEFI]] é preferível), do sistema operacional (configuração de swap/arquivo de hibernação) e que dispositivos essenciais lidem bem com o ciclo completo de desligamento/inicialização. Habilitar [[pcie_above_4g_decoding|Above 4G Decoding]] e desabilitar [[csm-support|CSM]] geralmente ajuda.