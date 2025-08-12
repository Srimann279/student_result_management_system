import database

# Create the database tables (only runs once, no harm in repeating)
database.create_tables()

def menu():
    while True:
        print("\n--- Student Result Management ---")
        print("1. Add Student")
        print("2. Add Result")
        print("3. View Result")
        print("4. Exit") 

        choice = input("Enter choice: ")

        if choice == "1":
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")
            database.add_student(roll_no, name, course)
            print("✅ Student added successfully!")

        elif choice == "2":
            roll_no = input("Enter Roll No: ")
            subject = input("Enter Subject: ")
            marks = float(input("Enter Marks: "))
            database.add_result(roll_no, subject, marks)
            print("✅ Result added successfully!")

        elif choice == "3":
            roll_no = input("Enter Roll No to view results: ")
            results = database.get_results(roll_no)
            if results:
                print("\nResults for Roll No:", roll_no)
                for r in results:
                    print(f"Name: {r[1]}, Course: {r[2]}, Subject: {r[3]}, Marks: {r[4]}")
            else:
                print("❌ No results found.")

        elif choice == "4":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice! Try again.")

# This line makes the menu run when you start the script
if __name__ == "__main__":
    menu() 
