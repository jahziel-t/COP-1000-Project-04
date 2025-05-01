# Define the list of allowed vehicles
AllowedVehiclesList = [
    'Ford F-150', 
    'Chevrolet Silverado', 
    'Tesla CyberTruck', 
    'Toyota Tundra', 
    'Nissan Titan',
    'Rivian R1T',
    'Ram 1500',
]

# Function to print all allowed vehicles
def print_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
    print("\n********************************")
# Function to search for a specific vehicle
def search_vehicle():
    search_term = input("\nPlease Enter the full Vehicle name: ").strip()
    found = False

    for vehicle in AllowedVehiclesList:
        if search_term.lower() == vehicle.lower():
            print(f"\n✔ '{vehicle}' is an authorized vehicle.")
            found = True
            break

    if not found:
        print(f"\n✘ '{search_term}' is not an authorized vehicle, "
              "if you received this in error please check the spelling "
              "and try again.")

    print("\n********************************")
# Function to add a new vehicle to the list (if not already present)
def add_vehicle():
    new_vehicle = input(
        "\nPlease Enter the full Vehicle name you would like to add: "
    ).strip()

    for vehicle in AllowedVehiclesList:
        if new_vehicle.lower() == vehicle.lower():
            print(f"\n⚠ '{new_vehicle}' is already in the list of authorized vehicles.")
            print("\n********************************")
            return

    AllowedVehiclesList.append(new_vehicle)
    print(f"\n✔ 'You have added {new_vehicle}' as an authorized vehicle.")
# Function to delete a vehicle from the list
def delete_vehicle():
    remove_vehicle = input(
        "\nPlease Enter the full Vehicle name you would like to REMOVE: "
    ).strip()

    for vehicle in AllowedVehiclesList:
        if remove_vehicle.lower() == vehicle.lower():
            confirmation = (
                input(
                    f'\nAre you sure you want to remove "{vehicle}" '
                    f'from the Authorized Vehicles List?: '
                )
                .strip()
                .lower()
            )
            if confirmation == 'yes':
                AllowedVehiclesList.remove(vehicle)
                print(f'\n✔ You have REMOVED "{vehicle}" as an authorized vehicle.')
            else:
                return  # Indented to be part of the else block
# Function to display the menu
def display_menu():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.4")
    print("********************************")
    print("Please Enter the following number below from the following menu:\n")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicles")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

# Main function to handle the menu selection and program flow
def main():
    while True:
        display_menu()
        
        # Get user input for menu choice
        try:
            choice = int(input("Enter your choice (1, 2, 3, 4, or 5.): "))
            if choice == 1:
                print_vehicles()
            elif choice == 2:  # Correct indentation for the elif block
                search_vehicle()
            elif choice == 3: 
                add_vehicle()
            elif choice == 4:
                delete_vehicle()
            elif choice == 5:
                print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
                break  # Exit the loop and end the program                    
            else:
                print("Invalid choice, please enter 1, 2, 3, 4, or 5.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the program
if __name__ == "__main__":
    main()
