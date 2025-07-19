---
language: pt
tags:
  - "#docker"
  - "#nixos"
  - "#nvidia"
  - gpu
refs:
  - https://nixos.wiki/wiki/Nvidia
  - https://nixos.wiki/wiki/Nvidia
gpt: 67c0ff49-62d8-800e-8c85-c35ff705b9cd
---

## Docker no NixOS com GPU Nvidia

### Configuração básica

No NixOS, o Docker não funciona de forma "plug and play" como em outras distros. Como ele roda em um ambiente imutável, é necessário ativar algumas opções manualmente. Se quiser rodar containers com GPU Nvidia, a configuração exige mais alguns passos.

### Habilitando Docker no NixOS

Adicione ao seu `configuration.nix`:

```nix
virtualisation.docker.enable = true;
virtualisation.docker.enableOnBoot = true;
```

Após adicionar, execute:

```sh
sudo nixos-rebuild switch
```

Se quiser rodar containers sem `sudo`, adicione seu usuário ao grupo do Docker:

```sh
sudo usermod -aG docker $USER
```

### Habilitando suporte à Nvidia

O suporte oficial da Nvidia para containers usa o NVIDIA Container Toolkit. No NixOS, ative com:

```nix
hardware.nvidia-container-toolkit.enable = true;
```

E reconstrua o sistema:

```sh
sudo nixos-rebuild switch
```

Se o driver Nvidia não estiver instalado, também precisa ativar:

```nix
hardware.nvidia.modesetting.enable = true;
hardware.nvidia.package = config.boot.kernelPackages.nvidiaPackages.stable;
```

### Executando containers com GPU

Se estiver usando `docker run`, use:

```sh
docker run --rm --device=nvidia.com/gpu=all imagem
```

Se estiver usando `docker-compose`, altere sua configuração para:

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: cdi
          device_ids:
            - nvidia.com/gpu=all
          capabilities:
            - compute
            - utility
```

Isso garante que a GPU será detectada corretamente dentro do container. O flag `--gpus all` não funciona mais com o modo OCI ativado no Docker 25+, então CDI é o método recomendado.

### Testando a GPU dentro do container

Depois de subir o container, verifique se a GPU está visível:

```sh
docker exec -it nome_do_container nvidia-smi
```

Se tudo estiver certo, deve aparecer a lista de GPUs disponíveis. Se der erro, revise as configurações do `configuration.nix` e veja se a GPU está ativa no host com `nvidia-smi`.