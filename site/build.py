#!/usr/bin/env python3
"""Gera site/index.html a partir do mockup do design system.

O mockup `full-scroll-mobile.html` é uma prancha de revisão: o site vive dentro
de um frame de 390x880 cercado por colunas de legenda, notas e o painel de ritmo.
Este script extrai o conteúdo do frame, troca o modelo de rolagem interna pela
rolagem do documento e acrescenta as composições de desktop aprovadas nos
mockups de 1180px (hero/about/gallery/reservation/delivery/contact.html).

Uso:  cd bistr-du-l-design-system/project && python3 ../../site/build.py
Requer Pillow para redimensionar as fotos.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = "ui_kits/website/full-scroll-mobile.html"
TOKENS = ["fonts.css", "colors.css", "typography.css", "spacing.css", "borders.css", "motion.css"]

# foto de origem -> (arquivo em site/img, largura máxima)
PHOTOS = {
    # hero da home (vídeo cobre) e hero do cardápio
    "465473846_18356323819184475_715987668432-msqcws7i-3w8b.jpg": ("hero.jpg", 1800),
    "whatsapp-image-2026-08-12-at-07-48-28-msqclhdg-j8en.jpeg": ("sobre.jpg", 1200),
    # Ambientes — seis salas, uma por vaga do mosaico
    "amb-sala-vermelha.jpg": ("amb-sala-vermelha.jpg", 1100),
    "amb-sala-azul.jpg": ("amb-sala-azul.jpg", 1100),
    "amb-sala-do-lustre.jpg": ("amb-sala-do-lustre.jpg", 1100),
    "amb-pergolado.jpg": ("amb-pergolado.jpg", 1300),
    "amb-sala-dos-pratos.jpg": ("amb-sala-dos-pratos.jpg", 1100),
    "amb-sala-labirinto.jpg": ("amb-sala-labirinto.jpg", 1100),
}
LOGOS = {"assets/logo-topo.png": ("logo-topo.png", 320), "assets/logo-monogram-areia.png": ("logo.png", 160)}

MENU_SVG = ('<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>')
CLOSE_SVG = ('<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" '
             'stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>')

DESKTOP_CSS = """
/* ============ DESKTOP — composições aprovadas nos mockups de 1180px ============ */
@media(min-width:1024px){
.phone{max-width:none}
.hd-m{height:var(--header-h-desktop);padding:0 var(--gutter-desktop);grid-template-columns:auto 1fr auto;gap:40px}
.hd-m .burger{display:none}
.hd-m img.mark{height:46px;justify-self:start}
.nav-d{display:flex;gap:34px;align-items:center;justify-self:end}
.nav-d a{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--areia-a80);transition:var(--t-color)}
.nav-d a:hover{color:var(--terracota-suave)}
.hd-m .cta{padding:14px 26px;font-size:12.5px}
/* hero — foto full-bleed, texto sobre a metade inferior */
.heroM{height:760px}
.heroM .copy{left:var(--gutter-desktop);right:var(--gutter-desktop);bottom:72px;gap:30px}
.heroM .wordmark{width:360px;margin:0;justify-self:start}
.heroM .cta{width:auto;padding:19px 34px;font-size:15px}
.heroM .meta{font-size:12px}
/* sobre — texto à esquerda, retrato sangrando à direita */
.abM{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,44%);align-items:stretch}
.abM .shot{order:2;height:auto;min-height:640px;border-bottom:0;border-left:1px solid var(--verde-garrafa)}
.abM .copy{order:1;align-self:center;padding:100px var(--s-7) 100px var(--gutter-desktop)}
.abM h2{font-size:52px;margin:18px 0 26px}
.abM p{font-size:17px;max-width:56ch}
.people{grid-template-columns:1fr 1fr;column-gap:44px;margin-top:44px}
.people .p{border-bottom:0}
/* ambientes — mosaico de três colunas, como no mockup de 1180 */
.galM{padding:104px 0 68px}
.galM .head{padding:0 var(--gutter-desktop);max-width:none;margin-bottom:48px;
  display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:60px;align-items:end}
.galM .head .eyebrow{grid-column:1;grid-row:1}
.galM h2{grid-column:1;grid-row:2;font-size:44px;margin:16px 0 0;max-width:20ch}
.galM .head p{grid-column:2;grid-row:2;justify-self:end;max-width:34ch;font-size:15px;padding-bottom:6px}
/* três colunas de larguras desiguais; os invólucros .col são display:contents no mobile */
.rail{display:grid;grid-template-columns:1.35fr 1fr 1.05fr;gap:20px;align-items:start;
  padding:0 var(--gutter-desktop);overflow:visible}
.rail>.col{display:grid;gap:20px}
.rail>.col.b{padding-top:56px}   /* o degrau entre colunas evita o quadriculado */
.rail>.col.c{padding-top:24px}
.shot-g{width:auto;height:auto;display:block}
/* alturas escolhidas para as três colunas somarem 1100px e para cada vaga
   ficar perto da proporção da foto que recebe — cinco são retrato (~0,7),
   só o Pergolado é quase quadrado (1,11) e vai para a vaga mais larga */
.col.a>*:nth-child(1){height:620px}
.col.a>*:nth-child(2){height:460px}
.col.b>*:nth-child(1){height:520px}
.col.b>*:nth-child(2){height:560px}
.col.c>*:nth-child(1){height:540px}
.col.c>*:nth-child(2){height:540px}
.shot-g .cap{font-size:12px;left:16px;bottom:14px}
.galM .foot{padding:56px var(--gutter-desktop) 0;margin-top:48px}
.galM .foot a{font-size:17px;padding-bottom:9px}
/* cardápio — pausa tipográfica, centrada para não deixar meia tela vazia */
.menuM{padding:104px var(--gutter-desktop) 108px;justify-items:center;text-align:center}
.menuM h2{font-size:44px;margin:18px 0 18px}
.menuM p{font-size:17px;max-width:52ch;margin-bottom:34px}
.menuM .btn2{padding:18px 30px}
/* reservas — copy à esquerda, horários e CTA à direita */
.resM .copy{padding:104px var(--gutter-desktop) 108px;display:grid;
  grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);column-gap:88px;align-items:start}
