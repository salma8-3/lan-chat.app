# Task Manager API

A simple Task Manager REST API built using FastAPI.  
This project provides CRUD operations to manage daily tasks.

## Technologies Used

- Python
- FastAPI
- Uvicorn

## Features

- Create a new task
- Retrieve all tasks
- Retrieve a specific task by ID
- Update an existing task
- Delete a task
- Automatic task ID generation
- Automatic creation timestamp

## Data Model

Each task contains:

- id: Unique identifier
- title: Task title (required)
- description: Task details (optional)
- status: Task status (pending/completed)
- created_at: Creation timestamp

## Installation

1. Clone the repository:

`bash
git clone YOUR_REPOSITORY_LINK
