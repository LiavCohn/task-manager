from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from ..database import tasks_collection
from ..models import Task, TaskUpdate
from typing import List

router = APIRouter(
    prefix="/task",
    tags=["Tasks"],
    responses={404: {"description": "Not found"}},
)


# Endpoint to get all tasks
@router.get("/", response_model=List[Task])
async def get_tasks():
    """
    Get all the tasks.
    Raises:
    - HTTPException 500: If there is an internal server error while fetching the tasks.
    """
    tasks = []
    cursor = tasks_collection.find()
    if cursor:
        for document in cursor:
            tasks.append(Task(**document))
        return tasks
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Error: could not fetch data.",
        )


@router.post("/", response_model=Task)
async def create_task(task_data: Task):
    """
    Create a new task.
    """
    # Convert task_data to dictionary
    task_dict = task_data.dict()
    try:
        # Insert the task data into the MongoDB collection
        inserted_task = tasks_collection.insert_one(task_dict)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error: Task could not be saved in the collection.",
        )
    # Retrieve the inserted task from the database
    inserted_task_document = tasks_collection.find_one(
        {"_id": inserted_task.inserted_id}
    )

    # If task is inserted successfully, return the inserted task
    if inserted_task_document:
        return inserted_task_document
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error: Task could not be created.",
        )


@router.get("/{id}", response_model=Task)
async def get_task(id: str):
    """
    Get a specific task by its ID.
    """
    # Convert the task_id string to an ObjectId
    task_object_id = ObjectId(id)

    # Retrieve the task from the database using its ID
    task_document = tasks_collection.find_one({"_id": task_object_id})

    # If the task is found, return it
    if task_document:
        return task_document
    else:
        # If the task is not found, raise an HTTPException with status code 404 (Not Found)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )


@router.put("/{id}", response_model=Task)
async def update_task(id: str, update_data: TaskUpdate):
    # Check if the task exists
    existing_task = tasks_collection.find_one({"_id": ObjectId(id)})
    if existing_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )

    # Update the task with the provided data
    task = {k: v for k, v in update_data.dict().items() if v is not None}

    if len(task) > 0:

        tasks_collection.update_one({"_id": ObjectId(id)}, {"$set": task})
        updated_task = tasks_collection.find_one({"_id": ObjectId(id)})
        return Task(**updated_task)


@router.delete("/{id}")
async def delete_task(id: str):
    res = tasks_collection.delete_one({"_id": ObjectId(id)})
    if res.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete task with id {id}",
        )
    return "Task was successfully deleted"
