import os

def calculate_hebrew_gematria(text):
    """
    Calculates the Gematria (numerical value) of a Hebrew string.
    Uses the standard Mispar Gadol (absolute value) method.
    """
    gematria_map = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
        'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
        'כ': 20, 'ך': 20, # Kaf and final Kaf (Kaf Sofit)
        'ל': 30, 'מ': 40, 'ם': 40, # Mem and final Mem (Mem Sofit)
        'נ': 50, 'ן': 50, # Nun and final Nun (Nun Sofit)
        'ס': 60, 'ע': 70, 'פ': 80,
        'ף': 80, # Peh and final Peh (Peh Sofit)
        'צ': 90, 'ץ': 90, # Tsadi and final Tsadi (Tsadi Sofit)
        'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
    }

    total_gematria = 0
    unknown_chars = []

    for char in text:
        if char in gematria_map:
            total_gematria += gematria_map[char]
        elif char.isspace() or char in ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '-', "'", '"']: # Ignore common punctuation and spaces
            continue
        else:
            unknown_chars.append(char) # Collect characters not in the map

    return total_gematria, unknown_chars

# NIEUWE FUNCTIE: Omgekeerde Hebreeuwse Gematria Calculator
def find_hebrew_words_for_number(target_number, dictionary_file="hebrew_words_cleaned.txt", max_word_length=15):
    """
    Finds Hebrew words whose Gematria value matches the target_number.
    Loads words from a specified Hebrew dictionary file.
    """
    
    # Gematria map (exact dezelfde als in calculate_hebrew_gematria)
    gematria_map = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
        'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
        'כ': 20, 'ך': 20, # Kaf and final Kaf (Kaf Sofit)
        'ל': 30, 'מ': 40, 'ם': 40, # Mem and final Mem (Mem Sofit)
        'נ': 50, 'ן': 50, # Nun and final Nun (Nun Sofit)
        'ס': 60, 'ע': 70, 'פ': 80,
        'ף': 80, # Peh and final Peh (Peh Sofit)
        'צ': 90, 'ץ': 90, # Tsadi and final Tsadi (Tsadi Sofit)
        'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
    }

    matching_words = []
    
    if not os.path.exists(dictionary_file):
        print(f"Fout: Woordenboekbestand '{dictionary_file}' niet gevonden.")
        print(f"Zorg ervoor dat '{dictionary_file}' in dezelfde map staat als dit script.")
        return matching_words

    print(f"Zoeken naar Hebreeuwse woorden met Gematria waarde {target_number}...")
    try:
        with open(dictionary_file, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                
                # Sla woorden over die te lang zijn (optioneel, voor efficiëntie)
                if len(word) > max_word_length:
                    continue

                current_word_value = 0
                is_valid_hebrew_word = True
                for char in word:
                    if char in gematria_map:
                        current_word_value += gematria_map[char]
                    else:
                        # Als er niet-Hebreeuwse karakters zijn (die niet in de map staan), sla dit woord over
                        is_valid_hebrew_word = False
                        break
                
                if is_valid_hebrew_word and current_word_value == target_number:
                    matching_words.append(word)
    except Exception as e:
        print(f"Er is een fout opgetreden bij het lezen van het woordenboek: {e}")

    return matching_words


def calculate_latin_numerology(text):
    """
    Calculates the numerological value of a string using the Latin alphabet (A=1, B=2, ..., Z=26).
    """
    numerology_map = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }
    
    total_value = 0
    unknown_chars = []

    for char in text.lower(): # Convert to lowercase for consistent mapping
        if char in numerology_map:
            total_value += numerology_map[char]
        elif char.isspace() or char in ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '-', "'", '"']: # Ignore common punctuation and spaces
            continue
        else:
            unknown_chars.append(char)

    return total_value, unknown_chars

