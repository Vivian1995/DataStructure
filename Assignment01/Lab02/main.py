from module import Queue

Queue = [] #using list as a queue

Queue.insert(0, 'smile') #enqueue of Queue
print(Queue)
Queue.insert(0, 13) #enqueue of Queue
print(Queue)
Queue.insert(0, 'happy')
print(Queue)
size = len(Queue) #size of Queue
print(size)
Queue.pop() #dequeue of Queue
print(Queue)
