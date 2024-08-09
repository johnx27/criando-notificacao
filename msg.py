from win10toast import ToastNotifier
from datetime import datetime

toaster= ToastNotifier()

def msg():
    mensagem= toaster.show_toast(
        "notificacao",
        "DEU CERTO",
        threaded= True,
        icon_path= None,
        duration=3
    )

hora_desejada="20:38"
hora_atual= datetime.now().strftime("%H:%M")
def executa_hora():
    if hora_desejada == hora_atual:
        return msg()
    
executa_hora()