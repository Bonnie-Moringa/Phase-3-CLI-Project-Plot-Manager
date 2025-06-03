from models.model_1 import (
    init_db,
    add_agent, get_all_agents, delete_agent,
    add_property, get_properties,
    add_client, get_clients,
    get_agent_by_id
)

def display_menu():
    print("\n====== Real Estate Management System ======")
    print("1. Add Agent")
    print("2. View All Agents")
    print("3. Delete Agent")
    print("4. Add Property")
    print("5. View All Properties")
    print("6. Add Client")
    print("7. View All Clients")
    print("8. Exit")

def add_agent_menu():
    name = input("Enter agent name: ")
    number = input("Enter agent number: ")
    email = input("Enter agent email: ")
    phone = input("Enter agent phone number: ")
    add_agent(name, number, email, phone)
    print("✅ Agent added successfully!")

def view_agents_menu():
    agents = get_all_agents()
    if not agents:
        print("No agents found.")
        return
    print("\n-- Agents --")
    for agent in agents:
        print(f"ID: {agent[0]}, Name: {agent[1]}, Number: {agent[2]}, Email: {agent[3]}, Phone: {agent[4]}")

def delete_agent_menu():
    view_agents_menu()
    try:
        agent_id = int(input("Enter Agent ID to delete: "))
        if get_agent_by_id(agent_id):
            delete_agent(agent_id)
            print("✅ Agent deleted successfully.")
        else:
            print("❌ Agent not found.")
    except ValueError:
        print("❌ Invalid input.")

def add_property_menu():
    name = input("Enter property name: ")
    status = input("Enter property status (available/sold): ")
    view_agents_menu()
    try:
        agent_id = int(input("Enter agent ID for this property: "))
        if get_agent_by_id(agent_id):
            add_property(name, status, agent_id)
            print("✅ Property added successfully!")
        else:
            print("❌ Agent not found.")
    except ValueError:
        print("❌ Invalid agent ID.")

def view_properties_menu():
    properties = get_properties()
    if not properties:
        print("No properties found.")
        return
    print("\n-- Properties --")
    for name, status, agent_name in properties:
        print(f"Name: {name}, Status: {status}, Agent: {agent_name}")

def add_client_menu():
    name = input("Enter client name: ")
    email = input("Enter client email: ")
    phone = input("Enter client phone number: ")
    view_agents_menu()
    try:
        agent_id = int(input("Enter agent ID for this client: "))
        if not get_agent_by_id(agent_id):
            print("❌ Agent not found.")
            return
    except ValueError:
        print("❌ Invalid agent ID.")
        return

    view_properties_menu()
    try:
        property_id = int(input("Enter property ID for this client: "))
    except ValueError:
        print("❌ Invalid property ID.")
        return

    add_client(name, email, phone, agent_id, property_id)
    print("✅ Client added successfully!")

def view_clients_menu():
    clients = get_clients()
    if not clients:
        print("No clients found.")
        return
    print("\n-- Clients --")
    for name, email, phone, agent_name, property_name in clients:
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Agent: {agent_name}, Property: {property_name}")

def main():
    init_db()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_agent_menu()
        elif choice == "2":
            view_agents_menu()
        elif choice == "3":
            delete_agent_menu()
        elif choice == "4":
            add_property_menu()
        elif choice == "5":
            view_properties_menu()
        elif choice == "6":
            add_client_menu()
        elif choice == "7":
            view_clients_menu()
        elif choice == "8":
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
