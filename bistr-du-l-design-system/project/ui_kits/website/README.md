# UI kit — Website (Bistrô du Lú)

`index.html` is a static mockup of the **header** and **footer** of the site, at desktop (1180px content frame) and mobile (390px), plus the two requested header compositions:

- **Variação A** — monogram left, uppercase nav right, terracota "Reservar uma mesa" pinned far right.
- **Variação B** — nav split around a centred monogram, CTA still far right (mobile swaps the empty cell for a menu toggle).

Both headers are the translucent sticky treatment: `--surface-sticky` (carvão 72%) + `--blur-sticky`, bottom hairline in verde-garrafa. The footer is carvão with a verde-garrafa top hairline, address, opening hours, and WhatsApp/Instagram as icons only in areia quente.

Hero photography is intentionally empty: the `<image-slot>` rectangles accept dropped photos (they persist). No vector food illustration is permitted.

The live React equivalents are `components/navigation/SiteHeader.jsx` (`variant="left" | "centered"`, `compact`) and `SiteFooter.jsx`; see `components/navigation/navigation.card.html`.

Not built (no source material was provided): home body sections, menu page, reservation page. Ask for copy/photos and they can follow the same foundations.
