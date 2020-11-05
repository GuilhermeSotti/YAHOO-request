import urllib.request
import os
import time

path = "C:/Users/Gpire/OneDrive/Área de Trabalho/Nova pasta"

def Check_YAHOO():

  stats_path = path + "/_KeyStats"
  stock_list = [x[0] for x in os.walk(stats_path)]
  for e in stock_list[1,:]:
    try:
      e = e.replace("C:/Users/Gpire/OneDrive/Área de Trabalho/Nova pasta\\", " ")
      link = "http://finance.yahoo.com/q/ks?s=" + e.upper() + "+Key+Statistics"
      resp = urllib.request.ulropen(link).read()
      save = "forward/" + str(e) + ".html"
      store = open(save, "w")
      store.write(str(resp))
      store.close() 

    except Exception as e:
      print(str(e))
      time.sleep(2)

Check_YAHOO()