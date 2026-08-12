import { Logo } from '../brand/Logo.jsx';
import { Button } from '../core/Button.jsx';

const NAV=['Menu','A casa','Reservas','Contato'];

function NavItem({children,active}){
  const [h,setH]=React.useState(false);
  return <a href="#" onMouseEnter={()=>setH(true)} onMouseLeave={()=>setH(false)}
    style={{fontFamily:'var(--font-sans-body)',fontSize:13,fontWeight:400,letterSpacing:'.16em',textTransform:'uppercase',textDecoration:'none',color:h||active?'var(--terracota-suave)':'var(--text-body)',transition:'var(--t-color)',paddingBottom:4,borderBottom:'1px solid '+(active?'var(--verde-300)':'transparent'),whiteSpace:'nowrap'}}>{children}</a>;
}

export function SiteHeader({variant='left',compact=false,items=NAV,cta='Reservar uma mesa',onCta,onMenu,style,...rest}){
  const pad=compact?'0 20px':'0 56px';
  const shell={position:'relative',height:compact?'var(--header-h-mobile)':'var(--header-h-desktop)',padding:pad,background:'var(--surface-sticky)',backdropFilter:'var(--blur-sticky)',WebkitBackdropFilter:'var(--blur-sticky)',borderBottom:'1px solid var(--verde-a55)',display:'grid',alignItems:'center',...style};
  const ctaEl=<Button variant="cta" size={compact?'sm':'md'} onClick={onCta}>{compact?'Reservar':cta}</Button>;

  if(compact){
    return <header style={{...shell,gridTemplateColumns:'auto 1fr auto',gap:10}} {...rest}>
      <button aria-label="Abrir menu" onClick={onMenu} style={{width:34,height:34,display:'inline-flex',alignItems:'center',justifyContent:'center',background:'transparent',border:'1px solid transparent',borderRadius:'var(--r-xs)',cursor:'pointer',padding:0}}>
        <img src="https://cdn.jsdelivr.net/npm/lucide-static@0.428.0/icons/menu.svg" width="20" height="20" alt="" style={{filter:'invert(85%) sepia(18%) saturate(310%) hue-rotate(348deg) brightness(96%)'}}/>
      </button>
      <Logo variant="monogram" height={34} style={{justifySelf:'center'}}/>
      {ctaEl}
    </header>;
  }
  if(variant==='centered'){
    return <header style={{...shell,gridTemplateColumns:'1fr auto 1fr',gap:32}} {...rest}>
      <nav style={{display:'flex',gap:30,justifySelf:'start'}}>{items.slice(0,2).map(i=><NavItem key={i}>{i}</NavItem>)}</nav>
      <Logo variant="monogram" height={48} style={{justifySelf:'center'}}/>
      <div style={{display:'flex',alignItems:'center',gap:30,justifySelf:'end'}}>
        {items.slice(2).map(i=><NavItem key={i}>{i}</NavItem>)}
        {ctaEl}
      </div>
    </header>;
  }
  return <header style={{...shell,gridTemplateColumns:'auto 1fr auto',gap:40}} {...rest}>
    <Logo variant="monogram" height={44}/>
    <nav style={{display:'flex',gap:34,justifySelf:'end',alignItems:'center'}}>{items.map(i=><NavItem key={i} active={i==='Menu'}>{i}</NavItem>)}</nav>
    {ctaEl}
  </header>;
}
