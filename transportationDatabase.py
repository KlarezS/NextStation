# Transportation Database

## http://www.bts.co.th/customer/th/02-route-current_new.aspx ##

# cost = 2, train_type = mrt_blue_line
mrt_blue_line = "hua_lamphong,sam_yan,si_lom,lumphini,klong_toei,queen_sirkit_national_covention_center,sukhumvit,phetchaburi,phra_ram_9,thailand_cultural_center,huai_kwang,sutthisan,ratchadaphisek,lat_phrao,phahon_yothin,chatuchak_park,kamphaen_phet,bang_sue,tao_poon"

# cost = 1, train_type = mrt_purple_line
mrt_purple_line = "khlong_bang_phai,talad_bang_yai,sam_yaek,bang_yai,bang_phlu,bang_rak_yai,bang_rak_noi_tha_it,sai_ma,phra_nang_klao_bridge,yaek_nonthaburi1,bang_krasor,nonthaburi_civic_center,ministry_of_public_health,yaek_tiwanon,wong_sawang,bang_son,tao_poon_purple"

# cost = 4, train_type = bts_sukhumvit_line
bts_sukhumvit_line = "mo_chit,saphan_kwai,ari,sanam_pao,victory_monument,phaya_thai,ratchathewi,siam,chit_lom,ploen_chit,nana,asok,phrom_phong,thong_lo,ekkamai,phra_khanong,on_nut,bang_chak,punnawithi,udom_suk,bang_na,bearing,samrong"

# cost = 3, train_type = bts_silom_line
bts_silom_line = "national_stadium,siam_silom_line,ratchadamri,sala_daeng,chong_nonsi,surasak,saphan_taksin,krung_thon_buri,wongwian_yai,pho_nimit,talat_phlu,wutthakat,bang_wa"

# cost = 5, train_type = airlink
air_link_line = "phaya_thai_airlink,ratchaprarop,makkasan,ramkhamhaeng,hua_mak,ban_thap_chang,latkrabang,suvarnabhumi"


station_list = bts_silom_line.split(",")

for i in range(len(station_list)):
    print(station_list[i]+ " = [\"1.N/A\",\"2.N/A\",\"3.N/A\",\"4.N/A\"]")


# Airlink Station
phaya_thai_airlink = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ratchaprarop = ["1.N/A","2.N/A","3.N/A","4.N/A"]
makkasan = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ramkhamhaeng = ["1.N/A","2.N/A","3.N/A","4.N/A"]
hua_mak = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ban_thap_chang = ["1.N/A","2.N/A","3.N/A","4.N/A"]
latkrabang = ["1.N/A","2.N/A","3.N/A","4.N/A"]
suvarnabhumi = ["1.N/A","2.N/A","3.N/A","4.N/A"]

# MRT - Blue Line
hua_lamphong = ["1.N/A","2.N/A","3.N/A","4.N/A"]
sam_yan = ["1.N/A","2.N/A","3.N/A","4.N/A"]
si_lom = ["1.N/A","2.N/A","3.N/A","4.N/A"]
lumphini = ["1.N/A","2.N/A","3.N/A","4.N/A"]
klong_toei = ["1.N/A","2.N/A","3.N/A","4.N/A"]
queen_sirkit_national_covention_center = ["1.N/A","2.N/A","3.N/A","4.N/A"]
sukhumvit = ["1.N/A","2.N/A","3.N/A","4.N/A"]
phetchaburi = ["1.N/A","2.N/A","3.N/A","4.N/A"]
phra_ram_9 = ["1.N/A","2.N/A","3.N/A","4.N/A"]
thailand_cultural_center = ["1.N/A","2.N/A","3.N/A","4.N/A"]
huai_kwang = ["1.N/A","2.N/A","3.N/A","4.N/A"]
sutthisan = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ratchadaphisek = ["1.N/A","2.N/A","3.N/A","4.N/A"]
lat_phrao = ["1.N/A","2.N/A","3.N/A","4.N/A"]
phahon_yothin = ["1.N/A","2.N/A","3.N/A","4.N/A"]
chatuchak_park = ["1.N/A","2.N/A","3.N/A","4.N/A"]
kamphaen_phet = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_sue = ["1.N/A","2.N/A","3.N/A","4.N/A"]
tao_poon = ["1.N/A","2.N/A","3.N/A","4.N/A"]

