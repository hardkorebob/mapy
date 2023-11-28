#!/usr/bin/env python3
import tkinter as tk
import segno as qr
import geopy as geo
import tkinter.font as font
import tkintermapview as mapy

class Main(tk.Tk):
    def __init__(_):
        super().__init__()
        maps = Maps(_)
        maps.pack(expand=1, fill='both')

class Maps(tk.Frame): 

    def __init__(_, ap, ):
        super().__init__(ap)
        _.fill = 'both'
        _.rel = 'flat'
        _.e = 0
        _.font = font.nametofont("TkFixedFont")
        _.font.configure(size=14)

        f = tk.Frame(_, )
        f.pack(expand=1, fill=_.fill)

        _.infoLabel = tk.Label(f, text = "Enter address: ", font=_.font, )
        _.infoLabel.pack(expand=_.e, fill=_.fill)

        _.gpsEntry = tk.Entry(f, cursor="dotbox", relief=_.rel, font=_.font, 
                              bg="#444", fg='green', )
        _.gpsEntry.insert(0, "Fredericksburg, VA")
        _.gpsEntry.pack(expand=_.e, fill=_.fill)

        _.msgLabel = tk.Text(f, height=1, font=_.font, takefocus=False, 
                             relief=_.rel, bg="#666", fg='orange')
        _.msgLabel.pack(expand=_.e, fill=_.fill)

        _.getCoor = tk.Button(f, command=_.getAddr, 
                              text = "Get!", font=_.font, )
        _.getCoor.pack(expand=_.e, fill=_.fill)

        _.myMap = mapy.TkinterMapView(f, width=800, height=800, corner_radius=0)
        _.myMap.pack(expand=_.e, fill=_.fill)
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
        address = _.gpsEntry.get()
        coordinates = _.getGps(address)   
        if coordinates:
            _.latitude, _.longitude = coordinates
            _.msgLabel.insert('1.0', f"#$%&*^ Latitude: {_.latitude}, Longitude: {_.longitude} {address}\n")
            _.myMap.set_position(_.latitude, _.longitude, marker=True)
            _.myMap.set_zoom(7)
        else:
            _.msgLabel.insert('1.0', "#$%&*^ Location not found.\n")

if __name__ == "__main__":
    go = Main()
    go.title("Maps App")
    go.mainloop()

#$%&*^ 11:50 cat map.py
