import json
data = {"name": "Asha", "active": True, "score": None}
text = json.dumps(data)
print(text)
print(type(text))
back = json.loads(text)
print(back["active"])

hours = [2, 1.5, 0, 3, 1, 2.5, 0.5]
with open("hours.txt",'w') as f:
    for h in hours:
        f.write(f"{h}\n")

with open("hours.txt", 'r') as f:
    total = 0
    for line in f:
        line.strip()
        total += float(line)
    print(f"Total hours : {total}")

def save_chat(messages: list, filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(messages, f, indent=2)

def load_chat(filename: str) -> list:
    with open(filename, 'r') as f:
        return json.load(f)

def add_message(messages: list, role: str, content: str) -> None:
    messages.append({"role": role, "content": content})

save_chat([
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "A programming language."},
    {"role": "user", "content": "Is it hard?"}
], "chat.json")
loaded = load_chat("chat.json")