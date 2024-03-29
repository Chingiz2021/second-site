

def send_admin_email(name, phone, email,types):
    style = """
    <style>
        .header{
            max-width: 100%;
            min-height: 20vh;
            padding: 1em;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .header img{
            max-width: 100%;
        }
        .text-email{
            min-height: 60vh;
            max-width: 100%;
            padding: 1em;
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }
        .detail{
            font-size: 1.3em;
            font-weight: bold;
        }
  
        h3{
            
        }
        .text-detail{
        
        
        }
        span{
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
    """
    html = '''\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width"/>
        <style type="text/css">
            {style}
        </style>
    </head>
    <body>
        <div class="header" style="background-color: #23164B;">
            <img src="https://unwanted.ae/static/images/logo1.png" alt="">
        </div>
        <div class="text-email">
            <h3>Здравствуйте ,Уважаемый(ая) администратор!</h3>
            
            <h4>Поступила новая заявка</h4>
            
            <div class="text-detail">
                <p class="detail">Детали сообщения :</p>
                <p><span>Имя клиента: </span> {name}</p>
                <p><span>Телефон клиента: </span> {phone}</p>
                <p><span>Адрес клиента: </span> {email}</p>
                <p><span>Тип вещей: </span> {types}</p>
                
            </div>
            <div>
                <p>Удачного бизнеса!</p>
            </div>
        </div>
    </body>
    </html>
    '''.format(**locals())
    return html
#gg
def send_client_email(name, phone, email):
    style = """
    <style>
        .header{
            max-width: 100%;
            min-height: 20vh;
            padding: 1em;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .header img{
            max-width: 100%;
        }
        .text-email{
            min-height: 60vh;
            max-width: 100%;
            padding: 1em;
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }
        .detail{
            font-size: 1.3em;
            font-weight: bold;
        }
  
        h3{
            
        }
        .text-detail{
        
        
        }
        span{
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
    """
    html = '''\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width"/>
        <style type="text/css">
            {style}
        </style>
    </head>
    <body>
        <div class="header" style="background-color: #23164B;">
            <img src="https://unwanted.ae/static/images/logo1.png" alt="">
        </div>
        <div class="text-email">
            <h3>Hello Dear {name}!</h3>
            
            <h4>New application received</h4>
            
            <div class="text-detail">
                <p class="detail">Message details :</p>
                <p><span>Your name: </span> {name}</p>
                <p><span>Your phone: </span> {phone}</p>
                <p><span>Your Email: </span> {email}</p>
                <h4>Our specialist will contact you shortly</h4>
            </div>
            <div>
                <p>We wish you a good day!</p>
            </div>
        </div>
    </body>
    </html>
    '''.format(**locals())
    return html

def send_admin_email_sotr(name, phone, email,message):
    style = """
    <style>
        .header{
            max-width: 100%;
            min-height: 20vh;
            padding: 1em;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .header img{
            max-width: 100%;
        }
        .text-email{
            min-height: 60vh;
            max-width: 100%;
            padding: 1em;
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }
        .detail{
            font-size: 1.3em;
            font-weight: bold;
        }
  
        h3{
            
        }
        .text-detail{
        
        
        }
        span{
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
    """
    html = '''\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width"/>
        <style type="text/css">
            {style}
        </style>
    </head>
    <body>
        <div class="header" style="background-color: #23164B;">
            <img src="https://unwanted.ae/static/images/logo1.png" alt="">
        </div>
        <div class="text-email">
            <h3>Здравствуйте ,Уважаемый(ая) администратор!</h3>
            
            <h4>Поступила новая заявка  на сотрудничество</h4>
            
            <div class="text-detail">
                <p class="detail">Детали сообщения :</p>
                <p><span>Имя клиента: </span> {name}</p>
                <p><span>Телефон клиента: </span> {phone}</p>
                <p><span>Email клиента: </span> {email}</p>
                <p><span>сообщение клиента: </span> {message}</p>
                
            </div>
            <div>
                <p>Удачного бизнеса!</p>
            </div>
        </div>
    </body>
    </html>
    '''.format(**locals())
    return html


def send_admin_email_commands(name, phone,message):
    style = """
    <style>
        .header{
            max-width: 100%;
            min-height: 20vh;
            padding: 1em;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .header img{
            max-width: 100%;
        }
        .text-email{
            min-height: 60vh;
            max-width: 100%;
            padding: 1em;
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
        }
        .detail{
            font-size: 1.3em;
            font-weight: bold;
        }
  
        h3{
            
        }
        .text-detail{
        
        
        }
        span{
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
    """
    html = '''\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width"/>
        <style type="text/css">
            {style}
        </style>
    </head>
    <body>
        <div class="header" style="background-color: #23164B;">
            <img src="https://unwanted.ae/static/images/logo1.png" alt="">
        </div>
        <div class="text-email">
            <h3>Здравствуйте ,Уважаемый(ая) администратор!</h3>
            
            <h4>Поступила новая заявка  из раздела хочу в команду</h4>
            
            <div class="text-detail">
                <p class="detail">Детали сообщения :</p>
                <p><span>Имя клиента: </span> {name}</p>
                <p><span>Телефон клиента: </span> {phone}</p>
                <p><span>сообщение клиента: </span> {message}</p>
                
            </div>
            <div>
                <p>Удачного бизнеса!</p>
            </div>
        </div>
    </body>
    </html>
    '''.format(**locals())
    return html
