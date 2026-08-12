import { Logo } from '../brand/Logo.jsx';
import { IconButton } from '../core/IconButton.jsx';
import { SocialIcon } from '../core/SocialIcon.jsx';
import { Eyebrow } from '../brand/Eyebrow.jsx';

const HOURS=[['Terça a sábado','19h — 00h'],['Domingo','12h — 16h'],['Segunda','Fechado']];

export function SiteFooter({compact=false,address=['Rua Jequitibá, 910 — Horto','Ipatinga · MG, 35160-306'],hours=HOURS,whatsapp='https://wa.me/5511999999999',instagram='https://instagram.com/bistrodulu',style,...rest}){
  const pad=compact?'40px 20px 28px':'72px 56px 40px';
  return <footer style={{background:'var(--carvao)',borderTop:'1px solid var(--verde-garrafa)',padding:pad,fontFamily:'var(--font-sans-body)',color:'var(--text-body)',...style}} {...rest}>
    <div style={{maxWidth:'var(--max-content)',margin:'0 auto',display:'grid',gap:compact?32:64,gridTemplateColumns:compact?'1fr':'1.1fr 1fr 1fr auto',alignItems:'start'}}>
      <div style={{display:'grid',gap:18,justifyItems:'start'}}>
        <Logo variant="vertical" height={compact?84:104}/>
      </div>
      <div style={{display:'grid',gap:10}}>
        <Eyebrow dotted={false}>Onde estamos</Eyebrow>
        <address style={{fontStyle:'normal',fontSize:15,fontWeight:300,lineHeight:1.7,color:'var(--text-muted)'}}>
          {address.map(l=><div key={l}>{l}</div>)}
        </address>
      </div>
      <div style={{display:'grid',gap:10}}>
        <Eyebrow dotted={false}>Horários</Eyebrow>
        <dl style={{margin:0,display:'grid',gap:6,fontSize:15,fontWeight:300}}>
          {hours.map(([d,t])=><div key={d} style={{display:'flex',gap:16,justifyContent:'space-between',maxWidth:320}}>
            <dt style={{color:'var(--text-muted)'}}>{d}</dt>
            <dd style={{margin:0,color:'var(--text-body)',whiteSpace:'nowrap'}}>{t}</dd>
          </div>)}
        </dl>
      </div>
      <div style={{display:'flex',gap:8,justifySelf:compact?'start':'end'}}>
        <IconButton label="WhatsApp" href={whatsapp}><SocialIcon name="whatsapp" size={22}/></IconButton>
        <IconButton label="Instagram" href={instagram}><SocialIcon name="instagram" size={22}/></IconButton>
      </div>
    </div>
    <div style={{maxWidth:'var(--max-content)',margin:compact?'28px auto 0':'48px auto 0',paddingTop:16,borderTop:'1px solid var(--areia-a08)',display:'flex',flexWrap:'wrap',gap:12,justifyContent:'space-between',fontSize:12,letterSpacing:'.08em',color:'var(--text-faint)'}}>
      <span>© {new Date().getFullYear()} Bistrô du Lú · Desde 2017</span>
      <span>Cozinha · Sabor · Afeto</span>
    </div>
  </footer>;
}
