CREATE TABLE IF NOT EXISTS planner (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 task_name TEXT,
 task_description TEXT,
 task_date DATE,
 task_status TEXT DEFAULT 'Не выполнено'
)