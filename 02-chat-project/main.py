from chat_utils import load_chat, add_message, save_chat
from chat_session import ChatSession

messages = load_chat("chat.json")
add_message(messages, "user", "What is Python new?")
save_chat(messages, "chat.json")

work_chat = ChatSession("work.json")
study_chat = ChatSession("study.json")

work_chat.add('user', "Day work")
work_chat.add('user', "Night work")
work_chat.save()

study_chat.add('assistant', 'Night study')
study_chat.add('assistant', 'Day study')
study_chat.save()

work_count = work_chat.count_by_role("user")
study_count = study_chat.count_by_role("assistant")
print(work_count)
print(study_count)
