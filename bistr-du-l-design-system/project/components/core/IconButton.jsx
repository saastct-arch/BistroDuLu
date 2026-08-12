export function IconButton({children,label,href,size=40,tone='areia',onClick,style,...rest}){
  const [h,setH]=React.useState(false);
  const El=href?'a':'button';
  const c=tone==='terracota'?'var(--terracota-suave)':'var(--areia-quente)';
  return <El href={href} aria-label={label} title={label} onClick={onClick}
    onMouseEnter={()=>setH(true)} onMouseLeave={()=>setH(false)}
    style={{width:size,height:size,display:'inline-flex',alignItems:'center',justifyContent:'center',borderRadius:'var(--r-xs)',border:'1px solid '+(h?'var(--verde-300)':'transparent'),background:'transparent',color:h?'var(--terracota-suave)':c,cursor:'pointer',transition:'var(--t-color)',padding:0,...style}} {...rest}>{children}</El>;
}