.res-l h2{font-size:56px;margin:18px 0 22px;max-width:15ch}
.res-l p.lead{font-size:18px;max-width:44ch;margin:0}
.res-r{display:grid;align-content:start;justify-items:start}
.hours{margin-top:0;padding-top:0;border-top:0;width:100%;max-width:none}
.resM .cta{width:auto;justify-self:start;padding:22px 40px;font-size:15px}
.sub{text-align:left}
/* o botão flutuante não tem foto para pousar aqui: entra na coluna, sob o CTA */
.resM .fab{position:static;margin-top:24px;padding:13px 18px}
/* peça em casa — copy à esquerda, retirada como nota lateral */
.delM{padding:84px var(--gutter-desktop) 88px;display:grid;
  grid-template-columns:minmax(0,1fr) minmax(0,340px);column-gap:80px;align-items:start}
.delM .eyebrow{grid-column:1;grid-row:1}
.delM h2{grid-column:1;grid-row:2;font-size:40px}
.delM p.lead{grid-column:1;grid-row:3;font-size:17px;max-width:52ch;margin-bottom:30px}
.delM .btn2{grid-column:1;grid-row:4;justify-self:start;padding:17px 30px}
.facts{grid-column:2;grid-row:1/5;margin:0;align-self:start}
/* como chegar — informações à esquerda, mapa sangrando à direita */
.ctM{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,600px);align-items:stretch}
.ctM .map{order:2;height:auto;min-height:520px;border-top:0;border-left:1px solid var(--verde-garrafa)}
.ctM .map .veil{background:linear-gradient(268deg,rgba(23,18,15,0) 62%,rgba(23,18,15,.62) 100%)}
.ctM .info{order:1;padding:88px var(--s-7) 88px var(--gutter-desktop);align-self:center}
.ctM .info>*{max-width:620px}   /* a coluna cresceu; a medida de leitura não */
.ctM h2{font-size:44px;margin:16px 0 30px}
/* rodapé */
.ft{padding:84px var(--gutter-desktop) 40px;grid-template-columns:auto minmax(0,1fr);column-gap:96px;align-items:start}
.ft img.mark{grid-row:1/3;height:96px}
.ft .cols{grid-template-columns:1fr 1fr;gap:56px}
.ft .legal{grid-column:1/-1;display:flex;justify-content:space-between;gap:24px;margin-top:16px}
}
/* acima de 1400px o conteúdo para de crescer e centraliza */
@media(min-width:1400px){
.abM .copy,.ctM .info{padding-left:calc((100vw - 1400px)/2 + var(--gutter-desktop))}
/* o mapa mede 600px dentro do quadro de 1400 e só a sangria cresce com a tela */
.ctM{grid-template-columns:minmax(0,1fr) minmax(0,calc(600px + (100vw - 1400px)/2))}
.heroM .copy,.galM .head,.rail,.galM .foot,.menuM,.resM .copy,.delM,.ft{padding-left:calc((100vw - 1400px)/2 + var(--gutter-desktop));padding-right:calc((100vw - 1400px)/2 + var(--gutter-desktop))}
.heroM .copy{left:calc((100vw - 1400px)/2 + var(--gutter-desktop));right:calc((100vw - 1400px)/2 + var(--gutter-desktop));padding:0}
.hd-m{padding:0 calc((100vw - 1400px)/2 + var(--gutter-desktop))}
}
"""


MOTION_CSS = """
/* ============ MOTION ============
Escala única para o site inteiro. Só transform e opacity — nada que force reflow.
As revelações dependem de JS, então ficam atrás de html.js: sem script, tudo
nasce visível em vez de sumir. */
:root{
--m-micro:220ms;              /* hover, botões, links */
--m-comp:420ms;               /* imagens, menus, componentes */
--m-enter:620ms;              /* entrada de conteúdo */
--m-ease:cubic-bezier(.22,1,.36,1);
--m-ease-micro:cubic-bezier(.33,1,.68,1);
--m-step:90ms;                /* stagger entre irmãos */
--m-shift:20px;               /* deslocamento da entrada */
}
html{scroll-behavior:smooth}
/* o header é sticky: sem isto a âncora para atrás dele */
.scroll>section,.scroll>footer{scroll-margin-top:calc(var(--header-h-mobile) + 8px)}

/* ---- hero: a única sequência elaborada do site ---- */
.heroM .photo .ph{animation:m-fade 900ms var(--m-ease) both,m-drift 9s var(--m-ease-micro) both}
/* com vídeo não há deriva: o movimento já está na imagem */
.heroM .photo video.ph{animation:m-fade 900ms var(--m-ease) both}
.heroM .copy>*{animation:m-rise var(--m-enter) var(--m-ease) both}
.heroM .wordmark{animation-delay:300ms}
.heroM .cta{animation-delay:460ms}
.heroM .meta{animation-delay:600ms}
@keyframes m-fade{from{opacity:0}to{opacity:1}}
@keyframes m-rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
/* zoom que termina — nada de laço infinito */
@keyframes m-drift{from{transform:scale(1)}to{transform:scale(1.03)}}

/* ---- revelação por seção, disparada a 20% de visibilidade ---- */
html.js .rv{opacity:0;transform:translateY(var(--m-shift));
  transition:opacity var(--m-enter) var(--m-ease) var(--d,0ms),transform var(--m-enter) var(--m-ease) var(--d,0ms)}
html.js .rv-ph{opacity:0;transform:scale(1.02);
  transition:opacity var(--m-enter) var(--m-ease) var(--d,0ms),transform var(--m-enter) var(--m-ease) var(--d,0ms)}
html.js .in .rv,html.js .in.rv{opacity:1;transform:none}
html.js .in .rv-ph,html.js .in.rv-ph{opacity:1;transform:none}

/* ---- microinterações ---- */
.cta,.btn2{transition:var(--t-color),transform var(--m-micro) var(--m-ease-micro)}
.blk a.dir,.galM .foot a,.drawer nav a{transition:var(--t-color),transform var(--m-micro) var(--m-ease-micro)}
.icons a,.fab{transition:var(--t-color),transform var(--m-micro) var(--m-ease-micro)}
.shot-g .ph,.shot-g .ph--empty{transition:transform var(--m-comp) var(--m-ease)}
/* header: só cor e sombra mudam. Altura ficaria em fluxo e empurraria a página. */
.hd-m{transition:background-color var(--m-comp) var(--m-ease-micro),
  border-color var(--m-comp) var(--m-ease-micro)}
/* elevação por fio, como o resto do sistema — só o fundo fecha de 72% para 90% */
.hd-m.stuck{background:var(--carvao-a90);border-bottom-color:var(--verde-garrafa)}
.hd-m img.mark{transition:transform var(--m-comp) var(--m-ease-micro)}
.hd-m.stuck img.mark{transform:scale(.92)}

