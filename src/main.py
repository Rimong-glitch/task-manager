"""Task Manager CLI - TP B (Gestion de Projets)."""
import argparse
import json
import os
from dataclasses import dataclass, asdict

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


class TaskStorage:
    """Persistance JSON."""

    def __init__(self, path=DATA_FILE):
        self.path = path

    def load(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, encoding="utf-8") as f:
            return [Task(**t) for t in json.load(f)]

    def save(self, tasks):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([asdict(t) for t in tasks], f, ensure_ascii=False, indent=2)


class TaskManager:
    """Logique métier."""

    def __init__(self, storage=None):
        self.storage = storage or TaskStorage()
        self.tasks = self.storage.load()

    def add(self, title):
        new_id = max((t.id for t in self.tasks), default=0) + 1
        task = Task(new_id, title)
        self.tasks.append(task)
        self.storage.save(self.tasks)
        return task

    def done(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                t.done = True
                self.storage.save(self.tasks)
                return True
        return False

    def delete(self, task_id):
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.storage.save(self.tasks)
        return len(self.tasks) < before

    def list(self):
        return list(self.tasks)


def build_parser():
    p = argparse.ArgumentParser(description="Task Manager CLI")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("title")
    sub.add_parser("list")
    d = sub.add_parser("done"); d.add_argument("id", type=int)
    r = sub.add_parser("delete"); r.add_argument("id", type=int)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    m = TaskManager()
    if args.cmd == "add":
        t = m.add(args.title)
        print(f"Added #{t.id}: {t.title}")
    elif args.cmd == "list":
        for t in m.list():
            print(f"[{'x' if t.done else ' '}] {t.id}. {t.title}")
    elif args.cmd == "done":
        print("Done." if m.done(args.id) else "Task not found.")
    elif args.cmd == "delete":
        print("Deleted." if m.delete(args.id) else "Task not found.")


if __name__ == "__main__":
    main()
