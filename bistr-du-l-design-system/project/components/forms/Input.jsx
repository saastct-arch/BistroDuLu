export function Input({label,hint,type='text',id,style,...rest}){
  const [foc,setFoc]=React.useState(false);
  const uid=id||'in-'+(label||'field').toLowerCase().replace(/\W+/g,'-');
  return <label htmlFor={uid} style={{display:'grid',gap:8,fontFamily:'var(--font-sans-body)'}}>
    {label&&<span style={{fontSize:'var(--fs-eyebrow)',letterSpacing:'var(--ls-eyebrow)',textTransform:'uppercase',color:'var(--text-muted)'}}>{label}</span>}
    <input id={uid} type={type} onFocus={()=>setFoc(true)} onBlur={()=>setFoc(false)}
      style={{background:'transparent',border:'1px solid '+(foc?'var(--terracota-suave)':'var(--verde-300)'),borderRadius:'var(--r-xs)',padding:'12px 14px',color:'var(--text-strong)',fontFamily:'var(--font-sans-body)',fontSize:15,fontWeight:300,outline:'none',transition:'var(--t-color)',...style}} {...rest}/>
    {hint&&<span style={{fontSize:12,color:'var(--text-faint)'}}>{hint}</span>}
  </label>;
}
