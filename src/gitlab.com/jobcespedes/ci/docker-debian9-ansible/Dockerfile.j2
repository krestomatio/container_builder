FROM geerlingguy/docker-debian9-ansible:latest

RUN apt-get update && apt-get install -y apt-transport-https \
    ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg \
    | sudo apt-key add - && apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] \
    https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" && apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir docker

RUN systemctl enable docker
