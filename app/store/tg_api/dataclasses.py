from dataclasses import dataclass


@dataclass
class UpdateMessage:
    date: int
    from_id: int
    chat_id: int
    text: str
    is_command: bool


@dataclass
class Update:
    update_id: int
    object: UpdateMessage


@dataclass
class Message:
    user_id: int
    text: str