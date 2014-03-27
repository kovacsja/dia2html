#!/usr/bin/env python3

""" 
A kód feladata, hogy a Petőfi Irodalmi Múzeum - Digitális Irodalmi
Akadémia (pim.hu/dia) könyveit előkészítse e-könyvvé alakításra. 
A .html-ként mentett könyvből kivágja a szövegközi oldalszámozást,
és jelöli a címsorok helyét a formázás megkönnyítésére. 
"""

import datetime as dt
import argparse

parser = argparse.ArgumentParser(description="opciók beállítása")
parser.add_argument("-o", dest="oldalmark", action="store_const", const="[brake]", default="",
                    help="a beépített oldalszámok eredeti helyét jelöli (ha nem adod meg, akkor semmilyen jelölést nem fog használni)")
parser.add_argument("input", metavar="S", type=str, help="a feldolgozandó file neve")

TORLES = (("<span class=\"old", "/span>"),
          ("<a name=", "rect\"/>"))
CSERE = ("<div class=\"szeparator\"> </div>", "<p>*</p>")
CIMSOR = ("<div class=\"cim\">", "rect\">")
OLDALMARK = parser.parse_args().oldalmark

f_name = parser.parse_args().input
stamp = dt.datetime.today()
w_name = f_name + str(stamp.isoformat(sep="-")[:-4])


def main():
  try:
    with open(f_name) as file:
      with open("f_name_tmp.html", "w") as file_w:
        for line in file:
          #markerek törlése
          for t in TORLES:
            i = line.find(t[0])
            if i > -1:
              j = line.find(t[1], i) + len(t[1])
              line = line[:i] + line[j:] + OLDALMARK
          #csere
          line = line.replace(CSERE[0], CSERE[1])
          #címsorok jelölése
          i = line.find(CIMSOR[0])
          if i > -1:
            j = line.find(CIMSOR[1], i) + len(CIMSOR[1])
            line = line[:i] + "<h1>--=CIM=--</h1>" + line[i:]
          #sorok kiírása új fájlba
          #print("{0}".format(line), end="")
          file_w.write(line)
  finally:
    print(f_name)


if __name__ == '__main__':
  main()

