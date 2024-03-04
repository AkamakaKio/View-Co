def view_completed_tasks(tasks):
    completed_tasks = [task for task in tasks if "(Completed)" in task]
    return completed_tasks

# Example usage:
tasks = ["Task 1", "Task 2 (Completed)", "Task 3"]
completed_tasks = view_completed_tasks(tasks)
print("Completed tasks:", completed_tasks)
