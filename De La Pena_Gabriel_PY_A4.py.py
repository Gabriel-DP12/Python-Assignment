while True:
    print("\n--- STUDENT RECORD SYSTEM ---")
    print("[1] Register New Student")
    print("[2] Display All Records")
    print("[3] Terminate Program")
    
    user_choice = input("Select an option (1-3): ").strip()
    
    if user_choice == "1":
        student_name = input("Enter student name: ").strip()
        student_grade = input("Enter student grade: ").strip()
    
        with open("students.txt", "a") as record_file:
            record_file.write(f"{student_name}, {student_grade}\n")
        print("-> Success: Information logged successfully.")
        
    elif user_choice == "2":
        try:
            with open("students.txt", "r") as record_file:
                print("\n--- CURRENT LOGGED RECORDS ---")
                content = record_file.readlines()
                
                if not content:
                    print("The file is currently empty.")
                else:
                    for record in content:
                        print(record.strip())
        except FileNotFoundError:
            print("Notice: No records found yet.")
            
    elif user_choice == "3":
        print("Shutting down the system. Goodbye!")
        break
        
    else:
        print("Alert: Invalid input. Please enter 1, 2, or 3.")