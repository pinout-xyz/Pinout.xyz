const boards=[...document.querySelectorAll('#boards .board')]
const facets=document.querySelector('.facets')
const filters=new Map()
const values=(board,key)=>(board.dataset[key]??'').split(',').map(value=>value.trim())
const collect=()=>{const collected=new Map()
for(const board of boards){for(const key of Object.keys(board.dataset)){const unique=collected.get(key)??new Set()
for(const value of values(board,key)){unique.add(value)}
collected.set(key,unique)
filters.set(key,'')}}
return collected}
const render=collected=>{for(const[key,unique]of collected){const heading=document.createElement('h2')
heading.textContent=key.split(/(?=[A-Z])/).join(' ').toLowerCase()
const list=document.createElement('ul')
list.className='facet'
for(const value of[...unique].sort((a,b)=>a.toLowerCase().localeCompare(b.toLowerCase()))){const item=document.createElement('li')
item.className='item'
item.dataset.key=key
item.dataset.value=value
item.textContent=value.length<=3?value.toUpperCase():value
list.append(item)}
facets.append(heading,list)}}
const matches=(board,ignored)=>[...filters].every(([key,value])=>key===ignored||!value||values(board,key).includes(value))
const available=(key,value)=>boards.some(board=>values(board,key).includes(value)&&matches(board,key))
const update=()=>{for(const board of boards){board.hidden=!matches(board)}
for(const item of facets.querySelectorAll('.item')){const{key,value}=item.dataset
const empty=filters.get(key)!==value&&!available(key,value)
item.classList.toggle('disabled',empty)
item.setAttribute('aria-disabled',empty)}}
const syncHash=()=>{window.location.hash=[...filters].filter(([,value])=>value).map(([key,value])=>`${key}=${encodeURIComponent(value)}`).join(':')}
const restore=()=>{for(const pair of window.location.hash.replace('#','').split(':')){const[key,encoded]=pair.split('=')
if(encoded&&filters.has(key)){filters.set(key,decodeURIComponent(encoded))}}
for(const item of facets.querySelectorAll('.item')){const value=item.dataset.value
item.classList.toggle('selected',Boolean(value)&&filters.get(item.dataset.key)===value)}
update()}
if(boards.length&&facets){render(collect())
facets.addEventListener('click',event=>{const item=event.target.closest('.item')
if(!item||item.classList.contains('disabled')){return}
const{key,value}=item.dataset
const selected=filters.get(key)!==value
for(const sibling of item.closest('ul').querySelectorAll('.item')){sibling.classList.remove('selected')}
item.classList.toggle('selected',selected)
filters.set(key,selected?value:'')
update()
syncHash()})
restore()}