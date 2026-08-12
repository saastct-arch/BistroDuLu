/**
 * Site header: translucent carvão bar, monogram, uppercase nav, always-visible terracota reservation CTA.
 * @startingPoint section="Website" subtitle="Sticky translucent header, logo left or centered" viewport="1280x120"
 */
export interface SiteHeaderProps {
  /** 'left' = monogram left, nav + CTA right; 'centered' = nav split around a centered monogram */
  variant?: 'left' | 'centered';
  /** mobile layout (390px): menu toggle left, centred monogram, short CTA right */
  compact?: boolean;
  items?: string[];
  cta?: string;
  onCta?: () => void;
  onMenu?: () => void;
  style?: React.CSSProperties;
}
export function SiteHeader(props: SiteHeaderProps): JSX.Element;
