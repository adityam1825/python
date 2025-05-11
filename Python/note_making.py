import os 

def menu():
    print("\n notes taking application ")
    print(" 1.view notes ")
    print(" 2.add note ")
    print(" 3.delete note ")
    print(" 4.exit ")
    

def add_note():
    note_title = input("enter the title of the note  :  ")
    note_content = input("enter the content of the note  :  ")

    notes_dir='notes'
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)

    note_path = os.path.join(notes_dir, f"{note_title}.txt")
    with open(note_path, 'a')as file:
        file.write(f"{note_content}\n")
    print(f"note {note_title} added succesfully")    

def view_notes():
    print("\n existing notes :  ")
    notes_dir='notes'
    if not os.path.exists(notes_dir):
        print(" no notes available ")
        return
    for filename in os.listdir(notes_dir):
        with open(os.path.join(notes_dir, filename), 'r')as file:
            content = file.read()
            print(f"{filename[:-4]}:{content}")


def delete_note():
    note_title= input (" enter the note to be deleted : ")
    notes_dir='notes'
    note_path = os.path.join(notes_dir,f"{note_title}.txt") 

    if os.path.exists(note_path):
        os.remove(note_path)
        print("note '{note_title} ' deleted successfully")        
    else:
        print("note '{note_title} not found")

def main():
    while True :
        menu()
        choice = input("enter your choice(1-4):  ")
        if choice == '1' :
            view_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("exiting the note taking app., bubbyee ")
            break
        else:
            print("invalid choice pls enter number between 1-4 ")

if __name__ == "__main__":
    main()