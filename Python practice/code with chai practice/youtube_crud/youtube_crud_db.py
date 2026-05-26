import sqlite3
from contextlib import contextmanager
class YoutubeRepository:
  def __init__(self,db_name:str="youtube.db"):
    self.db_name =db_name
    self.create_table()
  @contextmanager
  def _connect(self):
   con=sqlite3.connect(self.db_name)
   cur=con.cursor()
   try:
     yield cur
     con.commit()
   except Exception as e :
    con.rollback()
    print("error",str(e))
   finally:
    con.close()

  def create_table(self):
   with self._connect() as cur:
    cur.execute("""CREATE TABLE videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    duration TEXT NOT NULL
    )
    """)
  def add_data(self,name:str, duration:str):
    with self._connect() as cursor:
     cursor.execute("INSERT INTO videos(name,duration) VALUES(?,?)",(name,duration))
     print("data added successfully")

  def update_data(self,id:int,name:str,duration:str):
   with self._connect() as cursor:
    cursor.execute("UPDATE videos SET name=?,duration=? WHERE id =?",(name, duration, id))
    print("update data successfully")

  def delete_data(self,id:int):
   with self._connect() as cursor:
    cursor.execute("DELETE FROM videos WHERE id=?",(id,))
    print("data deleted successfully")

  def fetch_data(self):
   with self._connect() as cursor:
    cursor.execute("SELECT * FROM videos")
    data= cursor.fetchall()
    print("\n")
    print("Table videos")
    for d in data:
     print(f"ID:{d[0]}, NAME:{d[1]}, DURATION:{d[2]}") 
    print("\n")


def main():
 yt_obj=YoutubeRepository()  
 while True:
  print("\nYoutube Crud Menu")
  print("1.get data")
  print("2.Add data")
  print("3.update data")
  print("4.delete data")
  print("5.Exit")
  print("*"*20)
  
  choice=int(input("Enter the choice_number:"))
  match(choice):
   case 1:
    data=yt_obj.fetch_data()
   
   case 2:
     name=input("Enter the video name:")
     duration=input("Enter the video duration:")
     yt_obj.add_data(name,duration)
     yt_obj.fetch_data()

   case 3:
    id=int(input("Enter the id:"))
    new_name=input("Enter the video new_name:")
    new_duration=input("Enter the duration:")
    yt_obj.update_data(id,new_name,new_duration)
   case 4:
    id=int(input("Enter the id:"))
    yt_obj.delete_data(id)
   case 5:
    break

   case _:
    print("Invalid choice\n")

     



if __name__=="__main__":
  main()


