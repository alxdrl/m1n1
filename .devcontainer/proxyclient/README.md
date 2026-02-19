Devcontainer notes — proxyclient-focused

Quick start
- Open this repository with VS Code.
- Run the command: `Dev Containers: Rebuild and Reopen in Container`.
- The container workspace root is `/workspaces/m1n1/proxyclient`.

Post-create setup
- A virtualenv `.venv` is created automatically by the `postCreateCommand`.
- If you need to re-run dependency installation inside the container:
```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

Device / USB access
- The container image installs `libusb` system packages. To access host USB/serial devices you must enable device passthrough when starting the container (VS Code prompts to forward serial devices), or run the container with `--device` flags.

Notes
- If your workflow needs extra Python packages, add them to `proxyclient/requirements.txt`.
- The workspace opens at the `proxyclient` directory so you can work primarily with Python there.
