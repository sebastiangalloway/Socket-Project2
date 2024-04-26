# CNT-4731 Project 2 (Confundo)

Template for for FIU CNT-4731 Fall 2023 Project 2

## Provided Files

`server.py` and `client.py` are the entry points for the server and client part of the project.

## Academic Integrity Note

You are encouraged to host your code in private repositories on [GitHub](https://github.com/), [GitLab](https://gitlab.com), or other places.  At the same time, you are PROHIBITED to make your code for the class project public during the class or any time after the class.  If you do so, you will be violating academic honestly policy that you have signed, as well as the student code of conduct and be subject to serious sanctions.

## Wireshark dissector

For debugging purposes, you can use the wireshark dissector from `confundo.lua`. The dissector requires
at least version 1.12.6 of Wireshark with LUA support enabled.

To enable the dissector for Wireshark session, use `-X` command line option, specifying the full
path to the `confundo.lua` script:

    wireshark -X lua_script:./confundo.lua

To dissect tcpdump-recorded file, you can use `-r <pcapfile>` option. For example:

    wireshark -X lua_script:./confundo.lua -r confundo.pcap

## Project Report 
- Lauren Alonso, PID: 6226989
- Sebastian Galloway, PID: 6182888
- High-Level Design: High-level design can be seen through the expectSynAck method. Within the while/if refers to various 
  parts of the prok=ject such as the GLOBAL_TIMEOUT, seqNum and ackNum.    
- The major issue we had was getting the client and server to work together correctly. Since we both worked on the server and 
  client separately we went over the code together over a zoom call. Reviewing our thoughts and ideas this way helped us 
  solve the issue.
- Acknowledgements:
  * Socket Programming in Python guide we referred to: https://realpython.com/python-sockets/
  * Code reference used for the socket and overall: https://www.geeksforgeeks.org/socket-programming-python/
  * Example for a client server: https://stackoverflow.com/questions/7749341/basic-python-client-socket-example
