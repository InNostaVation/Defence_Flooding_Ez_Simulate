#!/bin/bash
#while true;do
for i in {1..1}; do
    ab -n 1000 -c 10 http://9.0.0.3/
    sleep 1
done
