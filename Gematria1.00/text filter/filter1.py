import os

def filter_hebrew_characters(text_string):
    """
    Filters a string, keeping only Hebrew characters.
    Hebrew Unicode range is U+0590 to U+05FF.
    """
    hebrew_only_chars = []
    for char in text_string:
        # Check if the character is within the Hebrew Unicode block
        if '\u0590' <= char <= '\u05FF':
            hebrew_only_chars.append(char)
    return "".join(hebrew_only_chars)

def clean_hebrew_wordlist_file(input_filename, output_filename):
    """
    Reads an input text file, filters out non-Hebrew characters from each line,
    and writes the cleaned lines to an output file.
    """
    if not os.path.exists(input_filename):
        print(f"Fout: Het invoerbestand '{input_filename}' is niet gevonden.")
        print("Zorg ervoor dat het bestand in dezelfde map staat als dit script.")
        return

    cleaned_lines_count = 0
    total_lines = 0
    print(f"Start opschonen van niet-Hebreeuwse karakters in '{input_filename}'...")

    try:
        with open(input_filename, 'r', encoding='utf-8', errors='ignore') as infile:
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    total_lines += 1
                    cleaned_line = filter_hebrew_characters(line.strip()) # strip() verwijdert witruimte
                    if cleaned_line: # Schrijf alleen de regel als er Hebreeuwse karakters overblijven
                        outfile.write(cleaned_line + '\n')
                        cleaned_lines_count += 1
        
        print(f"Opschonen voltooid.")
        print(f"Totaal aantal regels gelezen: {total_lines}")
        print(f"Aantal regels geschreven (met Hebreeuwse karakters): {cleaned_lines_count}")
        print(f"Het opgeschoonde bestand is opgeslagen als '{output_filename}'")

    except Exception as e:
        print(f"Er is een fout opgetreden bij het verwerken van het bestand: {e}")
        print("Controleer of het invoerbestand een geldig tekstbestand is.")

# --- Hoe te gebruiken ---
if __name__ == "__main__":
    # Gebruik het geüploade bestand als invoer
    input_file = "hebrew_words kopie.txt"
    # Naam voor het opgeschoonde uitvoerbestand
    output_file = "hebrew_words_cleaned.txt"

    clean_hebrew_wordlist_file(input_file, output_file)

    print("\nTest van de filter_hebrew_characters functie:")
    test_string1 = "שלום העולם! This is a test. 123"
    print(f"Origineel: '{test_string1}'")
    print(f"Gefilterd: '{filter_hebrew_characters(test_string1)}'")

    test_string2 = "Hello world!"
    print(f"Origineel: '{test_string2}'")
    print(f"Gefilterd: '{filter_hebrew_characters(test_string2)}'")
