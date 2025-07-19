# CPU C States Estados de Baixo Consumo da CPU

Estados de economia de energia nos quais a [[cpu|CPU]] pode entrar quando está ociosa. Quanto maior o número do C-State (C1, C2, C3, C6, C7...), mais componentes da CPU são desligados ou reduzidos em clock/voltagem, resultando em maior economia de energia, mas também maior latência para retornar ao estado ativo (C0). São cruciais para as funções de [[acpi_sleep_states|suspensão e hibernação]].

## Package C State Limit - Configuração

Define o estado C mais profundo que o pacote inteiro da CPU (incluindo uncore, etc.) tem permissão para entrar.

- Status: `[C6 (Retention)]`
- Justificativa: C6 oferece economia de energia significativa. O modo `Retention` significa que o estado interno (como caches) é preservado, permitindo um retorno mais rápido e estável comparado a modos C6 non-retention, sendo um bom equilíbrio para [[acpi_sleep_states#S3 Suspend to RAM|S3]] e [[acpi_sleep_states#S4 Hibernate to Disk|S4]].

## CPU C3 e C6 Report - Configuração

Permite que a [[bios|BIOS]] reporte ao sistema operacional a disponibilidade dos estados C3 e C6, respectivamente. O SO só pode usar os estados que são reportados como disponíveis.

- CPU C3 Report Status: `[Enabled]`
- CPU C6 Report Status: `[Enabled]`
- Importância: Ambos devem estar habilitados para que o sistema operacional (ex: kernel Linux em [[nixos|NixOS]]) possa efetivamente comandar a CPU a entrar nesses estados de baixo consumo durante idle ou suspensão.

## Autonomous C-State - Configuração

Permite que a CPU entre em C-States de forma autônoma, sem esperar um comando explícito do sistema operacional para cada transição. Frequentemente, converte a instrução legada `HALT` em `MWAIT`, que é mais eficiente para entrar em C-States profundos.

- Status: `[Enabled]`
- Benefício: Melhora a eficiência energética e a capacidade de resposta do sistema ao entrar e sair de estados de baixo consumo. Ajuda a garantir que a CPU aproveite os C-States configurados.