/** Small outlined label for dish attributes (vegetariano, safra, sazonal). */
export interface TagProps {
  children?: React.ReactNode;
  tone?: 'verde' | 'terracota' | 'areia';
  style?: React.CSSProperties;
}
export function Tag(props: TagProps): JSX.Element;
