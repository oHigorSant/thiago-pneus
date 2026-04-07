const fs = require('fs');

const htmlFile = 'C:/Users/Higor Sant\'Anna/Desktop/Thiago Pneus/index.html';
const cssFile = 'C:/Users/Higor Sant\'Anna/Desktop/Thiago Pneus/new_styles.css';

let html = fs.readFileSync(htmlFile, 'utf8');
const css = fs.readFileSync(cssFile, 'utf8');

// Replace styles
html = html.replace(/<style>[\s\S]*?<\/style>/, `<style>\n${css}\n    </style>`);

// Fix inline styles in HTML
html = html.replace(
  `style="color: #eab308; font-size: 0.85rem; margin-top: 15px; text-decoration: none; font-weight: 600; opacity: 0.8;"`,
  `style="color: #FFDE00; font-size: 0.95rem; margin-top: 15px; text-decoration: underline; font-weight: 900;"`
);

html = html.replace(
  `style="border-color: rgba(239, 68, 68, 0.4);"`,
  `style="border-color: #ef4444; border-width: 4px;"`
);

html = html.replace(
  `style="background: linear-gradient(135deg, #fca5a5 0%, #ef4444 100%); -webkit-background-clip: text; background-clip: text; color: transparent;"`,
  `style="color: #ef4444;"`
);

html = html.replace(
  `style="color: #ef4444; font-size: 0.85rem; margin-top: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;"`,
  `style="color: #ef4444; font-size: 1rem; margin-top: 15px; font-weight: 900; text-transform: uppercase;"`
);

html = html.replace(
  `style="text-align: left; font-size: 2rem"`,
  `style="text-align: left; font-size: 2.2rem"`
);

html = html.replace(
  `style="font-size: 1.2rem; margin-bottom: 20px; color: #eab308; font-weight: 700;"`,
  `style="font-size: 1.25rem; margin-bottom: 20px; color: #FFDE00; font-weight: 900; text-transform: uppercase;"`
);

html = html.replace(
  `style="color: #94a3b8; font-size: 1.1rem;"`,
  `style="color: #cbd5e1; font-size: 1.1rem; font-weight: 700;"`
);

html = html.replace(
  `style="width: 100%; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.05); object-fit: cover; aspect-ratio: 4/3;"`,
  `style="width: 100%; border: 5px solid #112360; box-shadow: 10px 10px 0px #000000; object-fit: cover; aspect-ratio: 4/3;"`
);

// Form background remove inline
html = html.replace(
  `style="background: #112360; border: 4px solid #FFDE00; border-radius: 6px; padding: 45px 50px; max-width: 850px; margin: 0 auto; box-shadow: 0 15px 25px rgba(0, 0, 0, 0.4);"`,
  `style="background: #0a1338; border: 4px solid #FFDE00; border-radius: 0; padding: 45px 50px; max-width: 850px; margin: 0 auto; box-shadow: 10px 10px 0px #000000;"`
);

// Footer socials
html = html.replace(
  `<a href="#" style="color: #94a3b8; font-size: 1.5rem; transition: 0.3s;"><i class="fab fa-instagram"></i></a>
              <a href="#" style="color: #94a3b8; font-size: 1.5rem; transition: 0.3s;"><i class="fab fa-facebook"></i></a>
              <a href="#" style="color: #3b82f6; font-size: 1.5rem; transition: 0.3s;"><i class="fab fa-whatsapp"></i></a>`,
  `<a href="#" style="color: #ffffff; font-size: 1.5rem; transition: 0.3s;"><i class="fab fa-instagram"></i></a>
              <a href="#" style="color: #ffffff; font-size: 1.5rem; transition: 0.3s;"><i class="fab fa-facebook"></i></a>
              <a href="#" style="color: #FFDE00; font-size: 1.5rem; transition: 0.3s;"><i class="fab fa-whatsapp"></i></a>`
);

fs.writeFileSync(htmlFile, html, 'utf8');

console.log('Successfully updated HTML styles and inline tags for dark theme.');
