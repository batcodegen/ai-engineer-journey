import json

def save_chat(messages: list, filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(messages, f, indent=2)

def load_chat(filename: str) -> list:
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []
    except json.JSONDecodeError:
        print(f"Chat file is broken: {filename}, starting afresh")
        return []

def add_message(messages: list, role: str, content: str) -> None:
    if role not in ["user", "assistant"]:
        raise ValueError(f"Unknown role : {role}")
    messages.append({"role": role, "content": content})

if __name__ == '__main__':
    messages = [
        {"role": "user", "content": "What is Python?"},
        {"role": "assistant", "content": "A programming language."},
        {"role": "user", "content": "Is it hard?"},
    ]
    # Test 1: normal file
    save_chat(messages, "chat.json")
    print(len(load_chat("chat.json")))        # expect: 3

    # Test 2: missing file
    print(load_chat("nothing.json"))          # expect: message + []

    # Test 3: broken file
    with open("broken.json", "w") as f:
        f.write("hello")
    print(load_chat("broken.json"))           # expect: message + []

    # Test 4: wrong role
    try:
        add_message(messages, "robot", "Hi")
    except ValueError as e:
        print(f"Caught: {e}")  