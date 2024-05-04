import networkx as nx
import pandas as pd

# Define tasks with durations and dependencies
tasks = {
    'Task 1': {'duration': 5, 'dependencies': []},
    'Task 2': {'duration': 3, 'dependencies': ['Task 1']},
    'Task 3': {'duration': 4, 'dependencies': ['Task 1']},
    'Task 4': {'duration': 2, 'dependencies': ['Task 2', 'Task 3']},
    'Task 5': {'duration': 6, 'dependencies': ['Task 4']}
}

# Define marker for the cell indicating the duration
duration_marker = '&'

# Create Directed Acyclic Graph (DAG)
G = nx.DiGraph()

# Add nodes (tasks) to the graph
for task, info in tasks.items():
    G.add_node(task, duration=info['duration'])

# Add edges (dependencies) to the graph
for task, info in tasks.items():
    for dependency in info['dependencies']:
        G.add_edge(dependency, task)

# Calculate start and end times for each task considering dependencies
start_times = {}
for node in nx.topological_sort(G):
    duration = G.nodes[node]['duration']
    predecessors = list(G.predecessors(node))
    if len(predecessors) == 0:
        start_times[node] = 0
    else:
        start_times[node] = max([start_times[pred] + G.nodes[pred]['duration'] for pred in predecessors])

# Create matrix for task schedule
max_time = max(start_times.values()) + max(tasks.values(), key=lambda x: x['duration'])['duration']
total_dependent_days = max([start_times[node] + G.nodes[node]['duration'] for node in G.nodes])
task_schedule = [['' for _ in range(max_time)] for _ in range(len(tasks))]

# Fill in task names in the first column
for idx, task in enumerate(tasks.keys()):
    task_schedule[idx][0] = task

# Fill in asterisks in subsequent columns
for task, start_time in start_times.items():
    duration = tasks[task]['duration']
    for day in range(1, duration + 1):
        if start_time + day < max_time:
            task_schedule[list(tasks.keys()).index(task)][start_time + day] = duration_marker

# Add header row
header_row = ['Name']
for day in range(1, total_dependent_days + 1):
    header_row.append(day)
task_schedule.insert(0, header_row)

# Output schedule matrix to Excel
excel_file = 'scheduler.xlsx'
sheet_name = 'Schedule_Matrix'

with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    sheet = writer.book.create_sheet(title=sheet_name)
    for row in task_schedule:
        sheet.append(row)

print("Scheduler Matrix has been exported to Excel successfully!")
