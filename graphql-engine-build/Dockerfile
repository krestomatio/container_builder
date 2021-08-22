# Ansible managed
FROM quay.io/krestomatio/graphql-engine-base AS graphql-engine-builder

ENV GHC_VERSION="8.10.2" \
    OS_INSTALL_PKGS="make curl git tar xz postgresql gcc gcc-c++ gmp gmp-devel ncurses ncurses-devel ncurses-compat-libs perl mysql-devel pcre pcre-devel ca-certificates krb5-libs numactl-libs libpq libpq-devel unixODBC-devel"

RUN install-pkgs ${OS_INSTALL_PKGS}

RUN curl https://downloads.haskell.org/~ghc/${GHC_VERSION}/ghc-${GHC_VERSION}-x86_64-centos7-linux.tar.xz | tar xJ  && \
    pushd ghc-${GHC_VERSION} && ./configure && make install && \
    popd && rm -rf ghc-${GHC_VERSION}

RUN curl https://gitlab.haskell.org/haskell/ghcup/raw/master/ghcup > /usr/local/bin/ghcup && \
    chmod +x /usr/local/bin/ghcup && \
    ghcup install-cabal && \
    cp -rp ~/.ghcup/bin/cabal /usr/local/bin/cabal

RUN git clone -b v${GRAPHQL_ENGINE_VERSION} https://github.com/hasura/graphql-engine /repo/graphql-engine

WORKDIR /repo/graphql-engine

ARG GHC_OPTION_MEMORY \
    GHC_OPTION_OPTIMIZATION \
    GHC_OPTION_NUM_JOBS

ENV GHC_OPTION_MEMORY=${GHC_OPTION_MEMORY:-15000m} \
    GHC_OPTION_OPTIMIZATION=${GHC_OPTION_OPTIMIZATION:-1} \
    GHC_OPTION_NUM_JOBS=${GHC_OPTION_NUM_JOBS:-}

RUN cabal update  && \
    echo "GHC_OPTION_MEMORY: ${GHC_OPTION_MEMORY}, GHC_OPTION_OPTIMIZATION: ${GHC_OPTION_OPTIMIZATION}, GHC_OPTION_NUM_JOBS: ${GHC_OPTION_NUM_JOBS}" && \
    cabal build exe:graphql-engine --ghc-options="+RTS -M${GHC_OPTION_MEMORY} -A128m -n2m -N -RTS -O${GHC_OPTION_OPTIMIZATION} -j${GHC_OPTION_NUM_JOBS}" -j${GHC_OPTION_NUM_JOBS} && \
    mv `find dist-newstyle/ -type f -name graphql-engine` /bin/ && \
    rm -rf dist-newstyle/


FROM quay.io/krestomatio/graphql-engine-base

# General variables
ENV IMAGE_NAME=graphql-engine-build \
    IMAGE_SUMMARY="Graphql-engine build image based on CentOS 8 Stream minimal" \
    IMAGE_DESCRIPTION="CentOS 8 Stream minimal based image" \
    IMAGE_TITLE="Graphql-engine build image based on CentOS 8 Stream minimal"

COPY --from=graphql-engine-builder /bin/graphql-engine /bin/graphql-engine
