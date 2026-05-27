# Thiago Pneus

Landing page para uma borracharia, com formulário de captação de leads integrado ao CRM Kommo e rastreamento de conversões via Google Tag Manager.

## Visualizar

[ohigorsant.github.io/thiago-pneus](https://ohigorsant.github.io/thiago-pneus/)

Nota: o layout completo é exibido pelo GitHub Pages. O formulário de envio de leads requer servidor com PHP.

## Funcionalidades

- Formulário de orçamento com campos: veículo, quantidade de pneus, tipo de instalação e urgência
- Envio de leads ao CRM Kommo via bridge PHP
- Rastreamento de eventos via dataLayer para Google Tag Manager e Meta Ads
- Captura de parâmetros UTM por URL
- Layout responsivo

## Tecnologias

- HTML, CSS e JavaScript
- PHP (integração com CRM)
- Google Tag Manager com eventos customizados no dataLayer
- Kommo CRM via API REST

## Arquitetura de integração

```
Formulário (JS)
  ├── datalayer_events.js  ->  dispara eventos GTM (form_submit, UTMs)
  └── fetch POST           ->  kommo_bridge.php  ->  API Kommo  ->  cria lead no CRM
```

## Contexto

Projeto freelance com rastreamento de conversão completo. As credenciais de API são carregadas via `.env` no servidor e não estão incluídas neste repositório.