---
title: Lecture Notes 19
course: CS_352
date: 2022-11-18
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 19</h1></center>

## Network Layer
The network layer's main function is to move data from the sending endpoint to the receiving endpoint.

On the sending endpoint, data is encapsulated into **datagrams**, which the receiving endpoint delivers to the transport layer.

The network layer is difficult to evolve because it **runs in every router**. The iteration of the network layer is deeply ingrained in our ecosystem.

### Key functions
**Forwarding** - move packets from router's input to appropriate router output.

An analogy for **forwarding** is taking a road trip, specifically getting through a single interchange.

**Routing** - determine route taken by packets from source to destination. Utilizes routing algorithms.

The process of planning a trip from source to destination is called **routing.**

### Planes
There are two planes:
- data plane
- control plane

#### Data plane
The data plane performs **forwarding**. Its' function is locally implemented. It determines how datagrams arriving on the router input port is forwarded to the router output port.

#### Control plane
The control plane performs **routing** and follows network-wide logic. It determines how datagrams are routed along end-to-end path from source to destination endpoint.

There are two common control-plane approaches:
- **distributed routing** - algorithms running on each router
- **centralized routing** - algorithm running on a logically centralized server

## Addressing
Internet addresses allow endpoints to *locate each other* but they do not identify endpoints.

The internet addresses only determine how to move a packet.

Network layer addresses are **designed** to help routers perform the forwarding and routing functions **efficiently**.

### IPv4
An IPv4 address is 32 bits long and it identifies a network interface. 

The IPv4 address corresponds to a point of attachment of an endpoint to a network, but it is NOT an identifier for the endpoint. If the endpoint relocates, the IP changes.

IPv4 addresses are written in **dotted quad notation**, where each byte is written in decimal in order, seperated by dots.

Example:
| 10000000 | 11000011 | 00000001 | 01010000 |
| -------- | -------- | -------- | -------- |
| 128      | 195      | 1        | 80         |

IP addresses can be grouped based on a **shared prefix on a specified length**.

So the two addresses below:
- 128.95.1.80
- 128.95.1.4
Share the prefix of length 24: $128.95.1$ but have different suffixes of bit length.

For each address, the prefix corresponds to the network component and the suffix to an **endpoint (host) component** of the address.

### Scaling
IP addresses use hierarchy to scale routing. For example, endpoints within Busch campus share a prefix of some length, but each endpoint has a different suffix.

Prefixes reduce the amount of information needed to forward packets over the internet.

IP prefixes are like **zip codes** and they allow for IP addresses to be delegated from one network to another.

In the past, the IP address itself is formatted to denote the IP prefix.

However, now we use classless addressing (known as classless inter-domain routing, or **CIDR**).

## Classless IPv4 addressing
Using CIDR, an ISP can obtain a block of addresses and partition it further to its customers.

If an ISP has 65,000 addresses, and a customer only needs 64 addresses starting from $200.8.4.128$, that block is specified as $200.8.4.128/26$.

This IP $200.8.4.128/26$ is contained within the block $200.8.0.0/16$.

### Netmask (Subnet mask)
A netmask is an alternative to denote the IP prefix length of an organization.

The subnet mask is 32 bits long, and a 1-bit denotes a prefix bit position. a 0 denotes host bit.

### Detecting addresses from same network
Two addresses $A$ and $B$ are on the same network if $A \& M == B \& M$, where $M$ is the netmask.

```python
IPs = ["192.168.127.0", "192.168.64.1"]
subnet = "255.255.192.0"
def IPsOnNetwork(ip1, ip2, sn):
	octets1 = [int(digit)
	for digit in ip1.split(".")]
		octets2 = [int(digit) for digit in ip2.split(".")]
		subnet_octets = [int(digit) for digit in sn.split(".")]
		for i in range(len(octets1)):
			if octets1[i] & subnet_octets[i] != octets2[i] & subnet_octets[i]:
				return False 

	return True
	
print(IPsOnNetwork(*IPs,subnet))
```

## Router Architecture
A router contains a 
- router processor
- switching fabric
- input ports
- output ports

On the control plane, we have the:
- route processor

and on the data plane, we have the:
- router input ports
- router output ports
- high-speed switching fabric

There are many different designs (access routers, chassis/core routers, top-of-rack switches) and these designs have evolved over time.

The router we will study is called the **MGR (multi-gigabit router)**

### Input port functions
The input port receives physical signals and turns them into digital signals, called **line termination**.

The rate of link connecting to a single port termed **line speed** or **line rate**. Modern routers can handle over 100+ Gbit/s.

The **link layer** performs medium access controls functions, like **ethernet**.

