#!/bin/bash
ls -alh $1
python packet_extract.py $1 |grep --binary-files=text Proxy-A > proxy_001.dat
python textscrapper.py proxy_001.dat proxy_002.dat proxy_tobetested.dat
cat proxy_002.dat |sort |uniq >> proxy_dataset.dat
cat proxy_002.dat |sort |uniq > proxy_run.dat
#cat proxy_dataset.dat |sort |uniq > proxy_dataset_unique.txt
#cat proxy_tobetested.dat |sort |uniq > proxy_tobetested_unique.txt
#python sanitize.py proxy_dataset_unique.txt proxy_sanitizedpassword.txt
#python proxy_test_multi.py proxy_tobetested_unique.txt working.txt
#cat working.txt |sort |uniq >working_unique.txt
mv proxy_run.dat proxy_8sept_run_$1.txt

rm -f proxy_tobetested.dat proxy_001.dat proxy_002.dat
echo $1":Done"
