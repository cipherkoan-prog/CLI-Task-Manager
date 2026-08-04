class Task:
    def __init__(self, title, priority, completed=False):
        self.title = title
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            'title' : self.title,
            'priority' : self.priority,
            'completed' : self.completed
        }
        
