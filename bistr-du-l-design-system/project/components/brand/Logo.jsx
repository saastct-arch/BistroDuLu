const dsRoot=()=>{const s=Array.from(document.querySelectorAll('script[src]')).map(x=>x.src).find(u=>u.indexOf('_ds_bundle.js')>-1);return s?s.replace(/_ds_bundle\.js.*$/,''):'';};
const FILES={monogram:'assets/logo-monogram-areia.png',vertical:'assets/logo-vertical-areia.png',horizontal:'assets/logo-horizontal-vinho.png'};

export function Logo({variant='monogram',height,src,alt='Bistrô du Lú',style,...rest}){
  const h=height||(variant==='monogram'?44:variant==='vertical'?96:40);
  return <img src={src||dsRoot()+FILES[variant]} alt={alt} style={{height:h,width:'auto',display:'block',...style}} {...rest}/>;
}
