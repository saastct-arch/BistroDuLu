export function Card({children,tone='dark',hairline=true,pad=24,style,...rest}){
  const skin=tone==='light'
    ? {background:'var(--surface-card-light)',color:'var(--text-on-light)',border:hairline?'var(--border-light)':'none'}
    : tone==='ghost'
    ? {background:'transparent',color:'var(--text-body)',border:hairline?'var(--border-hairline)':'none'}
    : {background:'var(--surface-card)',color:'var(--text-body)',border:hairline?'var(--border-hairline)':'none'};
  return <div style={{borderRadius:'var(--r-sm)',padding:pad,boxShadow:'none',...skin,...style}} {...rest}>{children}</div>;
}
