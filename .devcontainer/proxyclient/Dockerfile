FROM mcr.microsoft.com/devcontainers/python:0-3.11

# Install useful system packages for development and device access
RUN apt-get update \
 && export DEBIAN_FRONTEND=noninteractive \
 && apt-get install -y --no-install-recommends \
    build-essential \
    libusb-1.0-0-dev \
    pkg-config \
    git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Ensure the default user can access serial devices if needed (container runtime still must pass them through)
USER vscode
