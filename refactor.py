import re
import sys

def go():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. We will extract the HTML body
    body_match = re.search(r'(<body.*?>)(.*?)(</body>)', html, re.DOTALL | re.IGNORECASE)
    if not body_match:
        print("Body not found.")
        return

    body_tag = body_match.group(1)
    body_content = body_match.group(2)
    end_body = body_match.group(3)

    # 2. Add classes to sections to help with fluid transitions
    # Let's apply a "section-diagonal" class to alternate sections
    
    # Hero Section
    body_content = body_content.replace('class="hero"', 'class="hero section-dark"')
    
    # Form Section
    body_content = body_content.replace('<section id="orcamento" class="form-section">', '<section id="orcamento" class="form-section section-diagonal section-blue">')
    
    # Carousel Section
    body_content = body_content.replace('<section class="carousel-section">', '<section class="carousel-section section-white section-wave-top">')
    
    # Stats Section
    body_content = body_content.replace('<section class="stats-section">', '<section class="stats-section section-diagonal section-black">')
    
    # Benefits Section
    body_content = body_content.replace('<section>', '<section class="section-white section-wave-bottom">')
    
    # Risks Section
    body_content = body_content.replace('class="risks-section"', 'class="risks-section section-blue section-diagonal"')

    # Commercial Section
    body_content = body_content.replace('class="commercial-section"', 'class="commercial-section section-white"')

    # Brands Section
    body_content = body_content.replace('<section style="background: #050814;">', '<section class="section-black section-wave-top">')

    # FAQ Section
    body_content = body_content.replace('class="faq-section"', 'class="faq-section section-blue section-diagonal"')

    # 3. Create the brand new CSS
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
        font-family: "Inter", sans-serif;
        background-color: #0033A0;
        color: #FFFFFF;
        line-height: 1.6;
        -webkit-font-smoothing: antialiased;
        overflow-x: hidden;
      }
      h1, h2, h3 {
        font-family: "Montserrat", sans-serif;
        font-weight: 900;
        color: #FFFFFF;
        text-transform: uppercase;
        letter-spacing: -0.02em;
        text-wrap: balance;
      }
      p {
        text-wrap: pretty;
        line-height: 1.6;
      }
      .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
        position: relative;
        z-index: 2;
      }

      /* Transitions & Shapes */
      .section-blue { background-color: #0033A0; color: #FFFFFF; position: relative;}
      .section-white { background-color: #FFFFFF; color: #111111; position: relative;}
      .section-white h2, .section-white h3 { color: #111111; }
      .section-white p { color: #111111; }
      .section-black { background-color: #111111; color: #FFFFFF; position: relative;}
      
      .section-diagonal {
        position: relative;
        z-index: 1;
      }
      .section-diagonal::before {
        content: '';
        position: absolute;
        top: -4vw;
        left: 0;
        width: 100%;
        height: 8vw;
        background: inherit;
        transform: skewY(-2deg);
        z-index: -1;
      }
      .section-diagonal::after {
        content: '';
        position: absolute;
        bottom: -4vw;
        left: 0;
        width: 100%;
        height: 8vw;
        background: inherit;
        transform: skewY(2deg);
        z-index: -1;
      }

      .section-wave-top::before {
        content: '';
        position: absolute;
        top: -45px;
        left: 0;
        width: 100%;
        height: 50px;
        background: inherit;
        clip-path: ellipse(60% 100% at 50% 100%);
        z-index: -1;
      }
      .section-wave-bottom::after {
        content: '';
        position: absolute;
        bottom: -45px;
        left: 0;
        width: 100%;
        height: 50px;
        background: inherit;
        clip-path: ellipse(60% 100% at 50% 0%);
        z-index: -1;
      }

      /* Top Banner */
      .top-banner {
        background: #F5C800;
        color: #111111;
        text-align: center;
        padding: 12px 0;
        font-weight: 900;
        font-size: 0.95rem;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        position: relative;
        z-index: 10;
      }

      /* Hero */
      .hero {
        position: relative;
        min-height: 80vh;
        height: auto;
        padding: 120px 0 160px;
        background-image: url("Hero-photo.png");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        overflow: hidden;
      }
      .hero::before {
        content: "";
        position: absolute;
        inset: 0;
        background: rgba(0, 0, 0, 0.65); /* Escuro com 0.65 de opacidade */
        z-index: 1;
      }
      .hero-content {
        position: relative;
        z-index: 2;
        max-width: 1500px;
        text-align: center;
        margin: 0 auto;
      }
      .hero h1 {
        font-size: clamp(2.2rem, 5.5vw, 4.8rem);
        margin-bottom: 30px;
        line-height: 1.1;
      }
      .hero h1 .highlight {
        color: #F5C800;
        display: inline;
      }
      .hero h1 .sub-highlight {
        color: #111111;
        background-color: #F5C800;
        padding: 0 10px;
        border-radius: 8px;
        display: inline-block;
        margin-top: 5px;
      }
      .hero p {
        font-size: clamp(1rem, 1.5vw, 1.25rem);
        margin-bottom: 35px;
        color: #FFFFFF;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        font-weight: 500;
      }

      /* Botões */
      .cta-button {
        position: relative;
        background: #F5C800;
        color: #111111;
        padding: 18px 45px;
        border: none;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 900;
        font-family: 'Montserrat', sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        white-space: nowrap;
        z-index: 1;
        box-shadow: 0 10px 20px -5px rgba(245, 200, 0, 0.5);
      }
      .cta-button:hover {
        transform: translateY(-4px);
        background: #FFD633;
        box-shadow: 0 15px 25px -5px rgba(245, 200, 0, 0.6);
      }

      /* Sections General */
      section {
        padding: 100px 0;
      }
      .section-title {
        font-size: clamp(2rem, 3.5vw, 2.8rem);
        margin-bottom: 20px;
        text-align: center;
      }
      .section-subtitle {
        text-align: center;
        font-size: clamp(1.1rem, 1.5vw, 1.25rem);
        margin-bottom: 60px;
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
        background: #FFFFFF;
        border-radius: 24px;
        padding: 45px 50px;
        max-width: 850px;
        margin: -100px auto 0; /* Overlap hero */
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        color: #111111;
        position: relative;
      }
      .form-container h2 {
        color: #0033A0;
        text-align: center;
        margin-bottom: 12px;
      }
      .form-container > p {
        text-align: center;
        margin-bottom: 35px;
        color: #111111;
        font-weight: 500;
      }
      .form-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 24px;
      }
      .form-group.full-width { grid-column: 1 / -1; }
      .form-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: 700;
        color: #0033A0;
        font-size: 0.90rem;
      }
      .form-group input,
      .form-group select {
        width: 100%;
        padding: 15px;
        border: 2px solid #E2E8F0;
        border-radius: 12px;
        background: #F8FAFC;
        color: #111111;
        font-size: 1rem;
        font-family: "Inter", sans-serif;
        font-weight: 600;
        transition: all 0.3s ease;
      }
      .form-group input:focus,
      .form-group select:focus {
        outline: none;
        border-color: #0033A0;
        background: #FFFFFF;
        box-shadow: 0 0 0 4px rgba(0, 51, 160, 0.1);
      }
      .submit-btn {
        width: 100%;
        background: #0033A0;
        color: #FFFFFF;
        padding: 18px;
        border: none;
        border-radius: 12px;
        font-size: 1.1rem;
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        text-transform: uppercase;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-top: 25px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        box-shadow: 0 10px 20px -5px rgba(0, 51, 160, 0.4);
      }
      .submit-btn:hover {
        transform: translateY(-2px);
        background: #002277;
      }

      /* Utilities */
      .highlight { color: #F5C800; }
      .section-white .highlight { color: #0033A0; }

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
        background: #0033A0;
        padding: 50px 40px;
        border-radius: 24px;
        transition: all 0.4s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        border: 2px solid rgba(245, 200, 0, 0.2);
      }
      .stat:hover {
        transform: translateY(-8px);
        border-color: #F5C800;
      }
      .stat-number {
        font-size: 4.5rem;
        color: #F5C800;
        font-weight: 900;
        font-family: "Montserrat";
        line-height: 1.1;
        padding: 10px 0;
      }
      .stat-text {
        font-size: 1.15rem;
        color: #FFFFFF;
        font-weight: 600;
      }

      /* Benefits */
      .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 24px;
      }
      .benefit-card {
        background: #F8FAFC;
        border-radius: 20px;
        padding: 35px 30px;
        text-align: left;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        gap: 16px;
        border: 2px solid transparent;
      }
      .benefit-card:hover {
        transform: translateY(-4px);
        border-color: #0033A0;
        box-shadow: 0 15px 30px -10px rgba(0, 51, 160, 0.2);
      }
      .benefit-card i {
        font-size: 2.5rem;
        color: #0033A0;
      }
      .benefit-card h3 {
        font-size: 1.1rem;
        font-weight: 900;
        color: #111111;
      }

      /* Risks & Solutions */
      .comparison-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 60px;
        align-items: center;
      }
      .risks-list { list-style: none; }
      .risks-list li {
        display: flex;
        align-items: center;
        margin-bottom: 16px;
        font-size: 1.15rem;
        color: #FFFFFF;
        background: rgba(17, 17, 17, 0.4);
        padding: 16px 24px;
        border-radius: 12px;
        font-weight: 600;
      }
      .risks-list i {
        color: #F5C800;
        font-size: 1.3rem;
        margin-right: 16px;
      }
      .solution-box {
        background: #F5C800;
        padding: 45px;
        border-radius: 24px;
        color: #111111;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
      }
      .solution-box h2 { color: #111111; }
      .solution-box p { font-weight: 600; }
      .check-list { list-style: none; margin-top: 30px; }
      .check-list li {
        display: flex;
        align-items: flex-start;
        margin-bottom: 18px;
        font-size: 1.1rem;
        font-weight: 700;
        line-height: 1.5;
      }
      .check-list i {
        color: #0033A0;
        font-size: 1.4rem;
        margin-right: 15px;
      }

      /* Commercial Team */
      .commercial-content { max-width: 900px; margin: 0 auto; text-align: left; }
      .commercial-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 16px;
        margin: 45px 0;
      }
      .commercial-list-item {
        background: #F8FAFC;
        padding: 16px 20px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.05rem;
        font-weight: 700;
        color: #0033A0;
        border: 1px solid #E2E8F0;
      }
      .commercial-list-item i {
        color: #F5C800;
        font-size: 1.2rem;
      }

      /* Marcas Marquee */
      .brands-marquee {
        background: #FFFFFF;
        padding: 60px 0;
        overflow: hidden;
        white-space: nowrap;
        position: relative;
        border-radius: 24px;
        margin-top: 40px;
      }
      .marquee-content {
        display: inline-flex;
        align-items: center;
        animation: marquee 40s linear infinite;
        gap: 80px;
      }
      .brand-item {
        color: #0033A0;
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        font-size: 2rem;
        text-transform: uppercase;
      }
      @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

      /* FAQ */
      .faq-grid { max-width: 850px; margin: 0 auto; }
      .faq-item {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid transparent;
        border-radius: 16px;
        margin-bottom: 16px;
        transition: all 0.3s ease;
      }
      .faq-item.active {
        background: #FFFFFF;
        border-color: #F5C800;
      }
      .faq-question {
        padding: 24px;
        cursor: pointer;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-weight: 700;
        font-size: 1.15rem;
        color: #FFFFFF;
      }
      .faq-item.active .faq-question { color: #0033A0; }
      .faq-answer {
        padding: 0 24px 24px;
        color: #111111;
        display: none;
        line-height: 1.7;
        font-weight: 500;
      }
      .faq-item.active .faq-answer { display: block; }

      /* Footer */
      footer {
        background: #111111;
        color: #FFFFFF;
        padding: 100px 0 30px;
      }
      .footer-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1.5fr;
        gap: 60px;
        margin-bottom: 60px;
      }
      .footer-brand h4 { font-size: 1.8rem; margin-bottom: 20px; color: #F5C800; }
      .footer-brand p { font-weight: 500; opacity: 0.9; }
      .footer-links h4, .footer-contact h4 { margin-bottom: 25px; color: #FFFFFF; }
      .footer-links ul { list-style: none; }
      .footer-links li { margin-bottom: 12px; }
      .footer-links a { color: rgba(255,255,255,0.8); text-decoration: none; font-weight: 600; transition: 0.3s; }
      .footer-links a:hover { color: #F5C800; }
      .footer-contact-item { display: flex; gap: 15px; margin-bottom: 20px; }
      .footer-contact-item i { color: #F5C800; font-size: 1.4rem; padding-top: 3px; }
      .footer-contact-item p { font-weight: 700; color: #FFFFFF; margin-bottom: 4px; }
      .copyright {
        text-align: center;
        padding-top: 30px;
        border-top: 1px solid rgba(255,255,255,0.1);
        font-weight: 600;
        color: rgba(255,255,255,0.6);
      }

      /* Services Grid Update */
      .services-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        max-width: 1100px;
        margin: 60px auto 80px;
      }
      .service-badge {
        background: #FFFFFF;
        color: #0033A0;
        border-radius: 16px;
        font-family: "Montserrat", sans-serif;
        font-weight: 900;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 80px;
        text-align: center;
        text-transform: uppercase;
        border: 2px solid transparent;
        transition: 0.3s;
      }
      .service-badge:hover {
        transform: translateY(-4px);
        border-color: #F5C800;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
      }

      /* Image Carousel Update */
      .carousel-container { max-width: 1240px; margin: 40px auto; position: relative; }
      .carousel-viewport { border-radius: 24px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.15); }
      .carousel-track { display: flex; transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1); }
      .carousel-slide { min-width: 100%; padding: 10px; }
      @media(min-width:768px){ .carousel-slide{min-width:50%;} }
      @media(min-width:1100px){ .carousel-slide{min-width:33.333%;} }
      .carousel-slide img { width: 100%; height: 100%; object-fit: cover; border-radius: 18px; }
      .carousel-btn {
        position: absolute; top: 50%; transform: translateY(-50%);
        background: #FFFFFF; color: #0033A0; width: 50px; height: 50px;
        border-radius: 50%; border: none; cursor: pointer; z-index: 10;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); font-size: 1.2rem; transition: 0.3s;
      }
      .carousel-btn:hover { background: #F5C800; color: #111111; transform: translateY(-50%) scale(1.1); }
      .carousel-btn.prev { left: 5px; }
      .carousel-btn.next { right: 5px; }
      .carousel-nav { display: flex; justify-content: center; gap: 12px; margin-top: 20px; }
      .carousel-dot { width: 12px; height: 12px; border-radius: 50%; background: #E2E8F0; cursor: pointer; transition: 0.3s; }
      .carousel-dot.active { background: #0033A0; transform: scale(1.3); }

      /* Responsive */
      @media (max-width: 768px) {
        .form-grid { grid-template-columns: 1fr; }
        .comparison-grid { grid-template-columns: 1fr; gap: 40px; }
        .services-grid { grid-template-columns: 1fr; }
        .footer-grid { grid-template-columns: 1fr; }
        .hero { padding: 150px 0 100px; }
      }
    """

    # 4. Replace the old <style> block
    new_html = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}\n    </style>', html, flags=re.DOTALL)
    
    # 5. Inject the updated body
    new_html = re.sub(r'<body.*?>.*?</body>', f'{body_tag}\n{body_content}\n{end_body}', new_html, flags=re.DOTALL | re.IGNORECASE)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)

go()
print("Refactoring complete.")
