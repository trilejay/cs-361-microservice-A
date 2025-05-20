# Microservice A

# Description
This microservice converts between color names and their corresponding hex codes. The service handles two types of requests:
1. **Hex Code**: Sends a color name corresponding to the provided hex code.
2. **Color Name**: Sends the hex code corresponding to the provided color name.
The microservice communicates via Python sockets.

# How to Programmatically REQUEST & RECEIVE Data
To request data from the microservice, create a socket connection and send either a hex code or a color name to the microservice. 

**Example for Sending Hex Code:**

```python
import socket

# set up socket connection to the microservice
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 12345))

    # send the hex code
    s.sendall('#010101'.encode())

    # receive the response from the microservice
    response = s.recv(1024).decode()

print(f"Response: {response}")
```

**Example for Sending Color Name:**

```python
import socket

# set up socket connection to the microservice
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 12345)

    # send color name
    s.sendall('white'.encode())

    # receive response from the microservice
    response = s.recv(1024).decode()

print(f"Response: {response}")
```

**UML Sequence Diagram**

![uml sequence drawio](https://github.com/user-attachments/assets/990819d3-df8e-432f-b011-4cb8dc1785b1)

