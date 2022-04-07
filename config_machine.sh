#!/bin/bash

# to list all java versions in macos

/usr/libexec/java_home -V

# to set a java version, eg:

export JAVA_HOME=`/usr/libexec/java_home -v 1.8`

# replace docker desktop with lima:
# 1. completely remove docker desktop (docker menu -> troubleshooting -> uninstall, then remove from applications)
# 2.
# > brew install lima
# 3.
# > curl -o /tmp/docker.yaml https://raw.githubusercontent.com/lima-vm/lima/master/examples/docker.yaml 
# > limactl start /tmp/docker.yaml
# 4.
# > brew install docker docker-compose
# > export DOCKER_HOST=unix:///Users/<username>/.lima/docker/sock/docker.sock
# > docker run --rm hello-world
# 5.
# > docker login registry.gitlab.com -u <gitlab-username>
# 6. possibly need to run
# > rm -rf ~/.dockercfg
# > rm ~/.docker/config.json
