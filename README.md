# FoundIPAddr
Task: 
Find last 100 uniq ip addresses in file with a structure

01.01.2020 1.2.3.4 /index.html

12.01.2020 192.168.10.11 /debian.html

......

In general if the task was simply to output the last 100 unique IP addresses? then I would use the command

"cat {{ Name of file }} | sort -r -n -t . -k 3 -k 2 -k 1 | cut -d' ' -f2 | awk '!a[$0]++' | head -n 100"

But to complicate the task, I wrote 2 scripts, one on bash, the second on python.

1.How to use bash script:

"./foundip {{ Name of file }}"

It will create file "res.txt" with output, and it will print in output to console the same

2. How to use python script:

"python3 release.py  --f {{Name of file}} "

It will create file "final" with output (!it will create only file!)
