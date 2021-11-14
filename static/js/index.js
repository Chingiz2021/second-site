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
            let succes = document.querySelector('.order-alert')
            succes.classList.add('succes-al')
            setTimeout(() => {
                
           succes.classList.remove('succes-al')
            }, 2000);
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

const navLinks = document.querySelectorAll('.nav-item')
const menuToggle = document.getElementById('navbarSupportedContent')
const bsCollapse = new bootstrap.Collapse(menuToggle, {
  toggle: false
})
navLinks.forEach((l) => {
    l.addEventListener('click', () => { bsCollapse.toggle() })
})