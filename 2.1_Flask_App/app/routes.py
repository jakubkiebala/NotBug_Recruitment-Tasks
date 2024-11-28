from flask import redirect, render_template, request, url_for
from .models import (add_list, add_task, delete_list, get_list, get_task, get_tasks, delete_task, update_list,
                      update_task, get_lists)

def register_routes(app):

    @app.route('/', methods=['GET'])
    def home():

        return render_template('home.html')
    

    @app.route('/tasks', methods=['GET'])
    def tasks():

        tasks_list = get_tasks()
        return render_template('tasks_menu.html', tasks_list=tasks_list)
    

    @app.route('/task_add', methods=['GET', 'POST'])
    def task_add():

        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            add_task(name, description)
            return redirect(url_for('tasks'))

        else:
            return render_template('tasks_add.html')


    @app.route('/task_update/<int:task_id>', methods=['GET', 'POST'])
    def task_update(task_id):

        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            update_task(task_id, name, description)
            return redirect(url_for('tasks'))

        else:
            task = get_task(task_id)
            return render_template('task_update.html', task=task)

    @app.route('/task_delete/<int:task_id>', methods=['GET', 'POST'])
    def task_delete(task_id):

        if request.method == 'POST':
            delete_task(task_id)
            return redirect(url_for('tasks'))
        else:
            task = get_task(task_id)
            return render_template('task_delete.html', task=task)
            
    
    @app.route('/lists', methods=['GET'])
    def lists():
        lists_list = get_lists()
        return render_template('lists_menu.html', lists_list=lists_list)
    

    @app.route('/list_add', methods=['GET', 'POST'])
    def list_add():
        if request.method == 'POST':
            name = request.form['name']
            add_list(name)
            return redirect(url_for('lists'))

        else:
            return render_template('list_add.html')
        
    
    @app.route('/list_update/<int:list_id>', methods=['GET', 'POST'])
    def list_update(list_id):

        if request.method == 'POST':
            name = request.form['name']
            update_list(list_id, name)
            return redirect(url_for('lists'))
    
        else:
            list = get_list(list_id)
            return render_template('list_update.html', list=list)    
        
    
    @app.route('/list_delete/<int:list_id>', methods=['GET', 'POST'])
    def list_delete(list_id):

        if request.method == 'POST':
                delete_list(list_id)
                return redirect(url_for('lists'))
        else:
            list = get_list(list_id)
            return render_template('list_delete.html', list=list)

