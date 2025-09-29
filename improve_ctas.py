# IMPROVED CTA COPY - Marcus Campbell Style
# Before: Generic boring links that don't convert
# After: Emotional benefit-driven CTAs that make people want to click

import os
import re

directory = r'C:\Users\bigbr\OneDrive\Desktop\dailyspark-working'
html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

# Marcus Campbell's CTA formulas:
# 1. Lead with the pain point
# 2. Promise specific benefit
# 3. Add urgency or curiosity
# 4. Keep it conversational

cta_improvements = {
    # Generic CTAs → Emotional CTAs
    r'<a href="([^"]*myphysicianplan[^"]*)" target="_blank"[^>]*>MyPhysicianPlan</a>': 
        r'<a href="\1" target="_blank" rel="noopener" style="color: #667eea; font-weight: bold;">See Real Healthcare Pricing (No Deductibles) →</a>',
    
    r'Learn About MyPhysicianPlan':
        'Stop Paying Insurance Prices for Cash Care - See Plans →',
    
    r'Check Out MyPhysicianPlan':
        'Get Healthcare Without the Insurance Trap - See How →',
    
    r'Visit MyPhysicianPlan':
        'See Transparent Healthcare Pricing (Finally!) →',
}

# Count improvements
files_updated = 0
total_replacements = 0

for filename in html_files:
    filepath = os.path.join(directory, filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        replacements_in_file = 0
        
        # Apply each CTA improvement
        for old_pattern, new_text in cta_improvements.items():
            matches = len(re.findall(old_pattern, content, re.IGNORECASE))
            if matches > 0:
                content = re.sub(old_pattern, new_text, content, flags=re.IGNORECASE)
                replacements_in_file += matches
        
        # Only write if changes were made
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            files_updated += 1
            total_replacements += replacements_in_file
            print(f"UPDATED {filename}: {replacements_in_file} CTAs improved")
    
    except Exception as e:
        print(f"ERROR: {filename}: {str(e)}")

print(f"\nCOMPLETE!")
print(f"Files updated: {files_updated}")
print(f"Total CTAs improved: {total_replacements}")