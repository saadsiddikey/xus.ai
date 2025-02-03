from firebase_config import db
import datetime

def ask_tasks():
    tasks = []
    while True:
        task = input("What task do you want to add? (Type 'done' to finish): ")
        if task.lower() == "done":
            break
        time = input("What time for this task? (HH:MM): ")
        tasks.append({"task": task, "time": time})

    user_id = "user1"
    db.collection("tasks").document(user_id).set({"tasks": tasks})
    print("✅ Tasks saved successfully!")

ask_tasks()
