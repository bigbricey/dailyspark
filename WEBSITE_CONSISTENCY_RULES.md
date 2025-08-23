# ⚠️ WEBSITE CONSISTENCY RULES - NEVER VIOLATE THESE!

## CRITICAL: Every page MUST have:

### 1. EXACT COLORS (NO VARIATIONS!)
- **Header Background:** `#1a1a2e` (dark navy)
- **Logo Color:** `#4fbdba` (teal)
- **Hero Gradient:** `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Footer Background:** `#1a1a2e` (same as header)

### 2. NAVIGATION (ALL 4 LINKS!)
```html
<nav>
    <a href="/">Home</a>
    <a href="/all-articles.html">Articles</a>
    <a href="/#subsidy-cliff">Subsidy Cliff</a>
    <a href="/#alternatives">Resources</a>
</nav>
```
❌ NEVER use just a "← Back" button
❌ NEVER skip the navigation menu
✅ ALWAYS include all 4 links

### 3. FTC DISCLOSURE (LEGAL REQUIREMENT!)
Every article with affiliate links MUST have:
```html
<div class="disclosure-box">
    <strong>Affiliate Disclosure:</strong>
    This article contains affiliate links...
</div>
```

### 4. TEMPLATE STRUCTURE
1. Header (dark navy with full nav)
2. Hero section (purple gradient)
3. Article container (white box with shadow)
4. Footer (dark navy)

## HOW TO CREATE NEW ARTICLES:

1. **COPY** `MASTER_TEMPLATE.html`
2. **REPLACE** placeholders:
   - [ARTICLE TITLE]
   - [META DESCRIPTION]
   - [READ TIME]
   - [ARTICLE CONTENT]
3. **VERIFY** all navigation links work
4. **CHECK** FTC disclosure is present
5. **TEST** on mobile (375px width)

## VERIFICATION CHECKLIST:
Before publishing ANY page:
- [ ] Header is #1a1a2e (dark navy)?
- [ ] All 4 navigation links present?
- [ ] Hero has purple gradient?
- [ ] FTC disclosure visible (if affiliate links)?
- [ ] Footer matches header color?
- [ ] Mobile responsive works?

## COMMON MISTAKES TO AVOID:
❌ Creating pages with different header colors
❌ Using "← Back" instead of full navigation
❌ Forgetting FTC disclosure
❌ Changing the gradient colors
❌ Making header sticky vs fixed
❌ Using different fonts

## IF YOU FIND INCONSISTENCY:
1. STOP creating new content
2. FIX all existing pages first
3. Use MASTER_TEMPLATE.html as reference
4. Test 5 random pages to verify consistency

## DEPLOYMENT REMINDER:
After making changes:
1. `git add .`
2. `git commit -m "Fixed template consistency"`
3. `git push`
4. Wait 5 minutes for cron job
5. Check live site

---
⚠️ NEVER CREATE A PAGE WITHOUT CHECKING THESE RULES!