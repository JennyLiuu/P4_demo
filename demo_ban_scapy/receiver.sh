#!/bin/bash
P4C_BM_PATH=~/p4c-bmv2
BMV2_PATH=~/bmv2

[ "$#" -lt 1 ] && echo "Usage receiver.sh [host number]   Stop here." && exit 0

echo "start to receive~"

sudo python receiver.py ${1}

echo "======================================"
