from datetime import datetime

from .models import Message, User

class MessageDTO:
    def __init__(self, id: int, sender_id: int, sender_name: str, chat_room_id: int, content: str, created_at: datetime):
        self.id = id
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.chat_room_id = chat_room_id
        self.content = content
        self.created_at = created_at

def convert_to_message_dto(message: Message) -> MessageDTO:
    return MessageDTO(
        id=message.id,
        sender_id=message.sender_id,
        sender_name=User.query.filter_by(id=message.sender_id).first().username,
        chat_room_id=message.chat_room_id,
        content=message.content,
        created_at=message.created_at
    )

class ChatRoomDTO:
    def __init__(self, id: int, user_one_id: int, user_two_id: int):
        self.id = id
        self.user_one_id = user_one_id
        self.user_two_id = user_two_id

