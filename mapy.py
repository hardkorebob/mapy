#!/usr/bin/env python3
import tkinter as tk
import segno as qr
import geopy as geo
import tkinter.font as font
import tkintermapview as mapy
import datetime


class Main(tk.Tk):
    def __init__(_):
        super().__init__()
        maps = Maps(_)
        maps.pack(expand=1, fill='both')


class Maps(tk.Frame): 
    def __init__(_, ap, ):
        super().__init__(ap)
        _.qr_file = 'mapyQRcode.png'
        _.fill = 'both'
        _.rel = 'flat'
        _.e = 0
        _.font = font.nametofont("TkFixedFont")
        _.font.configure(size=14)

        f = tk.Frame(_, )
        f.pack(expand=1, fill=_.fill)

        _.infoLabel = tk.Label(f, text = "Enter address: ", font=_.font, )
        _.infoLabel.pack(expand=_.e, fill=_.fill)

        _.gpsEntry = tk.Entry(f, cursor='dotbox', relief=_.rel, font=_.font, fg='green', )
        _.gpsEntry.insert(0, "Fredericksburg, VA")
        _.gpsEntry.pack(expand=_.e, fill=_.fill)

        _.msgLabel = tk.Text(f, height=4, font=_.font, 
                             relief=_.rel, bg='#666', fg='orange')
        _.msgLabel.pack(expand=_.e, fill=_.fill)

        _.getCoor = tk.Button(f, command=_.getAddr, cursor='pirate',
                              text = "Get!", font=_.font, )
        _.getCoor.pack(expand=_.e, fill=_.fill)

        _.myMap = mapy.TkinterMapView(f, width=800, height=600, corner_radius=0)
        _.myMap.pack(expand=_.e, fill=_.fill)

        _.qr_label = tk.Label(f, cursor='cross', )
        _.qr_label.pack(expand=1, fill=_.fill)
        _.getAddr()
    
    def getGps(_, address):
        geolocator = geo.Nominatim(user_agent="uniqueName")
        location = geolocator.geocode(address)
        if location:
            _.latitude = location.latitude
            _.longitude = location.longitude
            return _.latitude, _.longitude
        else:
            return None

    def getAddr(_, event=None):
        _.address = _.gpsEntry.get()
        _.coordinates = _.getGps(_.address)   
        if _.coordinates:
            _.latitude, _.longitude = _.coordinates
            _.msgLabel.insert('1.0', f"#$%&*^ {_.address} :: Latitude: {_.latitude}, Longitude: {_.longitude}\n")
            _.myMap.set_position(_.latitude, _.longitude, marker=True)
            _.myMap.set_zoom(7)
        else:
            _.msgLabel.insert('1.0', "#$%&*^ Location not found.\n")
        _.mkQr()

    def mkQr(_):
        entry = f"{_.coordinates} {_.address}"
        _.qrcode = qr.make_qr(entry)
        _.qrcode.save(_.qr_file, scale=8, border=0, light='#FFF') 
        _.img = tk.PhotoImage(file=_.qr_file)
        _.qr_label.configure(image=_.img)
        _.qr_label.image = _.img
        _.msgLabel.insert('end', f"#$%&*^ {datetime.datetime.now().strftime('%H:%M')} _QR-code-generated_ :: {entry}\n")


if __name__ == "__main__":
    go = Main()
    go.title("Maps App")
    go.mainloop()
