from .config import connect_to_db

def add_task(name, description):
    query = f"""
    INSERT INTO tasks (name, description) VALUES (
    '{name}', '{description}')
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def get_tasks():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
    

def get_task(task_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM tasks where id='{task_id}'"
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def update_task(task_id, name, description):
    query = f"""
    UPDATE tasks 
    set name ='{name}',
        description = '{description}'
    WHERE id='{task_id}'
    """
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def delete_task(task_id):
    query = f"""
    delete from tasks
    WHERE id='{task_id}'
    """
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def get_lists():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM lists"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_list(list_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM lists where id='{list_id}'"
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def add_list(name):
    query = f"""
    INSERT INTO lists (name) VALUES (
    '{name}')
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def update_list(list_id, name):
    query = f"""
    UPDATE lists
        set name ='{name}'
    WHERE id='{list_id}'
    """
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def delete_list(list_id):
    query = f"""
    delete from lists
    WHERE id='{list_id}'
    """
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
