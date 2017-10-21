## http://www.bts.co.th/customer/th/02-route-current_new.aspx ##

# cost = 2, train_type = mrt_blue_line
mrt_blue_line = "hua_lamphong,sam_yan,si_lom,lumphini,khlong_toei,queen_sirikit_national_convention_center,sukhumvit,phetchaburi,phra_ram_9,thailand_cultural_center,huai_khwang,sutthisan,ratchadaphisek,lat_phrao,phahon_yothin,chatuchak_park,kamphaeng_phet,bang_sue,tao_poon"
mrt_blue_line_cost = 2

# cost = 1, train_type = mrt_purple_line
mrt_purple_line = "khlong_bang_phai,talad_bang_yai,sam_yaek,bang_yai,bang_phlu,bang_rak_yai,bang_rak_noi_tha_it,sai_ma,phra_nang_klao_bridge,yaek_nonthaburi1,bang_krasor,nonthaburi_civic_center,ministry_of_public_health,yaek_tiwanon,wong_sawang,bang_son,tao_poon_purple"
mrt_purple_line_cost = 1

# cost = 4, train_type = bts_sukhumvit_line
bts_sukhumvit_line = "mo_chit,saphan_kwai,ari,sanam_pao,victory_monument,phaya_thai,ratchathewi,siam,chit_lom,ploen_chit,nana,asok,phrom_phong,thong_lo,ekkamai,phra_khanong,on_nut,bang_chak,punnawithi,udom_suk,bang_na,bearing,samrong"
bts_sukhumvit_line_cost = 4

# cost = 3, train_type = bts_silom_line
bts_silom_line = "national_stadium,siam_silom_line,ratchadamri,sala_daeng,chong_nonsi,surasak,saphan_taksin,krung_thon_buri,wongwian_yai,pho_nimit,talat_phlu,wutthakat,bang_wa"
bts_silom_line_cost = 3

# cost = 5, train_type = airlink
air_link_line = "phaya_thai_airlink,ratchaprarop,makkasan,ramkhamhaeng,hua_mak,ban_thap_chang,latkrabang,suvarnabhumi"
air_link_line_cost = 5


def getDist(station_list, cost):
    for i in range (len(station_list)-1):
        print "dist("+station_list[i]+","+station_list[i+1]+","+cost+")."
       


def getTrain(station_list,train_type):
    for i in range(len(station_list)):
        print "train("+station_list[i]+","+train_type+")."



#station_list = mrt_blue_line.split(",")
#station_list = mrt_purple_line.split(",")
#station_list = bts_sukhumvit_line.split(",")
#station_list = bts_silom_line.split(",")
station_list = air_link_line.split(",")

#getDist(station_list)

train_type = "airlink"
getTrain(station_list, train_type)
