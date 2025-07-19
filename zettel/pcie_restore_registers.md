# Restore PCIe Registers on Wake

Opção da [[bios|BIOS]] que instrui o sistema a salvar e restaurar certos registros de configuração de dispositivos [[pci_express|PCIe]] ao entrar e sair de estados de [[acpi_sleep_states|suspensão/hibernação]] (como S3/S4).

## Status e Quando Ativar

Estado da configuração na [[huananzhi-x99-f8d-plus]].

- Status: `[Disabled]` (Padrão)
- Função: Pode resolver problemas onde um dispositivo PCIe (placa de vídeo, rede, som, etc.) não funciona corretamente após o sistema "acordar". Isso pode acontecer se o dispositivo não gerenciar corretamente seu próprio estado durante a transição de energia.
- Recomendação: Manter desativado por padrão, pois pode causar conflitos com alguns dispositivos. Ativar apenas como tentativa de solução se ocorrerem problemas específicos com dispositivos PCIe após retornar de sleep/hibernate.