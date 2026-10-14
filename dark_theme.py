import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace white backgrounds with deep dark charcoal/green
html = html.replace('bg-white', 'bg-gray-900')
html = html.replace('bg-gray-50', 'bg-gray-800')
html = html.replace('bg-gray-100', 'bg-gray-800')
html = html.replace('bg-slate-50', 'bg-slate-900')

# Replace dark text with light text
html = html.replace('text-gray-800', 'text-gray-100')
html = html.replace('text-gray-700', 'text-gray-300')
html = html.replace('text-gray-600', 'text-gray-400')
html = html.replace('text-black', 'text-white')
html = html.replace('text-slate-800', 'text-slate-100')

# Ensure the body itself is dark
if '<body' in html and 'class=' not in html.split('<body')[1].split('>')[0]:
    html = html.replace('<body', '<body class="bg-gray-900 text-white"', 1)
elif '<body' in html:
    html = html.replace('<body', '<body class="bg-gray-900 text-white"', 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Dark luxury theme applied successfully.")