@media(hover:hover){
.cta:hover,.btn2:hover{transform:translateY(-1px)}
.cta:active,.btn2:active{transform:translateY(0)}
.shot-g:hover .ph,.shot-g:hover .ph--empty{transform:scale(1.03)}
.icons a:hover,.fab:hover{transform:translateY(-2px)}
.blk a.dir:hover,.galM .foot a:hover{transform:translateX(3px)}
/* sublinhado que cresce na navegação de desktop */
.nav-d a{position:relative}
.nav-d a::after{content:"";position:absolute;left:0;right:0;bottom:-6px;height:1px;background:var(--terracota-suave);
  transform:scaleX(0);transform-origin:left;transition:transform 260ms var(--m-ease-micro)}
.nav-d a:hover::after{transform:scaleX(1)}
}

/* ---- mobile: menos deslocamento, sem zoom contínuo ---- */
@media(max-width:767px){
:root{--m-shift:12px;--m-step:70ms}
.heroM .photo .ph{animation:m-fade 900ms var(--m-ease) both}
}
@media(min-width:1024px){
.scroll>section,.scroll>footer{scroll-margin-top:calc(var(--header-h-desktop) + 8px)}
}

/* ---- respeitar quem pediu menos movimento ---- */
@media(prefers-reduced-motion:reduce){
html{scroll-behavior:auto}
*,*::before,*::after{animation-duration:1ms!important;animation-delay:0ms!important;
  animation-iteration-count:1!important;transition-duration:1ms!important;transition-delay:0ms!important}
html.js .rv,html.js .rv-ph{opacity:1;transform:none}
.heroM .photo .ph,.heroM .copy>*{animation:none;opacity:1;transform:none}
}
"""

MOTION_JS = """
(function(){
var root=document.documentElement;
if(!('IntersectionObserver' in window))return;          /* sem suporte, tudo fica visível */
var calm=matchMedia('(prefers-reduced-motion: reduce)').matches;

/* o que entra por seção, na ordem em que deve aparecer */
var GROUPS=[
 ['#sobre',       '.copy>.eyebrow,.copy>h2,.copy>p,.people .p', '.shot .ph,.shot .ph--empty'],
 ['#ambientes',   '.head>*,.foot',                              '.shot-g'],
 ['#cardapio',    '.eyebrow,h2,p,.btn2',                        ''],
 ['#reservas',    '.res-l>*,.res-r>*,.fab',                     ''],
 ['#peca-em-casa','.eyebrow,h2,.lead,.facts,.btn2',             ''],
 ['#como-chegar', '.info>*',                                    '.map'],
 ['#contato',     '.cols>*,.legal',                             '.mark']
];
var sections=[];
GROUPS.forEach(function(g){
  var sec=document.querySelector(g[0]); if(!sec)return;
  var i=0;
  function mark(sel,cls){
    if(!sel)return;
    [].forEach.call(sec.querySelectorAll(sel),function(el){
      el.classList.add(cls);
      el.style.setProperty('--d',Math.min(i,6)*90+'ms');   /* teto: ninguém espera de mais */
      i++;
    });
  }
  mark(g[1],'rv'); mark(g[2],'rv-ph');
  sections.push(sec);
});

if(calm){ sections.forEach(function(s){s.classList.add('in')}); }
else{
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  },{threshold:.2,rootMargin:'0px 0px -5% 0px'});
  sections.forEach(function(s){
    /* já visível no primeiro quadro: entra sem esperar o scroll */
    if(s.getBoundingClientRect().top < innerHeight*.85) s.classList.add('in'); else io.observe(s);
  });
}

/* quem pediu menos movimento fica no poster, não no vídeo */
var vid=document.querySelector('.heroM video');
if(vid&&calm){vid.autoplay=false;vid.pause();vid.currentTime=0;vid.removeAttribute('autoplay');}

