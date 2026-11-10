profile = {"name": "Prakhar", "city": "Indore", "years": 9, "skills": ["React Native", "Javascript"]}
print(f"{profile["name"]} has {profile["years"]} of experience as a developer")
profile["skills"].append("Python")
for skill in profile["skills"] :
    print(f"Skill : {skill}")

messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "A programming language."},
    {"role": "user", "content": "Is it hard?"}
]
for i in messages:
    print(f"{i["role"]}: {i["content"]}")
messages.append({"role": "assistant", "content": "Not really!"})
def my_filter(n):
    return n["role"] == "user"
print(f"count: {len(list(filter(my_filter, messages)))}")