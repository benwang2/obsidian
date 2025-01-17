---
title: Lecture Notes X
course: CS_XXX
date: YYYY/MM/DD
tags: 
- lectureNotes
- CS_XXX
---

<center><h1>Lecture 5</h1></center>

## DNS Resource Records
DNS is a distributed database that stores **resource records (RRs**)

Each resource record contains a class, type, name, value, and time to live.

### Types of Records
Type=A
- **name** is hostname
- **value** is IPv4 address

Type=AAAA
- **name** is hostname
- **value** is **IPv6** address

Type=NS
- **name** is domain
- **value** is hostname of authoritative name server for this domain
- sometimes see SOA record

Type=CNAME
- **name** is alias for some "canonical" (the real) name (ibm.com is ibm.com.cs186.net)
- **value** is canonical name

Type=MX
- **value** is name of mailserver associated with name

#a, #aaaa, #ns, #cname, #mx

### Example
An example DNS record example might look like the following:

A resource record in response to query
| NAME    | design.cs.rutgers.edu |
| ------- | --------------------- |
| TYPE    | A                     |
| CLASS   | IN                    |
| TTL     | 1 day (86400s)        |
| ADDRESS | 192.26.92.30          |

Records for authoritative servers information about nameserver
| NAME    | cs.rutgers.edu      |
| ------- | ------------------- |
| TYPE    | NS                  |
| CLASS   | IN                  |
| TTL     | 1 day (86400s)      |
| NSDNAME | ns-lcsr.rutgers.edu |

#resource_record
## HTTP
HTTP stands for "HyperText Transfer Protocol". Every web page is made up of many **objects**.

An object can be:
- HTML file
- JPEG image
- Video Stream chunk
- Audio file

#http
Web pages consist of **base HTML-file** which includes several referenced objects.

Each object is addressable by a **uniform resource locator (URL)**, which is also sometimes referred to as a **uniform resource identifier (URI)**.

#url #uri
### HTTP Protocol
The HTTP application is typically associated port 80. 

![[Pasted image 20221006003504.png]]

An HTTP request message appears as such
```
GET /352/syllabus.html HTTP/1.1
Host: www.cs.rutgers.edu
User-agent: Mozilla/4.0
Connection: close
Accept-language: en
```
The first line of the message is the request line.
The lines following are the header lines. 
Following the header lines is a carriage return, which indicates the end of header.

### Method Types
- **GET** - Get the resource specified in the requested URL (could be a process)
- **POST** - Send entities (specified in the entity body) to a data-handlig process at the requested URL
- **HEAD** - Asks server to leave requested object out of response, but then send the rest of the response (useful for debugging)
- **PUT** - Update a resource at the requested URL with the new entity specified in the entity body
- **DELETE** - Deletes file specified in URL

#get #post #head #put #delete
#### Form Input: GET and POST
The POST method is often implemented in a form iput. The input is uploaded to the server **in entity body**, but the posted content is not visible in URL.

With the GET method, the entity body is empty and the input is uploaded in **URL field of request line.** The URL must conform to a restricted set of characters.

#### POST vs PUT
In a POST request, the URL of the request identifies the resource that **processes** the entity body.

In a PUT request, the URL of the request identifies the resource that is **contained in** the entity body.

#### HEAD vs GET
With a GET request, the requested resource is returned in the entity body of the response along with the response headers.

With a HEAD request, return all the response headers in the GET response, but **without the resource** in the entity body.

### HTTP Response Status Codes
| CODE | NAME                       | DESC                                        |
| ---- | -------------------------- | ------------------------------------------- |
| 200  | OK                         | Request succeeded                           |
| 301  | Moved Permanently          | Requested objected moved to new location    |
| 403  | Forbidden                  | Insufficient permissions to access resource |
| 404  | Not Found                  | Requested resource not found on this server |
| 505  | HTTP Version Not Supported |                                             |
