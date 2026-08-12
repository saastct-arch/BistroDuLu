export function Eyebrow({children,dotted=true,tone='areia',as:As='span',style,...rest}){
  const color=tone==='terracota'?'var(--terracota-suave)':tone==='vinho'?'var(--text-on-light-muted)':'var(--text-muted)';
  const txt=dotted?'· '+String(children)+' ·':children;
  return <As style={{fontFamily:'var(--font-sans-body)',fontSize:'var(--fs-eyebrow)',fontWeight:500,letterSpacing:'var(--ls-eyebrow)',textTransform:'uppercase',color,display:'inline-block',...style}} {...rest}>{txt}</As>;
}
