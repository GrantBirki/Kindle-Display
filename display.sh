#!/bin/bash
hash=$(md5sum out.png)

lasthash=/var/tmp/root/lasthash.txt

if [ -f "$lasthash" ]
then 
    echo "$hash" > "$lasthash"
fi