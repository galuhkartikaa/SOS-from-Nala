# backgrounds
image tangga = Image("tangga.png")
image ruangtamu = Image("ruangtamu.png")
image pagar = Image("pagar.png")
image banjir = Image("banjir.png")
image pagarditutup = Image("pagarbanjir.png")
image kamar = Image("background.png")
image kotak = Image("kotak.png")
image buku = Image("bukutabungan.png")
image laptop = Image("laptop.png")
image dokumen = Image("map.png")
image colokan = Image("colokan.png")
image cabutcolokan = Image("colokan2.png")
image colokantutup = Image("colokantutup.png")
image naiktangga = Image("naiktangga.png")
image airmasuk = Image("masuk.png")
image airmasuk2 = Image("masuk2.png")
image kamarnala = Image("kamarnala.png")
image hp = Image("handphone.png")
image nomorpenting = im.Scale("nomor.png",570,900)
image kaget = Image("kakakkaget.png")
image kaki = Image("kaki.png")
image adiklari2 = Image("adiklari2.png")
image kakakadik = Image("kakakadik.png")
image bantuan1 = Image("bantuan1.png")
image bantuan2 = Image("bantuan2.png")

init python:
    res = False

# Minigame
init python:
    
    def piece_dragged(drags, drop):
        
        if not drop:
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][0] = drags[0].x
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][1] = drags[0].y
            return
            
        store.movedpiece = int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1])
        store.movedplace = [int(drop.drag_name[0]), int(drop.drag_name[1])]
        
        return True

