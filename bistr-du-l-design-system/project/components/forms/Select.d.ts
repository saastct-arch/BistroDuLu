/** Native select styled to match Input — used for party size and service. */
export interface SelectProps {
  label?: string;
  options?: Array<string | { value: string; label: string }>;
  id?: string;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLSelectElement>) => void;
  style?: React.CSSProperties;
}
export function Select(props: SelectProps): JSX.Element;
