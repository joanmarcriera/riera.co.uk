# Joan Marc Riera Duocastella - Professional Portfolio

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
- Mobile-responsive design

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

## 🚀 Quick Start Deployment

### Method 1: Automated Deployment Script

**For Linux/macOS:**
```bash
# Make the script executable
chmod +x deploy.sh

# Run the deployment script
./deploy.sh
```

**For Windows:**
```cmd
# Run the batch script
deploy.bat
```

### Method 2: Manual Setup

1. **Create GitHub Repository**
   ```bash
   # Create a new repository named 'riera.co.uk' on GitHub
   # Clone it locally
   git clone https://github.com/joanmarcriera/riera.co.uk.git
   cd riera.co.uk
   ```

2. **Add Website Files**
   - Copy `index.html`, `styles.css`, `CNAME`, and `README.md` to repository
   - Create `assets/documents/` directory
   - Upload all your PDF documents to `assets/documents/`

3. **Deploy to GitHub Pages**
   ```bash
   git add .
   git commit -m "Initial deployment of professional portfolio"
   git push origin main
   ```

4. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Set Source to "Deploy from a branch"
   - Select "main" branch and "/ (root)" folder
   - Save settings

5. **Configure Custom Domain**
   - In Pages settings, add custom domain: `riera.co.uk`
   - Configure DNS with your domain provider:
     ```
     Type: A,    Name: @,   Value: 185.199.108.153
     Type: A,    Name: @,   Value: 185.199.109.153
     Type: A,    Name: @,   Value: 185.199.110.153
     Type: A,    Name: @,   Value: 185.199.111.153
     Type: CNAME, Name: www, Value: riera.co.uk
     ```

## 📄 Document Management

### Required Documents
Place these PDF files in `assets/documents/`:

- `Marc Riera - Head of IT Operations.pdf`
- `Resume-MARC-RIERA-Octopus-Energy.pdf`
- `Marc Riera Head of Platform Engineering.pdf`
- `Marc Riera Head of Infrastructure Services.pdf`
- `Cover letter Head of IT Operations.pdf`
- `Marc Riera Head of Platform Engineering-cover letter.pdf`


### Adding New Documents
1. Upload PDF to `assets/documents/`
2. Add new entry in `index.html` documents section:
   ```html
   <div class="document-item">
       <div class="document-icon">
           <i class="fas fa-file-alt"></i>
       </div>
       <h3>Your Document Title</h3>
       <p>Document description</p>
       <a href="assets/documents/your-document.pdf" class="download-btn" target="_blank">
           <i class="fas fa-download"></i> Download PDF
       </a>
   </div>
   ```

## 🎨 Customisation Guide

### Personal Information
Update the following sections in `index.html`:

**Hero Section:**
```html
<h1>Joan Marc Riera Duocastella</h1>
<h2>Platform Engineering & Infrastructure Leader</h2>
<p class="tagline">Your professional tagline here</p>
```

**Contact Information:**
```html
<a href="mailto:marc@riera.co.uk" class="contact-btn">
<a href="https://linkedin.com/in/joanmarcriera" class="contact-btn">
<a href="https://github.com/joanmarcriera" class="contact-btn">
```

### Colour Scheme
Modify CSS custom properties in `styles.css`:
```css
:root {
    --primary-color: #2563eb;      /* Main brand colour */
    --secondary-color: #64748b;    /* Secondary text */
    --accent-color: #0ea5e9;       /* Accent highlights */
}
```

### Professional Experience
Update the timeline section with your specific roles and achievements.

### Skills and Achievements
Modify the skills grid and achievements section to reflect your expertise.

## 📱 Responsive Design

The website is fully responsive and tested on:
- **Desktop** (1200px+) - Full layout with sidebar elements
- **Tablet** (768px - 1199px) - Adjusted grid layouts
- **Mobile** (< 768px) - Single column layout with optimised navigation

## 🔍 SEO Optimisation

### Current SEO Features
- Semantic HTML structure
- Meta descriptions and keywords
- Open Graph tags ready for social sharing
- Fast loading times
- Mobile-responsive design

### Recommended Additions
- Add `sitemap.xml` for better search engine indexing
- Implement structured data markup (JSON-LD)
- Set up Google Analytics for performance tracking
- Add Google Search Console for monitoring

## 🚀 Performance

### Optimisation Features
- CSS custom properties for efficient styling
- Optimised images and assets
- Minimal JavaScript for core functionality
- Font display optimisation
- Print-friendly styles

### Performance Testing
Test your site with:
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [GTmetrix](https://gtmetrix.com/)
- [WebPageTest](https://www.webpagetest.org/)

## 🔒 Security & Privacy

- Static site with no server-side processing
- HTTPS enforced through GitHub Pages
- No cookies or tracking by default
- Professional email contact only

## 🤝 Professional Features

### What Makes This Portfolio Stand Out
1. **Domain Authority** - Custom domain (riera.co.uk) for professional credibility
2. **Comprehensive Documentation** - Multiple CVs and references available
3. **Technical Depth** - Showcases platform engineering expertise
4. **Professional Design** - Clean, modern interface
5. **Mobile Optimised** - Works perfectly on all devices
6. **Fast Loading** - Optimised for quick access by recruiters

### For Recruiters and Employers
- Direct access to multiple CV formats
- Professional references from EMBL-EBI colleagues
- Clear technical skills breakdown
- Quantified achievements (100+ PB managed, 1000+ hosts)
- Multiple contact methods

## 📊 Analytics (Optional)

### Adding Google Analytics
1. Create a Google Analytics account
2. Get your GA4 tracking ID
3. Add to `<head>` section in `index.html`:
   ```html
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'GA_TRACKING_ID');
   </script>
   ```

## 🛠 Local Development

### Prerequisites
- Git installed
- Web browser
- Text editor (VS Code recommended)

### Local Testing
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

## 🚨 Troubleshooting

### Common Issues

**GitHub Pages not updating:**
- Check GitHub Actions tab for deployment status
- Ensure CNAME file is in repository root
- Wait 5-10 minutes for propagation

**Documents not loading:**
- Verify PDF files are in `assets/documents/`
- Check file names match exactly in HTML links
- Ensure files are committed and pushed to GitHub

**Custom domain not working:**
- Verify DNS settings with your domain provider
- Check CNAME file contains only domain name
- DNS propagation can take up to 24 hours

**Responsive issues:**
- Test on multiple devices
- Use browser developer tools for debugging
- Check CSS media queries

## 📞 Support

For technical issues or questions:

**Joan Marc Riera Duocastella**
- **Email**: marc@riera.co.uk
- **LinkedIn**: [linkedin.com/in/joanmarcriera](https://linkedin.com/in/joanmarcriera)
- **GitHub**: [github.com/joanmarcriera](https://github.com/joanmarcriera)

## 📄 License

This project is open source and available under the MIT License.

---

*Last updated: January 2025*

**🎯 Professional Goals**: Platform Engineering Leadership • CTO Track • Large-scale Infrastructure • Bioinformatics Innovation
