import os
import glob

# Medical disclaimer HTML
medical_disclaimer = '''        <!-- Medical Disclaimer - REQUIRED for health content -->
        <div style="background: #e3f2fd; border: 2px solid #1976d2; border-radius: 8px; padding: 1.2rem; margin-bottom: 2rem;">
            <strong style="color: #0d47a1; display: block; margin-bottom: 0.5rem;">MEDICAL DISCLAIMER:</strong>
            <p style="color: #1565c0; margin: 0;">This content is for informational purposes only and is not medical advice. Health insurance decisions should be made in consultation with qualified insurance agents and healthcare providers. Individual results and coverage may vary.</p>
        </div>'''

# Stronger FTC disclosure
stronger_ftc = '''        <div class="disclosure-box" style="background: #fff3cd; border: 2px solid #ff0000;">
            <strong>AFFILIATE DISCLOSURE:</strong>
            We are a participant in the AWIN affiliate program. This means we earn commissions when you purchase MyPhysicianPlan through our links. This costs you nothing extra but helps support our site. We only recommend products we believe will help our readers.
        </div>'''

# Process all HTML files
count = 0
for file_path in glob.glob('*.html'):
    # Skip system pages
    if file_path in ['privacy.html', 'terms.html', 'index.html', 'all-articles.html', 
                     'privacy-policy.html', 'terms-of-service.html']:
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has medical disclaimer
    if 'MEDICAL DISCLAIMER' in content:
        print(f"Skipping {file_path} - already has medical disclaimer")
        continue
    
    # Replace the FTC disclosure with stronger version and add medical disclaimer
    if 'class="disclosure-box"' in content:
        # Find the disclosure box and its closing tag
        start = content.find('<div class="disclosure-box">')
        if start != -1:
            end = content.find('</div>', start) + 6
            # Replace with stronger FTC + medical disclaimer
            new_content = content[:start] + stronger_ftc + '\n\n' + medical_disclaimer + content[end:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated {file_path}")

print(f"\nTotal files updated: {count}")