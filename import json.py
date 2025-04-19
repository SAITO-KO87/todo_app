import json
import os
print("ToDoアプリが動いています！")

FILENAME = "todo_list.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("📭 タスクはありません。")
        return
    print("📋 現在のタスク:")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def add_task(tasks):
    task = input("📝 追加するタスク内容を入力: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ タスクを追加しました！")

def delete_task(tasks):
    show_tasks(tasks)
    num = input("❌ 削除するタスク番号を入力: ")
    if num.isdigit():
        num = int(num)
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ '{removed}' を削除しました！")
        else:
            print("⚠️ 無効な番号です。")
    else:
        print("⚠️ 数字を入力してください。")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- ToDoメニュー ---")
        print("1. タスクを見る")
        print("2. タスクを追加する")
        print("3. タスクを削除する")
        print("4. 終了する")
        choice = input("番号で選んでください: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 アプリを終了します。おつかれさま！")
            break
        else:
            print("⚠️ 無効な選択です。")

if __name__ == "__main__":
    main()
