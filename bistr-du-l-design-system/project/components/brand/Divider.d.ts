/** 1px hairline in verde-garrafa — the brand's only divider. Also the substitute for box-shadow elevation. */
export interface DividerProps {
  tone?: 'verde' | 'areia';
  /** px inset on the cross axis */
  inset?: number;
  vertical?: boolean;
  style?: React.CSSProperties;
}
export function Divider(props: DividerProps): JSX.Element;
