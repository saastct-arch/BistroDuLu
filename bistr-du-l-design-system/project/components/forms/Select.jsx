export function Select({label,options=[],id,style,...rest}){
  const uid=id||'sel-'+(label||'field').toLowerCase().replace(/\W+/g,'-');
  return <label htmlFor={uid} style={{display:'grid',gap:8,fontFamily:'var(--font-sans-body)'}}>
    {label&&<span style={{fontSize:'var(--fs-eyebrow)',letterSpacing:'var(--ls-eyebrow)',textTransform:'uppercase',color:'var(--text-muted)'}}>{label}</span>}
    <select id={uid} style={{background:'transparent',border:'1px solid var(--verde-300)',borderRadius:'var(--r-xs)',padding:'12px 14px',color:'var(--text-strong)',fontFamily:'var(--font-sans-body)',fontSize:15,fontWeight:300,outline:'none',appearance:'none',...style}} {...rest}>
      {options.map(o=>{const v=typeof o==='string'?o:o.value,l=typeof o==='string'?o:o.label;return <option key={v} value={v} style={{color:'#17120F'}}>{l}</option>;})}
    </select>
  </label>;
}
