/** Surface container. Elevation is a 1px verde-garrafa hairline — never a diffuse box-shadow. */
export interface CardProps {
  children?: React.ReactNode;
  tone?: 'dark' | 'light' | 'ghost';
  hairline?: boolean;
  /** padding in px */
  pad?: number;
  style?: React.CSSProperties;
}
export function Card(props: CardProps): JSX.Element;
