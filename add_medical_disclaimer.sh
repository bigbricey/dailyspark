#!/bin/bash

# Medical disclaimer HTML to insert
MEDICAL_DISCLAIMER='        <!-- Medical Disclaimer - REQUIRED for health content -->
        <div style="background: #e3f2fd; border: 2px solid #1976d2; border-radius: 8px; padding: 1.2rem; margin-bottom: 2rem;">
            <strong style="color: #0d47a1; display: block; margin-bottom: 0.5rem;">MEDICAL DISCLAIMER:</strong>
            <p style="color: #1565c0; margin: 0;">This content is for informational purposes only and is not medical advice. Health insurance decisions should be made in consultation with qualified insurance agents and healthcare providers. Individual results and coverage may vary.</p>
        </div>'

# Process all HTML files (excluding system pages)
for file in *.html; do
    # Skip system pages
    if [[ "$file" == "privacy.html" ]] || [[ "$file" == "terms.html" ]] || [[ "$file" == "index.html" ]] || [[ "$file" == "all-articles.html" ]]; then
        continue
    fi
    
    # Check if medical disclaimer already exists
    if grep -q "MEDICAL DISCLAIMER" "$file"; then
        echo "Skipping $file - already has medical disclaimer"
    else
        # Add medical disclaimer after FTC disclosure
        sed -i '/<\/div>/{
            :a
            N
            s|</div>\n\n|</div>\n\n'"$MEDICAL_DISCLAIMER"'\n\n|
            tb
            ba
            :b
        }' "$file" 2>/dev/null || \
        # Fallback: Add after disclosure-box if sed pattern fails
        awk '/class="disclosure-box"/{p=1} p && /<\/div>/{print; print ""; print "'"$MEDICAL_DISCLAIMER"'"; p=0; next} 1' "$file" > temp.html && mv temp.html "$file"
        
        echo "Added medical disclaimer to $file"
    fi
done

echo "Medical disclaimers added to all article files"
