from flask import Flask, render_template, url_for, redirect
import re

app = Flask(__name__)

nombre_de_empresa = "Precios Locos"
telefono = "(11) 5345-7787"     # formato: (11) 5345-7787
pattern = r'(\d)'
telefono_link = ''.join(re.findall(pattern, telefono))

mensaje_whatsapp = "Hola! Estoy interesado en hablar con algún representante de Precios Locos sobre un producto que me interesa."

lista_de_precios="https://docs.google.com/spreadsheets/d/1To91GePxRf-gTOqdDhFL_-ZIoMgvWOQMMdCi2nhLtFQ/edit?usp=drive_link"

@app.route("/")
def home():
    global nombre_de_empresa
    global telefono
    return render_template(
        "productos.html",
        titulo=nombre_de_empresa,
        mensaje1="Todas las publicaciones que ves en ML las podés obtener a precio de descuento pagando en efectivo o por transferencia.",
        mensaje2="Contactanos a nuestro WhatsApp. Clickeá sobre el teléfono para agregarnos a tus contactos.",
        envio="El envío se realiza a convenir entre nosotros y vos en algún lugar público para la seguridad de todos, aplica a CABA o AMBA. Para el resto del país, se envía por InterCargo.",
        telefono=telefono,
        telefono_link=telefono_link,
        bienvenida="Bienvenido a la Web Oficial de Precios Locos",
        medios_de_pago="Aceptamos MercadoPago, tarjetas (crédito y débito), transferencias y efectivo",
        envios="Enviamos a todo el pais",
        precios_comentarios="Lista de precios de celulares de alta y media gama - consultar stock",
        lista_de_precios=lista_de_precios,
        mensaje_whatsapp=mensaje_whatsapp
        )

"""
@app.route("/post")
def post_a_tweet():
    api_key = "PZWOlDaFJuBRlHjExc0TF8NWp"
    api_key_secret = "8vsqp60muuoz11KWosWTs1inyG5lDm6XOIRIMMfF26WRRpAnVC"
    access_token = "1699279935506894848-tvM9Z8IEs4dGCdAS7fQGsajvK4uoPn"
    access_token_secret = "eTXd50Jjlmf9cDRjy8UgOz0x5zhy1VEBPoXb3ADP0FCof"

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    # Create a tweet
    api.update_status("Test 1")

    return render_template("productos.html")
"""
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)