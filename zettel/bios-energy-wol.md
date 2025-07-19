#HUANANZHI #X99-F8D-PLUS

## ⚙️ Hibernação, suspensão, energia e Wake-on-LAN

### 🧭 Informações básicas
- **BIOS**: American Megatrends v5.11
- **UEFI**: Ativo (UEFI 2.4, PI 1.3)
- **Memória RAM**: 131072 MB 128 GB detectados) → [[RAM]]
- **Modo de boot**: UEFI
- **Acesso**: Administrator
- **Placa-mãe**: HUANANZHI X99-F8D PLUS

## ⚡ Energia & Suspensão
### [[CSM Support]]
![[Radix VM- Scalable address spaces for multithreaded applications]]
- Permite boot em modo **legado** (compatível com MBR e sistemas antigos).
- Quando **desativado**, força o uso de UEFI puro, o que:
    - Melhora segurança e boot
    - Permite usar recursos modernos como **hibernação UEFI/S4**, [[Secure Boot]] etc.
- Para sistemas como [[nixos]], desativar CSM é o ideal.

### CPU Power Management
#### **CPU HWPM State Control**
- HWPM = Hardware P-State Management (controle autônomo do processador)
- **HWPM Native Mode** foi selecionado — o ideal para sistemas modernos
- Deixa a CPU decidir sozinha como equilibrar performance x economia
#### **CPU Autonomous C-State**
- Ativado para permitir que a CPU entre sozinha em [[C-States]] profundos (idle/sleep)
- Usa instrução **MWAIT**, mais moderna e eficiente que `HLT`
- Garante melhor comportamento em hibernação/suspensão
#### CPU C-State Control
Configura quanto a CPU pode "dormir" para economizar energia:

| Configuração              | Valor Selecionado   | Observação                          |
| ------------------------- | ------------------- | ----------------------------------- |
| **C2C3TT**                | 0 (Auto)            | Timer de transição automático       |
| **Package C State Limit** | C6 (Retention)      | Profundo e estável, mantém contexto |
| **CPU C3 Report**         | Enabled             | Permite ao sistema usar C3          |
| **CPU C6 Report**         | Enabled (já estava) | C6 ativado, ideal pra hibernação    |

### Power Technology (Avançado)

- **Power Technology**: `[Custom]`
- Permaneceu assim pois as opções manuais foram otimizadas
- Recursos como `Uncore CLR`, `TDP`, `SOCKET/DRAM RAPL` permaneceram padrão (influenciam mais em overclock e limite de consumo, sem impacto direto em sleep)

## 🌐 [[Wake-on-LAN]] & Rede

### LAN Wake Up Control
- **Ativado** nas configurações da placa de rede onboard
- Permite que o computador acorde via sinal de rede (magic packet)
### Network Stack Configuration
- Stack de boot PXE pela rede foi **mantido desativado**, pois não é necessário se você não está fazendo boot por rede
- **Wake-on-LAN funciona mesmo com Network Stack desativado**, desde que `LAN Wake` esteja habilitado
    
### Driver de rede
- BIOS detecta corretamente a interface e seu MAC Address
- Nenhum ajuste adicional necessário aqui, apenas garantir que o driver no [[nixos]] também esteja configurado para WoL
    
## 🧬 PCIe e Periféricos

### [[PCI Express]] Deep States
- **Restore PCIe Registers**: mantido **desativado** (só ativar se algum dispositivo PCIe falhar ao acordar do sleep)
    - **Extended Tag** e **Latency Tolerance Reporting**: **ativados**, melhoram desempenho e controle de energia
    - **AtomicOp Request**: **desativado**, pois não é necessário e pode causar conflito
    
### PCIe Gen2/Gen3/Gen4
- Sua **RTX 3090** usa [[PCIe]] Gen4, mas é compatível com placas Gen2/Gen3 como a X99
    - As opções da BIOS específicas para Gen2 foram mantidas padrão, sem impacto direto
   
## 🌀 Ventoinhas & PWM
- Controle de ventoinha (Smart Fan/PWM Offset) não influencia diretamente sleep/hibernação
    - Ventoinhas podem continuar girando levemente em suspensão, dependendo do perfil térmico definido
    

## 🕹️ Miscellaneous (Outros)
- **RTC Wake from S5**: **desativado**
    - Permite acordar o PC em horário programado (S5 = desligado total)
    - Não interfere na hibernação normal (que é S4) ou suspensão (S3)
        
- **BIOS Guard / Anti-Flash Wearout**: desativados
    - Voltados para segurança em ambientes corporativos
- **Target VGA**: mantido como `Offboard`, pois você está usando uma [[gpu]] dedicada (RTX 3090)
   
## Notas 
Nixstation bios configurada  com foco em:
- Habilitar corretamente **hibernação e suspensão** (C-states, P-states, HWPM) 
- Preparar suporte para **Wake-on-LAN**
- Manter estabilidade e compatibilidade de [[PCIe]] e [[RAM]]
- Desativar recursos legados (CSM, PXE) para usar o sistema em UEFI puro

Essas alterações garantem um comportamento ideal para o [[nixos]], desde que o sistema operacional também esteja configurado para suportar:

- `sleep` via systemd
- hibernação (`/swap` ou swapfile configurado)
- WoL habilitado no driver da placa de rede
    
