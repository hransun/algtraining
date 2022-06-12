#!/bin/sh
# limit,target,count
vmstat -n 1 | awk -W interactive -v limit = " $1 " -v target= " $2 " -v count= " $3 "
'
{
if($1 == "procs") next;
if($1 == "r") {
print "header found" > "/dev/stderr";
for(i=1; i<NF; i++) {
header[$i] = i
}
if(header[target] == ""){
print "target not found" > "/dev/stderr";
exit 1;
}
next;
}
if($header[target] > limit) {
violation ++;
if(violation > count) print $0;
}else violation = 0;
}
' | ts "%H:%M:%S"
