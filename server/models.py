from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Field
import uuid
from typing import Annotated, Optional, List
from datetime import datetime


class User(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    username: str
    email: str


class Project(BaseModel):
    id: int = Field(alias="_id")
    name: str
    description: str
    owner: int  # User ID
    creation_date: datetime


class TaskStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "completed"


class ObjectIdStr(str):
    # Custom type to represent ObjectId as a string

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, (str, ObjectId)):
            raise ValueError("ObjectIdStr must be a string or ObjectId")
        if isinstance(v, ObjectId):
            return str(v)
        return v


class Task(BaseModel):
    # id: Optional[ObjectIdStr] = Field(alias="_id")
    project_id: ObjectIdStr
    name: str
    description: str
    assigned_users: Optional[List[ObjectIdStr]]
    due_date: datetime
    status: TaskStatus

    class Config:
        allow_population_by_field_name = True


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    assigned_users: Optional[List[ObjectIdStr]] = None
    due_date: Optional[datetime] = None
    status: Optional[str] = None


class Comment(BaseModel):
    id: int = Field(alias="_id")
    task_id: Optional[int]  # Task ID
    project_id: Optional[int]  # Project ID
    commenter: int  # User ID
    text: str
    timestamp: datetime


class Attachment(BaseModel):
    id: int = Field(alias="_id")
    task_id: Optional[int]  # Task ID
    project_id: Optional[int]  # Project ID
    uploader: int  # User ID
    file_name: str
    file_url: str
    file_type: str
    timestamp: datetime
