from chat_utils import load_chat, add_message, save_chat


messages = load_chat("chat.json")
add_message(messages, "user", "What is Python new?")
save_chat(messages, "chat.json")