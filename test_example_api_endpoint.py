import pytest # Importing pytest for testing 
import requests  # Importing request for endpoint connection
from helper_functions import task_creation_helper, modify_task
from connections import TEST_ENDPOINT, create_task_response, get_task_response, update_task_response, delete_task_response, get_list_of_task_response
from typing import Final
import random


"""Testing Endpoint
Example endpoint testing for FastAPI shared by: pixegami
His yt: https://www.youtube.com/@pixegami
"""

def test_endpoint_connection_status():
    """
    Test function to check whether provided endpoint returns propper status.
    """
    response = requests.get(TEST_ENDPOINT)
    assert response.status_code == 200
    
def test_task_creation_procedure():
    """
    Test function to check whether /create-task endpoint works propperly
    """
    # ! Changning request methof based on endpoint specification
    response = create_task_response(task_creation_helper(
        task_content="Task Creation Endpoint Testing",
        user_id="FK"
    ))
    # ! Ensuring ourselfs that endpoint propperly handle our request
    assert response.status_code == 200 
    
def test_get_task_data_extracting_procedure():
    """
    Test function to check whether for create task, we can extract it from the system.
    """
    # ! Creating test task
    payload: dict[str, str] = task_creation_helper(
        task_content="Task Creation Endpoint Testing",
        user_id="FK"
    )
    create_task_response_obj = create_task_response(data=payload)
    assert create_task_response_obj.status_code == 200
    
    # ! Extracting data from response to check get-task endpoint
    data = create_task_response_obj.json() # Extracting data from response
    task_id: str = data['task']['task_id']
    
    # ! Testing get-task endpoint
    task_response = get_task_response(task_id)
    assert task_response.status_code == 200 # Checking status
    extracted_task: dict[str, str] = task_response.json()
    assert extracted_task['content'] == payload['content'] # Checking send content data
    assert extracted_task['user_id'] == payload['user_id'] # Checking send user id
    assert extracted_task['is_done'] == payload['is_done'] # Checking send is_done status


def test_update_task_procedure():
    """
    Test function to check whether system propperly updates status of task.
    """
    # ! Payload for task creation
    before: dict[str, str] = task_creation_helper(
        task_content="Task before Update",
        user_id="FK"
    )
    
    # ! Creating task
    create_task_response_obj = create_task_response(data=before)
    assert create_task_response_obj.status_code == 200
    task_id: str = create_task_response_obj.json()['task']['task_id']
    
    # ! Updating task
    after: dict[str, str] = modify_task(task=before, task_id=task_id)
    update_task_response_obj = update_task_response(data=after, task_id=task_id)
    assert update_task_response_obj.status_code == 200
    
    # ! Extracting updated task Id and task data
    updated_task_data: dict[str, str] = update_task_response_obj.json()
    update_task_id: str = updated_task_data['updated_task_id']
    update_task_response_obj = get_task_response(update_task_id)
    assert update_task_response_obj.status_code == 200
    update_data: dict[str, str] = update_task_response_obj.json()
    
    # ! Checking whether content is the same as after payload - after dict
    assert update_data['content'] == after['content']
    assert update_data['user_id'] == after['user_id']
    assert update_data['is_done'] == after['is_done']
    
    # ! Checking whether content has changed between two payloads
    assert before['content'] != after['content']
    assert before['is_done'] != after['is_done']
    
def test_delete_task_procedure():
    # ! Creating task to delete after
    task_to_delete = create_task_response(task_creation_helper(
        task_content="Test Content to delte",
        user_id="FK"
    ))
    assert task_to_delete.status_code == 200
    data = task_to_delete.json()
    task_id: str = data['task']['task_id']
    
    # ! Deleting task
    delete_task_response_obj = delete_task_response(task_id=task_id)
    assert delete_task_response_obj.status_code == 200
    
    # ! Trying to extract data for given task
    get_task_response_obj = get_task_response(task_id=task_id)
    assert get_task_response_obj.status_code == 404

def test_list_of_task_for_given_user_procedure():
    user_randomizer: str = str(random.randint(100, 9999))
    user_id: str = f"TestUserIDFK{user_randomizer}"
    iterator: int = 3
    # ! Creating test tasks for given user
    for i in range(iterator):
        task_creation_obj = create_task_response(task_creation_helper(
            task_content=f"Test task nr: {i}",
            user_id=f"FK{user_randomizer}"
        ))
        assert task_creation_obj.status_code == 200
        
    list_of_tasks_response = get_list_of_task_response(user_id=user_id)
    assert list_of_tasks_response.status_code == 200
    data: dict[str, str] = list_of_tasks_response.json()
    
    assert len(data['tasks']) == iterator


    