

// Находим на странице форму и инпут
const form = document.querySelector('.form');

const form2 = document.querySelector('#form2');
const form3 = document.querySelector('.form3');
const form5 = document.querySelector('#myform');
const form6 = document.querySelector('#myform2');


function onCount(){
  if(localStorage.getItem('succes')){
    console.log(11);
  }
  else{
  fetch('/create_counts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
  })
  .then(function (responce) {
    return responce.json();
  }).then(function (data) {
    console.log(data);
  })
}
}

setTimeout(() => {
  onCount()
}, 4000)

let arrpovod = []
// Навешиваем на форму обработчик отправки 
function onDrugoe(){
  let drugoe = document.querySelector('.drugoe');
  
  if(!drugoe.value){
    drugoe.value = 'other'
    let mess = document.querySelector('#mess');
    arrpovod.push(drugoe.value)
   
    mess.classList.add('mess2')
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
          mess.classList.remove('mess2')
      }
  
  }
  
  }
  
  console.log(arrpovod);
}

function onDrugoe1(){
  let drugoe = document.querySelector('.prin');
  
  if(!drugoe.value){
    drugoe.value = 'Домашние принадлежности'
    arrpovod.push(drugoe.value)
  }else{
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  }
  
  console.log(arrpovod);
}

function onDrugoe2(){
  let drugoe = document.querySelector('.zapas');
  
  if(!drugoe.value){
    drugoe.value = 'Запасные части'
    arrpovod.push(drugoe.value)
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  
  }
  
  console.log(arrpovod);
}

function onDrugoe3(){
  let drugoe = document.querySelector('.book');
  
  if(!drugoe.value){
    drugoe.value = 'Книги'
    arrpovod.push(drugoe.value)
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  
  }
  
  console.log(arrpovod);
}
function onDrugoe4(){
  let drugoe = document.querySelector('.meb');
  
  if(!drugoe.value){
    drugoe.value = 'Мебель'
    arrpovod.push(drugoe.value)
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  
  }
  
  console.log(arrpovod);
}

function onDrugoe5(){
  let drugoe = document.querySelector('.texn');
  
  if(!drugoe.value){
    drugoe.value = 'Home Appliances'
    arrpovod.push(drugoe.value)
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  
  }
  
  console.log(arrpovod);
}
function onDrugoe6(){
  let drugoe = document.querySelector('.aks');
  
  if(!drugoe.value){
    drugoe.value = 'Furniture'
    arrpovod.push(drugoe.value)
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  
  }
  
  console.log(arrpovod);
}
function onDrugoe7(){
  let drugoe = document.querySelector('.pos');
  
  if(!drugoe.value){
    drugoe.value = 'Dishes'
    arrpovod.push(drugoe.value)
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  
  }
  
  console.log(arrpovod);
}
function onDrugoe8(){
  let drugoe = document.querySelector('.ob');
  
  if(!drugoe.value){
    drugoe.value = 'Shoes'
    arrpovod.push(drugoe.value)
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  
  }
  
  console.log(arrpovod);
}
function onDrugoe9(){
  let drugoe = document.querySelector('.od');
  
  if(!drugoe.value){
    drugoe.value = 'Clothes'
    arrpovod.push(drugoe.value)
  }else{
    
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === drugoe.value ) { 
  
        arrpovod.splice(i, 1); 
          drugoe.value = ''
      }
  
  }
  
  }
  
  console.log(arrpovod);
}
let clickbutton
function activefunc(element) {
  if(document.documentElement.clientWidth > 990){
  if(clickbutton){
    clickbutton.style = 'border: 2px #EB5534 solid;'
  }
  if (clickbutton != element){
    element.style = 'border: 2px #a9a7a7 solid;min-height: 18px;border-radius: 50%;margin: 1em;height: 20px;width: 20px;'
    clickbutton = element
  }
}
if(document.documentElement.clientWidth < 990){
  if(clickbutton){
    clickbutton.style = 'margin: 10px;padding: 0;border: 3px #EB5534 solid;width: 20px;height: 20px;'
  }
  if (clickbutton != element){
    element.style = 'border: 3px #a9a7a7 solid;margin: 10px;padding: 0;width: 20px;height: 20px;'
    clickbutton = element
  }
}


}
function onTextComment(params) {
  let docs = params.parentNode
  let name = docs.children[0]
  let comment = docs.children[1]
  
  document.querySelector('.bodys').innerHTML = comment.innerHTML
}
form.onsubmit = async function(e) {
    console.log(6666);
    const name = document.querySelector('.name');
    const phone = document.querySelector('.phone');
    const email = document.querySelector('.email');
    
    e.preventDefault();
    if(phone.value){
    if(name.value  && phone.value  && email.value ){
      let form = document.querySelector('.form')
      form.classList.add('form-none')
      let form2 = document.querySelector('#form2')
      form2.classList.add('form2-block')
      
    }
    else{
        
    }
  }else{

    let ph = document.querySelector('.err')
    ph.classList.add('blerr')
    setTimeout(() => {
      ph.classList.remove('blerr')
    }, 2000);
  }

};
form2.onsubmit = async function(e) {

  e.preventDefault();
 
  const name = document.querySelector('.name');
  const phone = document.querySelector('.phone');
  const adress = document.querySelector('.email');
  const mess = document.querySelector(".textmessage");
  if(mess.value){
    arrpovod.push(mess.value)
    mess.value = ''
    for( var i = 0; i < arrpovod.length; i++){ 
    
      if ( arrpovod[i] === 'другое' ) { 
  
        arrpovod.splice(i, 1); 
      }
  
  }
  }
  let data = {
    "name": name.value,
    "phone": phone.value,
    "adress": adress.value,
    "type": arrpovod.join()
 }
 

 if(localStorage.getItem('succes')){
  let form = document.querySelector('.form')
  form.classList.remove('form-none')
  let form2 = document.querySelector('#form2')
  form2.classList.remove('form2-block')
  let mess = document.querySelector('#mess');
  
  mess.classList.remove('mess2')
  let succes = document.querySelector('.nonel')
  succes.classList.add('addal')
  setTimeout(() => {
    succes.classList.remove('addal')
  }, 6000);
  name.value = ''
  phone.value = ''
  adress.value = ''
  arrpovod = []
 }
 else{
   if(arrpovod.join().length > 0){
  let succes = document.querySelector('.order-alert')
  succes.classList.add('succes-al')
  setTimeout(() => {
 
 succes.classList.remove('succes-al')
 let form = document.querySelector('.form')
 form.classList.remove('form-none')
 let form2 = document.querySelector('#form2')
 form2.classList.remove('form2-block')
 let mess = document.querySelector('#mess');
 
 mess.classList.remove('mess2')
  }, 2000);
 
 fetch('/orders/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(data)
  })
  .then(function (responce) {
    return responce.json();
  }).then(function (resp) {
    localStorage.setItem('succes', 'ok');
    name.value = ''
    phone.value = ''
    adress.value = ''
  })
}else{
  let ph = document.querySelector('.err2')
  ph.classList.add('blerr')
  setTimeout(() => {
    ph.classList.remove('blerr')
  }, 2000);
}
}
}