/* header ganha fundo sólido depois que o hero sai */
var hd=document.querySelector('.hd-m'),hero=document.querySelector('.heroM');
if(hd&&hero){
  new IntersectionObserver(function(es){
    hd.classList.toggle('stuck',!es[0].isIntersecting);
  },{threshold:0,rootMargin:'-80px 0px 0px 0px'}).observe(hero);
}
})();
"""


WA = "https://api.whatsapp.com/send?phone=5531988600512"
IG = "https://www.instagram.com/bistrodulu/"
PEDIDOS = "https://pedidobistrodulu.ccmpedidoonline.com.br/"
SITE_URL = "https://bistro-du-lu.vercel.app"
GETIN = "https://www.getin.app/ipatinga/bistro-du-lu"

# ---------------------------------------------------------------------------
# CARDÁPIO — conteúdo fornecido pelo restaurante, transcrito sem acréscimos.
# Item sem descrição fica só com nome e preço: descrição inventada seria pior
# que descrição nenhuma. (nome, descrição|None, preço)
# ---------------------------------------------------------------------------
MENU = [
 {"id": "entradas", "nav": "Entradas", "title": "Entradas", "tone": "a",
  "lead": "Para abrir a mesa e dividir.",
  "groups": [{"items": [
    ("Bife Ancho de Angus c/ Farofinha Crocante e Molho Pesto", None, "136"),
    ("Bife de Chorizo de Angus c/ Batatas ao Murro", None, "126"),
    ("Burrata com Tomates Confitados", None, "52"),
    ("Burrata Crocante com Parma e Panko", None, "76"),
    ("Bruschetta Tradicional", None, "39"),
    ("Bruschetta Parma Especial", "4 unidades", "59"),
    ("Camarão VG na Crosta de Coco", "5 unidades", "116"),
    ("Carpaccio Bovino", None, "59"),
    ("Carré de Cordeiro com Batatas ao Murro e Tomatinhos Tostados", None, "142"),
    ("Ceviche de Tilápia com Toque de Leite de Coco e Chips de Batata Doce", None, "58"),
    ("Coxinha de Costela c/ Queijo do Serro e Barbecue de Goiabada", "6 unidades", "39"),
    ("Dados de Queijo Coalho c/ Bacon Caramelizado", "6 unidades", "49"),
    ("Fritas na Páprica c/ Maionese de Bacon e Catchup de Picles", None, "29"),
    ("Pastelzinho de Queijo do Serro e Melado de Cachaça", "6 unidades", "39"),
    ("Picanha em Tiras c/ Batatas na Páprica e Molho de Mostarda", None, "136"),
    # REVISAR: R$ 3 veio assim na fonte. Destoa da faixa da seção (R$ 29–142) e
    # parece faltar um dígito. Mantido como recebido — corrigir exige confirmação.
    ("Salada Pesto", None, "3"),
    ("Tábua de Frios", None, "75"),
    ("Tartare de Salmão, Manga e Chips de Batata Doce", None, "78"),
  ]}]},

 {"id": "principais", "nav": "Principais", "title": "Pratos principais", "tone": "b",
  "lead": "O prato da ocasião.",
  "groups": [
    {"items": [
      ("Bife Ancho ao Alho Doce com Espaguete na Manteiga de Sálvia", None, "92"),
      ("Bife de Chorizo c/ Risoto de Pêra e Gorgonzola", None, "85"),
      ("Camarões VG Flambados na Absolut com Risoto de Abacaxi e Parma", None, "128"),
      ("Carré de Cordeiro com Risoto à Pomodoro", None, "142"),
      ("Filé Mignon ao Molho de Melado com Risoto de Queijo Coalho", None, "82"),
      ("Filé Mignon ao Molho de Mostarda c/ Risoto de Brie e Damasco", None, "82"),
      ("Lagosta no Abacaxi", None, "169"),
      ("Papardelle ao Molho de Queijos e Camarões VG", None, "116"),
      ("Penne ao Molho de Gorgonzola e Filé Mignon em Tiras", None, "64"),
      ("Risoto de Camarão", None, "84"),
      ("Risoto de Filé Mignon c/ Funghi", None, "64"),
      ("Salmão com Legumes Salteados", None, "98"),
      ("Stinco de Suíno c/ Polenta Cremosa", None, "71"),
      ("Talharim ao Pesto", None, "56"),
      ("Tilápia ao Molho de Alcaparras e Purê de Baroa", None, "69"),
    ]},
    {"sub": "Adicionais", "items": [
      ("Adicional de Risoto", None, "35"),
      ("Adicional de Risoto de Abacaxi e Parma", None, "48"),
    ], "opts": ("Sabores do adicional de risoto",
                ["Limão siciliano", "Funghi", "Pêra e gorgonzola", "Brie e damasco", "Parmesão"])},
    {"sub": "Especial Kids", "items": [
      ("Especial Kids", "Arroz, filé picadinho e fritas.", "39"),
    ]},
  ]},

 {"id": "sobremesas", "nav": "Sobremesas", "title": "Sobremesas", "tone": "a",
  "lead": "Para fechar sem pressa.",
  "groups": [
    {"items": [
      ("Cocada de Forno c/ Sorvete de Doce de Leite", None, "29"),
      ("Sorvete de Doce de Leite c/ Crocante de Amêndoas e Caramelo Salgado", None, "18"),
      ("Brownie Perfeito", "Creme de chocolate amargo, farofa de nozes e cookies.", "39"),
    ]},
    {"sub": "No potinho pra levar ♥", "items": [
      ("Sorvete de Doce de Leite Tradicional", "Feito por nós.", "15"),
      ("Sorvete de Doce de Leite c/ Crocante de Amêndoas e Caramelo Salgado", None, "18"),
      ("Cocada de Forno", None, "20"),
    ]},
  ]},

 {"id": "bebidas", "nav": "Bebidas", "title": "Bebidas", "tone": "b",
  "lead": "Sucos, águas e café.",
  "groups": [
    {"sub": "Sucos", "items": [
      ("Suco de Polpa de Maracujá", None, "10"),
      ("Suco Lata Del Valle", None, "7"),
      ("Suco de Uva Tinto Integral", "Casa Madeira, 250 ml.", "13"),
      ("Suco Natural de Abacaxi c/ Hortelã", None, "12"),
      ("Limonada c/ Água de Coco", None, "12"),
      ("Água de Coco", None, "12"),
    ]},
    {"sub": "Águas e refrigerantes", "items": [
      ("Água sem Gás", None, "4"),
      ("Água com Gás", None, "5"),
      ("Água Tônica", None, "5"),
      ("Energético", None, "13"),
      ("Refrigerante Lata", None, "6"),
    ]},
    {"sub": "Café", "items": [
      ("Café Expresso", None, "6"),
    ]},
  ]},
]

MENU_CSS = """
/* ============ CARDÁPIO ============ */
.mHero{position:relative;min-height:380px;display:grid;align-items:end;overflow:hidden}
.mHero .photo{position:absolute;inset:0}
.mHero .grad{position:absolute;inset:0;z-index:2;
  background:linear-gradient(180deg,rgba(23,18,15,.62) 0%,rgba(78,21,23,.22) 34%,rgba(53,14,16,.80) 72%,var(--carvao) 100%)}
.mHero .copy{position:relative;z-index:3;padding:64px var(--gutter-mobile) 34px;display:grid;gap:14px;justify-items:start}
.mHero h1{margin:0;font-family:var(--font-serif-display);font-weight:var(--w-heading);font-size:42px;line-height:1.04;color:var(--text-strong)}
.mHero .sub{margin:0;font-family:var(--font-serif-display);font-size:19px;line-height:1.3;color:var(--areia-a80)}
.mHero .lead{margin:0;font-size:15px;line-height:1.68;color:var(--areia-a60);max-width:52ch}

/* barra de categorias — encosta logo abaixo do header */
.mcat{position:sticky;top:var(--header-h-mobile);z-index:20;background:var(--carvao-a90);
  backdrop-filter:var(--blur-sticky);-webkit-backdrop-filter:var(--blur-sticky);
  border-top:1px solid var(--verde-garrafa);border-bottom:1px solid var(--verde-garrafa)}
.mcat ul{margin:0;padding:0 var(--gutter-mobile);list-style:none;display:flex;gap:26px;
  overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.mcat ul::-webkit-scrollbar{display:none}
.mcat a{display:block;padding:15px 0;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--areia-a60);white-space:nowrap;position:relative;transition:var(--t-color)}
.mcat a::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--terracota-suave);
  transform:scaleX(0);transform-origin:left;transition:transform 260ms var(--m-ease-micro)}
.mcat a.on{color:var(--text-strong)}
.mcat a.on::after{transform:scaleX(1)}

/* a âncora precisa limpar o header E a barra de categorias, que é sticky logo abaixo */
.mSec{padding:52px var(--gutter-mobile) 56px;scroll-margin-top:calc(var(--header-h-mobile) + 44px + 8px)}
.mSec.a{background:var(--carvao)}
.mSec.b{background:linear-gradient(180deg,var(--carvao) 0%,var(--vinho-arroxeado) 18%,var(--vinho-arroxeado) 100%)}
.mSec.a+.mSec.a{border-top:1px solid var(--verde-garrafa)}
.mSec.after-b{background:linear-gradient(180deg,var(--vinho-arroxeado) 0%,var(--carvao) 18%,var(--carvao) 100%)}
.mSec>.head{margin-bottom:30px}
.mSec h2{margin:12px 0 8px;font-family:var(--font-serif-display);font-weight:var(--w-heading);
  font-size:33px;line-height:1.1;color:var(--text-strong)}
