#!/bin/bash
source env.sh
json_file="demo.json"

if [ -f "$json_file" ]
then
    # $BMV2_PATH/tools/runtime_CLI.py --json $json_file --thrift-port 9091 < test1_cmd.txt
    # $BMV2_PATH/tools/runtime_CLI.py --json $json_file --thrift-port 9092 < test1_cmd.txt
    # $BMV2_PATH/tools/runtime_CLI.py --json $json_file --thrift-port 9093 < test1_cmd.txt
    # $BMV2_PATH/tools/runtime_CLI.py --json $json_file --thrift-port 9094 < test1_cmd.txt

    while [ 1 ]     # 判斷式[] 裡面前後都要加空格
    do
        $BMV2_PATH/tools/runtime_CLI.py --json $json_file --thrift-port 9091 < test1_cmd.txt
        sleep 1
    done 
else
    echo "$json_file not found."
fi



