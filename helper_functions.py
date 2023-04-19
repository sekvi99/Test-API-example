def task_creation_helper(task_content: str,
                         user_id: int,
                         ) -> dict[str, str]:
    """
    Helper function to handle test task creation 
    Returns:
        dict[str, str]: Dictionary representation of created task.
    """
    return {
        "content": f"Test Task - {task_content}",
        "user_id": f"TestUserID{user_id}",
        "is_done": False,
    }
    
def modify_task(task: dict[str, str], task_id: str) -> dict[str, str]:
    """
    Helper function to handle modification of task.
    Args:
        task (dict[str, str]): Task object representation as dictionary.

    Returns:
        dict[str, str]: Modified dictionary of task.
    """
    return {
        "content": f"Modified: {task['content']} - Changed",
        "user_id": task["user_id"],
        "task_id": task_id,
        "is_done": True,
    }