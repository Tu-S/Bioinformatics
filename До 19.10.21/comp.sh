#!/usr/bin/bash
read RES
CONSTANT="0.9"
if (( $(echo "$RES > $CONSTANT" |bc -l) ));
then
   echo "OK"
else
   echo "not OK"
fi

