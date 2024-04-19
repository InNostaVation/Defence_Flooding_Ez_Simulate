#!/bin/bash
#while true;do
for i in {1..100}; do
    ab -n 1000 -c 10 http://172.18.0.3/
    sleep 1
done
