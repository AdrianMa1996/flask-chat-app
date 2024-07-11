from datetime import datetime
from .models import Message, User

class MessageDTO:
    def __init__(self, id: int, sender_id: int, sender_name: str, content: str, created_at: datetime):
        self.id = id
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.content = content
        self.created_at = created_at
    
    def to_dict(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'sender_name': self.sender_name,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }

def convert_message_to_messagedto(message: Message) -> MessageDTO:
    return MessageDTO(
        id=message.id,
        sender_id=message.sender_id,
        sender_name=User.query.filter_by(id=message.sender_id).first().username,
        content=message.content,
        created_at=message.created_at
    )


