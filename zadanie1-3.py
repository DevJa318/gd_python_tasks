# 3. Create a script that reads the access log from a file. The name of the file is provided as an argument. An output of the script should provide the total number of different User Agents and then provide statistics with the number of requests from each of them. Here is a link to an example access.log file.

import sys

file = sys.argv

filename = sys.argv[1]

user_agents = {}

with open (filename, "r") as f:
    #print(list(f))
    for line in f:
        user_agent = line[line.rindex('"',0,len(line)-2)+1:len(line)-2]

        if user_agent not in user_agents.keys():
            user_agents[user_agent] = 1
        elif user_agent in user_agents.keys():
            user_agents[user_agent] = user_agents[user_agent] + 1


print(len(user_agents.keys()))
for k,v in user_agents.items():
    print(k,v)