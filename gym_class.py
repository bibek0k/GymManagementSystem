# Gym Management System

class GymMember:
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self.weight = weight  # in kilograms
        self.height = height  # in meters

class GymManagementSystem:
    def __init__(self):
        self.members = []

    def add_member(self):
        """Add a gym member with input validation."""
        name = input("Enter member's name: ").strip()
        if not name:
            print("Name cannot be empty. Try again.")
            return

        while True:
            try:
                age = int(input("Enter age: "))
                if age <= 0:
                    print("Age must be a positive number. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric age.")

        while True:
            try:
                weight = float(input("Enter body weight (kg): "))
                if weight <= 0:
                    print("Weight must be a positive number. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric weight.")

        while True:
            try:
                height = float(input("Enter height (meters): "))
                if height <= 0:
                    print("Height must be a positive number. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric height.")

        new_member = GymMember(name, age, weight, height)
        self.members.append(new_member)
        print("Member successfully added!")

    def view_member(self):
        """View all members or a specific one."""
        if not self.members:
            print("No members found.")
            return

        view_type = input("View all members or one? (all/one): ").lower()
        if view_type == "all":
            for member in self.members:
                print(f"Name: {member.name}\nAge: {member.age}\nWeight: {member.weight} kg\nHeight: {member.height} m\n")
        elif view_type == "one":
            name = input("Enter the member's name: ").strip()
            found = False
            for member in self.members:
                if member.name == name:
                    print(f"Name: {member.name}\nAge: {member.age}\nWeight: {member.weight} kg\nHeight: {member.height} m\n")
                    found = True
                    break
            if not found:
                print("Member not found.")
        else:
            print("Invalid option. Please enter 'all' or 'one'.")

    def delete_member(self):
        """Delete a member by name."""
        name = input("Enter the member's name to delete: ").strip()
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                print("Member successfully deleted!")
                return
        print("Member not found.")

    def update_member(self):
        """Update specific fields of a member with validation."""
        name = input("Enter the member's name to update: ").strip()
        for member in self.members:
            if member.name == name:
                print(f"Current details - Name: {member.name}, Age: {member.age}, Weight: {member.weight} kg, Height: {member.height} m")
                print("Enter field to update (name/age/weight/height) or 'done' to finish:")

                while True:
                    field = input("Field: ").lower()
                    if field == "done":
                        break
                    if field not in ["name", "age", "weight", "height"]:
                        print("Invalid field. Choose: name, age, weight, height.")
                        continue

                    if field == "name":
                        new_name = input("Enter new name: ").strip()
                        if not new_name:
                            print("Name cannot be empty. Try again.")
                            continue
                        member.name = new_name
                        print("Name updated.")
                    elif field == "age":
                        while True:
                            try:
                                age = int(input("Enter new age: "))
                                if age <= 0:
                                    print("Age must be positive. Try again.")
                                    continue
                                member.age = age
                                print("Age updated.")
                                break
                            except ValueError:
                                print("Invalid input. Enter a numeric age.")
                    elif field == "weight":
                        while True:
                            try:
                                weight = float(input("Enter new weight (kg): "))
                                if weight <= 0:
                                    print("Weight must be positive. Try again.")
                                    continue
                                member.weight = weight
                                print("Weight updated.")
                                break
                            except ValueError:
                                print("Invalid input. Enter a numeric weight.")
                    elif field == "height":
                        while True:
                            try:
                                height = float(input("Enter new height (meters): "))
                                if height <= 0:
                                    print("Height must be positive. Try again.")
                                    continue
                                member.height = height
                                print("Height updated.")
                                break
                            except ValueError:
                                print("Invalid input. Enter a numeric height.")

                print("Update complete.")
                return
        print("Member not found.")


print("Welcome to Gym Management System")
gym = GymManagementSystem()

while True:
    print("\n1. Add member")
    print("2. Delete member")
    print("3. Update member")
    print("4. View member")
    print("5. Exit The System")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            gym.add_member()
        elif choice == 2:
            gym.delete_member()
        elif choice == 3:
            gym.update_member()
        elif choice == 4:
            gym.view_member()
        elif choice == 5:
            print("Exiting the system. See you at the gym!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a numeric choice.")