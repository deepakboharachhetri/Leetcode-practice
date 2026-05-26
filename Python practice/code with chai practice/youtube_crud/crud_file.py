import json

file_name='youtube.txt'
def add_video(videos):
    name=input("Enter the video name:")
    duration=input("Enter the video duration:")
    videos.append({'name':name,'duration':duration})
    save_video(videos)

def save_video(videos):
    with open(file_name,'w') as file:
        json.dump(videos,file)

def update_vidoe(videos):
    list_all_videos(videos)
    index=int(input("Enter a index number:"))
    if 1<=index<=len(videos):
        name=input("\nEnter new name:")
        duration=input("\nEnter new duration:")
        videos[index-1]={'name':name,'duration':duration}
        save_video(videos)
    else:
        print('Invalid index')



def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter a index number:"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_video(videos)
    else:
        print('Invalid index')   
    
def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index}:{video['name']} {video['duration']}")

def load_video():
    try:
        with open(file_name,'r') as file:
            return json.load(file)
    except FileNotFoundError :
        return []    

def main():
    videos=load_video()
    while True:
        print("video",videos)   
        print("*"*30)
        print("Youtube | Crud file ")   
        print("1.List all videos")
        print("2.add video")
        print("3.update video")
        print("4.delete video")
        print("5.Exit")
        print("*"*30)

        choice=input("\nEnter the  choice:")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)

            case '3':
                update_vidoe(videos)
            
            case '4':
                delete_video(videos)
            
            case '5':
                break

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()