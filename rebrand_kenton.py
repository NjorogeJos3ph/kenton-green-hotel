with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("Theta Hotel", "Kenton Green Hotel")
html = html.replace("THETA HOTEL", "KENTON GREEN HOTEL")
html = html.replace("Theta Country Resort", "Kenton Green Hotel")
html = html.replace("THETA COUNTRY RESORT", "KENTON GREEN HOTEL")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ Rebranded to Kenton Green Hotel!")
