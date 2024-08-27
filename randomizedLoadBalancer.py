import numpy as np
import matplotlib.pyplot as plt

class RandomizedLoadBalancer:
    def __init__(self,num_servers):
        self.num_servers = num_servers
        self.servers={i:[] for i in range(num_servers)}

    def assign_task(self,task):
        server=np.random.randint(0,self.num_servers)
        self.servers[server].append(task)

    def visualize(self):
        server_ids=list(self.servers.keys())
        load=[len(self.servers[i]) for i in server_ids]
        plt.figure(figsize=(10,5))
        plt.bar(server_ids,load,color='skyblue')
        plt.xlabel('Server ID')
        plt.ylabel('Randomized Load Balancer Visualization')
        plt.xticks(server_ids)
        plt.show()

    def print_load(self):
            for server,tasks in self.servers.items():
                print(f"Server {server}:{len(tasks)} tasks")

tasks=np.arange(1,101)
load_balancer=RandomizedLoadBalancer(num_servers=5)
for task in tasks:
    load_balancer.assign_task(task)

load_balancer.print_load()
load_balancer.visualize()








