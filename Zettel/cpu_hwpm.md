# CPU HWPM State Control Hardware P States Management

Funcionalidade da [[cpu|CPU]] (principalmente Intel) que permite ao próprio processador gerenciar seus estados de performance ([[p_states|P-States]]) de forma autônoma e mais eficiente do que depender apenas do sistema operacional.

## HWPM Native Mode Configuracao

Modo de operação onde o processador tem controle total sobre os P-States, usando sua lógica interna para balancear performance e economia de energia dinamicamente.

- Status: `[Enabled]` (Selecionado sobre `OOB Mode` ou `Disabled`)
- Vantagem: Respostas mais rápidas a mudanças de carga, potencialmente melhorando a eficiência energética e a performance transiente. Recomendado para desktops e sistemas modernos. Ajuda a garantir transições suaves para e de [[cpu_c_states|C-States]] mais profundos.