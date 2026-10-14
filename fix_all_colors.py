import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_fix = """
<style>
    /* 1. Force DARK text on any LIGHT background */
    .bg-white h1, .bg-white h2, .bg-white h3, .bg-white h4, .bg-white p, .bg-white span, .bg-white a,
    .bg-gray-50 h1, .bg-gray-50 h2, .bg-gray-50 h3, .bg-gray-50 p, .bg-gray-50 span, .bg-gray-50 a,
    .bg-gray-100 h1, .bg-gray-100 h2, .bg-gray-100 h3, .bg-gray-100 p, .bg-gray-100 span, .bg-gray-100 a,
    .bg-slate-50 h1, .bg-slate-50 h2, .bg-slate-50 h3, .bg-slate-50 p, .bg-slate-50 span, .bg-slate-50 a {
        color: #111827 !important;
    }
    
    /* 2. Force WHITE text on any DARK background */
    .bg-gray-900 h1, .bg-gray-900 h2, .bg-gray-900 h3, .bg-gray-900 h4, .bg-gray-900 p, .bg-gray-900 span, .bg-gray-900 a,
    .bg-slate-900 h1, .bg-slate-900 h2, .bg-slate-900 h3, .bg-slate-900 p, .bg-slate-900 span, .bg-slate-900 a,
    .bg-black h1, .bg-black h2, .bg-black h3, .bg-black p, .bg-black span, .bg-black a {
        color: #FFFFFF !important;
    }

    /* 3. Force all previously dark green links/text to BRIGHT GOLD */
    a[href*="contact"], a[href*="get-in-touch"], 
    .text-green-700, .text-green-800, .text-green-900,
    .text-emerald-700, .text-emerald-800, .text-emerald-900,
    .text-teal-700, .text-teal-800, .text-teal-900 {
        color: #FBBF24 !important; /* Bright Gold */
    }

    /* 4. Specific fix for the "Find Your Room" white-on-white issue */
    .bg-gray-50 h2, .bg-gray-100 h2, .bg-white h2, .bg-slate-50 h2, 
    .bg-gray-50 h3, .bg-gray-100 h3, .bg-white h3, .bg-slate-50 h3 {
        color: #1F2937 !important; /* Dark Gray */
    }

    /* 5. Fix for "ACCOMMODATION" badge on the image */
    .badge, .tag, .bg-blue-900 span, .bg-slate-800 span {
        color: #FBBF24 !important;
    }
</style>
"""

if '<style>' not in html:
    html = html.replace('</head>', css_fix + '</head>')
else:
    html = html.replace('</head>', css_fix + '\n</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Comprehensive color fix applied. No more invisible text.")
