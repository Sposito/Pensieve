## _
Docker is software solution that enables platform as a service (SASS) by enabling running software in a somewhat isolated environments leveraging  [[linux|linux's]] [[chroot]] by  os-level virtualization, and those are called containers. It is partially open sourced, have free and premium tiers, it is developed in [[Go]].
[[podman]] is a mostly compatible solution developed initially by Rhel.


### Dockerfile
Docker works in a layered fashion, where incremental steps configure a system image, since those changes are incremental changes only need to be rebuilt from the change point onwards

```Dockerfile
ARG CODE_VERSION=latest
FROM ubuntu:${CODE_VERSION}
COPY ./examplefile.txt /examplefile.txt
ENV MY_ENV_VARIABLE="example_value"
RUN apt-get update
# Mount a directory from the Docker volume
# Note: This is usually specified in the 'docker run' command.
VOLUME ["/myvolume"]
# Expose a port (22 for SSH)
EXPOSE 22
```

### Docker-Compose
#todo

### Docker Swarm
#todo 

### Volumes
#todo