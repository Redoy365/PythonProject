import qrcode as qr

img = qr.make("https://www.youtube.com/@alorpothmultimedia/playlists")
img.save("alorpoth.png")

