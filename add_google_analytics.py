import os
import re

# Google Analytics code to add
GA_CODE = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-809NFNY2M5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-809NFNY2M5');
</script>
'''

# Get all HTML files in current directory
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Found {len(html_files)} HTML files")

added_count = 0
skipped_count = 0
error_count = 0

for filename in html_files:
    try:
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has Google Analytics
        if 'G-809NFNY2M5' in content:
            print(f"SKIPPED: {filename} (already has GA)")
            skipped_count += 1
            continue
        
        # Add GA code right after <head> tag
        if '<head>' in content:
            content = content.replace('<head>', '<head>\n' + GA_CODE, 1)
            
            # Write back
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"ADDED: {filename}")
            added_count += 1
        else:
            print(f"WARNING: {filename} - no <head> tag found")
            
    except Exception as e:
        print(f"ERROR: {filename} - {str(e)}")
        error_count += 1

print(f"\nGoogle Analytics installation complete!")
print(f"Added: {added_count} | Skipped: {skipped_count} | Errors: {error_count}")
