import pandas as pd

# Read your Excel file (adjust the filename)
excel_file = r"C:\Users\ssbus\Downloads\Testing dataset.xlsx"
df = pd.read_excel(excel_file)

# Assume the first column contains class labels and the rest are features
# Create SVMLight-style lines
with open('testing_pro1.txt', 'w') as txt_file:
    for index, row in df.iterrows():
        class_label = row.iloc[1]
        features = row.iloc[2:]  # Assuming features start from the second column
        svmlight_line = f"{class_label} " + " ".join(f"{i+1}:{val}" for i, val in enumerate(features))
        txt_file.write(svmlight_line + '\n')

print("Conversion complete. Output saved in 'testing_pro1.txt'.")
