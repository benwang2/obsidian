---
title: Lecture Notes 2
course: CS_352
date: 2022/09/09
tags: 
- lectureNotes
- CS_352
---

# Lecture 2
## Transmitting data
Machines communicate exclusively in binary, however the data that needs to be transmitted is often a much more complex data type than binary.

This is the **encoding and decoding problem**. The complex data types can be encoded and decoded on different entities in the network.

### Physical transmission on a single link
Physical signaling (light, AC, voltages) are often analog forms of transmission.

BIts are converted to signals through **modulation** of physical characteristics of signals. This is called **encoding**.

For example, one might modulate the voltage to achieve a certain pattern in the signals sent.

The receiving endpoint converts the signals back to digital by **decoding** physical signals.

There are three different types of modulation
- amplitude modulation
![[Pasted image 20221003163942.png]]
- frequency modulation
![[Pasted image 20221003164011.png]]
- phase modulation
![[Pasted image 20221003164128.png]]

## Switching
The term **switching** is used to denote physically moving data from one linke to another.

There are several different **switching schemes**.
- Circuit switching
- Message switching
- Packet switching

### Circuit Switching
With circuit switching, the full path of connected links are allocated to the connection.

An example of this is a telephone network.

This method of switching follows the certain steps.
1. **Setup:** Control message sets up path from origin to destination
2. Accept signal informs source that data transmission may proceed
3. **Data transmission** begins
4. Entire path remains allocated to the transmission (whether used or not)
5. Whether transmission is complete, source releases the circuit

![[Pasted image 20221003172520.png|300|center]]



### Message Switching
With message switching, each message is addressed to a destination. The message is addressed using the **header**.

The **header** includes metadata that denotes how to process a message, like a *destination address*

The message "hops" from node to node through a network, **while allocating only one link at a time**, as opposed to circuit switching where all links are reserved at the same time (regardless of use).

When the entire message is received at a router, the next step and link in its journey are selected (**routing**). If the selected link is busy, the message waits in a **queue** until the link is free.

An analogy for this is a postal service.

![[Pasted image 20221003172506.png]]