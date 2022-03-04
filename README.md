# FoundIPAddr
In general if the task was simply to output the last 100 unique IP addresses? then I would use the command

"cat {{ Name of file }} | sort -r -n -t . -k 3 -k 2 -k 1 | cut -d' ' -f2 | awk '!a[$0]++' | head -n 100"

But to complicate the task, I wrote 2 scripts, one on bash, the second on python.

1.How to use bash script:

"./test {{ Name of file }}"

It will create file res.txt with output, and it will print in output to console the same

2. How to use python script:

"python3 release.py  --f {{Name of file}} "
