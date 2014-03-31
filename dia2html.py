#!/usr/bin/env python3

""" 
A kód feladata, hogy a Petőfi Irodalmi Múzeum - Digitális Irodalmi
Akadémia (pim.hu/dia) könyveit előkészítse e-könyvvé alakításra. 
A .html-ként mentett könyvből kivágja a szövegközi oldalszámozást,
és jelöli a címsorok helyét a formázás megkönnyítésére. 
"""

import datetime as dt
import argparse

<<<<<<< HEAD
parser = argparse.ArgumentParser(description="opciók beállítása")
parser.add_argument("-o", dest="oldalmark", action="store_const", const="[brake]", default="",
                    help="a beépített oldalszámok eredeti helyét jelöli (ha nem adod meg, akkor semmilyen jelölést nem fog használni)")
parser.add_argument("input", metavar="S", type=str, help="a feldolgozandó file neve")

=======
parser = argparse.ArgumentParser(description="get rid of some stuff")
parser.add_argument("--brake", dest="oldalmark", action="store_const", const="[brake]", default="",
                    help="a beépített oldalszámok eredeti helyét jelöli [brake] szöveggel")
parser.add_argument("input", help="a feldolgozandó fájl neve")
parser.add_argument("--output", help="az eredmény fájl neve")

args = parser.parse_args()

>>>>>>> fileba_iras
TORLES = (("<span class=\"old", "/span>"),
          ("<a name=", "rect\"/>"))
CSERE = ("<div class=\"szeparator\"> </div>", "<p>*</p>")
CIMSOR = ("<div class=\"cim\">", "rect\">")
OLDALMARK = args.oldalmark

f_name = args.input
stamp = dt.datetime.today()


f_name = parser.parse_args().input
stamp = dt.datetime.today()
w_name = f_name + str(stamp.isoformat(sep="-")[:-4])


def main():
<<<<<<< HEAD
  try:
    with open(f_name) as file:
      with open("f_name_tmp.html", "w") as file_w:
=======
  if args.output:
    w_name = args.output
  else:
    w_name = f_name + "_" + stamp.isoformat(sep="-")[:-6] + ".html"

  try:
    with open(f_name) as file:
      with open(w_name, "w") as file_w:
>>>>>>> fileba_iras
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
<<<<<<< HEAD
    print(f_name)

=======
    print(w_name)


if __name__ == '__main__':
  main()
>>>>>>> fileba_iras

if __name__ == '__main__':
  main()
