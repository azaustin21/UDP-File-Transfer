# UDP-File-Transfer
* Open terminal or git bash and log into the UofM cluster
* Open a second terminal or git bash
  - Change your local directory to where the project is located.
  - Copy the programs to the remote cluster using the scp commands.
    For this project the server program is server.py and the client program
    is client.py.  This mirrors how the tutorial for getting the cluster working
    so it should be easy for Dr. Wang or any of her TAs to setup.
* Go back to the original terminal or git bash, run the server.py on one
  of the cluster nodes on the remote cluster.
  - Pick any node between (n001-n008), DO NOT PICK the head node.
  - Use command "ssh n001" n001 can change depending on what node you choose.
  - Then run "python server.py" in the same terminal
* Open a third terminal login to one of the cluster nodes
* Run Client.py in a different node then what the server.py is on.
  - Use command "ssh n002" n002 can change depending on the cluster you are using if cluster 3
    is used then it would be n003
  - Then run "python client.py"" in the same terminal
  
### Input
data = ['Neo','You','Are','The','Chosen','One']

### Ouput
timeout here
0
Neo
timeout here
1
You
timeout here
0
Are
timeout here
1
The
timeout here
0
Chosen
timeout here
1
One
