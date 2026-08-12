/** Wide-tracked uppercase micro-label, echoing the logo's ". COZINHA . SABOR . AFETO ." line. */
export interface EyebrowProps {
  children?: React.ReactNode;
  /** wrap the label in the brand's mid-dots */
  dotted?: boolean;
  tone?: 'areia' | 'terracota' | 'vinho';
  as?: keyof JSX.IntrinsicElements;
  style?: React.CSSProperties;
}
export function Eyebrow(props: EyebrowProps): JSX.Element;
