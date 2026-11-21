# 🤖 AI Engineer Journey

From **React Native engineer** to **AI Engineer**, learning in public over 16 weeks.

I'm starting from zero Python and documenting every step: lessons, practice code and projects.

## Week 1: Python Basics

| Day | Topic | Code |
|---|---|---|
| 1 | Lists, for loops, range | [day2.py](01-python-basics/day2.py) |
| 2 | Dictionaries + AI chat message format | [day3.py](01-python-basics/day3.py) |
| 3 | Functions, return vs print, type hints | [day4.py](01-python-basics/day4.py) |

### 💡 Key learnings

- **Indentation is syntax** in Python, not just style.
- **`print` is not `return`.** A function without `return` gives back `None`.
- **Lists passed into functions are the same list, not a copy.** Changes inside the function affect the original.
- **AI chat APIs use a list of dictionaries:**

```python
messages = [
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "A programming language."}
]
```

---

## ▶️ How to run

```bash
cd 01-python-basics
python3 day2.py
```

---

## 🛠️ Tech so far

Python 3 · VS Code · Git

---