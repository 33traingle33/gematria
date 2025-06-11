import os

input_filename = "hebrew_words kopie.txt" # Je oorspronkelijke .rtf bestand
output_filename = "hebrew_words_filtered.txt" # Het nieuwe bestand zonder de gespecificeerde regels

# Controleer of het invoerbestand bestaat
if not os.path.exists(input_filename):
    print(f"Fout: Het bestand '{input_filename}' is niet gevonden in dezelfde map als dit script.")
    print("Zorg ervoor dat je het .rtf bestand hier hebt opgeslagen.")
else:
    filtered_lines_count = 0
    total_lines = 0
    print(f"Start filtering '{input_filename}'...")

    try:
        with open(input_filename, 'r', encoding='utf-8', errors='ignore') as infile:
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    total_lines += 1
                    # Controleer of de regel begint met de te verwijderen strings
                    if not (line.strip().startswith("MAP") or line.strip().startswith("PFX a 0")):
                        outfile.write(line)
                    else:
                        filtered_lines_count += 1
        print(f"Filtering voltooid.")
        print(f"Totaal aantal regels gelezen: {total_lines}")
        print(f"Aantal verwijderde regels: {filtered_lines_count}")
        print(f"Het gefilterde bestand is opgeslagen als '{output_filename}'")

    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
        print("Mogelijk is de codering van het bestand een probleem. Probeer het .rtf bestand eerst handmatig op te slaan als UTF-8 tekst.")
