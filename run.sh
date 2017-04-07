#!/bin/sh

th eval.lua -model ~/Downloads/model_id1-501-1448236541.t7_cpu.t7 -gpuid -1 -image_folder ./images

## in docker run
## first run container:
#docker run -dit -p 8000:8000 -v /Users/xinglong/workspace/docker-neuraltalk2/images/:/images/ neuraltalk2
## then in container, run
# th eval.lua -model model_id1-501-1448236541.t7_cpu.t7 -gpuid -1 -image_folder /images 2>&1 | tee results.txt
