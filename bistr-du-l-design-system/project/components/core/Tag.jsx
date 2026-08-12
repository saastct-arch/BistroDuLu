export function Tag({children,tone='verde',style,...rest}){
  const skin=tone==='terracota'?{color:'var(--terracota-suave)',borderColor:'var(--terracota-600)'}
    :tone==='areia'?{color:'var(--text-body)',borderColor:'var(--areia-a38)'}
    :{color:'var(--text-body)',borderColor:'var(--verde-300)'};
  return <span style={{fontFamily:'var(--font-sans-body)',fontSize:11,fontWeight:500,letterSpacing:'.16em',textTransform:'uppercase',padding:'5px 9px',border:'1px solid',borderRadius:'var(--r-xs)',display:'inline-block',lineHeight:1,...skin,...style}} {...rest}>{children}</span>;
}
