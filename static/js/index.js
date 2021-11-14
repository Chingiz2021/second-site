// Находим на странице форму и инпут
const form = document.querySelector('.form');


// Навешиваем на форму обработчик отправки 
form.onsubmit = async function(e) {
    const name = document.querySelector('.name');
    const phone = document.querySelector('.phone');
    const email = document.querySelector('.email');
    
    e.preventDefault();
    if(name.value  && phone.value  && email.value ){
        let data = {
            "name": name.value,
            "phone": phone.value,
            "email": email.value
         }
         let succes = document.querySelector('.order-alert')
         succes.classList.add('succes-al')
         setTimeout(() => {
             
        succes.classList.remove('succes-al')
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
          }).then(function (data) {
            if(data.message){

            name.value = ''
            phone.value = ''
            email.value = ''
            }
          })
    }
    else{
        
    }


};

var element = document.getElementById('phone');
var maskOptions = {
    mask: '+7(000)000-00-00',
    lazy: false
} 
var mask = new IMask(element, maskOptions);
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