import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Fonts
html = re.sub(
    r'<link[^>]*href="https://fonts\.googleapis\.com/css2\?family=[^"]*"[^>]*>',
    '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;600;700&family=Montserrat:wght@400;500;700;800&display=swap" rel="stylesheet" />',
    html
)

# 2. Update CSS
new_css = """
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      html {
        scroll-behavior: smooth;
        overflow-x: hidden;
      }
      body {
        font-family: "Montserrat", sans-serif;
        background-color: #0B1547;
        color: #FFFFFF;
        line-height: 1.5;
        -webkit-font-smoothing: antialiased;
        overflow-x: hidden;
      }
      h1, h2, h3, h4, .price, .cta-button {
        font-family: "Oswald", sans-serif;
        font-weight: 700;
        color: #FFFFFF;
        text-transform: uppercase;
        letter-spacing: 0.5px;
      }
      p {
        line-height: 1.6;
      }
      .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        position: relative;
        z-index: 2;
      }

      /* Transitions & Shapes (Soft Gradients & Borders) */
      .section-blue { background-color: #142981; color: #FFFFFF; position: relative; border-bottom: 6px solid #FFDE00;}
      .section-dark-blue { background-color: #0B1547; color: #FFFFFF; position: relative;}
      
      .gradient-transition {
        background: linear-gradient(180deg, #142981 0%, #0B1547 100%);
        border-bottom: none;
      }
      .diagonal-transition {
        clip-path: polygon(0 0, 100% 0, 100% calc(100% - 40px), 0 100%);
        padding-bottom: 140px;
        margin-bottom: -40px;
      }

      /* Top Banner */
      .top-banner {
        background: #FFDE00;
        color: #111111;
        text-align: center;
        padding: 12px 0;
        font-weight: 800;
        font-size: 1.05rem;
        letter-spacing: 1px;
        text-transform: uppercase;
        position: relative;
        z-index: 10;
        font-family: "Oswald", sans-serif;
        border-bottom: 4px solid #111111;
      }

      /* Hero */
      .hero {
        position: relative;
        min-height: auto;
        padding: 100px 0 140px;
        background-image: url("Hero-photo.png");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        display: flex;
        align-items: center;
        overflow: hidden;
        border-bottom: 8px solid #FFDE00;
      }
      .hero::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(11, 21, 71, 0.8) 0%, rgba(0, 0, 0, 0.75) 100%);
        z-index: 1;
      }
      .hero-content {
        position: relative;
        z-index: 2;
        max-width: 1000px;
        text-align: center;
        margin: 0 auto;
      }
      .hero h1 {
        font-size: clamp(2.8rem, 6vw, 5.5rem);
        margin-bottom: 25px;
        line-height: 1.1;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
      }
      .hero h1 .highlight {
        color: #FFDE00;
        display: inline;
      }
      .hero h1 .sub-highlight {
        color: #111111;
        background-color: #FFDE00;
        padding: 0 15px;
        border-radius: 4px;
        display: inline-block;
        margin-top: 5px;
        text-shadow: none;
      }
      .hero p {
        font-size: clamp(1.1rem, 2vw, 1.4rem);
        margin-bottom: 40px;
        color: #FFFFFF;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 600;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
        font-family: "Montserrat", sans-serif;
      }

      /* Botões */
      .cta-button {
        position: relative;
        background: #FFDE00;
        color: #111111;
        padding: 18px 45px;
        border: 3px solid #111111;
        border-radius: 6px;
        font-size: 1.4rem;
        font-weight: 700;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.2s ease;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        z-index: 1;
        box-shadow: 5px 5px 0px #111111;
      }
      .cta-button:hover {
        transform: translate(2px, 2px);
        background: #FFED4A;
        box-shadow: 3px 3px 0px #111111;
      }

      /* Sections General */
      section {
        padding: 80px 0;
      }
      .section-title {
        font-size: clamp(2.2rem, 4vw, 3.5rem);
        margin-bottom: 20px;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
      }
      .section-subtitle {
        text-align: center;
        font-size: clamp(1.1rem, 1.5vw, 1.25rem);
        margin-bottom: 50px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 500;
      }

      /* Form Section */
      .form-section {
        position: relative;
        margin-top: 0;
        z-index: 20;
        padding-top: 20px;
      }
      .form-container {
        background: #142981;
        border-radius: 8px;
        padding: 40px 45px;
        max-width: 850px;
        margin: -80px auto 0;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.6);
        color: #FFFFFF;
        position: relative;
        border: 4px solid #FFDE00;
      }
      .form-container h2 {
        color: #FFDE00;
        text-align: center;
        margin-bottom: 15px;
        font-size: 2.5rem;
      }
      .form-container > p {
        text-align: center;
        margin-bottom: 30px;
        color: #FFFFFF;
        font-weight: 600;
        font-size: 1.1rem;
      }
      .form-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
      }
      .form-group.full-width { grid-column: 1 / -1; }
      .form-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: 700;
        color: #FFFFFF;
        font-size: 0.95rem;
        text-transform: uppercase;
      }
      .form-group input,
      .form-group select {
        width: 100%;
        padding: 16px;
        border: 2px solid #0B1547;
        border-radius: 6px;
        background: #FFFFFF;
        color: #111111;
        font-size: 1.05rem;
        font-family: "Montserrat", sans-serif;
        font-weight: 600;
        transition: all 0.2s ease;
      }
      .form-group input::placeholder {
        color: #666666;
      }
      .form-group input:focus,
      .form-group select:focus {
        outline: none;
        border-color: #FFDE00;
        box-shadow: 0 0 0 3px rgba(255, 222, 0, 0.3);
      }
      .submit-btn {
        width: 100%;
        background: #FFDE00;
        color: #111111;
        padding: 20px;
        border: 3px solid #111111;
        border-radius: 6px;
        font-size: 1.4rem;
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.2s ease;
        margin-top: 25px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        box-shadow: 5px 5px 0px #111111;
      }
      .submit-btn:hover {
        transform: translate(2px, 2px);
        background: #FFED4A;
        box-shadow: 3px 3px 0px #111111;
      }

      /* Utilities */
      .highlight { color: #FFDE00; }

      /* PRF Stats */
      .stats {
        display: flex;
        justify-content: center;
        gap: 30px;
        flex-wrap: wrap;
      }
      .stat {
        flex: 1;
        min-width: 280px;
        background: #142981;
        padding: 40px 30px;
        border-radius: 8px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        border: 3px solid #0B1547;
        box-shadow: 4px 4px 0px #0B1547;
      }
      .stat-number {
        font-size: 5rem;
        color: #FFDE00;
        font-weight: 700;
        font-family: "Oswald", sans-serif;
        line-height: 1;
        padding: 10px 0;
        text-shadow: 2px 2px 0px #111;
      }
      .stat-text {
        font-size: 1.1rem;
        color: #FFFFFF;
        font-weight: 600;
      }

      /* Benefits */
      .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 20px;
      }
      .benefit-card {
        background: #0B1547;
        border-radius: 8px;
        padding: 30px 25px;
        text-align: left;
        display: flex;
        flex-direction: column;
        gap: 15px;
        border: 2px solid #142981;
      }
      .benefit-card i {
        font-size: 2.8rem;
        color: #FFDE00;
      }
      .benefit-card h3 {
        font-size: 1.4rem;
        font-weight: 700;
        color: #FFFFFF;
      }

      /* Risks & Solutions */
      .comparison-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 50px;
        align-items: center;
      }
      .risks-list { list-style: none; }
      .risks-list li {
        display: flex;
        align-items: center;
        margin-bottom: 12px;
        font-size: 1.2rem;
        color: #FFFFFF;
        background: #0B1547;
        padding: 15px 20px;
        border-radius: 6px;
        font-weight: 600;
        border-left: 5px solid #FFDE00;
      }
      .risks-list i {
        color: #FFDE00;
        font-size: 1.4rem;
        margin-right: 15px;
      }
      .solution-box {
        background: #FFDE00;
        padding: 40px;
        border-radius: 8px;
        color: #111111;
        box-shadow: 8px 8px 0px #0B1547;
        border: 4px solid #111111;
      }
      .solution-box h2 { color: #111111; font-size: 2.4rem; text-shadow: none;}
      .solution-box p { font-weight: 700; color: #111111; font-size: 1.15rem; }
      .check-list { list-style: none; margin-top: 25px; }
      .check-list li {
        display: flex;
        align-items: flex-start;
        margin-bottom: 15px;
        font-size: 1.15rem;
        font-weight: 800;
        line-height: 1.4;
        color: #111111;
      }
      .check-list i {
        color: #142981;
        font-size: 1.5rem;
        margin-right: 12px;
      }
      .solution-box .highlight {
        color: #142981;
      }

      /* Commercial Team */
      .commercial-content { max-width: 900px; margin: 0 auto; text-align: left; }
      .commercial-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 12px;
        margin: 35px 0;
      }
      .commercial-list-item {
        background: #142981;
        padding: 14px 18px;
        border-radius: 6px;
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.1rem;
        font-weight: 700;
        color: #FFFFFF;
        border: 2px solid #0B1547;
      }
      .commercial-list-item i {
        color: #FFDE00;
        font-size: 1.3rem;
      }

      /* Marcas Marquee */
      .brands-marquee {
        background: #0B1547;
        padding: 50px 0;
        overflow: hidden;
        white-space: nowrap;
        position: relative;
        border-top: 4px solid #FFDE00;
        border-bottom: 4px solid #FFDE00;
        margin-top: 40px;
      }
      .marquee-content {
        display: inline-flex;
        align-items: center;
        animation: marquee 30s linear infinite;
        gap: 80px;
      }
      .brand-item {
        color: #FFFFFF;
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        font-size: 2.2rem;
        text-transform: uppercase;
        opacity: 0.4;
      }
      @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

      /* FAQ */
      .faq-grid { max-width: 850px; margin: 0 auto; }
      .faq-item {
        background: #142981;
        border: 3px solid #0B1547;
        border-radius: 8px;
        margin-bottom: 12px;
        transition: all 0.2s ease;
      }
      .faq-item.active {
        background: #0B1547;
        border-color: #FFDE00;
      }
      .faq-question {
        padding: 20px 24px;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 800;
        font-size: 1.2rem;
        color: #FFFFFF;
        font-family: 'Montserrat', sans-serif;
      }
      .faq-item.active .faq-question { color: #FFDE00; }
      .faq-answer {
        padding: 0 24px 20px;
        color: #FFFFFF;
        display: none;
        line-height: 1.6;
        font-weight: 500;
        font-size: 1.05rem;
      }
      .faq-item.active .faq-answer { display: block; }

      /* Footer */
      footer {
        background: #0B1547;
        color: #FFFFFF;
        padding: 80px 0 30px;
        border-top: 8px solid #FFDE00;
      }
      .footer-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1.5fr;
        gap: 50px;
        margin-bottom: 50px;
      }
      .footer-brand h4 { font-size: 2rem; margin-bottom: 15px; color: #FFDE00; }
      .footer-brand p { font-weight: 500; opacity: 0.9; font-size: 1.05rem;}
      .footer-links h4, .footer-contact h4 { margin-bottom: 20px; color: #FFFFFF; font-size: 1.4rem;}
      .footer-links ul { list-style: none; }
      .footer-links li { margin-bottom: 10px; }
      .footer-links a { color: #FFFFFF; text-decoration: none; font-weight: 600; transition: 0.2s; font-size:1.05rem;}
      .footer-links a:hover { color: #FFDE00; }
      .footer-contact-item { display: flex; gap: 15px; margin-bottom: 15px; }
      .footer-contact-item i { color: #FFDE00; font-size: 1.5rem; padding-top: 2px; }
      .footer-contact-item p { font-weight: 800; color: #FFFFFF; margin-bottom: 2px; text-transform: uppercase; }
      .copyright {
        text-align: center;
        padding-top: 25px;
        border-top: 2px solid rgba(255,255,255,0.1);
        font-weight: 600;
        color: rgba(255,255,255,0.5);
      }

      /* Services Grid Update */
      .services-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        max-width: 1100px;
        margin: 50px auto 60px;
      }
      .service-badge {
        background: #0B1547;
        color: #FFFFFF;
        border-radius: 6px;
        font-family: "Oswald", sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 70px;
        text-align: center;
        text-transform: uppercase;
        border: 2px solid #142981;
      }

      /* Image Carousel Update */
      .carousel-container { max-width: 1240px; margin: 40px auto; position: relative; }
      .carousel-viewport { border-radius: 8px; overflow: hidden; border: 4px solid #142981; }
      .carousel-track { display: flex; transition: transform 0.6s ease; }
      .carousel-slide { min-width: 100%; border-right: 4px solid #142981;}
      @media(min-width:768px){ .carousel-slide{min-width:50%;} }
      @media(min-width:1100px){ .carousel-slide{min-width:33.333%;} }
      .carousel-slide img { width: 100%; height: 100%; object-fit: cover; }
      .carousel-btn {
        position: absolute; top: 50%; transform: translateY(-50%);
        background: #FFDE00; color: #111111; width: 55px; height: 55px;
        border-radius: 4px; border: 3px solid #111; cursor: pointer; z-index: 10;
        box-shadow: 4px 4px 0px #111; font-size: 1.4rem; transition: 0.2s;
      }
      .carousel-btn:hover { background: #FFED4A; transform: translateY(-50%) translate(2px, 2px); box-shadow: 2px 2px 0px #111; }
      .carousel-btn.prev { left: -20px; }
      .carousel-btn.next { right: -20px; }
      .carousel-nav { display: flex; justify-content: center; gap: 10px; margin-top: 25px; }
      .carousel-dot { width: 14px; height: 14px; border-radius: 0; background: #0B1547; border: 2px solid #142981; cursor: pointer; }
      .carousel-dot.active { background: #FFDE00; border-color: #111;}

      /* Responsive */
      @media (max-width: 768px) {
        .form-grid { grid-template-columns: 1fr; }
        .comparison-grid { grid-template-columns: 1fr; gap: 40px; }
        .services-grid { grid-template-columns: 1fr; }
        .footer-grid { grid-template-columns: 1fr; }
        .hero { padding: 130px 0 100px; }
        .carousel-btn.prev { left: 5px; }
        .carousel-btn.next { right: 5px; }
        section { padding: 60px 0; }
        .hero h1 { font-size: 2.5rem; }
      }
"""

html = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}\n    </style>', html, flags=re.DOTALL)

# Let's clean up section classes to match the new simple CSS (section-blue, section-dark-blue, gradient-transition)
# Using heavy traditional feel, no rounded wave patterns. Just solid gradient blocks.
# We will just alternate between section-blue and section-dark-blue.
classes_to_remove = ["section-diagonal", "section-wave-top", "section-wave-bottom", "section-white", "section-black"]
for cls in classes_to_remove:
    html = html.replace(cls, "")

# Ensure sections alternate between section-blue and section-dark-blue properly.
# We will use regex to find all <section ...> and replace their classes.
def section_replacer(match):
    full_match = match.group(0)
    # Don't touch hero since it's header, not section
    if "hero" in full_match: return full_match
    return full_match

html = re.sub(r'<section[^>]*>', section_replacer, html)

# Let's manually set the backgrounds for the sections properly by targeting the current tags.
html = html.replace('<section id="orcamento" class="form-section  section-dark-blue">', '<section id="orcamento" class="form-section section-blue">')
html = html.replace('<section class="carousel-section section-dark-blue ">', '<section class="carousel-section section-dark-blue">')
html = html.replace('<section class="stats-section  section-dark-blue">', '<section class="stats-section section-blue">')
html = html.replace('<section class="section-dark-blue ">', '<section class="section-dark-blue">')
html = html.replace('<section class="risks-section section-blue ">', '<section class="risks-section section-blue gradient-transition">')
html = html.replace('<section class="commercial-section section-dark-blue">', '<section class="commercial-section section-dark-blue">')
html = html.replace('<section class="section-dark-blue ">', '<section class="section-dark-blue">')
html = html.replace('<section class="faq-section section-blue ">', '<section class="faq-section section-blue">')

# Wait, the replacements might not match perfectly because of multiple spaces.
# It's cleaner to remove all section-* classes and just re-add background utility classes
import re
html = re.sub(r'\s*section-blue\s*', ' ', html)
html = re.sub(r'\s*section-dark-blue\s*', ' ', html)
html = re.sub(r'\s*gradient-transition\s*', ' ', html)
html = re.sub(r'\s*section-diagonal\s*', ' ', html)

# Now manually add them based on order
html = html.replace('<section id="orcamento" class="form-section">', '<section id="orcamento" class="form-section section-blue">')
html = html.replace('<section class="carousel-section">', '<section class="carousel-section section-dark-blue gradient-transition">')
html = html.replace('<section class="stats-section">', '<section class="stats-section section-blue">')
html = html.replace('<section>', '<section class="section-dark-blue">') # This is the benefits section
html = html.replace('<section class="risks-section">', '<section class="risks-section section-blue">')
html = html.replace('<section class="commercial-section">', '<section class="commercial-section section-dark-blue gradient-transition">')
html = html.replace('<section class="faq-section">', '<section class="faq-section section-blue">')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
