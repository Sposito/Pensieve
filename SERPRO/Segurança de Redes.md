## Tipos de Ataque:
- Furto de Dados: referente a obtenção de dados por agente malicioso **através de interceptação**
- Ataque de Personificação: agente pode induzir que dispostivos atacados se conectem a um dispositivo comprometido
- Ataque de Força Bruta: uso de poder computacional intenso a fim de quebrar dados protegidos por senhas fracos ou de conhecimento comum.
- Atataque de Negação de Serviço: congestão intencional da rede através de ataque distribuído a fim de impedir que usuários legítimos se conectem ao sistema
- Exploração de Vulnerabilidade: invasão de dispositivo baseada em falhas de segurança
- Interceptação de Tráfego: interceptação de informação trafegando sem criptografia 
- Varredura: tentativa exaustiva de explorar vunerabilidade em todos elementos de uma determinada rede
- Uso indevido de Recurso: uso de dispositivo em que o atacante assume controle ilegítimo

## Segurança Física, Lógica e de Controle de Acesso
- Segurança Física:
	- UPS: sistema que usa baterias para que em eventual perda de alimentação os administradores tenha tempo de corrigir o problema
	- Gerador: Similar ao UPS porém pode ser usado por períodos muito mais longos
	- Sistema Físico Redundante: permite que me caso de falh crítica dados e infraestura possam ser restabelicidos em outro local
	- CFTV: uso de cameras pra eventual posterior análise ou aditoria
	- Traves de Equipamento: uso de travas físicas pra impedir acesso a portas e conexções de uma maquina, além de dispositivos que impeçam a movimentação física de componentes
	- Alarmes: uso de dispositivos para dectar condições ambientais adversas com água ou incêndio
	- Catracas: controle e compartimentalização de pessoal
	- Sala Cofre: ambientes com alto nível de dispositivos de controle de acesso e segurança
- Segurança Lógica: 
	- Acesso Root: a ideia é não permitir acesso direto como root, prefencialmente deve se utilizar métodos de escalação de privilégios a fim de gerar trilhas e lastros para posterior auditoria
	- Redução de Serviços: reduzir ao máximo o número de serviços em um servidor a fim de minimizar a área de exposição
	- Limitação de Acesso Remoto: uso de servoços como SSH pra proteger conexões externas bem como bloqueio de qualquer acesso remoto em partes críticas do sistema
	- Atualização do Sistema: manter os SO e as aplicações sempre atualizadas reduz o número de falhas de segurança em potencial
- Controle de Acesso
	- MAC (Mandatory Access Cojntrol): O acesso ao usuário é definido por um Label em cada objeto que indica quem pode acessalo
	- DAC (Discretionary Access Control): Sistema usado pelos pricipais SO onde cada usuário define quais outros usuários terão acesso aos seus arquivos
	- RBAC (Role-Based Access Control): nesta técnica o admin garante acesso aos recursos condicionado ao "papel" definido a cada usuário. (gerente, aluno, professor, etc)
	