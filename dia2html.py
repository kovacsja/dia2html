#!/usr/bin/env python3

""" 
A kód feladata, hogy a Petőfi Irodalmi Múzeum - Digitális Irodalmi
Akadémia (pim.hu/dia) könyveit előkészítse e-könyvvé alakításra. 
A .html-ként mentett könyvből kivágja a szövegközi oldalszámozást,
és jelöli a címsorok helyét a formázás megkönnyítésére. 
"""

import sys
import datetime 

TORLES = (("<span class=\"old","/span>"),
          ("<a name=", "rect\"/>"))
CSERE = ("<div class=\"szeparator\"> </div>", "<p>*</p>")
CIMSOR = ("<div class=\"cim\">", "rect\">")
OLDALMARK ="" #"<+>"

def main():    
  with open(sys.argv[1]) as file:
    for line in file:   
      #markerek törlése
      for t in TORLES:
        i = line.find(t[0])
        if i > -1:
          j = line.find(t[1],i) + len(t[1])
          line = line[:i]+line[j:]+OLDALMARK
      #csere
      line = line.replace(CSERE[0],CSERE[1])
      #címsorok jelölése
      i = line.find(CIMSOR[0])
      if i > -1:
        j = line.find(CIMSOR[1],i) + len(CIMSOR[1])
        line = line[:i]+ "<h1>CCC</h1>" + line[i:]
      print("{0}".format(line), end="")

if __name__ == '__main__':
	main()

