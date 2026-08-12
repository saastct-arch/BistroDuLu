/** Text field for the reservation form. Transparent fill, verde hairline, terracota focus. */
export interface InputProps {
  label?: string;
  hint?: string;
  type?: string;
  id?: string;
  placeholder?: string;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  style?: React.CSSProperties;
}
export function Input(props: InputProps): JSX.Element;
