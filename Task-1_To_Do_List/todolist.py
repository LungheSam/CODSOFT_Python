

class ToDoList:
    def __init__(self):
        self.tasking=[]
    def show_menu(self):
        print("Menu:")
        print("-"*50)
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
    def add_task(self):
        task=input("Enter task:")
        self.tasking.append({"task":task,"completed":False})
    def show_tasks(self):
        print("-"*10+'TASKS'+'-'*10)
        for i,task in enumerate(self.tasking):
            status=self.tasking[i]["completed"]
            status="Completed" if self.tasking[i]["completed"]==True else "Not Completed"
            print(f"{i+1}. {task['task']} -- {status}")
        print('-'*50)
    def mark_task_completed(self):
        ToDoList.show_tasks(self)
        index=int(input("Enter the number of the task to be mark completed:"))
        index=index-1
        if index <len(self.tasking):
            self.tasking[index]['completed']=True
            print("Task marked completed successfully...")
        else:
            print("Invalid Task")
    def delete_tasks(self):
        ToDoList.show_tasks(self)
        if self.tasking is []:
            return None
        index=int(input("Enter the number of the task to be deleted:"))
        index=index-1
        if index <len(self.tasking):
            # tasking[index]['completed']=True
            del self.tasking[index]
            print("Task Deleted successfully...")
        else:
            print("Invalid Input Task")



def main():           
    todo=ToDoList()
    print("-"*50)
    print("="*15+"TO DO LIST"+"="*15)
    print("-"*50)
    while True:
        todo.show_menu()
        choice=int(input("Enter Your Choice:"))
        match choice:
            case 1:
                todo.add_task()
            case 2:
                todo.show_tasks()
            case 3:
                todo.mark_task_completed()
            case 4:
                todo.delete_tasks()
            case 5:
                break

main()

