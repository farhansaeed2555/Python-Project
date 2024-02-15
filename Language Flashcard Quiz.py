flashcards = [
    {"word": "Hello", "translation": "Hola", "additional_info": "Common greeting in Spanish."},
    {"word": "Goodbye", "translation": "Adiós", "additional_info": "Farewell in Spanish."},
    {"word": "Thank you", "translation": "Gracias", "additional_info": "Expressing gratitude in Spanish."},
    {"word": "Please", "translation": "Por favor", "additional_info": "Polite request in Spanish."}
]

def quiz():
    if not flashcards:
        print("No flashcards available. Please add flashcards first.\n")
        return
    
    print("Language Flashcard Quiz:")
    for flashcard in flashcards:
        user_answer = input(f"What is the translation of '{flashcard['word']}'? ").strip().lower()
        correct_answer = flashcard['translation'].lower()
        
        if user_answer == correct_answer:
            print("Correct! " + flashcard['additional_info'])
        else:
            print(f"Incorrect. The correct translation is '{flashcard['translation']}'. {flashcard['additional_info']}")
    
    print("Quiz complete!\n")

def add_flashcard():
    word = input("Enter the word: ")
    translation = input("Enter the translation: ")
    additional_info = input("Enter additional information: ")
    
    flashcard = {
        "word": word,
        "translation": translation,
        "additional_info": additional_info
    }
    
    flashcards.append(flashcard)
    print("Flashcard added successfully!\n")

def main():
    while True:
        print("Language Flashcard Tool")
        print("1. Quiz Me")
        print("2. Add Flashcard")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            quiz()
        elif choice == '2':
            add_flashcard()
        elif choice == '3':
            print("Exiting Language Flashcard Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
