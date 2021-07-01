# pynettest -- test network connection between two hosts

This projects contains a simple echo server and a simple echo client for testing whether two hosts can communicate at
a given port. Used together, the client and server can ne used to isolate the cause of a network communication issue.

## Get the code

    ```git clone git@github.com:fengxizhou/pynettest.git```

## Usage
Assume we plan to test if a client on host B can communicate with a server on host A (ip=192.168.10.20) listening
on port 9000. You need to change the ip address and port according to your own test.

### 1. Start a server on host A
    
   ```
   python3 server.py 192.168.10.20 9000
   ```

### 2. Test at client on host B
    
    ```
    python3 client.py 192.168.10.20 9000 is server ok?
    ```

If the communication is good, you should be able to see the following results on host B.
  
  ```
    $ python3 client.py 192.168.10.20 9000 Is the network Ok?
    Sent:     Is the network Ok?
    Received: IS THE NETWORK OK?
    Duration: 0.000533 seconds
    Network OK between 192.168.10.20 and 127.0.1.1
   ```
