# Create README.md file with comprehensive documentation
readme_content = '''# Joan Marc Riera Duocastella - Professional Portfolio

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://joanmarcriera.github.io/riera.co.uk)
[![Website](https://img.shields.io/badge/Website-riera.co.uk-blue)](https://riera.co.uk)

> Platform Engineering & Infrastructure Leader at EMBL-EBI

This repository hosts the professional portfolio website for Joan Marc Riera Duocastella, showcasing experience in platform engineering, large-scale infrastructure, and bioinformatics systems management.

## 🚀 About

Joan Marc Riera Duocastella is an experienced Platform Engineering and Infrastructure Leader with over 15 years of expertise in large-scale data systems. Currently serving as SDO Service & Data Technical Coordinator at EMBL-EBI (European Bioinformatics Institute), he specialises in:

- **Petabyte-scale storage systems** - Scaled EMBL-EBI storage from 15 PB to over 100 PB
- **Data archiving solutions** - Led development of the FIRE (File Replication) archive system
- **Infrastructure automation** - Automated core data-transfer platforms and deployment processes
- **Identity and access management** - Delivered institute-wide IAM overhauls
- **High-availability systems** - Designed resilient, vendor-agnostic solutions

## 🛠 Technical Stack

This website is built with:

- **HTML5** - Semantic markup and accessibility
- **CSS3** - Modern styling with CSS Grid and Flexbox
- **JavaScript** - Smooth scrolling and interactive navigation
- **GitHub Pages** - Static site hosting
- **Font Awesome** - Professional iconography
- **Google Fonts** - Inter font family for optimal readability

## 📁 Project Structure

```
├── index.html          # Main HTML file
├── styles.css          # CSS styling
├── CNAME              # Custom domain configuration
├── README.md          # Project documentation
├── .gitignore         # Git ignore rules
└── assets/
    └── documents/     # CV and reference documents
        ├── Marc Riera - Head of IT Operations.pdf
        ├── Resume-MARC-RIERA-Octopus-Energy.pdf
        ├── Marc Riera Head of Platform Engineering.pdf
        ├── Marc Riera Head of Infrastructure Services.pdf
        ├── Cover letter Head of IT Operations.pdf
        ├── Marc Riera Head of Platform Engineering-cover letter.pdf
        ├── 20240705 Reference letter for Marc Riera - Mallory Freeberg.pdf
        └── 20240702 Reference letter for Marc Riera - Cortes-Ciriano.pdf
```

## 🌐 Features

### Professional Design
- Modern, responsive design that works across all devices
- Professional colour scheme optimised for readability
- Smooth animations and hover effects
- Clean typography using Inter font family

### Interactive Navigation
- Sticky navigation bar with smooth scrolling
- Active section highlighting
- Mobile-responsive hamburger menu

### Comprehensive Content
- Detailed professional experience timeline
- Technical skills categorised by expertise area
- Key achievements with visual icons
- Downloadable professional documents
- Contact information and location details

### Performance Optimised
- Fast loading times with optimised assets
- Semantic HTML for better SEO
- Accessible design following WCAG guidelines
- Print-friendly CSS for physical copies

## 🚀 Deployment

### GitHub Pages Setup

1. **Repository Creation**
   ```bash
   # Create repository named: riera.co.uk (or your-username.github.io)
   git clone https://github.com/joanmarcriera/riera.co.uk.git
   cd riera.co.uk
   ```

2. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Set Source to "Deploy from a branch"
   - Select "main" branch and "/ (root)" folder
   - Save settings

3. **Custom Domain Configuration**
   - Add CNAME file with your domain: `riera.co.uk`
   - Configure DNS settings:
     ```
     Type: A
     Name: @
     Value: 185.199.108.153
     Value: 185.199.109.153
     Value: 185.199.110.153
     Value: 185.199.111.153
     ```
     ```
     Type: CNAME
     Name: www
     Value: riera.co.uk
     ```

4. **Upload Documents**
   - Create `assets/documents/` directory
   - Upload all PDF files (CVs, cover letters, references)
   - Ensure file names match the links in HTML

### Local Development

```bash
# Clone the repository
git clone https://github.com/joanmarcriera/riera.co.uk.git
cd riera.co.uk

# Serve locally (Python 3)
python -m http.server 8000

# Or with Node.js
npx serve .

# Open browser to http://localhost:8000
```

## 📱 Responsive Design

The website is fully responsive and optimised for:

- **Desktop** (1200px+) - Full layout with sidebar elements
- **Tablet** (768px - 1199px) - Adjusted grid layouts
- **Mobile** (< 768px) - Single column layout with mobile navigation

## 🎨 Customisation

### Colours
Modify CSS custom properties in `styles.css`:
```css
:root {
    --primary-color: #2563eb;      /* Main brand colour */
    --secondary-color: #64748b;    /* Secondary text */
    --accent-color: #0ea5e9;       /* Accent highlights */
    /* ... */
}
```

### Content
Update content in `index.html`:
- Personal information and taglines
- Professional experience details
- Skills and achievements
- Contact information
- Document links

### Typography
Change fonts by updating Google Fonts import:
```html
<link href="https://fonts.googleapis.com/css2?family=YourFont:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

## 📊 Analytics & SEO

### SEO Optimisation
- Semantic HTML structure
- Meta descriptions and keywords
- Open Graph tags for social sharing
- Structured data markup
- Sitemap.xml (optional)

### Performance Monitoring
Consider adding:
- Google Analytics
- Google Search Console
- Core Web Vitals monitoring

## 🔒 Security & Privacy

- No client-side data collection
- Static files only (no server-side processing)
- HTTPS enforced through GitHub Pages
- No cookies or tracking by default

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

While this is a personal portfolio, suggestions and improvements are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Contact

**Joan Marc Riera Duocastella**
- **Email**: marc@riera.co.uk
- **LinkedIn**: [linkedin.com/in/joanmarcriera](https://linkedin.com/in/joanmarcriera)
- **GitHub**: [github.com/joanmarcriera](https://github.com/joanmarcriera)
- **ORCID**: [0000-0002-0609-0137](https://orcid.org/0000-0002-0609-0137)

---

*Last updated: January 2025*

**Professional Focus**: Platform Engineering • Infrastructure Leadership • Large-scale Data Systems • Bioinformatics • EMBL-EBI'''

# Create CNAME file for custom domain
cname_content = '''riera.co.uk'''

# Create .gitignore file
gitignore_content = '''# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo
*~

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Dependencies
node_modules/
.npm
.yarn-integrity

# Optional npm cache directory
.npm

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variables file
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Temporary folders
tmp/
temp/

# Cache
.cache/
.parcel-cache/

# Build outputs
dist/
build/
out/

# Jekyll (if used)
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata

# Local development
*.local
.vercel'''

print("Additional files created successfully!")
print(f"README.md length: {len(readme_content)} characters")
print(f"CNAME length: {len(cname_content)} characters")  
print(f".gitignore length: {len(gitignore_content)} characters")