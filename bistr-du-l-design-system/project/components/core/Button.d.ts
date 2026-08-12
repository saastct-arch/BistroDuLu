/**
 * Buttons. `cta` is the terracota reservation button — at most two terracota elements per screen.
 * @startingPoint section="Core" subtitle="CTA, outline and quiet buttons" viewport="700x150"
 */
export interface ButtonProps {
  children?: React.ReactNode;
  variant?: 'cta' | 'outline' | 'quiet';
  size?: 'sm' | 'md' | 'lg';
  /** renders an <a> instead of a <button> */
  href?: string;
  disabled?: boolean;
  /** opt into the fully rounded shape — allowed on 1–2 elements per screen, never site-wide */
  pill?: boolean;
  onClick?: (e: React.MouseEvent) => void;
  style?: React.CSSProperties;
}
export function Button(props: ButtonProps): JSX.Element;
