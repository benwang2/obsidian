---
title: Lecture Notes 11
course: CS_352
date: 2022-10-14
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 11</h1></center>

## Error Detection
We implement error detection because the network provides no guarantees for correctness.

We can use a computing function to verify that the packet has be transmitted correctly. This function is called the **checksum** and it must:
- be easy to compute
- change if the packet changes
- be easy to verify

#checksum

### Checksum
A checksum is the 16-bit one's complement of the one's complement sum of a pseudo header of information from the IP header, the UDP header, and the data, padded with zero octets at the end to make a multiple of two octets.

The pseudo header conceptually prefixed to the UDP header contains the source address, the destination address, the protocol, and the UDP length.


| sender                                                   | receiver                                                                  |
| -------------------------------------------------------- | ------------------------------------------------------------------------- |
| treat segment contents as sequences of 16-bit integers   | compute checksum of received segment, inclduing checksum in packet itself |
| check: addition (1's complement sum) of segment contents | check if resulting checksum is 0                                          |
| sender puts checksum value into UDP/TCP checksum field   | NO - an error is detected                                                 |
|                                                          | YES - assume no error                                                     |

Checksums are not the end-all-be-all; they don't detect all bit errors.
*analogy*: "you can't assume the package hasn't been meddled with if it's weight matches the one on the stamp"
The checksum is an **effective and lightweight method** that works in most cases. However, if it **insufficient for checking reliable data delivery**.

UDP and TCP share the same checksum function, but TCP also uses the lightweight error detection capability.

#### Checksum shortcomings
Checksums are not able to detect all bit errors, consider (x,y) vs. (x-1, y+1) as adjacent 16-bit values in packet. In this case, notice that we would have the same checksum.

The content of a message can be rearranged in such a way that the checksum would not change.

[RFC 768](https://www.rfc-editor.org/rfc/rfc768)

## UDP
UDP is a **simple transport protocol**, it simply sends or receives a single packet from/to the correct application process.

It's a thin shim around network layer's best-effort delivery. There's no connection building and as a result, there's also no latency.

UDP works best with:
- one-off request/response messages
	- loss-tolerant but delay-sensitive applications

## Reliable Data Delivery

To cope with packet loss, the receiver will return an **ACK** (acknowledgement) per packet, which indicates that the receiver has received the packet correctly. When the sender receives the ACK, the sender knows the receiver has received it.

On the flip side, the receiver could send a **NAK**, indicating that it has received a corrupted packet.

If a packet is dropped, wait for a duration of time (**retransmisssion timeout**) before re-sending the packet.

In TCP, the **onus** is on the sender to retransmit lost data when ACKS are not received.

#ack