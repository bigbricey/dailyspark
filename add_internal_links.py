"""
Add internal links to all DailySpark articles
This keeps visitors on site longer = more affiliate clicks
"""

import os
import re
from collections import defaultdict

directory = r'C:\Users\bigbr\OneDrive\Desktop\dailyspark-working'

# Map of articles and their related topics
article_relationships = {
    'aca-subsidy-cliff.html': ['calculate-your-cliff.html', 'december-income-panic.html', 'optimal-income-for-aca.html'],
    '10000-deductible-reality.html': ['high-deductible-reality.html', 'never-hit-deductible-trap.html', 'out-of-pocket-myth.html'],
    'gig-economy-health.html': ['part-time-trap.html', 'spouse-job-trap.html', 'w2-vs-1099-medical-debt.html'],
    'f1-student-insurance.html': ['best-states-self-employed-health-insurance.html', 'moving-states-health-insurance-savings.html'],
    'emergency-room-bankruptcy.html': ['5000-er-bill.html', 'emergency-room-trap.html', 'bank-account-frozen.html'],
    'prescription-drug-trap.html': ['diabetes-trap.html', 'coinsurance-trap.html'],
    'tax-deductions-guide.html': ['s-corp-health-insurance-hack.html', 'solo-401k-hack.html', 'hsa-strategies-self-employed.html'],
}

# Article titles for nice link text
article_titles = {
    'aca-subsidy-cliff.html': 'The ACA Subsidy Cliff Explained',
    'calculate-your-cliff.html': 'Calculate Your Subsidy Risk',
    'december-income-panic.html': 'December Income Panic',
    'optimal-income-for-aca.html': 'Optimal Income for ACA Subsidies',
    '10000-deductible-reality.html': 'The $10,000 Deductible Reality',
    'high-deductible-reality.html': 'High Deductible Health Plans Exposed',
    'never-hit-deductible-trap.html': 'The "Never Hit Deductible" Trap',
    'out-of-pocket-myth.html': 'Out-of-Pocket Maximum Myth',
    'gig-economy-health.html': 'Gig Economy Health Insurance Crisis',
    'part-time-trap.html': 'The Part-Time Job Trap',
    'spouse-job-trap.html': 'Spouse Job Trap',
    'w2-vs-1099-medical-debt.html': 'W2 vs 1099: Medical Debt',
    'f1-student-insurance.html': 'F-1 Student Insurance Nightmare',
    'best-states-self-employed-health-insurance.html': 'Best States for Self-Employed',
    'moving-states-health-insurance-savings.html': 'Moving States for Healthcare Savings',
    'emergency-room-bankruptcy.html': 'Emergency Room Bankruptcy',
    '5000-er-bill.html': '$5,000 ER Bill',
    'emergency-room-trap.html': 'Emergency Room Trap',
    'bank-account-frozen.html': 'Bank Account Frozen by Medical Bills',
    'prescription-drug-trap.html': 'Prescription Drug Trap',
    'diabetes-trap.html': 'Diabetes Insurance Trap',
    'coinsurance-trap.html': 'Coinsurance Trap',
    'tax-deductions-guide.html': 'Tax Deduction Guide',
    's-corp-health-insurance-hack.html': 'S-Corp Health Insurance Hack',
    'solo-401k-hack.html': 'Solo 401(k) Hack',
    'hsa-strategies-self-employed.html': 'HSA Strategies',
}

files_updated = 0

for article_file, related_articles in article_relationships.items():
    filepath = os.path.join(directory, article_file)
    
    if not os.path.exists(filepath):
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if internal links section already exists
        if 'Related Articles:' in content or 'Read Next:' in content:
            print(f"SKIP: {article_file} already has internal links")
            continue
        
        # Build related articles HTML
        related_html = '<div style="background: #f8f9fa; padding: 2rem; border-radius: 10px; margin: 2rem 0;">\n'
        related_html += '<h3 style="margin-bottom: 1rem; color: #1a1a2e;">Related Articles:</h3>\n'
        related_html += '<ul style="list-style: none; padding: 0;">\n'
        
        for related in related_articles[:3]:  # Max 3 related articles
            if related in article_titles:
                title = article_titles[related]
                related_html += f'<li style="margin-bottom: 0.5rem;">📄 <a href="/{related}" style="color: #667eea; font-weight: bold;">{title}</a></li>\n'
        
        related_html += '</ul>\n</div>\n\n'
        
        # Insert before footer
        content = content.replace('</article>', related_html + '</article>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        files_updated += 1
        print(f"UPDATED: {article_file}")
        
    except Exception as e:
        print(f"ERROR: {article_file}: {str(e)}")

print(f"\nTotal files updated: {files_updated}")
