export function Button({children,variant='cta',size='md',href,disabled,pill=false,onClick,style,...rest}){
  const [h,setH]=React.useState(false);
  const pad=size==='sm'?'9px 16px':size==='lg'?'18px 34px':'13px 26px';
  const fs=size==='sm'?13:size==='lg'?16:14;
  const base={fontFamily:'var(--font-sans-body)',fontSize:fs,fontWeight:500,letterSpacing:'.1em',textTransform:'uppercase',padding:pad,borderRadius:pill?'var(--r-pill)':'var(--r-xs)',cursor:disabled?'not-allowed':'pointer',display:'inline-flex',alignItems:'center',gap:10,textDecoration:'none',transition:'var(--t-color)',opacity:disabled?.42:1,lineHeight:1};
  const skin=variant==='cta'
    ? {background:h&&!disabled?'var(--cta-bg-hover)':'var(--cta-bg)',color:'var(--cta-fg)',border:'1px solid transparent'}
    : variant==='outline'
    ? {background:'transparent',color:h&&!disabled?'var(--terracota-suave)':'var(--text-body)',border:'1px solid '+(h&&!disabled?'var(--terracota-suave)':'var(--verde-300)')}
    : {background:'transparent',color:h&&!disabled?'var(--terracota-suave)':'var(--text-muted)',border:'1px solid transparent',padding:size==='sm'?'6px 2px':'8px 2px',letterSpacing:'.14em'};
  const El=href?'a':'button';
  return <El href={href} disabled={El==='button'?disabled:undefined} onClick={disabled?undefined:onClick}
    onMouseEnter={()=>setH(true)} onMouseLeave={()=>setH(false)}
    style={{...base,...skin,...style}} {...rest}>{children}</El>;
}
