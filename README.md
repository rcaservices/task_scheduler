# Project Scheduler

## Overview
The Project Scheduler is a Python script designed to assist developers in planning and budgeting their projects. By identifying tasks, determining their durations, and mapping dependencies between them, developers can create a comprehensive project schedule. This tool utilizes networkx and pandas libraries to generate a Directed Acyclic Graph (DAG) representing the project's tasks and dependencies, and then produces a schedule matrix in Excel format.

## Features
- **Task Definition**: Define project tasks with associated durations and dependencies.
- **Dependency Management**: Specify dependencies between tasks to ensure accurate sequencing.
- **Schedule Generation**: Automatically generate a project schedule matrix based on task durations and dependencies.
- **Customization**: Easily customize the duration marker used in the schedule matrix.

## Getting Started
1. Clone this repository to your local machine.
2. Install the required dependencies:
    ```
    pip install networkx pandas openpyxl
    ```
3. Modify the `tasks` dictionary in the `scheduler.py` script to define your project tasks, durations, and dependencies.
4. Run the `scheduler.py` script to generate the project schedule matrix in Excel format.

## Usage
### Defining Tasks
Edit the `tasks` dictionary in the `scheduler.py` script to define your project tasks. Each task should have a unique name, a duration (in days), and a list of dependencies (tasks that must be completed before the task can start).

```python
tasks = {
    'Task 1': {'duration': 5, 'dependencies': []},
    'Task 2': {'duration': 3, 'dependencies': ['Task 1']},
    'Task 3': {'duration': 4, 'dependencies': ['Task 1']},
    'Task 4': {'duration': 2, 'dependencies': ['Task 2', 'Task 3']},
    'Task 5': {'duration': 6, 'dependencies': ['Task 4']}
}
```

### Customization
You can customize the duration marker used in the schedule matrix by modifying the `duration_marker` variable in the `scheduler.py` script.

```python
# Define marker for the cell indicating the duration
duration_marker = '&'
```

### Generating Schedule
Run the `scheduler.py` script to generate the project schedule matrix in Excel format. The output will be saved as `scheduler.xlsx` in the current directory.

```bash
python scheduler.py
```

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [Apache License](LICENSE).

---
Feel free to customize this README as needed for your project. If you have any questions or need further assistance, please don't hesitate to reach out!

