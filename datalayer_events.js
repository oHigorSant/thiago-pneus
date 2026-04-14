/**
 * TRACKING DATALAYER - THIAGO PNEUS
 * Meta Ads (Principal) & GA4 (Complementar)
 * Instalação: Adicionar este script antes da tag GTM ou via GTM Custom HTML (com acionador Janela Carregada)
 */

(function() {
  window.dataLayer = window.dataLayer || [];

  // 1. [Meta Ads] - Evento - Lead / [GA4] - Evento - Lead
  // Acionador: [Acionador] - Envio de Formulário
  var contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function() {
      var formData = new FormData(contactForm);
      var urlParams = new URLSearchParams(window.location.search);
      
      var leadData = {
        event: 'form_submit',
        event_category: 'conversion',
        event_label: 'Solicitar Orçamento',
        
        // Dados capturados conforme index.html
        form_id: 'contactForm',
        form_name: 'Solicitar Orçamento',
        lead_name: formData.get('nome') || '',
        lead_email: '', // Não existe campo email no formulário
        lead_phone: formData.get('tel') || '',
        lead_message: 'Veículo: ' + (formData.get('veiculo') || '') + ' | Pneus: ' + (formData.get('qtd') || '') + ' | Instalação: ' + (formData.get('instalacao') || '') + ' | Quando: ' + (formData.get('quando') || ''),
        lead_service: formData.get('veiculo') || '', // Usando veículo como proxy de serviço se aplicável
        
        // UTMs no momento do envio (via DLV)
        utm_source: urlParams.get('utm_source') || '',
        utm_medium: urlParams.get('utm_medium') || '',
        utm_campaign: urlParams.get('utm_campaign') || '',
        utm_term: urlParams.get('utm_term') || '',
        utm_content: urlParams.get('utm_content') || '',
        
        // Contexto
        page_location: window.location.pathname,
        page_referrer: document.referrer
      };

      window.dataLayer.push(leadData);
    });
  }

  // 2. [Meta Ads] - Evento - Click Whatsapp / [GA4] - Evento - Click Whatsapp
  // Acionador: [Acionador] - Clique Whatsapp
  document.querySelectorAll("a[href*='wa.me'], a[href*='whatsapp.com'], .fa-whatsapp").forEach(function(el) {
    el.addEventListener('click', function() {
      var urlParams = new URLSearchParams(window.location.search);
      window.dataLayer.push({
        event: 'whatsapp_click',
        event_category: 'engagement',
        event_label: el.innerText.trim() || 'WhatsApp Icon',
        
        // UTMs capturados
        utm_source: urlParams.get('utm_source') || '',
        utm_medium: urlParams.get('utm_medium') || '',
        utm_campaign: urlParams.get('utm_campaign') || '',
        
        page_location: window.location.pathname
      });
    });
  });

  // 3. [Meta Ads] - Evento - ViewContent / [GA4] - Evento - ViewContent
  // Acionador: [Acionador] - Clique Badge Servico
  document.querySelectorAll(".service-badge, .benefit-card").forEach(function(el) {
    el.addEventListener('click', function() {
      window.dataLayer.push({
        event: 'view_content',
        event_category: 'engagement',
        event_label: el.innerText.trim() || 'Service Badge',
        content_name: el.innerText.trim() || 'Service',
        page_location: window.location.pathname
      });
    });
  });

  // 4. Scripts Auxiliares - Contador de Visitas
  // Armazena no localStorage para usar na variável [JS] - Tipo de Usuario
  (function() {
    var visits = parseInt(localStorage.getItem('gtm_visits') || 0);
    localStorage.setItem('gtm_visits', visits + 1);
  })();

})();
