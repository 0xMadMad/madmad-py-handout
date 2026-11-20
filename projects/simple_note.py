import os

file = "note.txt"

while True:
    print("\n===MENU===")
    print("1.write a note")
    print("2.read note")
    print("3.delete all notes")
    print("4.exit")
    choice = input("choose: ")

    if choice == "1":
        note = input("write your note: ")
        with open(file, "a") as f:
            f.write(" " + note + "\n")
        print("note saved.")

    elif choice == "2":
        if os.path.exists(file):
            with open(file, "r") as f:
                notes = f.read()
            if notes:
                print("\n===Your Notes===")
                print(notes)
            else:
                print("no notes found.")
        else:
            print("no notes found.")

    elif choice == "3":
        if os.path.exists(file):
            open(file, "w").close()
            print("all notes deleted.")
        else:
            print("no notes to delete.")

    elif choice == "4":
        break

    else:
        print("invalid choice!")
#MadMad_43