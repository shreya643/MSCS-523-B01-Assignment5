import heapq

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority > other.priority 

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_max(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return None

    def increase_key(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    self.heap[i].priority = new_priority
                    heapq._siftup(self.heap, i)
                break

    def is_empty(self):
        return len(self.heap) == 0
    
def run_scheduler():
    pq = PriorityQueue()
    
    tasks = [
        Task(task_id=1, priority=5, arrival_time="08:00", deadline="10:00"),
        Task(task_id=2, priority=3, arrival_time="11:05", deadline="12:30"),
        Task(task_id=3, priority=1, arrival_time="11:10", deadline="12:30"),
        Task(task_id=4, priority=4, arrival_time="11:15", deadline="12:45"),
        Task(task_id=5, priority=7, arrival_time="11:20", deadline="12:15")
    ]
    
    for task in tasks:
        pq.insert(task)
    
 
    print("Task Execution Order:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Executing {task}")

    print("\nPriority update for Task ID 2")
    pq.insert(tasks[1])  
    pq.increase_key(task_id=2, new_priority=10)
    print("Updated Task Order after Priority Change:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Executing {task}")


run_scheduler()
