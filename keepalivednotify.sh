#!/bin/bash

TYPE=$1
NAME=$2
STATE=$3

case $STATE in
        "MASTER") service cinder-volume start
                  rm /var/run/keepalived.state.*
                  touch /var/run/keepalived.state.master
                  exit 0
                  ;;
        "BACKUP") service cinder-volume stop
                  rm /var/run/keepalived.state.*
                  touch /var/run/keepalived.state.backup
                  exit 0
                  ;;
esac
