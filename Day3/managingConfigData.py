#Define the variables
server_name = "my_server"
port = 8080
is_https_enabled = True
max_connections = 3000

# Print the configurations
print(f"server_name : {server_name}")
print(f"port : {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")

#Update port value
port = 445

print(f"Port updated : {port}")
