export function SocialIcon({name,size=20,color='D9C9B3',style,...rest}){
  const hex=String(color).replace('#','');
  return <img src={`https://cdn.simpleicons.org/${name}/${hex}`} alt="" width={size} height={size} style={{display:'block',...style}} {...rest}/>;
}
