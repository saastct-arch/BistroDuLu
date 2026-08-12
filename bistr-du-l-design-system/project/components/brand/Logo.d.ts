/**
 * The Bistrô du Lú mark. Three official lockups only — never redraw or recolour.
 * @startingPoint section="Brand" subtitle="Monogram, vertical and horizontal lockups" viewport="700x220"
 */
export interface LogoProps {
  /** monogram = B flourish only; vertical = mark over wordmark; horizontal = dark mark beside wordmark (light backgrounds only) */
  variant?: 'monogram' | 'vertical' | 'horizontal';
  /** rendered height in px */
  height?: number;
  /** override the resolved asset URL */
  src?: string;
  alt?: string;
  style?: React.CSSProperties;
}
export function Logo(props: LogoProps): JSX.Element;
