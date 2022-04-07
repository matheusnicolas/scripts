#!/bin/bash

# to list all java versions in macos

/usr/libexec/java_home -V

# to set a java version, eg:

export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
