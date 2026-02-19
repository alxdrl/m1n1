# Dev Container for m1n1

This Dev Container configuration is designed for full development on the m1n1 project, including C, Assembly, Rust, and Python components.

## Features

- **Base Image**: Ubuntu with essential build tools
- **Languages Supported**:
  - C/C++ (GCC, CMake, GDB)
  - Assembly
  - Rust (rustc, cargo)
  - Python (for proxyclient scripts)
- **VS Code Extensions**:
  - C/C++ Tools
  - Rust Analyzer
  - CMake Tools
  - Python support (for proxyclient)
- **Workspace**: Opens at `/workspaces/m1n1` (full repository access)

## Setup

1. Open the repository in VS Code.
2. Run `Dev Containers: Reopen in Container`.
3. Select "m1n1 - Full Repo" when prompted.
4. The container will build and install necessary tools.

## Post-Create Commands

The container runs:
```bash
apt-get update && apt-get install -y build-essential cmake gdb rustc cargo
```

## Usage

- Build the project using the provided Makefile or CMake.
- For Python work in `proxyclient/`, you may need to set up a virtual environment manually.
- Access serial/USB devices by configuring Docker device passthrough.

## Notes

- If you need Python-focused development, consider using the `.devcontainer/python/` configuration instead.
- For device access, ensure Docker is configured to pass through USB/serial ports.

## Troubleshooting

- Rebuild the container if tools are missing: `Dev Containers: Rebuild and Reopen in Container`
- Check Docker logs for build errors.