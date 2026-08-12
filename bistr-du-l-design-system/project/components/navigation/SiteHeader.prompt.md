One-sentence: the site's sticky header — use `variant="left"` as the default and `compact` below 768px.

```jsx
<SiteHeader variant="left" />
<SiteHeader compact />
```

Chosen composition: `variant="left"` on desktop; `compact` on mobile renders the centred-monogram layout (menu toggle left, monogram centred, short CTA right). The CTA is always visible, including on mobile (label shortens to "Reservar"). Background is carvão at 72% with blur so content shows through on scroll; bottom edge is a verde-garrafa hairline.
