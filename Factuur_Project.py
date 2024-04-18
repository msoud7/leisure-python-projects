from docx import Document
from datetime import datetime, timedelta
import win32com.client as win32

# Ask for the working directory:
pathxl = input("Voer de Excel file path in: ").strip('"')
doc_path = input("Voer de WORD TEMPLATE file path in: ").strip('"')

# Get the password from the user
password = input("Voer de Excel workbook password in: ")

# Ask for the invoice number
factuur_nummer = int(input("Voer eerstvolgende factuur nummer in: "))
begindatum_training = input("Voer begin datum_training in: ")
einddatum_training = input("Voer eind datum training in: ")

# Define today's date and calculate vandaag and vervaldatum
today = datetime.now()
vandaag = (today + timedelta(days=1)).strftime("%d-%m-%Y")
vervaldatum = (today + timedelta(days=15)).strftime("%d-%m-%Y")

expected_rows = 8

# Load the Excel workbook with password using win32com.client
excel_app = win32.Dispatch("Excel.Application")
workbook = excel_app.Workbooks.Open(pathxl, False, True, None, password)
worksheet = workbook.ActiveSheet

# Now you can work with the 'workbook' object
print("Workbook loaded successfully!")

# Define cell coordinates
cell_coordinates = {
    "naam": "B",
    "plaats": "D",
    "adres": "E",
    "postcode": "F",
    "naam_contactpersoon": "C"
}

start_row_naam_plaats = 3  # Start from row 3 for "naam" and "plaats"
start_row_others = 16  # Start from row 16 for "adres," "postcode," and "naam_contactpersoon"
end_row_naam_plaats = start_row_naam_plaats + 7  # Extract 8 rows for "naam" and "plaats"
end_row_others = start_row_others + 7  # Extract 8 rows for "adres," "postcode," and "naam_contactpersoon"

# List to store extracted data
data_list_naam_plaats = []
data_list_others = []

# Extract data from Excel
for row_num in range(start_row_naam_plaats, end_row_naam_plaats + 1):
    data = {}
    for key, col_letter in cell_coordinates.items():
        if key in ["naam", "plaats"]:
            cell_value = worksheet.Range(f"{col_letter}{row_num}").Value
            data[key] = cell_value
    data_list_naam_plaats.append(data)

for row_num in range(start_row_others, end_row_others + 1):
    data = {}
    for key, col_letter in cell_coordinates.items():
        if key not in ["naam", "plaats"]:
            cell_value = worksheet.Range(f"{col_letter}{row_num}").Value
            data[key] = cell_value
    data_list_others.append(data)

# Merge the two lists into a single data_list
data_list = [{**na, **ot} for na, ot in zip(data_list_naam_plaats, data_list_others)]

# Print extracted data (for demonstration)
for idx, item in enumerate(data_list, start=1):
    print(f"Row {idx}: {item}")

# Define placeholder map with exact placeholder text from your template
placeholder_map = {
    "naam_placeholder": "naam",
    "plaats_placeholder": "plaats",
    "adres_placeholder": "adres",
    "postcode_placeholder": "postcode",
    "naam_contactpersoon_placeholder": "naam_contactpersoon",
    "factuurnummer_placeholder": "factuur_nummer",
    "begindatum_training_placeholder": "begindatum_training",
    "einddatum_training_placeholder": "einddatum_training",
    "vandaag_placeholder": "vandaag",
    "vervaldatum_placeholder": "vervaldatum"
}

#DEFINE FUNCTION FOR REPLACING
def replace_placeholders(doc, placeholder_map, data):
    for placeholder, key in placeholder_map.items():
        for paragraph in doc.paragraphs:
            if placeholder in paragraph.text:
                value = str(data.get(key, ''))
                if key == "vandaag":
                    value = vandaag
                elif key == "vervaldatum":
                    value = vervaldatum
                paragraph.text = paragraph.text.replace(placeholder, value)

# Iterate over each row in the extracted data list
for idx, data in enumerate(data_list, start=1):
    # Check if any value in the data is None
    if any(value is None for value in data.values()):
        print(f"Skipping document for {data['naam_contactpersoon']} as some values are missing.")
        continue

    # Create a new document based on the template
    new_doc = Document(doc_path)

    # Replace placeholders in the new document with actual data
    replace_placeholders(new_doc, placeholder_map, {**data, "factuur_nummer": factuur_nummer,
                                                    "begindatum_training": begindatum_training,
                                                    "einddatum_training": einddatum_training})

    # Save the modified document with a unique name based on the row index and invoice number
    new_doc.save(f"factuur_{factuur_nummer}_{data['naam_contactpersoon']}.docx")
    # ADD 1 to the INVOICE NUMBER
    factuur_nummer += 1

# Close the workbook and quit Excel
workbook.Close(False)
excel_app.Quit()

print("Documents created successfully!")