form3.onsubmit = async function(e) {
  
  const name = document.querySelector('.names');
  const phone = document.querySelector('.phone2');
  const email = document.querySelector('.emails');
  const message = document.querySelector('.message');
  
  e.preventDefault();
  if(name.value  && phone.value  && email.value ){
    let data = {
      "name": name.value,
      "phone": phone.value,
      "email": email.value,
      "message":message.value
   }
   let succes = document.querySelector('.sotrm')
 succes.classList.add('sorm2')
 setTimeout(() => {
  succes.classList.remove('sorm2')
 }, 2000);
   fetch('/sotrudnichestvo', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(data)
  })
  .then(function (responce) {
    return responce.json();
  }).then(function (data) {
    name.value = ''
    phone.value = ''
    email.value = ''
    message.value = ''
  })
    
  }
  else{
      
  }


};
var element = document.getElementById('phone');
var maskOptions = {
  mask: '+{7}(000)000-00-00',
  
} 

var element2 = document.getElementById('phone2');
var element22 = document.getElementById('phone22');

var mask = new IMask(element, maskOptions);
var mask2 = new IMask(element2, maskOptions);
var mask22 = new IMask(element22, maskOptions);
if(document.documentElement.clientWidth < 990){
  const navLinks = document.querySelectorAll('.nav-item')
  const menuToggle = document.getElementById('navbarSupportedContent')
  const bsCollapse = new bootstrap.Collapse(menuToggle, {
    toggle: false
  })
  navLinks.forEach((l) => {
      l.addEventListener('click', () => { bsCollapse.toggle() })
  })
}


let links = document.querySelectorAll('.nav-link');
for(let i=0; i<links.length; i++){
  links[i].addEventListener('click', function() {
    for(let j=0; j<links.length; j++)
      links[j].classList.remove('active');
    this.classList.add('active');
  });
}

form5.onsubmit = async function(e) {
  e.preventDefault();
  console.log(1212);
  const name = document.querySelector('.nameso');
  const mess = document.querySelector(".messageso");

  let data = {
    "name_user": name.value,
    "message_text": mess.value
 }

 let succes = document.querySelector('.sotrmes')
 console.log(succes);
 succes.classList.add('succes-als')
 setTimeout(() => {
  name.value = ''
  mess.value = ''
succes.classList.remove('succes-als')
 }, 2000);
 fetch('/comment_create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(data)
  })
  .then(function (responce) {
    return responce.json();
  }).then(function (data) {
    console.log(data);
  })
}

form6.onsubmit = async function(e) {
  e.preventDefault();
  const name = document.querySelector('.nameso2');
  const  phone = document.querySelector(".phone22");
  const  mess = document.querySelector(".messageso2");

  let data = {
    "name_user": name.value,
    "phone": phone.value,
    "message_text": mess.value,
 }

 let succes = document.querySelector('.sotrmes2')
 console.log(data);
 succes.classList.add('succes-als')
 setTimeout(() => {
  name.value = ''
  mess.value = ''
  phone.value = ''
succes.classList.remove('succes-als')
 }, 2000);
 fetch('/create_commands', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(data)
  })
  .then(function (responce) {
    return responce.json();
  }).then(function (data) {
    console.log(data);
  })
}

