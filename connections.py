from typing import Final
import requests
# ! Declaration const for endpoint
TEST_ENDPOINT: Final[str] = r"https://todo.pixegami.io/"

def create_task_response(data: dict[str, str]) -> requests.Response:
    """
    Connection function to generetare response for given API Endpoint.
    Args:
        data (dict[str, str]): Data to be sent to server.

    Returns:
        requests.Response: Server response obj.
    """
    create_task_endpoint: str = f"{TEST_ENDPOINT}/create-task"
    return requests.put(create_task_endpoint, json=data)

def get_task_response(task_id: str) -> requests.Response:
    """
    Connection function to get data for given task id.
    Args:
        task_id (str): String representation of task id.

    Returns:
        requests.Response: Server response obj.
    """
    get_task_endpoint: str = f"{TEST_ENDPOINT}/get-task/{task_id}"
    return requests.get(get_task_endpoint)

def update_task_response(data: dict[str, str],
                           task_id: str) -> requests.Response:
    """
    Connection function to update given task by provided task id.
    Args:
        data (dict[str, str]): Dictionary modified data representation.
        task_id (str): String representation of task id.

    Returns:
        requests.Response: Server response obj.
    """
    update_task_endpoint: str = TEST_ENDPOINT + f"update-task"
    return requests.put(update_task_endpoint, json=data)

def delete_task_response(task_id: str) -> requests.Response:
    """
    Connection function to delete given task by provided task id.
    Args:
        task_id (str): String representation of task id.

    Returns:
        requests.Response: Server response obj.
    """
    delte_task_endpoint: str = f"{TEST_ENDPOINT}/delete-task/{task_id}"
    return requests.delete(delte_task_endpoint)
    
    
def get_list_of_task_response(user_id: str) -> requests.Response:
    """
    Connection function to retrive all of the task for given user id.
    Args:
        user_id (str): String representation of user id.

    Returns:
        requests.Response: Server response obj.
    """
    get_task_endpoint: str = f"{TEST_ENDPOINT}/list-tasks/{user_id}"
    return requests.get(get_task_endpoint)
