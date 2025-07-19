# Verificar Aviso de Configuração Regional

## Problema
O aviso sobre as configurações regionais no [[linux]] pode aparecer em diversos contextos e não necessariamente está ligado a um problema específico. No entanto, resolver esse aviso pode evitar complicações futuras e assegurar que a configuração regional esteja corretamente definida no sistema.

## Solução
Você pode tentar exportar as configurações regionais para garantir que elas estejam disponíveis para o script Perl. Para fazer isso, siga os passos abaixo:

### Editar Configuração do Shell
Edite o arquivo de configuração do shell apropriado (por exemplo, `~/.bashrc` ou `~/.profile`) e adicione:
```bash
export LC_ALL=pt_US.UTF-8
export LANG=pt_US.UTF-8
```

### Aplicar Mudanças
Depois, aplique as mudanças com:
```bash
source ~/.bashrc
```
