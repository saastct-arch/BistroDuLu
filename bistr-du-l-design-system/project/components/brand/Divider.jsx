export function Divider({tone='verde',inset=0,vertical=false,style,...rest}){
  const c=tone==='areia'?'var(--areia-a14)':'var(--verde-garrafa)';
  const s=vertical
    ? {width:1,alignSelf:'stretch',background:c,margin:`${inset}px 0`}
    : {height:1,width:'100%',background:c,margin:`0 ${inset}px`,border:0};
  return <div role="separator" style={{...s,...style}} {...rest}/>;
}
