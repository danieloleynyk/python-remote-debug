# Use your desired python base image
FROM python:3.8.8

ENV PYTHONUNBUFFERED 1
ENV WORKON_HOME=~/.venvs

# Please Don't change it
WORKDIR /workspace

# Setup SSH with secure root login
# Please don't change it
RUN apt-get update \
 && apt-get install -y sudo openssh-server netcat \
 && mkdir /var/run/sshd \
 && echo 'root:password' | chpasswd \
 && sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Installs pipenv and initializes the venv
# if you do not wish using pipenv just remove it
RUN apt-get install -y pipenv vim && \
    python -m venv /.venvs/venv

# Configures zsh
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)" -- \
    -t miloshadzic \
    -p git \
    -p safe-paste \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -a "bindkey '^ ' autosuggest-accept" \
    -a "cd /workspace" && \
    echo "source /.venvs/venv/bin/activate" >> ~/.zshrc

# Copies your code for the first time
COPY . .

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
