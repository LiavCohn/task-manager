from datetime import datetime, timezone
from database import *
from bson import ObjectId

# Sample data for each collection
users_data = [
    {
        "_id": ObjectId("6617fb53f3883743c246e090"),
        "username": "john_doe",
        "email": "john@example.com",
    },
    {
        "_id": ObjectId("6617fb53f3883743c246e091"),
        "username": "jane_smith",
        "email": "jane@example.com",
    },
    {
        "_id": ObjectId("6617fb53f3883743c246e092"),
        "username": "sam_wilson",
        "email": "sam@example.com",
    },
    {
        "_id": ObjectId("6617fb53f3883743c246e093"),
        "username": "kate_perr",
        "email": "katep@example.com",
    },
    {
        "_id": ObjectId("6617fb53f3883743c246e094"),
        "username": "michael_stinson",
        "email": "michaelstinson@example.com",
    },
    {
        "_id": ObjectId("6617fb53f3883743c246e095"),
        "username": "rita_rose",
        "email": "ritarose@example.com",
    },
    # Add more sample users as needed
]

projects_data = [
    {
        "_id": ObjectId("6617fb67f3883743c246e097"),
        "name": "Project A",
        "description": "Developing new feature",
        "owner": ObjectId("6617fb53f3883743c246e090"),
        "creation_date": datetime(2024, 2, 29, 15, 15, 0, tzinfo=timezone.utc),
    },
    {
        "_id": ObjectId("6617fb67f3883743c246e098"),
        "name": "Project B",
        "description": "Designing user interface",
        "owner": ObjectId("6617fb53f3883743c246e091"),
        "creation_date": datetime(2024, 2, 28, 10, 30, 0, tzinfo=timezone.utc),
    },
    {
        "_id": ObjectId("6617fb67f3883743c246e099"),
        "name": "Project C",
        "description": "Testing application",
        "owner": ObjectId("6617fb53f3883743c246e092"),
        "creation_date": datetime(2024, 2, 27, 9, 0, 0, tzinfo=timezone.utc),
    },
    # Add more sample projects as needed
]

tasks_data = [
    {
        "_id": ObjectId("6617fb0df3883743c246e08b"),
        "project_id": ObjectId("6617fb67f3883743c246e097"),
        "name": "Implement authentication",
        "description": "Implement authentication system using JWT",
        "assigned_users": [
            ObjectId("6617fb53f3883743c246e090"),
            ObjectId("6617fb53f3883743c246e091"),
        ],
        "due_date": datetime(2024, 3, 10, 12, 0, 0, tzinfo=timezone.utc),
        "status": "open",
    },
    {
        "_id": ObjectId("6617fb0df3883743c246e08c"),
        "project_id": ObjectId("6617fb67f3883743c246e098"),
        "name": "Create wireframes",
        "description": "Create wireframes for main screens",
        "assigned_users": [ObjectId("6617fb53f3883743c246e090")],
        "due_date": datetime(2024, 3, 8, 12, 0, 0, tzinfo=timezone.utc),
        "status": "in_progress",
    },
    {
        "_id": ObjectId("6617fb0df3883743c246e08d"),
        "project_id": ObjectId("6617fb67f3883743c246e099"),
        "name": "Write test cases",
        "description": "Write test cases for critical functionalities",
        "assigned_users": [
            ObjectId("6617fb53f3883743c246e091"),
            ObjectId("6617fb53f3883743c246e092"),
        ],
        "due_date": datetime(2024, 3, 6, 12, 0, 0, tzinfo=timezone.utc),
        "status": "completed",
    },
    {
        "_id": ObjectId("6617fb0df3883743c246e08e"),
        "project_id": ObjectId("6617fb67f3883743c246e098"),
        "name": "Create the home page",
        "description": "Create basic home page with a header and a gallery",
        "assigned_users": [
            ObjectId("6617fb53f3883743c246e093"),
            ObjectId("6617fb53f3883743c246e095"),
        ],
        "due_date": datetime(2024, 4, 2, 10, 15, 0, tzinfo=timezone.utc),
        "status": "open",
    },
]

comments_data = [
    {
        "_id": ObjectId("6617fb8ff3883743c246e09b"),
        "task_id": ObjectId("6617fb0df3883743c246e08b"),
        "commenter": ObjectId("6617fb53f3883743c246e090"),
        "text": "This is a great task! not...",
        "timestamp": datetime(2024, 3, 1, 10, 0, 0, tzinfo=timezone.utc),
    },
    {
        "_id": ObjectId("6617fb8ff3883743c246e09c"),
        "task_id": ObjectId("6617fb0df3883743c246e08c"),
        "commenter": ObjectId("6617fb53f3883743c246e090"),
        "text": "I've started working on it.",
        "timestamp": datetime(2024, 3, 2, 9, 30, 0, tzinfo=timezone.utc),
    },
    {
        "_id": ObjectId("6617fb8ff3883743c246e09d"),
        "task_id": ObjectId("6617fb0df3883743c246e08d"),
        "commenter": ObjectId("6617fb53f3883743c246e092"),
        "text": "All test cases passed successfully.",
        "timestamp": datetime(2024, 3, 3, 11, 0, 0, tzinfo=timezone.utc),
    },
    {
        "_id": ObjectId("6617fb8ff3883743c246e09e"),
        "task_id": ObjectId("6617fb0df3883743c246e08e"),
        "commenter": ObjectId("6617fb53f3883743c246e095"),
        "text": "On it",
        "timestamp": datetime(2024, 4, 3, 11, 0, 0, tzinfo=timezone.utc),
    },
    # Add more sample comments as needed
]

attachments_data = [
    {
        "task_id": ObjectId("6617fb0df3883743c246e08b"),
        "uploader": ObjectId("6617fb53f3883743c246e090"),
        "file_name": "Design.pdf",
        "file_url": "https://example.com/design.pdf",
        "file_type": "pdf",
        "timestamp": datetime(2024, 3, 1, 14, 0, 0, tzinfo=timezone.utc),
    },
    {
        "task_id": ObjectId("6617fb0df3883743c246e08c"),
        "uploader": ObjectId("6617fb53f3883743c246e091"),
        "file_name": "Screenshot.png",
        "file_url": "https://example.com/screenshot.png",
        "file_type": "image",
        "timestamp": datetime(2024, 3, 2, 15, 0, 0, tzinfo=timezone.utc),
    },
    {
        "task_id": ObjectId("6617fb0df3883743c246e08d"),
        "uploader": ObjectId("6617fb53f3883743c246e092"),
        "file_name": "Report.docx",
        "file_url": "https://example.com/report.docx",
        "file_type": "docx",
        "timestamp": datetime(2024, 3, 3, 16, 0, 0, tzinfo=timezone.utc),
    },
    # Add more sample attachments as needed
]
tasks_collection.insert_many(tasks_data)
projects_collection.insert_many(projects_data)
attachments_collection.insert_many(attachments_data)
users_collection.insert_many(users_data)
comments_collection.insert_many(comments_data)