screen jigsaw:
    
    draggroup:
        
        drag:
            drag_name "00"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[0]
            
        drag:
            drag_name "01"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[1]
            
        drag:
            drag_name "02"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[2]
            
        drag:
            drag_name "10"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[0]
            
        drag:
            drag_name "11"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[1]
            
        drag:
            drag_name "12"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[2]
            
        drag:
            drag_name "20"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[0]
            
        drag:
            drag_name "21"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[1]
            
        drag:
            drag_name "22"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[2]
            
        drag:
            drag_name "30"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[0]
            
        drag:
            drag_name "31"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[1]
        
        drag:
            drag_name "32"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[2]
            
        drag:
            drag_name "00 piece"
            child im.Crop("ShizukaClassroom_0001.png", 0,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[0][0] ypos piecelist[0][1]
            
        drag:
            drag_name "01 piece"
            child im.Crop("ShizukaClassroom_0001.png", 120,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[1][0] ypos piecelist[1][1]
            
        drag:
            drag_name "02 piece"
            child im.Crop("ShizukaClassroom_0001.png", 240,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[2][0] ypos piecelist[2][1]
            
        drag:
            drag_name "03 piece"
            child im.Crop("ShizukaClassroom_0001.png", 360,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[3][0] ypos piecelist[3][1]
            
        drag:
            drag_name "04 piece"
            child im.Crop("ShizukaClassroom_0001.png", 0,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[4][0] ypos piecelist[4][1]
            
        drag:
            drag_name "05 piece"
            child im.Crop("ShizukaClassroom_0001.png", 120,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[5][0] ypos piecelist[5][1]
            
        drag:
            drag_name "06 piece"
            child im.Crop("ShizukaClassroom_0001.png", 240,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[6][0] ypos piecelist[6][1]
            
        drag:
            drag_name "07 piece"
            child im.Crop("ShizukaClassroom_0001.png", 360,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[7][0] ypos piecelist[7][1]
            
        drag:
            drag_name "08 piece"
            child im.Crop("ShizukaClassroom_0001.png", 0,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[8][0] ypos piecelist[8][1]
            
        drag:
            drag_name "09 piece"
            child im.Crop("ShizukaClassroom_0001.png", 120,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[9][0] ypos piecelist[9][1]
            
        drag:
            drag_name "10 piece"
            child im.Crop("ShizukaClassroom_0001.png", 240,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[10][0] ypos piecelist[10][1]
            
        drag:
            drag_name "11 piece"
            child im.Crop("ShizukaClassroom_0001.png", 360,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[11][0] ypos piecelist[11][1]

# video
image balik = Movie(play="Images/jalan.webm", size=(1950,1110), loop=True, xalign=0.10, yalign=0.10)
image awan = Movie(play="Images/awan.webm", size=(1920,1080), loop=True)
image bantuan = Movie(play="Images/bantuan.webm", size=(1920,1080), loop=True)
image ending1 = Movie(play="Images/ending1.webm", size=(1920,1080), loop=True)
image ending3 = Movie(play="Images/endingsad.webm", size=(1920,1080), loop=True)
image kampung = Movie(play="Images/hujanending.webm", size=(1920,1080), loop=True)
image adiklari = Movie(play="Images/adiklari.webm", size=(1920,1080), loop=True)
image ambulance = Movie(play="Images/ambulance.webm", size=(1920,1080), loop=True)


# character
image adik1 = im.Scale("adiksenyum.png",392,720)
image kakak1 = im.Scale("kakaksenyum1.png",570,900)
image kakak2 = im.Scale("kakaksenyum2.png",570,900)
image kakaktas = im.Scale("kakakpakaitas.png",570,900)
image ibu = im.Scale ("ibu.png",650,1100)
image kakaksip = im.Scale("kakakjempol.png",570,900)
image kakakbingung = im.Scale("kakakbingung.png",570,900)
image kakaknangis = im.Scale("kakaknangis.png",570,900)
image hp = im.Scale("handphone.png",570,900)
image adik2 = im.Scale("adiknangis.png",392,720)

# character objects
define j = Character(_("Jaka"), color="#ffc419")
define n = Character(_("Nala"), color="#afeeee")
define b = Character(_("Ibu"), color="#7dba97")
define t = Character(_("Tetangga 1"), color ='#ffffff')
define e = Character(_("Tetangga 2"), color ='#ffffff')
define h = Character(_("Google"), color ='#ffffff')
define hp = Character(_("Nomor Darurat"), color = '#ffffff')

# The game starts here.

label start:

    play music "memories.mp3"

    show balik

    "Surabaya, 2 Maret 202x"

    "Nala baru saja pulang dari sekolahnya yang tidak jauh dari rumah."

    "Hari itu udara terasa sejuk dan langit mendung berada di mana-mana."

    show tangga

    "Nala berjalan tergesa menuju rumahnya yang berada di bagian bawah kampung."

    show pagar

    "Nala membuka pagar sembari mengucap salam seperti biasanya."

    show ruangtamu
    show kakaktas with dissolve

    n "Assalamualaikum, bu."

    #kakak shadow
    show kakaktas at right with dissolve:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    show ibu at left with dissolve

    b "Waalaikumsalam, Nala."

    #kakak normal
    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    
    #ibu shadow
    show ibu at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Ibu mau kemana?"

    n "Sepertinya Ibu mau ke suatu tempat."

    #kakak shadow
    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    #ibu noromal
    show ibu at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    b "Ibu tadi dihubungi oleh Nenek."

    b "Ada sesuatu yang harus Ibu lakukan di Kampung sebelah."

    b "Tidak akan lama, kok. Tolong jaga Adik dulu, ya."

    menu:
        
        "Maukah Nala menjaga Adik selama Ibu tidak di rumah?"
        "Siap, Ibu.":
            
            jump maumembantu

        "Apa yang harus Nala lakukan, Bu?":

            jump kebingungan

label maumembantu:

    show ibu at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    b "Tolong ya, Kakak Nala."

    b "Terima kasih, anak Ibu."

    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show ibu at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Baik, Bu."

    n "Hati-hati di jalan."

    jump ceritakedua

label kebingungan:

    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show ibu at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Nala harus melakukan apa, Bu?"

    show ibu at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    b "Ajak Adik bermain di ruang tamu, ya."

    b "Nanti tolong perhatikan jika cuaca berubah."

    b "Jika hujan yang turun deras, Kakak tolong kunci pagar dan tempelkan plastisin agar air tidak masuk ke rumah."

    b "Tolong juga cabut peralatan listrik, terutama di lantai satu."

    b "Karena banjir cepat surut, Kakak dan Adik cukup berada di lantai dua saja, ya."

    b "Kalau ada keadaan darurat, tolong hubungi nomor darurat."

    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show ibu at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Baik, Bu."

    n "Hati-hati di jalan."

    hide kakaktas
    hide ibu

label ceritakedua:
    hide kakaktas with fade
    hide ibu with fade
    
    "Nala menaruh tas di kamarnya yang berada di lantai dua."

    "Kemudian dia turun untuk menjaga Adik di ruang tamu."

    show kakak1 with dissolve

    n "Apa yang harus aku lakukan ya?"

    menu:

        "Apa yang harus Nala lakukan pertama kali?"
        "Makan camilan bersama Adik":

            jump makan

        "Bermain bersama Adik":

            jump bermain

label makan:

    hide kakak1 with fade

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik1 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Jaka mau camilan?"

    n "Kakak tadi beli di warung sebelum pulang ke rumah."

    n "Ada cokelat, roti, permen. Jaka mau yang mana, Dik?"

    show adik1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    j "Mau roti yang ini."

    j "Terima kasih, Kakak."

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Kalau Kakak mau makan cokelat."

    n "Makannya pelan-pelan ya, Dik."

    n "Kalau mau minum, ini Kakak bawa air putih."

    hide kakak1
    hide adik1

    stop music fadeout 1.0

    jump mendung

label bermain:

    hide kakak1 with fade

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik1 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Ayo kita bermain."

    n "Jaka mau ngapain?"

    j "Jaka mau menggambar, Kak."

    n "Okeeeeeee."

    scene expression "#fff"
    "Ayo menggambar!"
    $ my_drawing = draw_logic.Draw.main()
    show expression my_drawing
    "Keren, Adik Kakak."

    stop music fadeout 1.0

    hide kakak2
    hide adik1

    jump mendung

label mendung:

    play music "filaments.mp3"

    show awan

    "Ketika asyik mengobrol dengan Adik, Nala mendapati langit di luar kian mendung."
    
    show kampung

    "Dia berjalan ke luar dan mendengarkan tetangga yang sedang bersiap-siap jika terjadi banjir."

    t "Hujannya mulai deras, nih, Bu."

    e "Iya, tadi motor saya sudah dibawa ke Kampung sebelah, takut kena banjir."

    t "Hati-hati ya, Bu. Kadang airnya deras sampai bisa ngebawa barang-barang dari kampung atas."

    show banjir

    "Karena air mulai naik, Nala menutup dan mengunci pagar rumahnya."

    show pagarditutup

    "Ada sebuah teknik yang diajarkan oleh Ibu Nala dan orang-orang Kampung Dukuh Kupang."

    "Ketika menutup pagar, terkadang air masih bisa masuk lewat sela-sela pagar dan tembok."

    "Maka warga menggunakan plastisin yang kedap air untuk bisa menutup sela-sela pagar."

    window hide dissolve

    pause

    window show dissolve

    show kakaksip with dissolve

    n "Sepertinya sudah cukup."
    n "Sekarang waktunya mengambil barang-barang penting dan meletakkan di tempat aman."

    jump find

label find:
    show kamar

    "Mari mencari barang-barang penting di kamar Ibu dan Ayah sesuai yang sudah Ibu ajari dulu."

    "Ada buku tabungan keluarga, laptop, kotak perhiasan, dan surat-surat berharga di dalam map."

    window hide dissolve

    $ InitGame("background.png", 5.0, (1000, 700), "kotak.png", (50, 750), "laptop.png", (700, 80), "map.png", (1500, 900), "bukutabungan.png")

    $ GameAsBG()
    with dissolve

    $ res = StartGame()

    $ GameAsBG()

    if oRes:
        show kakak1

        window show dissolve
        
        n "Yeay, barang-barang berharga sudah masuk ke dalam tas. Aku sudah membawa map berisi surat-surat penting, kotak perhiasan milik Ibu, laptop milik Ayah, dan tabungan keluarga."
        
        n "Semuanya di bawa agar tidak basah jika air masuk ke dalam rumah."
        
        n "Untung saja tidak memakan banyak waktu."

        n "Sekarang, aku harus mencari kertas berisi nomor telepon penting."

        jump puzzle

    else:
        show kakaknangis
        n "Yah, kurang tepat waktu."

        jump find

label minigame:
    call screen jigsaw

    window hide dissolve

    if ([coorlistx[movedplace[0]], coorlisty[movedplace[1]]] in piecelist):
        python:
            t1 = piecelist[movedpiece]
            t2 = piecelist.index([coorlistx[movedplace[0]], coorlisty[movedplace[1]]])
            piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
            piecelist[t2] = t1
    else:
        $ piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
    if piecelist == [[coorlistx[0],coorlisty[0]],
                        [coorlistx[1],coorlisty[0]],
                        [coorlistx[2],coorlisty[0]],
                        [coorlistx[3],coorlisty[0]],
                        [coorlistx[0],coorlisty[1]],
                        [coorlistx[1],coorlisty[1]],
                        [coorlistx[2],coorlisty[1]],
                        [coorlistx[3],coorlisty[1]],
                        [coorlistx[0],coorlisty[2]],
                        [coorlistx[1],coorlisty[2]],
                        [coorlistx[2],coorlisty[2]],
                        [coorlistx[3],coorlisty[2]]]:
        jump win
    jump minigame

label puzzle:
    scene kamar
    image whole = "ShizukaClassroom_0001.png"

    window hide dissolve

    python:
        coorlistx = [10, 130, 250, 370]
        coorlisty = [10, 217, 424]
        piecelist = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        for i in range(12):
            x = renpy.random.randint(0, 59) + 621
            y = renpy.random.randint(0, 480)
            piecelist[i] = [x,y]
        movedpiece = 0
        movedplace = [0, 0]
    jump minigame
   
label win:
    show ruangtamu
    show kakakbingung

    n "Karena semuanya sudah aman, apakah aku perlu mencabut peralatan listrik?"

    hide kakakbingung
    show colokan
    show kakakbingung at right

    menu:

        "Apakah Nala perlu mencabut peralatan listrik di lantai satu?"
        "Iya perlu":
            jump cabut

        "Tidak perlu":
            jump tidakcabut

label cabut:

    hide kakakbingung
    hide ruangtamu

    show cabutcolokan

    show kakak1 at right

    n "Nah, dengan begini akan aman."

    n "Jangan lupa penutupnya juga ditutup agar lebih aman."

    hide kakak1

    show colokantutup

    show kakak2 at right

    n "Sip, lanjut."

    hide kakak2
    hide cabutcolokan
    hide colokan
    hide colokantutup

    show ruangtamu
    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik1 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Ayo, Adik sekarang kita ke lantai dua dan mencari informasi bantuan."

    show adik1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaktas:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    j "Ayo, Kakak."

    hide adik1
    hide kakaktas
    hide ruangtamu

    show naiktangga
    "Nala dan Jaka kemudian berjalan menuju lantai dua rumah mereka."

    window hide dissolve

    pause

    window show dissolve

    "Nala membawa tas yang berisi barang-barang penting, menghindari rusak dan hilang ketika banjir."

    hide naiktangga
    show airmasuk

    "Tanpa mereka berdua sadari, banjir yang terjadi hari itu sangat besar."

    "Kali ini banjir tak seperti yang biasanya terjadi, dan hujan pun seperti badai di luar sana."

    hide airmasuk
    show airmasuk2

    "Walau sudah ditutup dengan rapat, air banjir tetap masuk ke dalam rumah melewati ketinggian pagar."

    hide airmasuk2
    show kamarnala

    "Nala dan Jaka beristirahat di kamar."

    "Nala menaruh tasnya dan mulai menelepon Ibu."

    show kakaknangis at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Ibu maaf Nala baru bisa menelepon. Tadi sinyalnya hilang dan Nala sedang menyiapkan barang mitigasi."

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaknangis at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    b "Nala dan Jaka tidak apa-apa? Ibu dan Nenek sedang menunggu di rumah Nenek."

    b "Tolong jangan kemana-mana ya. Di lantai dua saja sampai banjir surut atau bantuan tiba."

    hide kakaknangis
    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Iya ibu, Nala sudah mengerjakan yang selalu Ibu ajarkan."

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    b "Anak pintar. Hati-hati ya, Nala dan Jaka."

    b "Ibu tutup dulu teleponnya ya, Ibu harus membantu Nenek karena banjir sudah mulai masuk."

    b "Assalamualaikum."

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Iya Ibu, hati-hati jugaaa. Waalaikumsalam."

    hide kakak1
    hide hp

    "Nala teringat dengan kertas berisi nomor-nomor penting yang dia temukan di kamar orang tuanya tadi."

    show nomorpenting

    "Di kertas itu tertulis,"

    "Nomor darurat 112"

    "Nomor ambulance 118"

    "Nomor layanan PLN 123"

    "Nomor layanan SAR 115"

    "dan nomor darurat kepolisian 110"

    window hide dissolve

    pause

    window show dissolve

    hide nomorpenting

    show kakakbingung
    n "Ini sepertinya harus dihapalkan, siapa tau terjadi sesuatu yang diluar keinginan."

    n "Ayo dibaca lagi"

    hide kakakbingung
    show nomorpenting

    "Di kertas itu tertulis,"

    "Nomor darurat 112"

    "Nomor ambulance 118"

    "Nomor layanan PLN 123"

    "Nomor layanan SAR 115"

    "dan nomor darurat kepolisian 110"
    window hide dissolve

    pause

    window show dissolve

    hide nomorpenting

    show kakak1

    n "Nah sekarang ayo kita periksa semuanya."

    hide kakak1

    show kakakbingung

    n "Tadi barang-barang yang harus diselamatkan apa saja ya?"

    jump pertanyaansatu

label pertanyaansatu:

    menu:

        "Tadi barang-barang yang harus diselamatkan apa saja ya?"
        "Surat-surat penting":
            jump pertanyaandua

        "Kipas angin":
            jump kurangbenar

label pertanyaandua:

    menu:

        "Lalu selain surat berharga?"
        "Senter":
            jump ulang

        "Laptop":
            jump pertanyaantiga

label pertanyaantiga:

    menu:
    
        "Sisanya?"
        "Kotak perhiasan Ibu dan buku tabungan":
            jump selanjutnya

        "Kotak perhiasan Ibu dan buku diary":
            jump ulang

label ulang:

    n "Wah sepertinya harus cek lagi."
    jump pertanyaansatu

label selanjutnya:

    hide kakakbingung

    show kakaksip
    window show dissolve
    n "Yak, selanjutnya aku harus menghapal beberapa nomor penting."

    hide kakaksip
    
    show kakakbingung

    menu:
    
        "Nomor 118 adalah nomor?"
        "Tim SAR":
            jump ngulang

        "Ambulance":
            jump next1

        "Kepolisian":
            jump ngulang

label ngulang:

    hide kakakbingung
    show kakaknangis

    n "Masih belum tepat."

    hide kakaknangis

    show nomorpenting

    "Di kertas itu tertulis,"

    "Nomor darurat 112"

    "Nomor ambulance 118"

    "Nomor layanan PLN 123"

    "Nomor layanan SAR 115"

    "dan nomor darurat kepolisian 110"

    window hide dissolve

    pause

    window show dissolve

    hide nomorpenting

    jump selanjutnya

label next1:

    menu:
    
        "Nomor darurat nasional adalah"
        "112":
            jump next2

        "123":
            jump ngulang

        "115":
            jump ngulang

label next2:

    n "Aku jadi ingin tahu nomor darurat itu apa."

    hide kakakbingung

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Apa itu nomor darurat 112?"

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    h "Call Center 112 dilaksanakan secara Desentralisasi oleh Pemerintah Daerah Kabupaten/Kota"
    
    h "(kecuali DKI Jakarta dilakukan oleh Pemerintah Provinsi) dengan mempertimbangkan"

    h "bahwa unit yang terjun ke lapangan untuk memberikan bantuan darurat secara administratif dan kecepatan penanganan"
    
    h "berada didaerah (Organisasi Pemerintah Daerah/OPD)"

    h "seperti Pemadam Kebakaran/BPBD, Dinas Kesehatan/RSUD, Dinas Perhubungan, Satpol PP, dll,"

    h "instansi vertikal seperti Polres, dan instansi/lembaga terkait didaerah."

    h "Kondisi saat ini beberapa nomor darurat seperti Kepolisian = 110, Pemadam Kebakaran = 113, Basarnas = 115, Ambulan/Kemenkes = 119, BNPB = 117 yang diselenggarakan"

    h "oleh Pemerintah Pusat masih bisa digunakan. Dengan hadirnya nomor 112 yang diselenggarakan oleh Pemerintah Daerah, maka masyarakat cukup perlu mengingat 1 (satu) nomor saja,"

    h "yaitu nomor 112 yang mengintegrasikan seluruh nomor darurat untuk mendapatkan pertolongan semua jenis kejadian darurat didaerahnya."

    h " Panggilan masyarakat ke nomor 112 tidak dipungut biaya atau gratis dan masih dapat dipanggil ketika ponsel terkunci."

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Jadi 112 itu untuk semua keadaan darurat dan nomornya di bawah tanggung jawab daerah masing-masing."

    hide kakak1
    show kakak2 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Paham-paham."

    hide kakak2
    hide hp

    "Setelah memastikan semua barang yang diperlukan telah aman, Nala kembali duduk di samping Jaka."

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Loh, Adik kenapa?"

    show adik2:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    j "Jaka takut, Kak."

    j "Nanti kalau enggak bisa keluar gimana?"

    j "Kalau nanti banjir terus gimana?"

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Jaka enggak boleh ngomong gitu."

    hide kakak1

    show kakak2 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Kita pasti akan baik-baik saja, kok."

    n "Jaka, kita main aja yuk?"

    hide kakak2

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Jangan sedih teruuus."

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    j "Jaka mau main gajah saja."

    hide kakak1
    hide adik1

    show bantuan

    "Setelah menunggu beberapa saat, sebuah perahu karet beserta orang-orang profesional tiba di depan rumah Nala."

    window hide dissolve

    pause

    window show dissolve

    show ending1

    "Semua barang-barang penting aman di dalam tas Nala."

    "Alat elektronik di lantai satu aman dari air banjir."

    "Kini keduanya belajar bagaimana cara mitigasi ketika banjir besar terjadi."

    window hide dissolve

    pause

return
    
label tidakcabut:

    hide kakakbingung
    hide colokan

    show ruangtamu

    show kakakbingung

    n "Sepertinya akan aman untuk ke depannya."

    hide kakakbingung

    show ruangtamu
    show kakaktas at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik1 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Ayo, Adik sekarang kita ke lantai dua dan mencari informasi bantuan."

    show adik1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaktas:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    j "Ayo, Kakak."

    hide adik1
    hide kakaktas
    hide ruangtamu

    show naiktangga
    "Nala dan Jaka kemudian berjalan menuju lantai dua rumah mereka."

    window hide dissolve

    pause

    window show dissolve

    "Nala membawa tas yang berisi barang-barang penting, menghindari rusak dan hilang ketika banjir."

    hide naiktangga
    show airmasuk

    "Tanpa mereka berdua sadari, banjir yang terjadi hari itu sangat besar."

    "Kali ini banjir tak seperti yang biasanya terjadi, dan hujan pun seperti badai di luar sana."

    hide airmasuk
    show airmasuk2

    "Walau sudah ditutup dengan rapat, air banjir tetap masuk ke dalam rumah melewati ketinggian pagar."

    hide airmasuk2
    show kamarnala

    "Nala dan Jaka beristirahat di kamar."

    "Nala menaruh tasnya dan mulai menelepon Ibu."

    show kakaknangis at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Ibu maaf Nala baru bisa menelepon. Tadi sinyalnya hilang dan Nala sedang menyiapkan barang mitigasi."

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaknangis at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    b "Nala dan Jaka tidak apa-apa? Ibu dan Nenek sedang menunggu di rumah Nenek."

    b "Tolong jangan kemana-mana ya. Di lantai dua saja sampai banjir surut atau bantuan tiba."

    hide kakaknangis
    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Iya ibu, Nala sudah mengerjakan yang selalu Ibu ajarkan."

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    b "Anak pintar. Hati-hati ya, Nala dan Jaka."

    b "Ibu tutup dulu teleponnya ya, Ibu harus membantu Nenek karena banjir sudah mulai masuk."

    b "Assalamualaikum."

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Iya Ibu, hati-hati jugaaa. Waalaikumsalam."

    hide kakak1
    hide hp

    "Nala teringat dengan kertas berisi nomor-nomor penting yang dia temukan di kamar orang tuanya tadi."

    show nomorpenting

    "Di kertas itu tertulis,"

    "Nomor darurat 112"

    "Nomor ambulance 118"

    "Nomor layanan PLN 123"

    "Nomor layanan SAR 115"

    "dan nomor darurat kepolisian 110"

    window hide dissolve

    pause

    window show dissolve

    hide nomorpenting

    show kakakbingung

    n "Ini sepertinya harus dihapalkan, siapa tau terjadi sesuatu yang diluar keinginan."

    n "Ayo dibaca lagi"

    hide kakakbingung
    show nomorpenting

    "Di kertas itu tertulis,"

    "Nomor darurat 112"

    "Nomor ambulance 118"

    "Nomor layanan PLN 123"

    "Nomor layanan SAR 115"

    "dan nomor darurat kepolisian 110"

    window hide dissolve

    pause
    window show dissolve
    hide nomorpenting
    
    show kakak1

    n "Nah sekarang ayo kita periksa semuanya."

    hide kakak1

    show kakakbingung

    n "Tadi barang-barang yang harus diselamatkan apa saja ya?"

    jump pertanyaan1

label pertanyaan1:

    menu:

        "Tadi barang-barang yang harus diselamatkan apa saja ya?"
        "Surat-surat penting":
            jump pertanyaan2

        "Kipas angin":
            jump kurangbenar

label pertanyaan2:

    menu:

        "Lalu selain surat berharga?"
        "Senter":
            jump kurangbenar

        "Laptop":
            jump pertanyaan3

label pertanyaan3:

    menu:
    
        "Sisanya?"
        "Kotak perhiasan Ibu dan buku tabungan":
            jump benar

        "Kotak perhiasan Ibu dan buku diary":
            jump kurangbenar

label kurangbenar:

    n "Wah sepertinya harus cek lagi."
    jump pertanyaan1

label benar:

    n "Yak, selanjutnya aku harus menghapal beberapa nomor penting."

    hide kakaksip
    
    show kakakbingung

    menu:
    
        "Nomor 118 adalah nomor?"
        "Tim SAR":
            jump mengulang

        "Ambulance":
            jump lanjut1

        "Kepolisian":
            jump mengulang

label mengulang:

    hide kakakbingung
    show kakaknangis

    n "Masih belum tepat."

    hide kakaknangis

    show nomorpenting

    "Di kertas itu tertulis,"

    "Nomor darurat 112"

    "Nomor ambulance 118"

    "Nomor layanan PLN 123"

    "Nomor layanan SAR 115"

    "dan nomor darurat kepolisian 110"
    
    pause

    window show dissolve

    hide nomorpenting

    jump benar

label lanjut1:

    menu:
    
        "Nomor darurat nasional adalah"
        "112":
            jump lanjut2

        "123":
            jump mengulang

        "115":
            jump mengulang

label lanjut2:

    n "Aku jadi ingin tahu nomor darurat itu apa."

    hide kakakbingung

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Apa itu nomor darurat 112?"

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    h "Call Center 112 dilaksanakan secara Desentralisasi oleh Pemerintah Daerah Kabupaten/Kota"
    
    h "(kecuali DKI Jakarta dilakukan oleh Pemerintah Provinsi) dengan mempertimbangkan"

    h "bahwa unit yang terjun ke lapangan untuk memberikan bantuan darurat secara administratif dan kecepatan penanganan"
    
    h "berada didaerah (Organisasi Pemerintah Daerah/OPD)"

    h "seperti Pemadam Kebakaran/BPBD, Dinas Kesehatan/RSUD, Dinas Perhubungan, Satpol PP, dll,"

    h "instansi vertikal seperti Polres, dan instansi/lembaga terkait didaerah."

    h "Kondisi saat ini beberapa nomor darurat seperti Kepolisian = 110, Pemadam Kebakaran = 113, Basarnas = 115, Ambulan/Kemenkes = 119, BNPB = 117 yang diselenggarakan"

    h "oleh Pemerintah Pusat masih bisa digunakan. Dengan hadirnya nomor 112 yang diselenggarakan oleh Pemerintah Daerah, maka masyarakat cukup perlu mengingat 1 (satu) nomor saja,"

    h "yaitu nomor 112 yang mengintegrasikan seluruh nomor darurat untuk mendapatkan pertolongan semua jenis kejadian darurat didaerahnya."

    h " Panggilan masyarakat ke nomor 112 tidak dipungut biaya atau gratis dan masih dapat dipanggil ketika ponsel terkunci."

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Jadi 112 itu untuk semua keadaan darurat dan nomornya di bawah tanggung jawab daerah masing-masing."

    hide kakak1
    show kakak2 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Paham-paham."

    hide kakak2
    hide hp

    "Setelah memastikan semua barang yang diperlukan telah aman, Nala kembali duduk di samping Jaka."

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Loh, Adik kenapa?"

    show adik2:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    j "Jaka takut, Kak."

    j "Nanti kalau enggak bisa keluar gimana?"

    j "Kalau nanti banjir terus gimana?"

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Jaka enggak boleh ngomong gitu."

    hide kakak1

    show kakak2 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Kita pasti akan baik-baik saja, kok."

    n "Jaka, kita main aja yuk?"

    hide kakak2

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik2 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Jangan sedih teruuus."

    hide adik2

    show adik1 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    j "Jaka mau main petak umpet!"

    show kakak1 at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show adik1 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Okey! Kakak yang jaga ya."

    n "Jaka tolong jangan jauh-jauh ya, bahayaaa."

    hide adik2

    show adik1 at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakak1:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    j "SIAPPPPP"

    hide kakak1
    hide adik1

    "Nala kemudian menghitung sembari menutup matanya."

    show kakak2

    n "Satu, dua, tiga..."

    n "Empat, lima, enam..."

    n "Tujuh, delapan, sembilan..."

    hide kakak2
    show kakak1

    n "SEPULUH!"

    hide kakak1

    show adiklari

    "Dengan tergesa Jaka berlari keluar kamar."

    window hide dissolve

    pause

    window show dissolve

    "Nala sangat terkejut dan dia mengejar Jaka yang kini sedang menuruni tangga."

    show adiklari2

    "Jaka berlari dengan cepat hingga Nala kewalahan."

    "Dia tidak peduli dengan teriakan Nala dan terus berlari hingga lantai satu."

    show kaki

    "Karena tidak memperhatikan sekitar, Jaka jadi tidak melihat genangan air sudah mulai masuk ke ruang tamu bagian depan."

    show kaget

    "Sebuah kilatan terlihat oleh Nala."

    "Itu berasal dari lantai 1 dan Jaka sudah terkapar ketika mata Nala kembali normal."

    show kakakadik

    "Karena melihat Jaka tersetrum, dengan segera Nala mengambil tongkat pramuka miliknya dan menggeser badan Jaka agar tidak mengenai konduktor listrik seperti air."

    "Sembari menangis Nala memanggil-manggil nama Jaka."

    "Jaka kehilangan kesadaran dan ini saatnya untuk menelepon bantuan darurat."

    show ruangtamu

    show kakaknangis at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    menu:
    
        "Nomor mana yang harus Nala telepon?"
        "115":
            jump ending3

        "112":
            jump ceritaketiga

        "110":
            jump ending3

        "118":
            jump ceritaketiga

label ending3:

    show kakaknangis at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Halo."

    n "Tolong, disini ada yang tersetrum."

    show hp:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaknangis:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    hp "Maaf, untuk kejadian darurat bencana sebagiknya menghubungi nomor darurat daerah atau ambulance."

    "Nala salah menuliskan nomor telepon."

    "Nala melihat ke arah Jaka yang mulai kejang-kejang lagi."

    "Dia kemudian menelepon orang tuanya."

    show kakaknangis:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Ibu, Adik tadi tersetrum dan sekarang masih pingsan."

    show hp:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaknangis:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    b "Astagfirullah."

    b "Ibu akan menelepon ambulance. Tolong terus jaga adik, ya."

    show kakaknangis:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Iya Ibu."

    hide hp
    hide kakaknangis

    show kakaknangis

    "Bantuan tiba tak lama setelah Ibu menelepon ambulance."

    hide kakaknangis

    show bantuan

    "Sebuah perahu karet beserta orang-orang profesional tiba di depan rumah Nala."

    window hide dissolve

    pause

    window show dissolve

    show ambulance

    "Mereka memindahkan Jaka ke dalam ambulance dan membawa keduanya menuju rumah sakit terdekat."

    window hide dissolve

    pause

    window show dissolve

    "Nala juga membawa tas yang berisi barang-barang berharga."

    "Dia terus menerus menangis sepanjang perjalanan."

    show ending3

    "Tapi setibanya di rumah sakit Jaka harus pergi dari Nala dan kedua orangtuanya."

    "Nala dan kedua orangtuanya sangat menyayangi Jaka, namun Tuhan lebih sayang kepadanya."

    window hide dissolve

    pause

return



label ceritaketiga:

    show kakaknangis at right:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show hp at left:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    n "Halo."

    n "Tolong, disini ada yang tersetrum."

    show hp:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
        linear 2.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    show kakaknangis:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 2.0 matrixcolor TintMatrix("#ccccff") * SaturationMatrix(0.0)

    hp "Selamat siang. Boleh disebutkan alamatnya?"

    show kakaknangis at right
    show hp at left

    "Nala menjelaskan keadaan sekitar dan alamat rumah dengan tangis yang tidak kunjung reda."

    "Nomor darurat tersebut menjelaskan akan mengirim bantuan dalam waktu yang tidak lama."

    hide hp
    hide kakaknangis

    show kakaknangis

    "Nala harus terus memperhatikan keadaan Jaka."

    hide kakaknangis

    show bantuan2

    "Setelah menunggu beberapa saat, sebuah perahu karet beserta orang-orang profesional tiba di depan rumah Nala."

    window hide dissolve

    pause

    window show dissolve

    show ambulance

    "Mereka memindahkan Jaka ke dalam ambulance dan membawa keduanya menuju rumah sakit terdekat."

    window hide dissolve

    pause

    window show dissolve

    show ending1

    "Setelah dirawat, tubuh Jaka kembali sehat seperti sebelumnya."

    "Semua barang-barang penting aman di dalam tas Nala."

    "Hanya beberapa alat elektronik yang rusak terkena air banjir."

    "Kini keduanya belajar bagaimana cara mitigasi ketika banjir besar terjadi."

    window hide dissolve

    pause

return
