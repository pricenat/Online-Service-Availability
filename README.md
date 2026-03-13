# Online-Service-Availability
HTTP Server Microservice for testing server availability. It expects JSON data with a couple of options for specifying parameters:
(1) "url" parameter containing the server ip address and port combined with a colon, i.e. "http://127.0.0.1:6003".
or (2) "server_ip" containing the ip address of server ie "http://127.0.0.1" and "server_port" ie "6003"
It returns the status code of the server being connected to.
