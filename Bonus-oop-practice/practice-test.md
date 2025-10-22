🎯 Scenario: Build a Simple Network Topology Explorer

You are given a mini dataset from an imaginary API that gives this structure:

A Data Center has multiple Switches

Each Switch connects to multiple Hosts

You want to:

Model this using Python classes

Write a small script (main.py) to print the structure like:

🏢 Data Center: DC-1
  └── Switch: Switch-A
        ├── Host: Host-101
        └── Host: Host-102
  └── Switch: Switch-B
        └── Host: Host-201


Let’s go one step at a time 🚶‍♂️


Breaking this down. 

Step 1 : Think of the Things ( nouns )
    Datacenters , Switches , Hosts
Step 2 : Think of the relationships
    DataCenters have many switches
    Switches have many Hosts
    Hosts have attributes
Step 3 : Model the Classes
    class Datacenter:
        def __init__(self,name):
            self.name = name
            self.switches = []

    class Switch:
        def __init__(self):
            self.hosts = []

    class Host:
        def __init__(self):
            self.name = name
            self.ip = ip
            self.type = type
            self.model = model

Step 4: Model the flow of data.

 for each Datacenter : 
    fetch Switches,
        for each switch :
            fetch host,
                for each host : 
                    print attribute
                append host to switch
            append host to switch
        append switch to Data center

Step 5: Print out the data 
            
