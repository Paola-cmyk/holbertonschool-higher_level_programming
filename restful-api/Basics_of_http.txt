#  Differences between HTTP and HTTPS.
- HTTP (HYpertext Transfer Protocol) is the standard protocol used for transmitting data over the web, although it **does not encrypt** the data, 
making it vulnerable to attackers. 
- HTTPS (Hypertext Transfer Protocol Secure) is an **encrypted** version of HTTP that uses **SSL/TLS** encryption to secure data tranamission.

**Key differences**: HTTPS ensures security, confidentiality, integrity and authenticity while HTTP does not.

# Outline of an HTTP. 
An HTTP request and response  follow a structure of:

- A start Line
- Headers 
- Body

# Request and Response.
- A HTTP request begins iwth a request line that includes the HTTP method, (GET, POST, or PUT) the path to the resource being requested (index.html) and the HTTP version.

- The HTTP response is sent back by the server, it also allows a structured format. It begins with a status line that includes the HTTP version, a status code and a brief status message.

# Lists of common HTTP methods.
**METHODS**:
- GET: requests data from the server
    
    - Retrieves a web page or data from an API
- POST: Submits data to the server

    - Submitting a form or user login information
- PUT: Updates existing data

    - Editing an user profile on a website
- DELETE: Deletes data from the server

    - Removing a comment or a file from system

**STATUS CODES**:
- 200: OK

    - Loading home page succesfully
- 301: Moved Permanently

    - Redirecting an old URL to new domain
- 403: Forbidden

    - Trying to access admin-only content without rights
- 404: Not Found

    - Mistyped URL or deleted page
- 500: Internal Server Error

    - Website crashes due to a coding bug
