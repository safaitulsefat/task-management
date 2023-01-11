
from datetime import datetime
import uuid

class Task:    
    all_task=[] 

    def __init__(self,task, created_time, updated_time,completed_time, task_done,id) -> None:
        self.task=task
        self.created_time=created_time
        self.updated_time=updated_time
        self.completed_time=completed_time
        self.task_done= task_done
        self.id=id

        
    def update_task(self):

        for i in range(len(self.all_task)):
            if(self.all_task[i]["task_done"]==False):
                print("Task no: ", i+1)
                print("ID: ",self.all_task[i]["id"])
                print("Task name: ",self.all_task[i]["task"])
                print("created time: ",self.all_task[i]["created_time"])
                print("update time: ",self.all_task[i]["updated_time"])
                print("completed: ",self.all_task[i]["task_done"])
                print("completed_time: ",self.all_task[i]["completed_time"])    
                print("\n")

        number =int(input("Select task number to update: "))
        task_name=input("write update task name: ")

        update_task={'task':task_name}
        update_time={'updated_time':str(datetime.now())}

        for i in range(len(self.all_task)):
            if(i+1==number):
                self.all_task[i].update(update_task)
                self.all_task[i].update(update_time)                
                break
        
        
    def complete_task(self):
        for i in range(len(self.all_task)):
            if(self.all_task[i]["task_done"]==False):
                print("Task no: ", i+1)
                print("ID: ",self.all_task[i]["id"])
                print("Task name: ",self.all_task[i]["task"])
                print("created time: ",self.all_task[i]["created_time"])
                print("update time: ",self.all_task[i]["updated_time"])
                print("completed : ",list["task_done"]) 
                print("completed_time: ",self.all_task[i]["completed_time"])   
                print("\n")

        number =int(input("Select which task  to complete: "))

        check_task={'task_done':True}
        update_time={'completed_time': str(datetime.now())}

        
        for i in range(len(self.all_task)):
            if(i+1==number):
                self.all_task[i].update(check_task)
                self.all_task[i].update(update_time)                
                break
    
    




Admin =Task("NA","NA","NA",'NA','NA',"none")

while True:
    print("1. Add new task\n2. Show all task\n3. Show incomplete tasks\n4. Show completed tasks\n5. update task\n6. Mark a task completed\n7. quit")
    n =int(input("Enter option: "))
    if n==1:
        task_name=input("enter new task: ")
        create_time=str(datetime.now())
        unique_id=str(uuid.uuid1())

        Admin.create_task=Task(task_name, create_time, "NA","NA",False,unique_id)
        Admin.all_task.append(vars(Admin.create_task))
        print("Task Created Successfully.")
        print("\n")

    elif n==2:
        print("\nshowing all tasks: \n")
        for list in Admin.all_task:
            print("ID: ",list["id"])
            print("Task name: ",list["task"])
            print("created time: ",list["created_time"])
            print("update time: ",list["updated_time"])
            print("completed : ",list["task_done"])  
            print("completed_time: ",list["completed_time"])  
            print("\n")
    
    elif n==3:
        print("\nshowing incomplete tasks: \n")
        count=0

        for list in Admin.all_task:
            if(list["task_done"]==False):
                print("ID: ",list["id"])
                print("Task name: ",list["task"])
                print("created time: ",list["created_time"])
                print("update time: ",list["updated_time"])
                print("completed : ",list["task_done"]) 
                print("completed_time: ",list["completed_time"])  
                print("\n")
                count=1
        
        if count==0:
                print("No incomplete task\n")
    
    elif n==4:
        print("\nshowing complete tasks: \n")
        count=0
        for list in Admin.all_task:
            if(list["task_done"]==True):
                print("ID: ",list["id"])
                print("Task name: ",list["task"])
                print("created time: ",list["created_time"])
                print("update time: ",list["updated_time"])
                print("completed : ",list["task_done"]) 
                print("completed_time: ",list["completed_time"])   
                print("\n")
                count=1
        if count==0:
                print("No complete task\n")

    elif n==5:
        print("\n")
        print("\nshowing tasks to update: \n")

        count=0

        for list in Admin.all_task:
            if(list["task_done"]==False):
                count=1
        if(count==1):
            Admin.update_task()
        else:
            print("no task to update\n")
        

    elif n==6:
        print("\n")
        print("\nshowing tasks to complete: \n")
        count=0

        for list in Admin.all_task:
            if(list["task_done"]==False):
                count=1
        if(count==1):
            Admin.complete_task()
        else:
            print("no task to complete\n")
    elif n==7:
        break

