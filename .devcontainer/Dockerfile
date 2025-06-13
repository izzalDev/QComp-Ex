FROM mcr.microsoft.com/devcontainers/base:bookworm

# Install dependencies as root
RUN apt-get update && apt-get install -y \
  curl git \
  build-essential \
  libssl-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  libncursesw5-dev \
  xz-utils \
  tk-dev \
  libxml2-dev \
  libxmlsec1-dev \
  libffi-dev \
  liblzma-dev \
  uuid-dev \
  socat

# Ganti ke user vscode (UID 1000)
USER 1000

# Jalankan semua install script sebagai user vscode
RUN curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh -s -- --yes && \
    curl -fsSL https://pyenv.run | bash && \
    curl -sS https://starship.rs/install.sh | sh -s -- --yes

# Kembali ke root untuk copy file ke home vscode
USER root
COPY bashrc /home/vscode/.bashrc
COPY jupyter_lab_config.py /home/vscode/.jupyter/jupyter_lab_config.py
# RUN chown vscode:vscode /home/vscode/.bashrc

# Balik lagi ke user vscode untuk container runtime
USER 1000

