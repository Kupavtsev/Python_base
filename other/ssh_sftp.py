"""
Requirements:
tabulate==0.8.9
"""
import os
from tabulate import tabulate

headers = ["ALIAS",'USER',"IP","PRIVATE KEY FILE","LOCAL FORWARD","ID"]
PRIMARY_SSH_KEY = r"C:\Users\costa\.ssh\sample"

servers =  [
    ['server-01', "root","172.24.5.50",PRIMARY_SSH_KEY,"3309 127.0.0.1:3306"], 
    ['server-02', "teste","54.214.155.147",PRIMARY_SSH_KEY,"NA"]
]
servers.sort()

counter = 0
for i in servers:
    i.append(counter)
    counter +=1

servers_table = tabulate(servers,headers,tablefmt="fancy_grid")

print(f"{len(servers)} available connections")
print(servers_table)

def get_connection_type(alias)-> str:
    headers = ["TYPE","ID"]
    connections = [
        ["SSH",0],
        ["SFTP",1]
    ]
    connections_table = tabulate(connections,headers,tablefmt="fancy_grid")
    print(connections_table)

    while True:
        choice = input(f"Connection type ID for {alias}: ")
        try:
          choice = int(choice)
          return connections[choice][0]
        except:
            print(f"Type a number from 0-{len(connections)-1}")
            continue


while True:
    choice = input("Server ID or 'Q' for quitting: ")
    if choice.lower() == "q":
        break
    else:
        try:
            choice = int(choice)
            alias = servers[choice][0]
            user = servers[choice][1]
            ip = servers[choice][2]
            key = servers[choice][3]
            local_forward = servers[choice][4]
            connection_type = get_connection_type(alias).lower()

            if local_forward.upper() != "NA" and connection_type.upper() == "SSH":
                local_forward = local_forward.split()
                os.system(f"{connection_type} -i {key} -o IdentitiesOnly=yes -L {local_forward[0]}:{local_forward[1]} {user}@{ip}")
                break
            
            os.system(f"{connection_type} -i {key} -o IdentitiesOnly=yes {user}@{ip}")
            break
        except:
            print(f"Type a number from 0-{len(servers)-1}")
            continue