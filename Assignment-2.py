def record(userType: str, input_no: int, id_counters: dict):

    info_list = []

    for i in range(input_no):
        info = {}

        print(f"\nPlease add a {userType}'s info. Kindly enter 'stop' to terminate.")
        key = input(f'Enter first key: ')

        if key != "":
            while key != "stop":
                value = input(f"Enter {userType}'s information for this field ->{key}: ")
                info[key] = value
                key = input(f'Enter another key: ')
            info["id"] = f"{userType}_{id_counters[userType]}"
            id_counters[userType] += 1

        if userType == 'HR' or userType == 'Teacher':
            salary = int(input('Enter salary: '))
            info["Salary"] = salary
            info["Dept"] = userType

        if userType == 'Student':
            std_class = int(input('Enter class: '))
            fathername = str(input("Enter Father's name: "))
            info["Class"] = std_class
            info["Fathers_name"] = fathername

        if userType == 'Student' or userType == 'Teacher':
            total_subject_no = int(input('Enter total subject no: '))
            subject_list = [input('Enter subject name: ') for _ in range(total_subject_no)]
            info["Subjects"] = subject_list

        if userType == 'Teacher':
            total_class_no = int(input('Enter total class no: '))
            class_list = [input('Enter class name: ') for _ in range(total_class_no)]
            info["Classes"] = class_list

        info_list.append(info)

    return info_list

# Task - make it dynamic
user_types = ["Student", "HR", "Teacher"]

all_records = {}  # Dictionary to store records for each user type

for userType in user_types:
    input_no = int(input(f"How many {userType}'s info you want to record? : "))
    # Initialize specific ID counters for each user type
    id_counters = {"Student": 101, "HR": 201, "Teacher": 301}
    # Calling record function for each user type
    record_list = record(userType, input_no, id_counters)
    # Store the records in the dictionary
    all_records[userType] = record_list

# Display the output with generated IDs for each user type
print("All User Type Records:")
print(all_records)
