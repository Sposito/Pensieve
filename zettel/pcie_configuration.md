# Configuracoes Gerais PCIe na X99

A plataforma X99 (e a [[bios|BIOS]] da [[huananzhi-x99-f8d-plus]]) oferece diversas opções para ajustar o comportamento do barramento [[pci_express|PCIe]].

## Configuracoes Adicionais X99

Ajustes finos que podem impactar performance, compatibilidade e eficiência energética.

- PCIe Extended Tag Enable: `[Enabled]`
    - Permite o uso de tags maiores nos pacotes PCIe, potencialmente melhorando a performance em algumas cargas de trabalho. Geralmente seguro habilitar.
- PCIe Latency Tolerance Reporting (LTR): `[Enabled]`
    - Permite que dispositivos reportem suas tolerâncias de latência, ajudando o sistema a tomar decisões mais inteligentes sobre gerenciamento de energia (como entrar em estados de link PCIe de baixo consumo, ASPM).
- Relaxed Ordering: `[Enabled]`
    - Permite que transações PCIe sejam reordenadas para otimizar o fluxo de dados. Geralmente benéfico para performance.
- No Snoop: `[Enabled]` (Geralmente padrão)
    - Otimização onde transações que não precisam checar a coerência de cache podem evitar esse passo.
- AtomicOp Request Support: `[Disabled]`
    - Suporte para operações atômicas específicas via PCIe, mais relevante em ambientes de computação de alta performance ou servidores. Desabilitado para evitar possíveis instabilidades em uso desktop.

Nota: As configurações específicas de `Gen2 Settings` (como `Clock Power Management`, `Autonomous Width`) foram mantidas nos padrões (`Disabled`), pois a [[gpu|GPU]] principal (RTX 3090) opera em Gen3/Gen4, embora o slot na X99 seja Gen3.