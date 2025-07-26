# Create comprehensive CSS for the professional website
css_content = '''/* Modern Professional CSS for Marc Riera's GitHub Pages */

:root {
    --primary-color: #2563eb;
    --primary-dark: #1d4ed8;
    --secondary-color: #64748b;
    --accent-color: #0ea5e9;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --text-light: #94a3b8;
    --background: #ffffff;
    --background-alt: #f8fafc;
    --border-color: #e2e8f0;
    --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    --border-radius: 8px;
    --border-radius-lg: 12px;
    --transition: all 0.3s ease;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: var(--text-primary);
    background-color: var(--background);
}

/* Typography */
h1 {
    font-size: 3.5rem;
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 1rem;
}

h2 {
    font-size: 2.5rem;
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 1.5rem;
}

h3 {
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.3;
    margin-bottom: 1rem;
}

h4 {
    font-size: 1.25rem;
    font-weight: 500;
    color: var(--primary-color);
    margin-bottom: 0.5rem;
}

p {
    margin-bottom: 1rem;
    color: var(--text-secondary);
}

.lead {
    font-size: 1.25rem;
    font-weight: 400;
    color: var(--text-primary);
    margin-bottom: 2rem;
}

/* Hero Section */
.hero {
    height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a" cx="0.5" cy="0.5"><stop offset="0%" stop-color="%23ffffff" stop-opacity="0.1"/><stop offset="100%" stop-color="%23000000" stop-opacity="0.05"/></radialGradient></defs><rect width="100%" height="100%" fill="url(%23a)"/></svg>');
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(30, 41, 59, 0.4);
    z-index: 1;
}

.hero-overlay {
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.hero-content {
    text-align: center;
}

.profile-section {
    color: white;
}

.profile-text h1 {
    color: white;
    margin-bottom: 0.5rem;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.profile-text h2 {
    color: rgba(255, 255, 255, 0.9);
    font-weight: 400;
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.tagline {
    font-size: 1.125rem;
    color: rgba(255, 255, 255, 0.8);
    margin-bottom: 2.5rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.contact-links {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.contact-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    background: rgba(255, 255, 255, 0.1);
    color: white;
    text-decoration: none;
    border-radius: var(--border-radius);
    font-weight: 500;
    transition: var(--transition);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.contact-btn:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
}

/* Navigation */
.navigation {
    position: sticky;
    top: 0;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    z-index: 100;
    border-bottom: 1px solid var(--border-color);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
}

.nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: var(--border-radius);
    transition: var(--transition);
}

.nav-link:hover,
.nav-link.active {
    color: var(--primary-color);
    background: rgba(37, 99, 235, 0.1);
}

/* Container */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

/* Sections */
.section {
    padding: 4rem 0;
    border-bottom: 1px solid var(--border-color);
}

.section:last-child {
    border-bottom: none;
}

.section-title {
    text-align: center;
    color: var(--text-primary);
    margin-bottom: 3rem;
    position: relative;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -1rem;
    left: 50%;
    transform: translateX(-50%);
    width: 4rem;
    height: 3px;
    background: var(--primary-color);
    border-radius: 2px;
}

.section-description {
    text-align: center;
    font-size: 1.125rem;
    color: var(--text-secondary);
    margin-bottom: 3rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* About Section */
.about-content {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 4rem;
    align-items: center;
}

.highlight-list {
    list-style: none;
    margin: 2rem 0;
}

.highlight-list li {
    padding: 0.75rem 0;
    border-bottom: 1px solid var(--border-color);
    color: var(--text-secondary);
}

.highlight-list li:last-child {
    border-bottom: none;
}

.highlight-list strong {
    color: var(--primary-color);
}

.stats-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
}

.stat-item {
    text-align: center;
    padding: 2rem;
    background: var(--background-alt);
    border-radius: var(--border-radius-lg);
    border: 1px solid var(--border-color);
}

.stat-number {
    display: block;
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 0.5rem;
}

.stat-label {
    color: var(--text-secondary);
    font-weight: 500;
    font-size: 0.9rem;
}

/* Timeline */
.timeline {
    position: relative;
    padding-left: 2rem;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--border-color);
}

.timeline-item {
    position: relative;
    margin-bottom: 3rem;
    padding-left: 3rem;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -3rem;
    top: 0.5rem;
    width: 12px;
    height: 12px;
    background: var(--primary-color);
    border-radius: 50%;
    border: 3px solid var(--background);
    box-shadow: 0 0 0 3px var(--border-color);
}

.timeline-date {
    color: var(--primary-color);
    font-weight: 600;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}

.timeline-content h3 {
    color: var(--text-primary);
    margin-bottom: 0.25rem;
}

.timeline-content ul {
    margin-top: 1rem;
    color: var(--text-secondary);
}

.timeline-content li {
    margin-bottom: 0.5rem;
}

/* Skills Grid */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}

.skill-category {
    background: var(--background-alt);
    padding: 2rem;
    border-radius: var(--border-radius-lg);
    border: 1px solid var(--border-color);
    transition: var(--transition);
}

.skill-category:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

.skill-category h3 {
    color: var(--primary-color);
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1.5rem;
}

.skill-category i {
    font-size: 1.25rem;
}

.skill-category ul {
    list-style: none;
}

.skill-category li {
    padding: 0.5rem 0;
    color: var(--text-secondary);
    border-bottom: 1px solid var(--border-color);
}

.skill-category li:last-child {
    border-bottom: none;
}

/* Achievements Grid */
.achievements-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
}

.achievement-item {
    background: var(--background-alt);
    padding: 2rem;
    border-radius: var(--border-radius-lg);
    border: 1px solid var(--border-color);
    text-align: center;
    transition: var(--transition);
}

.achievement-item:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}

.achievement-icon {
    width: 4rem;
    height: 4rem;
    background: var(--primary-color);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    color: white;
    font-size: 1.5rem;
}

/* Documents Grid */
.documents-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.document-item {
    background: var(--background-alt);
    padding: 2rem;
    border-radius: var(--border-radius-lg);
    border: 1px solid var(--border-color);
    text-align: center;
    transition: var(--transition);
}

.document-item:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.document-icon {
    width: 3rem;
    height: 3rem;
    background: var(--accent-color);
    border-radius: var(--border-radius);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1rem;
    color: white;
    font-size: 1.25rem;
}

.document-item h3 {
    margin-bottom: 0.5rem;
    color: var(--text-primary);
}

.document-item p {
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
}

.download-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    background: var(--primary-color);
    color: white;
    text-decoration: none;
    border-radius: var(--border-radius);
    font-weight: 500;
    transition: var(--transition);
}

.download-btn:hover {
    background: var(--primary-dark);
    transform: translateY(-1px);
}

/* Contact Section */
.contact-content {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 4rem;
}

.contact-methods {
    margin-top: 2rem;
}

.contact-method {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 0;
    border-bottom: 1px solid var(--border-color);
}

.contact-method:last-child {
    border-bottom: none;
}

.contact-method i {
    color: var(--primary-color);
    font-size: 1.25rem;
    width: 1.5rem;
}

.contact-method a {
    color: var(--primary-color);
    text-decoration: none;
}

.contact-method a:hover {
    text-decoration: underline;
}

.location-info {
    background: var(--background-alt);
    padding: 2rem;
    border-radius: var(--border-radius-lg);
    border: 1px solid var(--border-color);
    height: fit-content;
}

.location-info p {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.location-info i {
    color: var(--primary-color);
}

/* Footer */
.footer {
    background: var(--background-alt);
    border-top: 1px solid var(--border-color);
    padding: 2rem 0;
    text-align: center;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.footer p {
    color: var(--text-light);
    margin-bottom: 0.5rem;
}

.footer a {
    color: var(--primary-color);
    text-decoration: none;
}

.footer a:hover {
    text-decoration: underline;
}

/* Responsive Design */
@media (max-width: 768px) {
    h1 { font-size: 2.5rem; }
    h2 { font-size: 2rem; }
    
    .hero {
        height: 80vh;
        padding: 2rem 0;
    }
    
    .nav-container {
        padding: 1rem;
        gap: 1rem;
    }
    
    .container {
        padding: 0 1rem;
    }
    
    .section {
        padding: 3rem 0;
    }
    
    .about-content,
    .contact-content {
        grid-template-columns: 1fr;
    }
    
    .stats-grid {
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    }
    
    .timeline {
        padding-left: 1rem;
    }
    
    .timeline-item {
        padding-left: 2rem;
    }
    
    .timeline-item::before {
        left: -2rem;
    }
    
    .contact-links {
        flex-direction: column;
        align-items: center;
    }
    
    .contact-btn {
        width: 100%;
        max-width: 250px;
        justify-content: center;
    }
}

@media (max-width: 480px) {
    h1 { font-size: 2rem; }
    
    .hero {
        height: 70vh;
    }
    
    .section {
        padding: 2rem 0;
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    .stat-item {
        padding: 1.5rem;
    }
    
    .achievements-grid,
    .documents-grid {
        grid-template-columns: 1fr;
    }
}

/* Smooth animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.section {
    animation: fadeInUp 0.6s ease-out;
}

/* Print styles */
@media print {
    .hero,
    .navigation,
    .footer {
        display: none;
    }
    
    .section {
        page-break-inside: avoid;
        padding: 1rem 0;
        border-bottom: none;
    }
    
    .container {
        max-width: none;
        padding: 0;
    }
    
    body {
        font-size: 12pt;
        line-height: 1.4;
    }
    
    h1, h2, h3, h4 {
        page-break-after: avoid;
    }
}'''

print("CSS file created successfully!")
print(f"Length: {len(css_content)} characters")