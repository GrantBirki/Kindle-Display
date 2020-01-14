#!/bin/bash

lasthashfile=/var/tmp/root/lasthash.txt
lasttimefile=/var/tmp/root/lasttime.txt

hash=$(md5sum out.png)
time=$(stat out.png | grep "Change")

lasthash=$(head -n 1 $lasthashfile)
lasttime=$(head -n 1 $lasttimefile)

if [ "$hash" == "$lasthash" ] && [ "$time" == "$lasttime" ]
then
    exit 0
    echo "Quitting"
else
    if [ -f "$lasthashfile" ]
    then 
        echo "$hash" > "$lasthashfile"

    else
        touch $lasthashfile
        echo "$hash" > "$lasthashfile"
    fi

    if [ -f "$lasttimefile" ]
    then 
        echo "$time" > "$lasttimefile"

    else
        touch $lasttimefile
        echo "$time" > "$lasttimefile"
    fi
    echo "Displaying Image"
    eips -g /var/tmp/root/out.png
fi
