# CSM Support Compatibility Support Module

Módulo de compatibilidade na [[uefi|UEFI]] [[bios|BIOS]] que permite inicializar sistemas operacionais e hardware que não são totalmente compatíveis com UEFI nativo, emulando um ambiente de [[bios|BIOS]] legado.

## Configuração Recomendada para UEFI Puro

Para sistemas operacionais modernos como [[nixos|NixOS]], Windows 10/11, e para usar funcionalidades avançadas, o ideal é desabilitar o CSM.

- Status: `[Disabled]`
- Benefícios de Desabilitar:
    - Força o boot em modo [[uefi|UEFI]] nativo.
    - Requer disco em formato [[gpt_partition_table|GPT]].
    - Permite o uso de [[secure_boot|Secure Boot]].
    - Habilita funcionalidades como hibernação [[acpi_sleep_states#S4 Hibernate to Disk|S4]] mais eficiente.
    - Geralmente resulta em tempos de boot mais rápidos.
- Requisitos: Sistema operacional e todos os dispositivos de boot (especialmente a [[gpu|GPU]]) devem suportar [[uefi|UEFI]].