.mSec .head p{margin:0;font-size:14.5px;line-height:1.7;color:var(--areia-a60)}
.mSub{margin:38px 0 20px;padding-top:20px;border-top:1px solid var(--verde-garrafa);
  font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--areia-a38)}
.mGrid{display:grid;gap:12px}
.mItem{border:1px solid var(--verde-garrafa);border-radius:var(--r-xs);padding:18px 18px 19px;
  background:var(--areia-a08);display:grid;gap:7px;
  transition:transform var(--m-micro) var(--m-ease-micro),border-color var(--m-micro) var(--m-ease-micro)}
.mItem .row{display:flex;align-items:baseline;justify-content:space-between;gap:16px}
.mItem .n{font-family:var(--font-serif-display);font-weight:var(--w-heading);font-size:17.5px;
  line-height:1.28;color:var(--text-strong)}
.mItem .pr{flex:0 0 auto;font-size:14px;letter-spacing:.04em;color:var(--areia-quente);
  font-variant-numeric:tabular-nums;white-space:nowrap}
.mItem .d{margin:0;font-size:13.5px;line-height:1.62;color:var(--areia-a60)}
.mOpts{margin:14px 0 0;padding:16px 18px;border:1px dashed var(--verde-300);border-radius:var(--r-xs)}
.mOpts .lbl{display:block;font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--areia-a38);margin-bottom:10px}
.mOpts ul{margin:0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:8px}
.mOpts li{font-size:13px;color:var(--areia-a80);border:1px solid var(--verde-garrafa);
  border-radius:var(--r-xs);padding:6px 12px}

/* carta de bebidas adultas: estrutura pronta, sem conteúdo nesta implementação */
.mCarta{padding:46px var(--gutter-mobile) 50px;
  background:linear-gradient(180deg,var(--vinho-arroxeado) 0%,var(--carvao) 18%,var(--carvao) 100%)}
.mCarta h2{margin:12px 0 10px;font-family:var(--font-serif-display);font-weight:var(--w-heading);
  font-size:26px;line-height:1.15;color:var(--text-strong)}
.mCarta p{margin:0;font-size:14px;line-height:1.7;color:var(--areia-a60);max-width:46ch}

.mEnd{padding:56px var(--gutter-mobile) 60px;border-top:1px solid var(--verde-garrafa);
  background:linear-gradient(180deg,var(--carvao) 0%,var(--vinho-arroxeado) 18%,var(--vinho-arroxeado) 100%)}
.mEnd h2{margin:12px 0 10px;font-family:var(--font-serif-display);font-weight:var(--w-heading);
  font-size:31px;line-height:1.1;color:var(--text-strong)}
.mEnd p{margin:0 0 26px;font-size:15px;line-height:1.68;color:var(--areia-a80)}
.mEnd .acts{display:grid;gap:12px}
.mEnd .cta,.mEnd .btn2{width:100%;justify-content:center;padding:18px 20px;font-size:13.5px}
.flinks{list-style:none;margin:0;padding:0;display:grid;gap:9px}
.flinks a{font-size:15px;line-height:1.5;color:var(--text-muted);transition:var(--t-color)}
.flinks a:hover{color:var(--terracota-suave)}
.mNote{margin:0;padding:22px var(--gutter-mobile) 26px;background:var(--vinho-arroxeado);
  font-size:12px;line-height:1.66;color:var(--text-faint);border-top:1px solid var(--verde-a55)}

.totop{position:fixed;right:16px;bottom:16px;z-index:35;width:46px;height:46px;display:grid;place-items:center;
  background:var(--carvao-a90);border:1px solid var(--verde-300);border-radius:var(--r-xs);color:var(--areia-quente);
  cursor:pointer;padding:0;backdrop-filter:var(--blur-sticky);-webkit-backdrop-filter:var(--blur-sticky);
  opacity:0;visibility:hidden;transform:translateY(8px);
  transition:opacity var(--m-comp) var(--m-ease),transform var(--m-comp) var(--m-ease),
    visibility var(--m-comp),border-color var(--m-micro) var(--m-ease-micro)}
.totop.on{opacity:1;visibility:visible;transform:none}

