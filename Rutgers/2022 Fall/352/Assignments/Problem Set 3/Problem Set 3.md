---
title: Problem Set 3
course: CS_352
released: YYYY-MM-DD
due: 2022-12-13
tags:
- Assignments
- CS_352
---
<center><h1>Problem Set 3</h1></center>
<center><h3>CS352</h3></center>

## Instructions

Please read and follow these instructions carefully.  
1. You must work on this problem set individually.  
2. Please complete your answers to the questions below and upload your responses to Canvas as a single PDF file.  
3. Your answers (preferably typed up rather than handwritten) must be clear, legible, and concise. If we cannot understand your answer with reasonable effort, you will get zero credit. 
4. If you leave a question out or clearly state “I don’t know”, you will receive 25% of the points for that question.  
5. We care not just about your final answer, but also how you approach the questions. In  general, if you show us your reasoning for your answers, we will do our best to provide partial credit even if your final answer is incorrect. However, if you provide no reasoning, and your answer turns out to be incorrect, you will typically receive zero points. So, please explain yourself.  
6. You are free to discuss the problem set on Piazza or through other means with your peers and the instructors. You may refer to the course materials, textbook, and resources on the Internet for a deeper understanding of topics. However, you cannot lift solutions from other students or from the web. Do not post these problems to question-answering services like Chegg. All written solutions must be your own. We run sophisticated software to detect plagiarism and carefully monitor student answers.  
7. There is a due date/time but no “time limit” on problem sets. That is, you may take as long as you need to work on problem sets, as long as you submit them on time. Further, you may make an unlimited number of submissions on Canvas. 
8. As a response to the last question of this problem set, please specify who you collaborated with, and also include all the resources you consulted to answer questions in this problem set, including URLs of pages you visited on the Internet. Also specify which question and aspect you got help with. Please be as thorough and complete as possible here. It is mandatory to answer this question.  
9. If you have any questions or clarifications on the problem set, please post them on Piazza or contact the course staff. We are here to help.
<div style="page-break-after: always;"></div>
<div style="page-break-after: always;"></div>


# Questions
There are 8 questions in this problem set totalling to 50 points.

### (1) Functional differences. (4 points)
(a) What is the key difference between the functions of the transport and network layer?
```
The transport layer is a communication abstraction between processes and delivers packets to the process. However, the network layer is an abstraction to communicate between endpoints. The key difference is that the network layer moves data between endpoints, while the transport layer receives from the network layer and then moves data from to processes.
```

(b) What is the key difference between the control and data planes of a router?
```
The data plane performs forwarding and is locally implemented, while the control plane performs  performs **routing** and follows network-wide logic.
```

### (2) Netmask (2 points).
Suppose hosts A and B have the same netmask M. Host A has IP address 102.45.56.7. Host B has IP address 102.46.47.8. The netmask   is 255.252.0.0. Are A and B in the same IP network? Why or why not?

```
No, they are not. 

102 & 255 = 102
45 & 252 = 45
46 & 252 = 46

Therefore, after checking the second octet of both IPs, we can conclude that they are not on the same network, because A & N != B & N, where N is the subnet mask.
```

### (3) Forwarding lookup (2 points).
Which field on the packet is used to lookup the router’s forwarding table? What are the consequences of using this packet field (and ignoring others)?

```
The destination IP address is used to lookup the router's forwarding table. The consequences of using this packet field are that the forwarding behavior independent of source and application, meaning that forwarding is vulnerable to bad actors and traffic is not optimized for type of traffic.
```

### (4) Benefits of IP aggregation (2 points). 
Describe any one benefit for aggregating IP addresses into IP prefixes, or aggregating smaller IP prefixes into larger ones.
```
Route aggregation helps save forwarding table memory  by reducing number of routing protocol messages.
```

### (5) Fabrics (3 points)
(a) What is the benefit of using nonblocking fabrics in routers? (1.5 points)
```
Nonblocking fabric prevent queues from forming and as a result. If there is data to be transmitted, it will always be transmitted, as long as there is an available output port.
```

(b) Is a crossbar fabric nonblocking? Say YES or NO. (0.5 points)
```
YES
```

(c) Is a shared memory fabric nonblocking? Justify. (1 point)
```
Shared memory fabric can be nonblocking if the software and hardware are capable of accessing the memory quickly enough.
```

### (6) Forwarding table matching (10 points).

Suppose a router has the forwarding table entries shown in the picture below.

