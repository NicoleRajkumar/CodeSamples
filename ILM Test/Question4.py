#Implement a simple priority queue. Assume an incoming stream of dictionaries containing two keys; command to be executed and priority. Priority is an integer value [0, 10], where work items of the same priority are processed in the order they are received. 

#incoming dict: {"command":"a string of command", "priority": 4} 

class PriorityQueue(object):

    def __init__(self) -> None:
        self.queue = []  # list of dicts

    def insert(self, command):
        #command is dict
        self.queue.append(command)

    def process(self):
        if not self.isEmpty():
            itemtoprocess = 0
            #iterate through all items in queue and check if priority is bigger
            for i in range(len(self.queue)):
                if self.queue[i]["priority"] > self.queue[itemtoprocess]["priority"]:
                    itemtoprocess = i

            #remove from queue
            commandtoprocess = self.queue[itemtoprocess]["command"]
            self.queue.pop(itemtoprocess)
            return commandtoprocess


    def isEmpty(self):
        return len(self.queue) == 0


if __name__ == '__main__':
    TestQueue = PriorityQueue()
    TestQueue.insert({"command": "a test command", "priority": 7})
    TestQueue.insert({"command": "test2", "priority": 3})
    TestQueue.insert({"command": "foo", "priority": 5})
    TestQueue.insert({"command": "bar", "priority": 1})
    TestQueue.insert({"command": "hello world", "priority": 10})
    TestQueue.insert({"command": "nicole test test", "priority": 4})

    while not TestQueue.isEmpty():
        print(TestQueue.process())

