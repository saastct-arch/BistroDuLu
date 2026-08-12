# Site publicável — Bistrô du Lú

Página única, mobile-first, gerada a partir de
`bistr-du-l-design-system/project/ui_kits/website/full-scroll-mobile.html`
(as colunas de documentação da prancha foram removidas; o conteúdo do site é idêntico).

- `index.html` — todas as 8 seções, CSS e tokens embutidos, sem dependências externas
  além das webfonts do Google e dos ícones Lucide via CDN.
- `img/` — fotos redimensionadas para uso web (o original fica no design system).

## Deploy

O `vercel.json` na raiz aponta `outputDirectory` para esta pasta, então basta
importar o repositório no Vercel — sem build, sem configuração extra.

## Pendências

- Três fotos da galeria (Canto reservado para dois, Adega, Fachada à noite) ainda não
  foram fornecidas e aparecem como marcadores tracejados.
- `Ver o cardápio`, `Ver menu para viagem`, `Reservar no Get In`, WhatsApp e Instagram
  apontam para `#` — faltam os destinos reais.
