# Bistrô du Lú — Design System

Bistrô du Lú is a small neighbourhood bistro (Horto, Ipatinga — MG — *"desde 2017"*). Its self-description, taken from the logo lockup, is the whole brand brief: **cozinha · sabor · afeto** — cooking, flavour, affection. Short seasonal menu, one small room, the owner ("Lú") at every table. The register is warm and quietly upscale: candlelight, wine, aged wood — *not* fine-dining formality and *not* casual-trattoria cheer.

Primary language is **Brazilian Portuguese**.

## Sources given

- `uploads/Logo Clara sem texto.png` → `assets/logo-monogram-areia.png` (monogram, sand/rose)
- `uploads/Logo Clara com texto.png` → `assets/logo-vertical-areia.png` (monogram over wordmark, sand/rose)
- `uploads/Logo Escura com texto ao lado.png` → `assets/logo-horizontal-vinho.png` (wine mark beside wordmark)
- A written brief specifying the five-colour palette, usage rules, a PROIBIDO / OBRIGATÓRIO list, and a request for header + footer mockups (desktop + mobile 390px, two header compositions).

No codebase, Figma file, deck, website or photography was provided. Everything here is derived from the logos and that brief; nothing was reconstructed from memory. **No logo was drawn or altered** — only the three supplied files are used.

## Index

| File | What it is |
| --- | --- |
| `styles.css` | Global entry point — only `@import` lines |
| `tokens/colors.css` | Palette, alphas, gradients, semantic surfaces/text/lines |
| `tokens/typography.css` | Font stacks, weights, scale, tracking |
| `tokens/spacing.css` | Space scale, gutters, section rhythm, header heights |
| `tokens/borders.css` | Radii, border widths, hairline "elevation", sticky blur |
| `tokens/motion.css` | Durations, easings, transition recipes |
| `tokens/fonts.css` | Google Fonts import (substituted — see Caveats) |
| `guidelines/*.html` | 17 foundation specimen cards (Colors, Type, Spacing, Brand) |
| `components/**` | React primitives + `.d.ts` + `.prompt.md` + one card per group |
| `ui_kits/website/` | Header & footer mockup (desktop + mobile 390, two header variants) |
| `assets/` | Three logo lockups, `image-slot.js` photo placeholder |
| `SKILL.md` | Agent-Skills wrapper |

### Components

**Brand** — `Logo`, `Eyebrow`, `Divider`.
**Core** — `Button`, `IconButton`, `SocialIcon`, `Card`, `Tag`.
**Forms** — `Input`, `Select`.
**Navigation** — `SiteHeader`, `SiteFooter`.

*Intentional additions*: the brief defined no component inventory, so this is a from-scratch set sized to a restaurant site. `SocialIcon` exists only as a thin wrapper over the Simple Icons CDN (no icon set was supplied). No Dialog, Toast, Tooltip, Tabs or Avatar — nothing in the brief needs them; add them only when a real screen does.

## Content fundamentals

- **Voice: "we" implied, never "I".** The house speaks, not the chef: *"Servimos o que a feira oferece na semana."* Address the guest as **você**, sparingly.
- **Tone: understated, concrete, affectionate.** Facts and ingredients carry the emotion — *"massa amanteigada, creme de castanhas"*, not *"uma explosão de sabores"*. No superlatives (*"o melhor"*, *"inesquecível"*), no exclamation marks.
- **Short sentences.** Headlines 3–6 words: *"Cozinha de bairro, feita com afeto"*, *"A sala pequena de sempre"*. Body paragraphs of 2–3 sentences max.
- **Casing.** Sentence case for headings and body. UPPERCASE only for nav, buttons, eyebrows and the wordmark — always with wide tracking. Never ALL-CAPS a sentence.
- **Mid-dot as the brand punctuation mark:** `Cozinha · Sabor · Afeto`, `Horto · Ipatinga, MG`, `19h — 00h`. Ranges use an em dash with spaces.
- **Time and dates in Brazilian form:** `19h — 00h`, `Terça a sábado`, `Segunda: fechado`. Currency `R$ 68`.
- **CTA copy is an invitation, not a command stack:** *"Reservar uma mesa"*, *"Ver o menu"*, *"Falar no WhatsApp"*. One CTA verb per screen.
- **No emoji. Ever.** Not in UI, not in social captions rendered inside the product.
- **Words to avoid:** *gastronômico*, *experiência única*, *aconchegante* (overused), *premium*, *chef assinatura*.

## Visual foundations

