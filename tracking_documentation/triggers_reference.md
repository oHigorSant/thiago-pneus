# GTM Tracking Reference - Thiago Pneus

Este documento serve como guia de referência para a configuração do container GTM e verificação do tracking instalado.

## 1. Acionadores (Triggers)

| Acionador | Tipo GTM | Condição/Filtro | Tags Vinculadas |
|-----------|----------|-----------------|-----------------|
| [Acionador] - Janela Carregada | Janela carregada | Nenhuma | [Meta Ads] - Page Performance, [GA4] - Page Performance, [Script] - Contador de Visitas |
| [Acionador] - Scroll Depth | Profundidade de rolagem | 25, 50, 75, 90% | [Meta Ads] - Evento - Scroll, [GA4] - Evento - Scroll |
| [Acionador] - 30 Segundos na Pagina | Timer | 30000ms (1 vez) | [Meta Ads] - Evento - Engaged User, [GA4] - Evento - Engaged User |
| [Acionador] - Clique Whatsapp | Clique - Todos os elementos | Click Element: `a[href*='wa.me'], .fa-whatsapp` | [Meta Ads] - Evento - Click Whatsapp, [GA4] - Evento - Click Whatsapp |
| [Acionador] - Clique Link Externo | Clique - Apenas links | Click URL não contém `{{Page Hostname}}` | [Meta Ads] - Evento - Outbound Click, [GA4] - Evento - Outbound Click |
| [Acionador] - Cliques em Botões e Menus | Clique - Todos os elementos | Click Classes (RegEx): `btn\|button\|menu\|nav\|cta\|submit-btn` | Tags de Clique gerais |
| [Acionador] - Envio de Formulário | Envio de formulário | Form ID: `contactForm` | [Meta Ads] - Evento - Lead, [GA4] - Evento - Lead |
| [Acionador] - Clique Badge Servico | Clique - Todos os elementos | Click Classes: `service-badge\|benefit-card` | [Meta Ads] - Evento - ViewContent, [GA4] - Evento - ViewContent |

## 2. Variáveis

| Variável | Tipo GTM | Descrição |
|----------|----------|-----------|
| [Meta Ads] - Pixel ID | Permanente | 1614247633167400 |
| GA4 - ID | Permanente | G-WQGDDWYTV5 |
| [URL] - utm_* | URL | Parâmetros de campanha na URL (source, medium, etc.) |
| [DLV] - Lead Nome | DataLayer | Valor do campo `nome` do formulário |
| [DLV] - Lead Telefone | DataLayer | Valor do campo `tel` do formulário |
| [DLV] - Lead Mensagem | DataLayer | Concatenado de Veículo, Qtd, Instalação e Urgência |
| [DLV] - Event Label | DataLayer | Texto do elemento clicado ou nome do evento |
| [JS] - Tempo de Carregamento | Custom JS | Tempo de carregamento da página em ms |
| [JS] - Tipo de Usuario | Custom JS | Retorna 'recorrente' ou 'novo' baseado no localStorage |

## 3. Dados Capturados por Evento

### Evento: Lead (Envio de Formulário)
- **Campos capturados**: `nome`, `tel`, `veiculo`, `qtd`, `instalacao`, `quando`.
- **UTMs**: Capturadas via DataLayer no momento do submit.
- **Evento Meta**: `Lead`
- **Evento GA4**: `form_submit`

### Evento: Contact (Clique WhatsApp)
- **Localização**: Hero, Footer e ícones flutuantes.
- **UTMs**: Capturadas via URL Variables.
- **Evento Meta**: `Contact`
- **Evento GA4**: `whatsapp_click`

### Evento: ViewContent (Badges de Serviço)
- **Badges**: Pneus, Alinhamento, Balanceamento, Suspensão, Freios, etc.
- **Evento Meta**: `ViewContent`
- **Evento GA4**: `view_content`

## 4. Checklist de Instalação

- [ ] Snippet GTM instalado no `<head>` e `<body>` de `index.html`.
- [ ] Script `datalayer_events.js` carregado antes do GTM ou injetado via Custom HTML.
- [ ] Pixel Base Meta confirmado no GTM Preview (PageView em todas as páginas).
- [ ] GA4 TAG ID confirmado no GTM Preview.
- [ ] Evento `Lead` confirmado no console (`dataLayer.push`) ao enviar o formulário.
- [ ] UTMs chegando no dataLayer ao testar com URL: `?utm_source=teste_antigravity`.
- [ ] Evento `ViewContent` disparando ao clicar nos badges de serviço.
- [ ] Evento `Lead` refletido no Pixel Helper do Facebook.
- [ ] Versão publicada no container GTM.
