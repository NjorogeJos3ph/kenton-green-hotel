import os

file_path = 'index.html'
backup_path = 'index.html.bak_rebrand'

# 1. Read the file
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Save a backup
with open(backup_path, 'w', encoding='utf-8') as f:
    f.write(content)

# 3. Perform replacements (Longest strings first to avoid partial matches)
content = content.replace("THETA COUNTRY RESORT", "THETA HOTEL")
content = content.replace("Theta Country Resort", "Theta Hotel")
content = content.replace("THETA RESORT", "THETA HOTEL")
content = content.replace("Theta Resort", "Theta Hotel")

# 4. Write it back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Successfully rebranded to 'Theta Hotel'! Backup saved as index.html.bak_rebrand")
