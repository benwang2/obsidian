---
title: Lecture Notes 7
course: CS_352
date: 2022-09-27
tags: 
- lectureNotes
- CS_352
---

<center><h1>Lecture 7</h1></center>
## Simple Mail Transfer Protocol
Simple Mail Transfer Protocol (SMTP ) allosw us to send and receive messages from a server.

#smtp
#mail_server

### Components
SMTP is composed of 3 main components:
- user agents
- mail server
- smtp protocol

#### User Agent
A user agent is the client a user may use to access their mailbox. This may be an application like Outlook or Apple Mail. It could also be a web client, like Gmail or Yahoo Mail.

#user_agent

#### Mail Server
The mail server contains a **mailbox** for incoming messages for a user. It also queues outgoing messages from a user. The sender's mail server makes a connection to the receiver's mail server on port 25.

#### SMTP
The SMTP protocol is used to send messages from client to server. The client (either a user agent or sending mail server) sends the message. The server is the *receiving* mail server.

### Scenario
1. **User 1** composes a message to **User 2**
2. **User 1**'s client is sent to the mail server and the message is placed in outgoing queue
3. Client side of SMTP opens TCP connection with **User 2**'s mail server.
4. SMTP client sends **User 1** message over TCP connection
5. **User 2**'s mail server places inbound message in mailbox
6. **User 2** invokes client to read message

### Observations
Mail servers are the **infrastructure** for email functionality and can act as both the client or the server based on the context.

SMTP is **push-based**, meaning that everything is reliant on info being *pushed* from client to server.

#push-based

### Mail Response Codes
| code | description              |
| ---- | ------------------------ |
| 220  | Service ready            |
| 250  | Request command complete |
| 354  | Start mail input         |
| 421  | Service not available    |
| 500  | Unrecognized command     |


### Message Format
The message format for SMTP was standardized in [RFC 822](https://learn.microsoft.com/en-us/previous-versions/office/developer/exchange-server-2010/aa493918(v=exchg.140)). It as constructed as such:
- Header lines (to, from, subject)
- Body (message, ascii characters only)

There is a blank space between the header and the body when the message is transmitted. This format was stored on the **mail server**.

#### MIME
Multipurpose Internet mail extension ([MIME](https://en.wikipedia.org/wiki/MIME)) was established in [RFC 2045](https://www.rfc-editor.org/rfc/rfc2045) and [RFC 2046](https://www.rfc-editor.org/rfc/rfc2046)

Additional headers in the data header specify the MIME content type and version. The message can have many parts.

#MIME

## Mail Access Protocols
### Access protocols
Whereas SMTP is focused on pushing data, the mail access protocols are focused on pulling data.
- POP: Post Office Protocol ([RFC 1939](https://www.rfc-editor.org/rfc/rfc1939))
- IMAP: Internet Mail Access Protocol ([RFC 1730](https://www.rfc-editor.org/rfc/rfc1730))
- HTTP: Gmail, Outlook, etc.

#POP, #IMAP, #HTTP
### Web-based email (HTTP)
Web-based emails connect to mail servers via web browser. Browsers work in HTTP requests, whereas email servers use SMTP. The browser makes a HTTP request to the HTTP server, which then communicates to the mail server in SMTP.

In some configurations, the HTTP server and SMTP server can be on the same machine.

### SMTP vs. HTTP
| HTTP                               | SMTP                                       |
| ---------------------------------- | ------------------------------------------ |
| pull                               | push                                       |
| 1:1 object to message              | multiple objects sent in multipart message |
| can put non-ascii data in response | need ascii-based encoding (base64)

Both protocols have ASCII command/response interactions and status codes.

#base64
#ascii

### Themes from app-layer protocols
**Keep it simple until you need complexity**.
- start with ASCII-based design, stateles servers
- cookies for HTTP state
- multimedia extensions (MIME) in e-mail

Performance optimizations are often an after-thought. Headers can easily be upgraded without breaking old functionality.

Utilize modularity by **partitioning functions based on what's best at each place**.
For example,
- leave content rendering to the user agent - why would the mail server need to see content?
- rely on mail server for reliable delivery - client can be asleep or offline

## Question
1. When you read email on your browser (e.g. by visiting mail.google.com), which protocol is being used by your browser?
   <input type="radio"> MAILP
   <input type="radio"> SMTP
   <input type="radio"> IMAP
   <input type="radio" checked> HTTP

2. Could you share any experiences you have had (as a user, programmer, etc.) on any of the concepts on email that we covered in the lecture today? Example response: "I have configured IMAP settings for my mail client on my laptop to receive Rutgers email." (Note: You cannot provide the response above.)
```
I have completed projects in web development and I often have to configure web pages to properly recieve different MIME content types.
```

3. When you receive email through the desktop mail client (e.g., AppleMail), which protocol may be used?
   <input type="radio"> MAILP
   <input type="radio"> SMTP
   <input type="radio" checked> IMAP
   <input type="radio"> HTTP

4. When you send email from the desktop mail client (e.g., AppleMail), which protocol is being used?
   <input type="radio"> MAILP
   <input type="radio" checked> SMTP
   <input type="radio"> IMAP
   <input type="radio"> HTTP