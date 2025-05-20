import socket

# dictionary of color names and their hex codes
COLOR_DATA = {
    'white': '#FFFFFF',
    'black': '#000000',
    'red': '#FF0000',
    'green': '#00FF00',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
    'cyan': '#00FFFF',
    'magenta': '#FF00FF'
}

# get the closest color name to a given hex code
def get_closest_color(hex_code):
    hex_code = hex_code.lstrip('#')
    closest_color = None
    min_diff = float('inf')

    # calculate the RGB difference between the given hex code and all colors in dictionary
    target_r, target_g, target_b = int(hex_code[:2], 16), int(hex_code[2:4], 16), int(hex_code[4:], 16)
    
    for color_name, color_hex in COLOR_DATA.items():
        r, g, b = int(color_hex[1:3], 16), int(color_hex[3:5], 16), int(color_hex[5:], 16)
        
        # euclidean distance
        diff = (target_r - r) ** 2 + (target_g - g) ** 2 + (target_b - b) ** 2  
        
        if diff < min_diff:
            min_diff = diff
            closest_color = color_name

    return closest_color

# function to handle requests from the client
def handle_request(data):
    if data.startswith('#'):  # if data is hex
        return get_closest_color(data)
    elif data.lower() in COLOR_DATA:  # if data is a color name
        return COLOR_DATA[data.lower()]
    else:
        return 'Invalid input'

# set up the server
def start_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f'Server listening on {host}:{port}...')

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f'Connection from {client_address}')
                
                data = client_socket.recv(1024).decode()  # receive the request
                print(f'Received: {data}')

                if not data:
                    break

                # process the data
                response = handle_request(data)
                print(f'Response: {response}')

                # send the response back to the client
                client_socket.sendall(response.encode())

if __name__ == '__main__':
    start_server()
