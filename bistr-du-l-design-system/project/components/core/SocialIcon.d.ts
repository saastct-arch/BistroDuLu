/** Brand glyph from the Simple Icons CDN (whatsapp, instagram, ...), tinted by hex. Substitution: no icon set was supplied with the brand. */
export interface SocialIconProps {
  /** Simple Icons slug, e.g. "whatsapp" | "instagram" */
  name: string;
  size?: number;
  /** hex without '#' or with — defaults to areia-quente */
  color?: string;
  style?: React.CSSProperties;
}
export function SocialIcon(props: SocialIconProps): JSX.Element;
