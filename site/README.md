# Site publicável — Bistrô du Lú

Duas páginas, mobile-first, geradas por `build.py` a partir de
`bistr-du-l-design-system/project/ui_kits/website/full-scroll-mobile.html`
(as colunas de documentação da prancha são removidas; o conteúdo do site é idêntico).

- `index.html` — primeira dobra, cozinha, ambientes, história (com os vinhos), reservas,
  peça em casa, localização e rodapé. CSS e tokens embutidos; só as webfonts vêm do Google.
- `cardapio.html` — cardápio completo, com a mesma navegação e o mesmo rodapé.
- `img/` — fotos redimensionadas para uso web (o original fica no design system).

Para gerar de novo: `cd bistr-du-l-design-system/project && python3 ../../site/build.py`
(requer Pillow). Não edite os `.html` daqui à mão — o build sobrescreve.

## Identidade

Segue as *Diretrizes obrigatórias de identidade visual e copywriting* (out/2026):

- **Vinho estrutural.** `#4E1517`, o mesmo tom do logo, abre a página, volta como bordô
  em Ambientes, vira painel na história, fundo inteiro em Reservas e fecha no rodapé.
  O marfim (`--marfim`) dá as áreas claras de leitura; o carvão aparece em Localização.
- **Botão de reserva vinho**, letra marfim. Sobre fundo vinho ele se inverte (marfim com
  letra vinho). Secundário é sempre contorno. O verde garrafa saiu da interface.
- **Fotos sem filtro.** Nenhuma foto recebe véu vinho; legendas usam degradê neutro.
- **Texto.** Caixa alta só em marcadores e rótulos. Nenhum fato novo: pratos, salas,
  horários e a história vêm do que a casa já publicou.

Todas as cores ficam em `bistr-du-l-design-system/project/tokens/colors.css`.

## Deploy

O `vercel.json` na raiz aponta `outputDirectory` para esta pasta, então basta
importar o repositório no Vercel — sem build, sem configuração extra.

## Para confirmar com a casa

- Bolinho de Cupim, Torresmo de Barriga, Bolo de Cenoura e Tal do Pudim aparecem no
  carrossel da home (fotos das Dicas do Lú), mas não constam do cardápio atual.
- O ceviche do carrossel foi nomeado "Ceviche de Tilápia", o único ceviche do cardápio.
- Salada Pesto está a R$ 3 na fonte recebida — parece faltar um dígito.
