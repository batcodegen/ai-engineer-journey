from chat_utils import load_chat, save_chat

class ChatSession:
    def __init__(self, filename):
        self.filename = filename
        self.messages = load_chat(filename)

    def add(self, role: str, content: str) -> None:
        if role not in ['user', 'assistant']:
            raise ValueError(f"Unknown role: {role}")
        self.messages.append({"role": role, "content": content})

    def count_by_role(self, role) -> int:
        count = 0
        for msg in self.messages:
            if msg["role"] == role:
                count += 1
        return count

    def save(self):
        save_chat(self.messages, self.filename)

    def last_message(self):
        if not self.messages:
            return None
        return self.messages[-1]