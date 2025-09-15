# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a GitHub Pages static website for "DY Prods", a photography studio business. The site is a single-page application built with vanilla HTML, CSS, and JavaScript using Bootstrap 5 for styling and responsiveness.

**Live Site**: https://chris474849.github.io/
**Repository**: https://github.com/Chris474849/Chris474849.github.io.git

## Architecture

### File Structure
- `index.html` - Main and only HTML page containing all site content
- `css/styles.css` - Custom CSS with CSS variables for theming
- `js/main.js` - JavaScript for smooth scrolling and form handling
- `.git/` - Git repository configuration

### Technology Stack
- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Framework**: Bootstrap 5.3.0 (CDN)
- **Icons**: Font Awesome 6.4.0 (CDN)  
- **Hosting**: GitHub Pages (automatic deployment from main branch)
- **Version Control**: Git

### Page Sections
1. **Hero Section** - Landing area with call-to-action
2. **Services** - Photography and videography services offered
3. **Portfolio** - Gallery of work (using placeholder images)
4. **About** - Company information and history
5. **Contact** - Booking form and contact details
6. **Footer** - Social media links and business hours

## Common Development Commands

### Local Development
```bash
# Serve locally using Python (recommended for testing)
python -m http.server 8000

# Or using Node.js http-server (if installed)
npx http-server

# Or using PowerShell (Windows)
python -m http.server 8080
```

### Git Operations
```bash
# Check current status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub Pages (deploys automatically)
git push origin main

# View commit history
git log --oneline

# Check remote configuration
git remote -v
```

### Testing and Validation
```bash
# Validate HTML (requires online validator or local setup)
# No local build process - direct file editing

# Test responsive design by opening in browser at different sizes
# Test form functionality locally before deployment
```

## Development Guidelines

### CSS Customization
- Custom properties (CSS variables) are defined in `:root` in `styles.css`
- Primary color: `#2c3e50` (dark blue-gray)
- Secondary color: `#e67e22` (orange)
- Light color: `#ecf0f1` (off-white)
- Dark color: `#1a252f` (very dark blue)

### JavaScript Functionality
- Smooth scrolling navigation between page sections
- Form submission handling with browser alerts (no backend integration)
- Mobile-specific Instagram app opening logic
- All JavaScript is vanilla (no frameworks/libraries)

### Content Management
- All content is hard-coded in `index.html`
- Images use placeholder URLs (`/api/placeholder/`) and should be replaced with actual assets
- Contact information and business details are embedded in HTML
- Spanish language content throughout

### Deployment Process
- **Automatic**: Any push to `main` branch triggers GitHub Pages deployment
- **No build step**: Files are served directly as static assets
- **Domain**: Uses default GitHub Pages domain (chris474849.github.io)

## Business Context

This website represents a photography studio business offering:
- Portrait photography sessions
- Videography services  
- Commercial photography
- Event photography

Contact information:
- Phone: +53 56601651, +53 55494545
- Email: dyprods0581@gmail.com
- Instagram: @DY_Prods
- Hours: Mon-Fri 9AM-6PM, Sat 10AM-3PM, Sun Closed

## Important Notes

- **Language**: All content is in Spanish
- **Mobile-first**: Bootstrap responsive design with mobile considerations
- **Form handling**: Currently simulated with JavaScript alerts - no backend
- **Images**: Placeholder images need replacement with actual photography portfolio
- **Social media**: Instagram link has special mobile app detection logic
- **No dependencies**: No package.json, build process, or local dependencies required