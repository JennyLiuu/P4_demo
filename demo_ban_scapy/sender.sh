#!/bin/bash

P4C_BM_PATH=~/p4c-bmv2
BMV2_PATH=~/bmv2
json_file="demo.json"

[ "$#" -lt 1 ] && echo "Usage sender.sh [host number]   Stop here." && exit 0

echo "start to send~"

while [ 1 ]     # 判斷式[] 裡面前後都要加空格
do
    sudo python sender.py ${1}
done

echo "========================================="
