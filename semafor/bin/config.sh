#!/bin/sh
######################## ENVIRONMENT VARIABLES ###############################
######### change the following according to your own local setup #############


# assumes this script (config.sh) lives in "${BASE_DIR}/semafor/bin/"
export BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../.." > /dev/null && pwd )"
# path to the absolute path
# where you decompressed SEMAFOR.
export SEMAFOR_HOME="${BASE_DIR}/semafor"

export CLASSPATH=".:${SEMAFOR_HOME}/target/Semafor-3.0-alpha-04.jar"

# Change the following to the bin directory of your $JAVA_HOME
export JAVA_HOME_BIN="/Library/Java/JavaVirtualMachines/jdk1.8.0_172.jdk/Contents/Home/bin"

# Change the following to the directory where you decompressed
# the models for SEMAFOR 2.0.

export MALT_MODEL_DIR="/Users/steffenvan/Downloads/semafor_malt_model_20121129"
export FILE="${BASE_DIR}/semafor/engmalt.linear-1.7.mco"
export TURBO_MODEL_DIR="{BASE_DIR}/models/turbo_20130606"



######################## END ENVIRONMENT VARIABLES #########################

echo "Environment variables:"
echo "SEMAFOR_HOME=${SEMAFOR_HOME}"
echo "CLASSPATH=${CLASSPATH}"
echo "JAVA_HOME_BIN=${JAVA_HOME_BIN}"
echo "MALT_MODEL_DIR=${MALT_MODEL_DIR}"