**Colour.** Five colours, no others. Vinho arroxeado `#4E1517` and carvão `#17120F` carry every background — always as a gradient or as alternating sections, **never one flat fill across a page** (`--grad-vinho-carvao`, `--grad-carvao-vinho`, `--grad-carvao-deep`). Verde garrafa `#1F3327` is a line colour only: dividers, 1px borders, icon strokes — never a large field. Terracota suave `#B06A55` is reserved for the reservation CTA and hover states; **max two terracota elements per screen**. Areia quente `#D9C9B3` is the only "light" — it replaces white and gold as text on dark, and as an alternate light surface with vinho type on it. Pure `#FFFFFF` and `#000000` are forbidden; so is any saturated gold.

**Type.** Serif display at **medium weight (500)** for headings — Playfair Display; neutral geometric sans (Jost, 300 body / 500 labels) for everything else. Script/cursive exists only inside the logo artwork, never as live type. Scale is a 1.25 ratio on a 16px base, display clamped 44→84px. Tracking is the brand's signature: `-0.01em` on display, `+0.26em` uppercase on eyebrows (echoing `. COZINHA . SABOR . AFETO .`), `+0.18em` on the wordmark. Body line-height 1.68; prose capped at 62ch.

**Layout & spacing.** 4px base scale up to 128/160px; desktop sections breathe at 128px vertical, mobile at 64px. Gutters 56px desktop / 20px mobile, content max 1280px. Alignment alternates between sections — left-aligned text, then an asymmetric split with a large photo on one side; never centre-symmetric all the way down. The header is the only fixed/sticky element.

**Backgrounds & imagery.** Real photography dominates: warm, low-key, candle-lit, slight grain, shallow depth of field; food shot close and off-centre, room shots wide and dim. No vector food illustration, no repeating pattern, no stock "fork and knife" or wine-glass motif as decoration. Text over photography always sits on `--grad-protection` (transparent → carvão), never on a blurred capsule.

**Transparency & blur.** Only two uses: the sticky header (`--surface-sticky`, carvão at 72%, `blur(14px)`) and overlay scrims. Body content is never translucent.

**Borders, cards, elevation.** Radii 4px (default), 6px (cards), 8px (large frames). Pill radius is rationed to 1–2 elements per screen. **Elevation is a 1px verde-garrafa hairline, not a shadow** — diffuse `box-shadow` is banned except on true floating overlays (`--elev-overlay`). Cards: `--surface-card` (#241C18) or transparent "ghost", hairline border, 6px radius, no shadow.

**Motion.** Restrained. 140ms colour transitions, 240ms state changes, 520ms reveals (`opacity` + `translateY(8px)`), ease-out `cubic-bezier(.22,.61,.36,1)`. No bounce, no spring, no parallax, no auto-playing carousel.

**Interaction states.** Hover = colour shift to terracota (links, icons) or terracota-600 (CTA fill) plus, on icon buttons, a verde hairline appearing — never scale, never opacity fade. Press = the darker terracota, no shrink. Focus = 1px terracota-300 ring/border. Active nav item = verde-garrafa underline, not a filled pill. Disabled = 42% opacity.

## Iconography

No icon set was supplied with the brand, so two CDN sources are used and both are flagged substitutions:

- **Brand glyphs** — [Simple Icons](https://simpleicons.org) via `https://cdn.simpleicons.org/<slug>/<hex>`, tinted `D9C9B3`. Used for WhatsApp and Instagram only, **icon-only, never labelled with text** (brief rule). Wrapped by `SocialIcon`.
- **UI glyphs** — [Lucide](https://lucide.dev) static SVGs via jsDelivr (`lucide-static@0.428.0`), 1.5px stroke, tinted to areia with a CSS filter. Used for menu toggle, map-pin, clock, phone, chevron.

Rules: icons are 20–24px, stroke-only (no filled or duotone), never enclosed in a coloured circle, never used decoratively to illustrate food or dining. Unicode is used for punctuation (`·`, `—`) but never as an icon. No emoji, no icon font. Hand-drawn SVG icons are not permitted — pull from the CDNs above.

## Caveats / open items

1. **Fonts are substitutions.** No brand font files were provided. Playfair Display stands in for the Didone-ish wordmark serif; Jost for body. If licensed brand fonts exist, send the files and I'll swap the `@font-face` rules.
2. **Icon sets are substitutions** (Simple Icons + Lucide), as above.
3. **No photography.** Hero images in the mockup are drag-and-drop `<image-slot>` placeholders.
4. **Address, phone, hours and social handles are placeholders** — replace with the real ones.
5. Only header/footer surfaces were requested, so the website kit stops there.
