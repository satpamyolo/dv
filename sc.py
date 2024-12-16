import pandas as pd
import plotly.graph_objects as go

# Baca data dari file Excel
file_path = "Book1.xlsx"  # Ganti dengan path file Excel kamu
df = pd.read_excel(file_path)

# Debugging: Periksa data
print("Dataframe Preview:")
print(df.head())
print("Columns:", df.columns)

# Pastikan kolom sesuai
source = df['Asal']
target = df['Tujuan']
value = df['Frekuensi Perjalanan']

# Pastikan nilai 'value' positif
df = df[df['Frekuensi Perjalanan'] > 0]

# Buat daftar unik label
labels = pd.concat([source, target]).dropna().unique()
label_mapping = {label: idx for idx, label in enumerate(labels)}

# Debugging: Periksa labels
print("Labels:", labels)

# Mapping source dan target ke indeks numerik
source_indices = source.map(label_mapping).tolist()
target_indices = target.map(label_mapping).tolist()

# Buat diagram Sankey
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=value
    )
))

fig.update_layout(title_text="Sankey Diagram (Original Dataset Order)", font_size=10)

# Debugging: Periksa apakah diagram dibuat
print("Sankey Diagram Created")

# Tampilkan diagram
fig.show()