@media(hover:hover){
.mcat a:hover{color:var(--text-strong)}
.mItem:hover{transform:translateY(-2px);border-color:var(--terracota-suave)}
.totop:hover{border-color:var(--terracota-suave)}
}
@media(min-width:768px){
.mGrid{grid-template-columns:1fr 1fr;gap:14px}
.mOpts{grid-column:1/-1}
.mEnd .acts{display:flex;flex-wrap:wrap}
.mEnd .cta,.mEnd .btn2{width:auto}
}
@media(min-width:1024px){
.mcat{top:var(--header-h-desktop)}
.mSec{scroll-margin-top:calc(var(--header-h-desktop) + 52px + 8px)}
.mcat ul{padding:0 var(--gutter-desktop);gap:38px}
.mcat a{padding:18px 0;font-size:12.5px}
.mHero{min-height:440px}
.mHero .copy{padding:100px var(--gutter-desktop) 56px;gap:16px}
.mHero h1{font-size:64px}
.mHero .sub{font-size:23px}
.mHero .lead{font-size:16.5px}
.mSec{padding:84px var(--gutter-desktop) 88px}
.mSec h2{font-size:44px}
.mSec>.head{margin-bottom:42px}
.mItem{padding:22px 22px 23px}
.mItem .n{font-size:19px}
.mItem .pr{font-size:15px}
.mCarta,.mEnd{padding-left:var(--gutter-desktop);padding-right:var(--gutter-desktop)}
.ft .cols{grid-template-columns:repeat(3,minmax(0,1fr));gap:44px}
.mNote{padding-left:var(--gutter-desktop);padding-right:var(--gutter-desktop)}
.totop{right:28px;bottom:28px;width:52px;height:52px}
}
@media(min-width:1400px){
.mcat ul,.mHero .copy,.mSec,.mCarta,.mEnd,.mNote{
  padding-left:calc((100vw - 1400px)/2 + var(--gutter-desktop));
  padding-right:calc((100vw - 1400px)/2 + var(--gutter-desktop))}
}
"""

MENU_JS = """
(function(){
var bar=document.querySelector('.mcat'),top=document.querySelector('.totop');
if(bar){
  var links={},secs=[];
  [].forEach.call(bar.querySelectorAll('a'),function(a){
    var id=a.getAttribute('href').slice(1),s=document.getElementById(id);
    if(s){links[id]=a;secs.push(s);}
  });
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting)return;
      for(var k in links)links[k].classList.toggle('on',k===e.target.id);
      /* mantém a categoria ativa à vista na barra rolável do celular */
      var a=links[e.target.id];
      if(a&&bar.scrollWidth>bar.clientWidth)a.scrollIntoView({block:'nearest',inline:'center'});
    });
  },{rootMargin:'-30% 0px -60% 0px'});
  secs.forEach(function(s){io.observe(s)});
}
if(top){
  top.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})});
  var io2=new IntersectionObserver(function(es){top.classList.toggle('on',!es[0].isIntersecting)},{threshold:0});
  var h=document.querySelector('.mHero'); if(h)io2.observe(h);
}
})();
"""


def money(v):
    return "R$&nbsp;" + v


def menu_markup():
    """Monta as seções do cardápio. Uma seção por categoria, subgrupos dentro."""
    out = []
    nav = "".join(f'<li><a href="#{s["id"]}">{s["nav"]}</a></li>' for s in MENU)
    out.append(f'<nav class="mcat" aria-label="Categorias do cardápio"><ul>{nav}</ul></nav>')
    for si, sec in enumerate(MENU):
        tone = sec["tone"] + (" after-b" if si and MENU[si - 1]["tone"] == "b" and sec["tone"] == "a" else "")
        body = [f'<div class="head"><span class="eyebrow">Cardápio</span><h2>{sec["title"]}</h2>'
                f'<p>{sec["lead"]}</p></div>']
        for g in sec["groups"]:
            if g.get("sub"):
                body.append(f'<h3 class="mSub">{g["sub"]}</h3>')
            cards = []
            for name, desc, price in g["items"]:
                d = f'<p class="d">{desc}</p>' if desc else ""
                cards.append(f'<article class="mItem"><div class="row"><span class="n">{name}</span>'
                             f'<span class="pr">{money(price)}</span></div>{d}</article>')
            if g.get("opts"):
                lbl, opts = g["opts"]
                lis = "".join(f"<li>{o}</li>" for o in opts)
                cards.append(f'<div class="mOpts"><span class="lbl">{lbl}</span><ul>{lis}</ul></div>')
            body.append(f'<div class="mGrid">{"".join(cards)}</div>')
        out.append(f'<section class="mSec {tone}" id="{sec["id"]}">{"".join(body)}</section>')
    return "".join(out)


def build_images():
    from PIL import Image
    out = os.path.join(ROOT, "img")
    os.makedirs(out, exist_ok=True)
    for src, (dst, w) in PHOTOS.items():
        im = Image.open(f"ui_kits/website/{src}").convert("RGB")
        if w < im.width:
            im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
        im.save(f"{out}/{dst}", "JPEG", quality=78, optimize=True, progressive=True)
    for src, (dst, h) in LOGOS.items():
        im = Image.open(src)          # mantém o canal alpha
        if h < im.height:
            im = im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
        im.save(f"{out}/{dst}", "PNG", optimize=True)


def build_html():
    raw = open(SRC, encoding="utf-8").read()
    sheet = raw.split("<style>", 1)[1].split("</style>")[0]
    body = raw.split("</style></head><body>", 1)[1]
    site = body[body.index('<div class="drawer"'):body.index('</div></div>\n</div>')]

    # 1. remove o CSS que só serve à prancha de documentação
    for pat in (r'\.sheet\{[^}]*\}', r'\.caption[^{]*\{[^}]*\}', r'\.note[^{]*\{[^}]*\}',
                r'\.ritmo[^{]*\{[^}]*\}', r'\.legend\{[^}]*\}', r'\.flag\{[^}]*\}',
                r'[^\n{}]*\bimage-slot\b[^{}]*\{[^}]*\}'):  # regras órfãs: os slots viram <img> abaixo
        sheet = re.sub(pat, "", sheet)

    # 2. rolagem do documento no lugar do frame de 880px com rolagem interna
    sheet = sheet.replace(
        "body{margin:0;background:var(--carvao-900);font-family:var(--font-sans-body);"
        "font-weight:var(--w-body);color:var(--text-body);padding:56px}",
        "body{margin:0;background:var(--carvao);font-family:var(--font-sans-body);"
        "font-weight:var(--w-body);color:var(--text-body)}")
    sheet = sheet.replace(
        ".phone{position:relative;width:390px;height:880px;border:1px solid var(--verde-garrafa);"
        "border-radius:var(--r-md);overflow:hidden;background:var(--carvao)}",
        ".phone{position:relative;width:100%;max-width:430px;margin:0 auto;background:var(--carvao);overflow-x:clip}\n"
        "@media(min-width:431px) and (max-width:1023px){.phone{border-left:1px solid var(--verde-garrafa);"
        "border-right:1px solid var(--verde-garrafa)}}")
    sheet = sheet.replace(".scroll{height:100%;overflow-y:auto;scrollbar-width:none;position:relative}",
                          ".scroll{position:relative}")
    sheet = sheet.replace(".scroll::-webkit-scrollbar{display:none}", "")
    sheet = sheet.replace(".drawer{position:absolute;inset:0;z-index:20;pointer-events:none}",
                          ".drawer{position:fixed;inset:0;z-index:40;pointer-events:none}")
    sheet = sheet.replace(".drawer .panel{position:absolute;",
                          "body.menu-open{overflow:hidden}\n.drawer .panel{position:absolute;")
    sheet = sheet.replace(";margin-bottom:calc(-1 * var(--header-h-mobile))}", "}")
    sheet = sheet.replace(".hd-m{position:sticky;top:0;z-index:9;", ".hd-m{position:sticky;top:0;z-index:30;")

    sheet += ("\n.ph{display:block;width:100%;height:100%;object-fit:cover}\n"
              # painel calmo em carvão: a hachura tracejada gritava 'foto faltando'
              ".ph--empty{display:grid;place-items:center;width:100%;height:100%;padding:16px;text-align:center;"
              "background:linear-gradient(160deg,var(--carvao-900) 0%,var(--carvao) 100%)}\n"
              ".ph--empty span{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--areia-a38)}\n"
              # o mosaico do desktop agrupa as peças em colunas; no mobile o carrossel volta a ser plano
              ".rail>.col{display:contents}\n"
              # a régua só separa dois dados: sozinha na frente vira um traço solto
              ".heroM .meta span.sep:first-child{display:none}\n"
              ".nav-d{display:none}\n"
              ".hd-m .burger,.drawer .close{color:var(--areia-quente)}\n"
              ".drawer .close:hover{color:var(--terracota-suave)}\n")

    # 3. <image-slot> vira <img>; slot sem foto vira marcador tracejado
    def slot(m):
        tag = m.group(0)
        ph = re.search(r'placeholder="([^"]*)"', tag)
        ph = ph.group(1) if ph else "Foto"
        src = re.search(r'src="\./([^"]+)"', tag)
        if src:
            return f'<img class="ph" src="./img/{PHOTOS[src.group(1)][0]}" alt="{ph}" loading="lazy">'
        return f'<div class="ph--empty"><span>{ph}</span></div>'

    site = re.sub(r'<image-slot\b[^>]*></image-slot>', slot, site)
    site = site.replace('src="../../assets/logo-monogram-areia.png"', 'src="./img/logo.png"')
    site = site.replace('src="../../assets/logo-topo.png"', 'src="./img/logo-topo.png"')

    # 4. ícones do menu embutidos — no mobile o botão é a única navegação
    site = re.sub(r'<img src="https://cdn\.jsdelivr\.net/npm/lucide-static@[^"]*/icons/menu\.svg"[^>]*>', MENU_SVG, site)
    site = re.sub(r'<img src="https://cdn\.jsdelivr\.net/npm/lucide-static@[^"]*/icons/x\.svg"[^>]*>', CLOSE_SVG, site)

    # 4b. o hero da home recebe o vídeo; o do cardápio segue com a foto.
    #     O poster é um quadro do próprio vídeo, então não há salto ao começar a tocar,
    #     e sem JS (ou sem suporte ao codec) o poster é o que fica.
    site = re.sub(
        r'<img class="ph" src="\./img/hero\.jpg"[^>]*>',
        '<video class="ph" poster="./img/hero-poster.jpg" autoplay muted loop playsinline '
        'preload="auto" aria-label="Salão do Bistrô du Lú">'
        '<source src="./img/hero.webm" type="video/webm">'
        '<source src="./img/hero.mp4" type="video/mp4"></video>', site, count=1)

    # 5. navegação horizontal do desktop (no mobile o menu é a gaveta)
    site = re.sub(r'<a class="cta" href="#reservas"[^>]*>Reservar</a>',
                  '<nav class="nav-d"><a href="#sobre">Sobre nós</a><a href="#ambientes">Ambientes</a>'
                  '<a href="/cardapio">Cardápio</a><a href="#peca-em-casa">Peça em casa</a>'
                  '<a href="#como-chegar">Como chegar</a></nav>\n<a class="cta" href="#reservas">Reservar</a>', site)

    # 6. duas colunas em Reservas no desktop (texto | horários + CTA)
    site = site.replace('<span class="eyebrow">Reservas</span>', '<div class="res-l"><span class="eyebrow">Reservas</span>')
    site = re.sub(r'<p class="lead"[^>]*>O ambiente ideal para o casal, amigos ou família\.</p>',
                  '<p class="lead">O ambiente ideal para o casal, amigos ou família.</p></div><div class="res-r">', site)
    site = site.replace('<span class="sub">Confirmação imediata · sem taxa</span>\n</div>',
                        '<span class="sub">Confirmação imediata · sem taxa</span>\n</div></div>')

    # 7. o WhatsApp entra na coluna da direita: no desktop não há foto sob a qual flutuar.
    #    No mobile ele continua absoluto em relação a .resM, que é o ancestral posicionado.
    fab = re.search(r'<a class="fab".*?</a>\n', site, re.S).group(0)
    anchor = '<span class="sub">Confirmação imediata · sem taxa</span>\n</div>'
    site = site.replace(fab, "").replace(anchor, anchor + fab, 1)

    # 8. mosaico do desktop: as seis peças passam a viver em três colunas
    head, rest = site.split('<div class="rail">\n', 1)
    items, tail = rest.split('\n</div>\n<div class="foot">', 1)
    items = items.split("\n")
    assert len(items) == 6, f"o mosaico espera 6 peças, encontrei {len(items)}"
    # foto e marcador alternados em cada coluna; a ordem preserva o ritmo de larguras do carrossel
    order, cols = [0, 3, 2, 1, 4, 5], "abc"
    rail = "".join(f'<div class="col {c}">{items[order[2 * i]]}{items[order[2 * i + 1]]}</div>'
                   for i, c in enumerate(cols))
    site = f'{head}<div class="rail">{rail}</div>\n<div class="foot">{tail}'

    tokens = "".join(open(f"tokens/{f}", encoding="utf-8").read() + "\n" for f in TOKENS)
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            + head_meta("Bistrô du Lú — Ipatinga MG",
                        "Bistrô du Lú — cozinha, sabor e afeto. Rua Jequitibá, 910, Horto, Ipatinga MG.",
                        "/") +
            '<style>' + tokens + sheet + DESKTOP_CSS + MOTION_CSS +
            '</style></head><body>'
            '<div class="phone">' + site + '</div></div><script>'
            '(function(){var d=document.getElementById("drawer"),b=document.getElementById("burger");if(!d||!b)return;'
            'function close(){d.classList.remove("open");document.body.classList.remove("menu-open")}'
            'b.addEventListener("click",function(){d.classList.add("open");document.body.classList.add("menu-open")});'
            'd.addEventListener("click",function(e){if(e.target.closest("[data-close]"))close()});'
            'document.addEventListener("keydown",function(e){if(e.key==="Escape")close()});})();'
            + MOTION_JS +
            '</script></body></html>')
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
    return html, sheet, site


def head_meta(title, desc, path):
    """<head> comum às duas páginas: SEO, Open Graph e canônica."""
    url = SITE_URL + path
    return ('<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            f'<meta name="theme-color" content="#17120F">'
            f'<meta name="description" content="{desc}">'
            f'<link rel="canonical" href="{url}">'
            f'<meta property="og:type" content="website">'
            f'<meta property="og:locale" content="pt_BR">'
            f'<meta property="og:site_name" content="Bistrô du Lú">'
            f'<meta property="og:title" content="{title}">'
            f'<meta property="og:description" content="{desc}">'
            f'<meta property="og:url" content="{url}">'
            f'<meta property="og:image" content="{SITE_URL}/img/hero.jpg">'
            f'<meta name="twitter:card" content="summary_large_image">'
            f'<title>{title}</title>'
            # marcada antes da pintura: sem JS as revelações nem chegam a esconder nada
            '<script>document.documentElement.className="js"</script>')


def build_menu(sheet, site):
    """Página /cardapio, reaproveitando cabeçalho, gaveta e rodapé do site."""
    def grab(pat):
        m = re.search(pat, site, re.S)
        assert m, f"não achei no site: {pat}"
        return m.group(0)

    drawer = grab(r'<div class="drawer".*?</aside>\n</div>')
    header = grab(r'<header class="hd-m">.*?</header>')
    footer = grab(r'<footer class="ft".*?</footer>')
    # as âncoras do menu passam a apontar para a home; /cardapio e links externos ficam
    drawer = drawer.replace('href="#', 'href="/#')
    header = header.replace('href="#', 'href="/#')
    # na página do cardápio, o item da própria página fica marcado
    header = header.replace('<a href="/cardapio">Cardápio</a>', '<a href="/cardapio" aria-current="page">Cardápio</a>')

    # o rodapé do site não tem links (os ícones sociais moram em "Como chegar");
    # aqui ele ganha uma coluna de navegação, como pede a especificação da página
    flinks = "".join(f'<li><a href="{u}"{e}>{t}</a></li>' for t, u, e in [
        ("Cardápio", "/cardapio", ""),
        ("Peça em casa", PEDIDOS, ' target="_blank" rel="noopener"'),
        ("WhatsApp", WA, ' target="_blank" rel="noopener"'),
        ("Instagram", IG, ' target="_blank" rel="noopener"'),
        ("Como chegar", "/#como-chegar", ""),
    ])
    footer = footer.replace('</div>\n<div class="legal">',
                            f'<div><span class="lbl">Navegue</span><ul class="flinks">{flinks}</ul></div>'
                            '</div>\n<div class="legal">', 1)

    hero = (
        '<section class="mHero">'
        '<div class="photo"><img class="ph" src="./img/hero.jpg" alt="Prato do Bistrô du Lú"></div>'
        '<div class="grad"></div>'
        '<div class="copy">'
        '<span class="eyebrow">Bistrô du Lú</span>'
        '<h1>Cardápio</h1>'
        '<p class="sub">Sabores para cada ocasião.</p>'
        '<p class="lead">Da cozinha do Bistrô du Lú para a sua mesa. Conheça nossas entradas, '
        'pratos principais, sobremesas e bebidas.</p>'
        '</div></section>')

    # Estrutura pronta para a carta de bebidas adultas. O conteúdo não entra aqui:
    # basta trocar o parágrafo abaixo por um bloco .mGrid quando o restaurante enviar.
    carta = ('<section class="mCarta" id="carta">'
             '<span class="eyebrow">Carta</span>'
             '<h2>Vinhos e destilados</h2>'
             '<p>Consulte a carta no restaurante — nossa equipe ajuda a escolher o acompanhamento '
             'para o seu prato.</p></section>')

    end = ('<section class="mEnd">'
           '<span class="eyebrow">Próximo passo</span>'
           '<h2>Gostou do que viu?</h2>'
           '<p>Agora é só escolher a ocasião.</p>'
           '<div class="acts">'
           # os dois botões deste bloco agem direto: mandar para a seção de reservas
           # da home seria um salto a mais, enquanto o vizinho já abre o sistema de pedidos
           f'<a class="cta" href="{GETIN}" target="_blank" rel="noopener">'
           '<span>Reservar uma mesa</span><span>→</span></a>'
           f'<a class="btn2" href="{PEDIDOS}" target="_blank" rel="noopener">'
           '<span>Pedir para levar</span><span class="arw">→</span></a>'
           '</div></section>')

    note = ('<p class="mNote">Os itens e valores podem sofrer alterações. '
            'Consulte a disponibilidade no dia.</p>')

    totop = ('<button class="totop" type="button" aria-label="Voltar ao topo">'
             '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" '
             'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M12 19V5M5 12l7-7 7 7"/></svg></button>')

    # dados estruturados: só o que o restaurante forneceu
    ld = {
        "@context": "https://schema.org", "@type": "Menu", "name": "Cardápio — Bistrô du Lú",
        "inLanguage": "pt-BR", "url": SITE_URL + "/cardapio",
        "hasMenuSection": [{
            "@type": "MenuSection", "name": s["title"],
            "hasMenuItem": [dict([("@type", "MenuItem"), ("name", n)]
                                 + ([("description", d)] if d else [])
                                 + [("offers", {"@type": "Offer", "price": p, "priceCurrency": "BRL"})])
                            for g in s["groups"] for n, d, p in g["items"]]
        } for s in MENU]}
    import json
    jsonld = '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'

    tokens = "".join(open(f"tokens/{f}", encoding="utf-8").read() + "\n" for f in TOKENS)
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            + head_meta("Cardápio | Bistrô du Lú — Ipatinga MG",
                        "Conheça o cardápio do Bistrô du Lú, em Ipatinga. Entradas, pratos principais, "
                        "sobremesas e bebidas para tornar cada ocasião especial.", "/cardapio")
            + jsonld
            + '<style>' + tokens + sheet + DESKTOP_CSS + MOTION_CSS + MENU_CSS
            + '</style></head><body>'
            + '<div class="phone">' + drawer + '<div class="scroll">'
            + header + hero + menu_markup() + carta + end + note + footer
            + '</div></div>' + totop + '<script>'
            '(function(){var d=document.getElementById("drawer"),b=document.getElementById("burger");if(!d||!b)return;'
            'function close(){d.classList.remove("open");document.body.classList.remove("menu-open")}'
            'b.addEventListener("click",function(){d.classList.add("open");document.body.classList.add("menu-open")});'
            'd.addEventListener("click",function(e){if(e.target.closest("[data-close]"))close()});'
            'document.addEventListener("keydown",function(e){if(e.key==="Escape")close()});})();'
            + MENU_JS + '</script></body></html>')
    open(os.path.join(ROOT, "cardapio.html"), "w", encoding="utf-8").write(html)
    return html


if __name__ == "__main__":
    if not os.path.exists(SRC):
        sys.exit(f"rode a partir de bistr-du-l-design-system/project/ (não encontrei {SRC})")
    build_images()
    html, sheet, site = build_html()
    menu = build_menu(sheet, site)
    for page, doc in (("index.html", html), ("cardapio.html", menu)):
        assert "../../assets" not in doc, f"{page}: sobrou caminho relativo ao design system"
        assert "cdn.jsdelivr.net" not in doc, f"{page}: sobrou ícone vindo de CDN"
        assert "<image-slot" not in doc, f"{page}: sobrou <image-slot> sem converter"
        assert "canva.site" not in doc, f"{page}: ainda aponta para o Canva"
    itens = sum(len(g["items"]) for s in MENU for g in s["groups"])
    print(f"site/index.html — {len(html) // 1024} KB")
    print(f"site/cardapio.html — {len(menu) // 1024} KB, {itens} itens em {len(MENU)} categorias")
