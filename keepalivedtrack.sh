#!/bin/bash

if [ -e "/var/run/keepalived.state.backup" ]
then
    exit 0
fi
/usr/bin/killall -0 cinder-volume
