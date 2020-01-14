#!/bin/bash
hash=$(md5sum out.png)
time=$(stat out.png | grep "Change")

lasthash=/var/tmp/root/lasthash.txt
lasttime=/var/tmp/root/lasttime.txt

if [ -f "$lasthash" ]
then 
    echo "$hash" > "$lasthash"

else
    touch $lasthash
    echo "$hash" > "$lasthash"
fi

if [ -f "$lasttime" ]
then 
    echo "$time" > "$lasthash"

else
    touch lasttime
    echo "$time" > "$lasthash"
fi