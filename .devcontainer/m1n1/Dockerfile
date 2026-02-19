FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install C/Asm/Rust tools
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install build-essential cmake gdb rustc cargo \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*