def find_words_for_number(target_number, language="english", max_word_length=15):
    """
    Finds words from a dictionary file whose numerological value matches the target_number.
    """
    if language == "english":
        dictionary_file = "words_alpha.txt"
    elif language == "dutch":
        dictionary_file = "dutch_words_alpha.txt"
    else:
        print("Fout: Ongeldige taal voor woordzoekfunctie. Kies 'english' of 'dutch'.")
        return []

    numerology_map = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

    matching_words = []

    if not os.path.exists(dictionary_file):
        print(f"Fout: Woordenboekbestand '{dictionary_file}' niet gevonden.")
        print(f"Zorg ervoor dat '{dictionary_file}' in dezelfde map staat als dit script.")
        return matching_words

    print(f"Zoeken naar {language} woorden met numerologische waarde {target_number}...")
    try:
        with open(dictionary_file, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower() # Convert to lowercase for consistent mapping
                
                if not word.isalpha(): # Skip words that contain non-alphabetic characters
                    continue
                
                if len(word) > max_word_length:
                    continue

                current_word_value = 0
                for char in word:
                    current_word_value += numerology_map.get(char, 0) # Add 0 if char not in map (shouldn't happen with .isalpha() check)
                
                if current_word_value == target_number:
                    matching_words.append(word)
    except Exception as e:
        print(f"Er is een fout opgetreden bij het lezen van het woordenboek: {e}")

    return matching_words

# --- Main part of the script ---
if __name__ == "__main__":
    print("Welcome to the Alphabetical Numerology Calculator!")

    while True: # Outer loop for choosing the alphabet system
        print("\nChoose an option:")
        print("1. Hebrew Gematria (calculate word value)")
        print("2. English Numerology (calculate word value)")
        print("3. Dutch Numerology (calculate word value)")
        print("4. Find English words for a numerical value (reverse calculator)")
        print("5. Find Dutch words for a numerical value (reverse calculator)")
        print("6. Find Hebrew words for a numerical value (reverse calculator)") # NIEUWE OPTIE
        print("Q. Quit")

        choice = input("Enter your choice (1, 2, 3, 4, 5, 6, or Q): ").strip().lower()

        if choice == 'q':
            print("Exiting calculator. Goodbye!")
            break
        elif choice == '1':
            text_input = input("Enter Hebrew text: ")
            gematria_value, unknown_chars = calculate_hebrew_gematria(text_input)
            print(f"Gematria value: {gematria_value}")
            if unknown_chars:
                print(f"Warning: Unknown characters ignored: {', '.join(set(unknown_chars))}")
        elif choice == '2':
            text_input = input("Enter English text: ")
            numerology_value, unknown_chars = calculate_latin_numerology(text_input)
            print(f"Numerology value (A=1, B=2...): {numerology_value}")
            if unknown_chars:
                print(f"Warning: Unknown characters ignored: {', '.join(set(unknown_chars))}")
        elif choice == '3':
            text_input = input("Enter Dutch text: ")
            numerology_value, unknown_chars = calculate_latin_numerology(text_input)
            print(f"Numerology value (A=1, B=2...): {numerology_value}")
            if unknown_chars:
                print(f"Warning: Unknown characters ignored: {', '.join(set(unknown_chars))}")
        elif choice == '4':
            print("\n--- English Reverse Numerology Calculator ---")
            print("Finds English words for a given numerical value (A=1, B=2...Z=26).")
            print("Type 'back' to return to the main menu.")
            while True:
                try:
                    target_input = input("Enter the target number: ")
                    if target_input.lower() == 'back':
                        print("Returning to main menu.")
                        break
                    
                    target_number = int(target_input)
                    if target_number <= 0:
                        print("Please enter a positive number.")
                        continue

                    max_len_input = input("Max word length (e.g., 15 for common words, leave empty for no limit): ")
                    max_word_len = int(max_len_input) if max_len_input.isdigit() and int(max_len_input) > 0 else 15

                    found_words = find_words_for_number(target_number, language="english", max_word_length=max_word_len)
                    
                    if found_words:
                        print(f"\nFound {len(found_words)} words for the number {target_number} (max length {max_word_len}):")
                        # Print words in columns
                        for i, word in enumerate(found_words):
                            print(f"{word:<15}", end="\t") # Adjust 15 for desired column width
                            if (i + 1) % 5 == 0: # Print 5 words per line
                                print()
                        print() # New line after all words are printed
                    else:
                        print(f"No words found for the number {target_number} with specified criteria.")

                except ValueError:
                    print("Invalid input. Please enter a valid number or 'back'.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
        elif choice == '5':
            print("\n--- Dutch Reverse Numerology Calculator ---")
            print("Finds Dutch words for a given numerical value (A=1, B=2...Z=26).")
            print("Type 'back' to return to the main menu.")
            while True:
                try:
                    target_input = input("Enter the target number: ")
                    if target_input.lower() == 'back':
                        print("Returning to main menu.")
                        break
                    
                    target_number = int(target_input)
                    if target_number <= 0:
                        print("Please enter a positive number.")
                        continue

                    max_len_input = input("Max word length (e.g., 15 for common words, leave empty for no limit): ")
                    max_word_len = int(max_len_input) if max_len_input.isdigit() and int(max_len_input) > 0 else 15

                    found_words = find_words_for_number(target_number, language="dutch", max_word_length=max_word_len)
                    
                    if found_words:
                        print(f"\nFound {len(found_words)} words for the number {target_number} (max length {max_word_len}):")
                        for i, word in enumerate(found_words):
                            print(f"{word:<15}", end="\t")
                            if (i + 1) % 5 == 0:
                                print()
                        print()
                    else:
                        print(f"No words found for the number {target_number} with specified criteria.")

                except ValueError:
                    print("Invalid input. Please enter a valid number or 'back'.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
        elif choice == '6': # NIEUWE OPTIE AFHANDELING VOOR HEBREEUWS
            print("\n--- Hebrew Reverse Gematria Calculator ---")
            print("Finds Hebrew words for a given Gematria value.")
            print("Type 'back' to return to the main menu.")
            while True:
                try:
                    target_input = input("Enter the target number: ")
                    if target_input.lower() == 'back':
                        print("Returning to main menu.")
                        break
                    
                    target_number = int(target_input)
                    if target_number <= 0:
                        print("Please enter a positive number.")
                        continue

                    max_len_input = input("Max word length (e.g., 15 for common words, leave empty for no limit): ")
                    max_word_len = int(max_len_input) if max_len_input.isdigit() and int(max_len_input) > 0 else 15

                    # Let op: de dictionary_file is hier 'hebrew_words_cleaned.txt'
                    found_words = find_hebrew_words_for_number(target_number, dictionary_file="hebrew_words_cleaned.txt", max_word_length=max_word_len)
                    
                    if found_words:
                        print(f"\nFound {len(found_words)} Hebrew words for the number {target_number} (max length {max_word_len}):")
                        for i, word in enumerate(found_words):
                            print(f"{word:<15}", end="\t")
                            if (i + 1) % 5 == 0:
                                print()
                        print()
                    else:
                        print(f"No Hebrew words found for the number {target_number} with specified criteria.")

                except ValueError:
                    print("Invalid input. Please enter a valid number or 'back'.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid choice. Please enter '1', '2', '3', '4', '5', '6', or 'Q'.")
