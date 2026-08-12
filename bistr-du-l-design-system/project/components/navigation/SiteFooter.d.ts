/**
 * Site footer on carvão: vertical lockup, address, opening hours, and WhatsApp/Instagram icon-only links in areia.
 * @startingPoint section="Website" subtitle="Carvão footer with hours, address and social icons" viewport="1280x420"
 */
export interface SiteFooterProps {
  /** mobile (390px) single-column stack */
  compact?: boolean;
  address?: string[];
  /** [day range, hours] pairs */
  hours?: Array<[string, string]>;
  whatsapp?: string;
  instagram?: string;
  style?: React.CSSProperties;
}
export function SiteFooter(props: SiteFooterProps): JSX.Element;
