FROM geerlingguy/docker-ubuntu1604-ansible:latest

RUN apt-get update && apt-get install --no-install-recommends -y \
    apt-transport-https ca-certificates curl gnupg-agent \
    software-properties-common && curl -fsSL \
    https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
    && apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] \
    https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" && apt-get update && \
    apt-get install --no-install-recommends  -y docker-ce docker-ce-cli \
    containerd.io && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir docker

RUN systemctl enable docker