# MRT - Purple Line
khlong_bang_phai = ["1.N/A","2.N/A","3.N/A","4.N/A"]
talad_bang_yai = ["1.N/A","2.N/A","3.N/A","4.N/A"]
sam_yaek = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_yai = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_phlu = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_rak_yai = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_rak_noi_tha_it = ["1.N/A","2.N/A","3.N/A","4.N/A"]
sai_ma = ["1.N/A","2.N/A","3.N/A","4.N/A"]
phra_nang_klao_bridge = ["1.N/A","2.N/A","3.N/A","4.N/A"]
yaek_nonthaburi1 = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_krasor = ["1.N/A","2.N/A","3.N/A","4.N/A"]
nonthaburi_civic_center = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ministry_of_public_health = ["1.N/A","2.N/A","3.N/A","4.N/A"]
yaek_tiwanon = ["1.N/A","2.N/A","3.N/A","4.N/A"]
wong_sawang = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_son = ["1.N/A","2.N/A","3.N/A","4.N/A"]
tao_poon_purple = ["1.N/A","2.N/A","3.N/A","4.N/A"]

# BTS - Sukhumvit Line
mo_chit = ["1.N/A","2.N/A","3.N/A","4.N/A"]
saphan_kwai = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ari = ["1.N/A","2.N/A","3.N/A","4.N/A"]
sanam_pao = ["1.N/A","2.N/A","3.N/A","4.N/A"]
victory_monument = ["1.N/A","2.N/A","3.N/A","4.N/A"]
phaya_thai = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ratchathewi = ["1.N/A","2.N/A","3.N/A","4.N/A"]
siam = ["1.N/A","2.N/A","3.N/A","4.N/A"]
chit_lom = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ploen_chit = ["1.N/A","2.N/A","3.N/A","4.N/A"]
nana = ["1.N/A","2.N/A","3.N/A","4.N/A"]
asok = ["1.N/A","2.N/A","3.N/A","4.N/A"]
phrom_phong = ["1.N/A","2.N/A","3.N/A","4.N/A"]
thong_lo = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ekkamai = ["1.N/A","2.N/A","3.N/A","4.N/A"]
phra_khanong = ["1.N/A","2.N/A","3.N/A","4.N/A"]
on_nut = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_chak = ["1.N/A","2.N/A","3.N/A","4.N/A"]
punnawithi = ["1.N/A","2.N/A","3.N/A","4.N/A"]
udom_suk = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_na = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bearing = ["1.N/A","2.N/A","3.N/A","4.N/A"]
samrong = ["1.N/A","2.N/A","3.N/A","4.N/A"]

# BTS - Silom Line
national_stadium = ["1.N/A","2.N/A","3.N/A","4.N/A"]
siam_silom_line = ["1.N/A","2.N/A","3.N/A","4.N/A"]
ratchadamri = ["1.N/A","2.N/A","3.N/A","4.N/A"]
sala_daeng = ["1.N/A","2.N/A","3.N/A","4.N/A"]
chong_nonsi = ["1.N/A","2.N/A","3.N/A","4.N/A"]
surasak = ["1.N/A","2.N/A","3.N/A","4.N/A"]
saphan_taksin = ["1.N/A","2.N/A","3.N/A","4.N/A"]
krung_thon_buri = ["1.N/A","2.N/A","3.N/A","4.N/A"]
wongwian_yai = ["1.N/A","2.N/A","3.N/A","4.N/A"]
pho_nimit = ["1.N/A","2.N/A","3.N/A","4.N/A"]
talat_phlu = ["1.N/A","2.N/A","3.N/A","4.N/A"]
wutthakat = ["1.N/A","2.N/A","3.N/A","4.N/A"]
bang_wa = ["1.N/A","2.N/A","3.N/A","4.N/A"]
