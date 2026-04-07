with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace HTML classes
html = html.replace('section-white', 'section-dark-blue')
html = html.replace('section-black', 'section-dark-blue')

# Replace Transitions & Shapes CSS
old_shapes_css = """      /* Transitions & Shapes */
      .section-blue { background-color: #0033A0; color: #FFFFFF; position: relative;}
      .section-white { background-color: #FFFFFF; color: #111111; position: relative;}
      .section-white h2, .section-white h3 { color: #111111; }
      .section-white p { color: #111111; }
      .section-black { background-color: #111111; color: #FFFFFF; position: relative;}"""

new_shapes_css = """      /* Transitions & Shapes */
      .section-blue { background-color: #0033A0; color: #FFFFFF; position: relative;}
      .section-dark-blue { background-color: #001E5E; color: #FFFFFF; position: relative;}
      .section-dark-blue h2, .section-dark-blue h3 { color: #FFFFFF; }
      .section-dark-blue p { color: #FFFFFF; }"""

html = html.replace(old_shapes_css, new_shapes_css)

# Fix Form Container
old_form = """      .form-container {
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
      }"""

new_form = """      .form-container {
        background: #001E5E;
        border-radius: 24px;
        padding: 45px 50px;
        max-width: 850px;
        margin: -100px auto 0; /* Overlap hero */
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        color: #FFFFFF;
        position: relative;
        border: 2px solid #0033A0;
      }
      .form-container h2 {
        color: #F5C800;
        text-align: center;
        margin-bottom: 12px;
      }
      .form-container > p {
        text-align: center;
        margin-bottom: 35px;
        color: #FFFFFF;
        font-weight: 500;
      }"""

html = html.replace(old_form, new_form)

# Inputs
old_inputs = """      .form-group label {
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
      }"""

new_inputs = """      .form-group label {
        display: block;
        margin-bottom: 8px;
        font-weight: 700;
        color: #FFFFFF;
        font-size: 0.90rem;
      }
      .form-group input,
      .form-group select {
        width: 100%;
        padding: 15px;
        border: 2px solid #0033A0;
        border-radius: 12px;
        background: #0033A0;
        color: #FFFFFF;
        font-size: 1rem;
        font-family: "Inter", sans-serif;
        font-weight: 600;
        transition: all 0.3s ease;
      }
      .form-group input::placeholder {
        color: rgba(255, 255, 255, 0.6);
      }
      .form-group input:focus,
      .form-group select:focus {
        outline: none;
        border-color: #F5C800;
        background: #001A52;
        box-shadow: 0 0 0 4px rgba(245, 200, 0, 0.1);
      }
      .form-group select option {
        background: #0033A0;
        color: #FFFFFF;
      }"""

html = html.replace(old_inputs, new_inputs)

# Utils highlight class
old_utils = """.highlight { color: #F5C800; }
      .section-white .highlight { color: #0033A0; }"""
new_utils = """.highlight { color: #F5C800; }"""
html = html.replace(old_utils, new_utils)

# Benefits Card
old_benefit = """      .benefit-card {
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
      }"""

new_benefit = """      .benefit-card {
        background: #0033A0;
        border-radius: 20px;
        padding: 35px 30px;
        text-align: left;
        transition: all 0.3s ease;
        display: flex;
        flex-direction: column;
        gap: 16px;
        border: 2px solid rgba(255,255,255,0.05);
      }
      .benefit-card:hover {
        transform: translateY(-4px);
        border-color: #F5C800;
        box-shadow: 0 15px 30px -10px rgba(0, 0, 0, 0.4);
      }
      .benefit-card i {
        font-size: 2.5rem;
        color: #F5C800;
      }
      .benefit-card h3 {
        font-size: 1.1rem;
        font-weight: 900;
        color: #FFFFFF;
      }"""
html = html.replace(old_benefit, new_benefit)

# Commercial List
old_commercial = """      .commercial-list-item {
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
      }"""

new_commercial = """      .commercial-list-item {
        background: #0033A0;
        padding: 16px 20px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.05rem;
        font-weight: 700;
        color: #FFFFFF;
        border: 1px solid rgba(255,255,255,0.1);
      }"""
html = html.replace(old_commercial, new_commercial)

# Brands Marquee
old_marquee = """      .brands-marquee {
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
      }"""

new_marquee = """      .brands-marquee {
        background: #0033A0;
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
        color: #FFFFFF;
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        font-size: 2rem;
        text-transform: uppercase;
        opacity: 0.5;
      }"""
html = html.replace(old_marquee, new_marquee)

# Service Badge
old_badge = """      .service-badge {
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
      }"""

new_badge = """      .service-badge {
        background: rgba(255,255,255,0.05);
        color: #FFFFFF;
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
      }"""
html = html.replace(old_badge, new_badge)

# Carousel button
old_carousel_btn = """      .carousel-btn {
        position: absolute; top: 50%; transform: translateY(-50%);
        background: #FFFFFF; color: #0033A0; width: 50px; height: 50px;
        border-radius: 50%; border: none; cursor: pointer; z-index: 10;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); font-size: 1.2rem; transition: 0.3s;
      }"""

new_carousel_btn = """      .carousel-btn {
        position: absolute; top: 50%; transform: translateY(-50%);
        background: #0033A0; color: #FFFFFF; width: 50px; height: 50px;
        border-radius: 50%; border: 2px solid rgba(255,255,255,0.2); cursor: pointer; z-index: 10;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4); font-size: 1.2rem; transition: 0.3s;
      }"""
html = html.replace(old_carousel_btn, new_carousel_btn)

# Footer background
# I will leave the footer logic unchanged except the black color to dark blue `#001133` so it stays blue.
old_footer = """      footer {
        background: #111111;
        color: #FFFFFF;
        padding: 100px 0 30px;
      }"""
new_footer = """      footer {
        background: #000F2E;
        color: #FFFFFF;
        padding: 100px 0 30px;
      }"""
html = html.replace(old_footer, new_footer)

html = html.replace('p style="color: #111111; font-size: 1.1rem;"', 'p style="color: #FFFFFF; font-size: 1.1rem;"')
html = html.replace('p style="font-size: 1.2rem; margin-bottom: 20px; color: #0033A0; font-weight: 700;"', 'p style="font-size: 1.2rem; margin-bottom: 20px; color: #F5C800; font-weight: 700;"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
