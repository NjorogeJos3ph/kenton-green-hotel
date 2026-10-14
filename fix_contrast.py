import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace dark green text classes with premium gold and bright white
html = re.sub(r'text-(green|emerald|teal)-(700|800|900)', 'text-amber-400', html)
html = re.sub(r'text-(green|emerald|teal)-(500|600)', 'text-amber-200', html)

# Add a CSS override just in case some classes are hardcoded
css_override = """
<style>
    .text-amber-400 { color: #FBBF24 !important; }
    .text-amber-200 { color: #FDE68A !important; }
    h1, h2, h3 { color: #FFFFFF !important; }
</style>
"""
if '<style>' not in html:
    html = html.replace('</head>', css_override + '</head>')
else:
    html = html.replace('</head>', css_override + '\n</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Contrast fixed. Green text is now Gold/White.")
