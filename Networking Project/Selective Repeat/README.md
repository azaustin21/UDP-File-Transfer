# SELECTIVE REPEAT PROTOCOL


## DESCRIPTION
This is an implementation of Selective Repeat Implementation for COMP-3825 Network/Info Assurance.

## Follow Clustering instructions
This is using python, so please follow previous readme file for alternating bit implementation.  As for installation the cluster guid should be enough for you to be able to follow and upload the server file and run the client file.

## RUNNING SERVER
python Server.py -a [sender_ip] -b [sender_port] -x [receiver_ip] -y [receiver_port] -m [sequence_number_bits] -w [window_size]

e.g. python Server.py -a "127.0.0.1" -b 8081 -x "127.0.0.1" -y 8080 -m 2 -w 2


## RUNNING CLIENT
python Client.py -f [filename] -a [sender_ip] -b [sender_port] -x [receiver_ip] -y [receiver_port] -m [sequence_number_bits] -w [window_size] -s [max_segment_size] -n [total_packets] -t [timeout]

e.g. python Client.py -f "index.html" -a "127.0.0.1" -b 8081 -x "127.0.0.1" -y 8080 -m 2 -w 2 -s 1500 -n "ALL" -t 10

