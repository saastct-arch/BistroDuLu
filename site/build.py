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
    "465473846_18356323819184475_715987668432-msqcws7i-3w8b.jpg": ("hero.jpg", 1800),
    "whatsapp-image-2026-08-12-at-07-48-28-msqclhdg-j8en.jpeg": ("sobre.jpg", 1200),
    "467206514_18358169875184475_752019178811-msqd1ao6-28da.jpg": ("gal1.jpg", 900),
    "captura-de-tela-2026-08-12-143254-msqdb3mu-t9du.png": ("gal2.jpg", 700),
    "472721185_18365296549184475_468369343161-msqd1lcm-nlj1.jpg": ("gal3.jpg", 900),
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
.heroM .copy{left:var(--gutter-desktop);right:var(--gutter-desktop);bottom:64px;gap:30px}
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
/* ambientes — mosaico editorial de alturas desiguais */
.galM{padding:104px 0 108px}
.galM .head{padding:0 var(--gutter-desktop);max-width:760px;margin-bottom:44px}
.galM h2{font-size:44px}
.galM .head p{font-size:16px}
/* colunas em vez de grid: as peças empilham sem o vão que o alinhamento de linha deixaria */
.rail{display:block;column-count:3;column-gap:20px;padding:0 var(--gutter-desktop);overflow:visible}
.shot-g{width:auto;height:auto;display:block;break-inside:avoid;margin-bottom:20px}
.rail>*:nth-child(1){height:520px}
.rail>*:nth-child(2){height:400px}
.rail>*:nth-child(3){height:300px}
.rail>*:nth-child(4){height:300px}
.rail>*:nth-child(5){height:420px}
.rail>*:nth-child(6){height:360px}
.shot-g .cap{font-size:12px;left:16px;bottom:14px}
.galM .foot{padding:0 var(--gutter-desktop);margin-top:44px;padding-top:26px}
.galM .foot a{font-size:17px;padding-bottom:9px}
/* cardápio — pausa tipográfica */
.menuM{padding:104px var(--gutter-desktop) 108px}
.menuM h2{font-size:44px;margin:18px 0 18px}
.menuM p{font-size:17px;max-width:52ch;margin-bottom:34px}
.menuM .btn2{padding:18px 30px}
/* reservas — copy à esquerda, horários e CTA à direita */
.resM .copy{max-width:1180px;margin:0 auto;padding:104px var(--gutter-desktop) 116px;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);column-gap:88px;align-items:start}
.res-l h2{font-size:56px;margin:18px 0 22px}
.res-l p.lead{font-size:18px;max-width:44ch;margin:0}
.res-r{display:grid;align-content:start}
.hours{margin-top:0;padding-top:0;border-top:0}
.resM .cta{width:auto;justify-self:start;padding:22px 40px;font-size:15px}
.sub{text-align:left}
.fab{left:var(--gutter-desktop);right:auto;bottom:34px;padding:13px 18px}
/* peça em casa — hierarquia secundária, faixa baixa e larga */
.delM{padding:84px var(--gutter-desktop) 88px}
.delM h2{font-size:40px}
.delM p.lead{font-size:17px;max-width:52ch}
.facts{display:flex;gap:64px;margin-bottom:34px}
.delM .btn2{padding:17px 30px}
/* como chegar — informações à esquerda, mapa sangrando à direita */
.ctM{display:grid;grid-template-columns:minmax(0,520px) minmax(0,1fr);align-items:stretch}
.ctM .map{order:2;height:auto;min-height:620px;border-top:0;border-left:1px solid var(--verde-garrafa)}
.ctM .map .veil{background:linear-gradient(268deg,rgba(23,18,15,0) 62%,rgba(23,18,15,.62) 100%)}
.ctM .info{order:1;padding:100px var(--s-7) 100px var(--gutter-desktop);align-self:center}
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
.heroM .copy,.galM .head,.rail,.galM .foot,.menuM,.resM .copy,.delM,.ft{padding-left:calc((100vw - 1400px)/2 + var(--gutter-desktop));padding-right:calc((100vw - 1400px)/2 + var(--gutter-desktop))}
.heroM .copy{left:calc((100vw - 1400px)/2 + var(--gutter-desktop));right:calc((100vw - 1400px)/2 + var(--gutter-desktop));padding:0}
.hd-m{padding:0 calc((100vw - 1400px)/2 + var(--gutter-desktop))}
}
"""


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
              ".ph--empty{display:grid;place-items:center;width:100%;height:100%;padding:12px;text-align:center;"
              "background:repeating-linear-gradient(135deg,var(--areia-a08) 0 8px,transparent 8px 16px);"
              "border:1px dashed var(--verde-300)}\n"
              ".ph--empty span{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--areia-a38)}\n"
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

    # 5. navegação horizontal do desktop (no mobile o menu é a gaveta)
    site = re.sub(r'<a class="cta" href="#reservas"[^>]*>Reservar</a>',
                  '<nav class="nav-d"><a href="#sobre">A casa</a><a href="#ambientes">Ambientes</a>'
                  '<a href="#cardapio">Cardápio</a><a href="#peca-em-casa">Peça em casa</a>'
                  '<a href="#como-chegar">Como chegar</a></nav>\n<a class="cta" href="#reservas">Reservar</a>', site)

    # 6. duas colunas em Reservas no desktop (texto | horários + CTA)
    site = site.replace('<span class="eyebrow">Reservas</span>', '<div class="res-l"><span class="eyebrow">Reservas</span>')
    site = re.sub(r'<p class="lead"[^>]*>O ambiente ideal para o casal, amigos ou família\.</p>',
                  '<p class="lead">O ambiente ideal para o casal, amigos ou família.</p></div><div class="res-r">', site)
    site = site.replace('<span class="sub">Confirmação imediata · sem taxa</span>\n</div>',
                        '<span class="sub">Confirmação imediata · sem taxa</span>\n</div></div>')

    tokens = "".join(open(f"tokens/{f}", encoding="utf-8").read() + "\n" for f in TOKENS)
    html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            '<meta name="theme-color" content="#17120F">'
            '<meta name="description" content="Bistrô du Lú — cozinha, sabor e afeto. '
            'Rua Jequitibá, 910, Horto, Ipatinga MG.">'
            '<title>Bistrô du Lú — Ipatinga MG</title><style>' + tokens + sheet + DESKTOP_CSS +
            '</style></head><body>'
            '<div class="phone">' + site + '</div></div><script>'
            '(function(){var d=document.getElementById("drawer"),b=document.getElementById("burger");if(!d||!b)return;'
            'function close(){d.classList.remove("open");document.body.classList.remove("menu-open")}'
            'b.addEventListener("click",function(){d.classList.add("open");document.body.classList.add("menu-open")});'
            'd.addEventListener("click",function(e){if(e.target.closest("[data-close]"))close()});'
            'document.addEventListener("keydown",function(e){if(e.key==="Escape")close()});})();'
            '</script></body></html>')
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
    return html


if __name__ == "__main__":
    if not os.path.exists(SRC):
        sys.exit(f"rode a partir de bistr-du-l-design-system/project/ (não encontrei {SRC})")
    build_images()
    html = build_html()
    assert "../../assets" not in html, "sobrou caminho relativo ao design system"
    assert "cdn.jsdelivr.net" not in html, "sobrou ícone vindo de CDN"
    assert "<image-slot" not in html, "sobrou <image-slot> sem converter"
    print(f"site/index.html — {len(html) // 1024} KB")
