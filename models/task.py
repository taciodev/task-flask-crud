from shortuuid import uuid

class Task:
    def __init__(self, title, description, completed=False) -> None:
        self.id = uuid()
        self.title = title
        self.description = description
        self.completed = completed
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

