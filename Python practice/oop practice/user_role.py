class User:
    def __init__(self,name:str):
        self.name=name

    
    def show_info(self):
        print(f"name:{self.name}")


class Admin(User):

    def manage_users(self):
       print("use manage_users()")


class SuperAdmin(Admin):

    def delete_system(self):
        print("use delete_system()")

if __name__=="__main__":
    super_obj=SuperAdmin("helo")
    super_obj.show_info()
    super_obj.manage_users()
    super_obj.delete_system()
    