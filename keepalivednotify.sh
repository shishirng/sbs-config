#!/bin/bash

TYPE=$1
NAME=$2
STATE=$3

case $STATE in
        "MASTER") service cinder-volume start
                  exit 0
                  ;;
        "BACKUP") service cinder-volume stop
                  exit 0
                  ;;
esac
