import os
import re

# Directory containing the HTML files
directory = r'C:\Users\bigbr\OneDrive\Desktop\dailyspark-working'

# Get all HTML files except index, privacy-policy, terms-of-service
html_files = [f for f in os.listdir(directory) 
              if f.endswith('.html') 
              and f not in ['index.html', 'privacy-policy.html', 'terms-of-service.html', 'all-articles.html']]

files_fixed = 0

for filename in html_files:
    filepath = os.path.join(directory, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix broken footer links
        content = re.sub(r'<a href="/about\.html">About</a>', '<a href="/">Home</a>', content)
        content = re.sub(r'<a href="/contact\.html">Contact</a>', '<a href="mailto:contact@jaxsod.com">Contact</a>', content)
        content = re.sub(r'<a href="/privacy\.html">Privacy</a>', '<a href="/privacy-policy.html">Privacy</a>', content)
        
        # Only write if changes were made
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            files_fixed += 1
            print(f"Fixed: {filename}")
    
    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

print(f"\nTotal files fixed: {files_fixed}")