| IP prefix | Output port |
| --------- | ----------- |
| 100.16.0.0/12 | 5 |
| 100.32.0.0/12 | 7 |
| 245.128.45.0/24 | 3 |
| 93.5.6.0/23 | 8 |
| 189.23.64.0/18 | 6 |
| 189.23.64.0/19 | 9 |
| 189.23.96.0/19 | 10 |

For the questions below, partial credit will be provided if you explain the reasoning behind your answers.

(a) Suppose a packet enters the router with a source IP address of 93.5.6.145 and a destination IP address of 245.128.45.168. What output port is it forwarded to? (2 points)

```
Port 3, 245.128.45.0/24
```

(b) Suppose another packet arrives with a destination IP address of 100.31.105.54. What output port is it forwarded to? (3 points)

```
Port 5, 100.16.0.0/12
```

(c) Suppose another packet arrives with a destination IP address of 189.23.80.4. What output port is it forwarded to? (3 points)

```
Port 9, 189.23.64.0/19
```

(d) Suppose another packet arrives with a destination IP address of 8.8.8.8. What output port is it forwarded to? (2 points)

### (7) Intra-domain routing protocols (27 points)
Consider the network whose graph abstraction is shown in this picture. The IP prefixes “owned” by the router, i.e., the set of endpoints reachable directly through the router, are provided alongside the routers, labeled and identified as A, B, C, etc. The link metrics are shown next to the edges in the graph.

![[Pasted image 20221212155353.png]]

(a) Suppose the network uses a link state routing protocol. Populate the following information in the link state advertisement originating from router B. (5 points)

router ID: $B$

IP prefix owned by the router (1 point): `128.64.45.0/24`
IDs of neighboring routers (2 points): `A, C, D, E`
Link metrics to neighbors (2 points): `3, 1, 4, 6`

(For the last question, please write the metrics in the same order as the neighbor IDs before.)

(b) This question builds on part (a). Suppose d(V) represents the current best estimate of the shortest path distance from router A to a fixed router V, and p(V) represents the predecessor on that shortest path. Suppose router A has received the link state advertisements from all other routers in the network. What are the initial values of the following? (6 points)

$d(B), p(B)$: $3, A$
$d(C), p(C)$: $8, A$
$d(D), p(D)$: $\infty, null$


(c) This question builds on part (b). After 2 iterations of Dijkstra’s algorithm, what are the values of the following? (6 points)

$d(C), p(C)$: $4, B$
$d(D), p(D)$: $7, B$
$d(E), p(E)$: $8, B$

(d) After all routers have computed their shortest paths, suppose a packet with destination IP address 128.64.203.67 arrives at router B. Towards which router is this packet directed? (2 points)

```
This packet is directed towards router C.
```

(e) Let’s start afresh from the figure for this question. Suppose the network uses a distance vector protocol. For this part and the ones that follow, please assume that all routers know the existence of all other routers in the network. However, initially, each router is unaware of the shortest distances to any other router. To begin with, each router only knows the costs of its direct edges to its immediate neighbors. We use dX(Y) to denote the component of the distance vector of X corresponding to destination Y at any point in time. What are the initial values of the following components (4 points)?

$d_A(A): 0$
$d_A(B): 3$
$d_B(D): 4$
$d_C(E): \infty$

(f) This question builds on part (e). Suppose router B just shared its current distance vector with A. This distance vector is:
$d_B(A) = 3$, $d_B(B) = 0$, $d_B(C) = 1$, $d_B(D) = 4$, $d_B(E) = 6$

Show the working of the Bellman-Ford equation at router A for destination D. What is the value of $d_A(D)$ after this exchange? (4 points)

$$
\begin{align}
d_A(D) &= min(c(a,e) + d_E(d), c(a,b) + d_B(B), c(a,d) + d_D(d), c(a,c) + d_C(d)) \\
c(a, e) &= \infty \\
d_E(D)  &= \infty \\
c(a,b) &= 3 \\
d_D(D) &= 4 \\
c(a,d) &= \infty \\
d_B(d) &= 0 \\
c(a,c) &= \infty \\
d_C(d) &= \infty
\end{align}
$$

$d_A(D) = min(\infty+\infty, 3+4, \infty+0, \infty+\infty)$

### (8) Collaboration and References (mandatory).
Who did you collaborate with on this problem set? What resources and references did you consult? Please also specify on what questions and aspects of the problem set you got help on. If you did not consult any resources other than the lecture slides and textbook, just say “no collaboration”.

```
No collaboration.
```