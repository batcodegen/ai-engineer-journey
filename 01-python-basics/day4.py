def rate_hours(hours):
    if hours < 1:
        return "Too little"
    elif hours >= 1 and hours <= 2 :
        return "Good"
    else :
        return "Great"

print(rate_hours(1.5))
print(rate_hours(0.5))
print(rate_hours(2.5))

def average(numbers) -> float:
    if len(numbers) == 0: 
        return 0
    total = 0
    for i in numbers:
        total += i
    return total/len(numbers)
print(average([2, 1.5, 0, 3, 1, 2.5, 0.5]))

def add_message(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
print(add_message([
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "A programming language."},
    {"role": "user", "content": "Is it hard?"}
], "assistant", "Not really!"))

def count_by_role(messages, role) -> int:
    count = 0
    for msg in messages:
        if msg["role"] == role:
            count += 1
    return count
print(count_by_role([
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "A programming language."},
    {"role": "user", "content": "Is it hard?"}
], "user"))
print(count_by_role([
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "A programming language."},
    {"role": "user", "content": "Is it hard?"}
], "assistant"))


def add_message(messages: list, role: str, content: str) -> None:
    messages.append({"role": role, "content": content})

def count_by_role(messages: list, role: str) -> int:
    count = 0
    for msg in messages:
        if msg["role"] == role:
            count += 1
    return count

messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "A programming language."},
    {"role": "user", "content": "Is it hard?"},
]
add_message(messages, "assistant", "Not really!")
add_message(messages, "user", "Great, thanks!")

print(count_by_role(messages, "user"))       # 3
print(count_by_role(messages, "assistant"))