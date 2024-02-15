tickets = []

def create_ticket():
    customer_name = input("Enter customer name: ")
    issue_description = input("Enter issue description: ")
    
    ticket = {
        "customer_name": customer_name,
        "issue_description": issue_description,
        "status": "Open"
    }
    
    tickets.append(ticket)
    print("Ticket created successfully!\n")

def view_tickets():
    if not tickets:
        print("No tickets found.\n")
    else:
        print("Tickets:")
        for i, ticket in enumerate(tickets, 1):
            print(f"{i}. Customer: {ticket['customer_name']}, Status: {ticket['status']}")
        print()

def update_ticket_status(index, new_status):
    tickets[index]['status'] = new_status
    print(f"Ticket status updated to {new_status} successfully!\n")

def view_ticket_details(index):
    ticket = tickets[index]
    print(f"\nTicket Details for {ticket['customer_name']}:")
    print(f"Issue Description: {ticket['issue_description']}")
    print(f"Status: {ticket['status']}\n")

def main():
    while True:
        print("Customer Support Ticket System")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Ticket Status")
        print("4. View Ticket Details")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            create_ticket()
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            view_tickets()
            if tickets:
                ticket_index = int(input("Enter the ticket number to update status: ")) - 1
                if 0 <= ticket_index < len(tickets):
                    new_status = input("Enter the new status (Open/In Progress/Closed): ")
                    update_ticket_status(ticket_index, new_status)
                else:
                    print("Invalid ticket number. Please enter a valid number.\n")
            else:
                print("No tickets available. Please create a ticket first.\n")
        elif choice == '4':
            view_tickets()
            if tickets:
                ticket_index = int(input("Enter the ticket number to view details: ")) - 1
                if 0 <= ticket_index < len(tickets):
                    view_ticket_details(ticket_index)
                else:
                    print("Invalid ticket number. Please enter a valid number.\n")
            else:
                print("No tickets available. Please create a ticket first.\n")
        elif choice == '5':
            print("Exiting Customer Support Ticket System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
