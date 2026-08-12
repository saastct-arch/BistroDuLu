/** Square icon-only control (social links, menu toggle). Icon inherits areia; hover shifts to terracota with a verde hairline. */
export interface IconButtonProps {
  children?: React.ReactNode;
  /** required accessible label — icon-only means no visible text */
  label: string;
  href?: string;
  size?: number;
  tone?: 'areia' | 'terracota';
  onClick?: (e: React.MouseEvent) => void;
  style?: React.CSSProperties;
}
export function IconButton(props: IconButtonProps): JSX.Element;
