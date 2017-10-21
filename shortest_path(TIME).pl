dijkstra(Vertex, Ss):-
  create(Vertex, [Vertex], Ds),
  dijkstra_1(Ds, [s(Vertex,0,[])], Ss).

dijkstra_1([], Ss, Ss).
dijkstra_1([D|Ds], Ss0, Ss):-
  best(Ds, D, S),
  delete([D|Ds], [S], Ds1),
  S=s(Vertex,Distance,Path),
  reverse([Vertex|Path], Path1),
  merge(Ss0, [s(Vertex,Distance,Path1)], Ss1),
  create(Vertex, [Vertex|Path], Ds2),
  delete(Ds2, Ss1, Ds3),
  incr(Ds3, Distance, Ds4),
  merge(Ds1, Ds4, Ds5),
  dijkstra_1(Ds5, Ss1, Ss).


path(Vertex0, Vertex, Path, Dist):-
  dijkstra(Vertex0, Ss),
  member(s(Vertex,Dist,Path), Ss), !.
  

create(Start, Path, Edges):-
  setof(s(Vertex,Edge,Path), e(Start,Vertex,Edge), Edges), !.
create(_, _, []).
  

best([], Best, Best).
best([Edge|Edges], Best0, Best):-
  shorter(Edge, Best0), !,
  best(Edges, Edge, Best).
best([_|Edges], Best0, Best):-
  best(Edges, Best0, Best).

shorter(s(_,X,_), s(_,Y,_)):-X < Y.


delete([], _, []). 
delete([X|Xs], [], [X|Xs]):-!. 
delete([X|Xs], [Y|Ys], Ds):-
  eq(X, Y), !, 
  delete(Xs, Ys, Ds). 
delete([X|Xs], [Y|Ys], [X|Ds]):-
  lt(X, Y), !, delete(Xs, [Y|Ys], Ds). 
delete([X|Xs], [_|Ys], Ds):-
  delete([X|Xs], Ys, Ds). 
  

merge([], Ys, Ys). 
merge([X|Xs], [], [X|Xs]):-!. 
merge([X|Xs], [Y|Ys], [X|Zs]):-
  eq(X, Y), shorter(X, Y), !, 
  merge(Xs, Ys, Zs).
merge([X|Xs], [Y|Ys], [Y|Zs]):-
  eq(X, Y), !, 
  merge(Xs, Ys, Zs).
merge([X|Xs], [Y|Ys], [X|Zs]):-
  lt(X, Y), !, 
  merge(Xs, [Y|Ys], Zs).
merge([X|Xs], [Y|Ys], [Y|Zs]):-
  merge([X|Xs], Ys, Zs).

eq(s(X,_,_), s(X,_,_)).  

lt(s(X,_,_), s(Y,_,_)):-X @< Y.


incr([], _, []).  
incr([s(V,D1,P)|Xs], Incr, [s(V,D2,P)|Ys]):-
  D2 is D1 + Incr,
  incr(Xs, Incr, Ys).



e(X, Y, Z):-dist(X, Y, Z).
e(X, Y, Z):-dist(Y, X, Z).





% Train Junction
dist(phaya_thai, phaya_thai_airlink, 7).
dist(sukhumvit, asok, 3).
dist(si_lom,sala_daeng, 5).
dist(phetchaburi, makkasan, 5).
dist(tao_poon,tao_poon_purple,2).
dist(mo_chit,chatuchak_park,5).
dist(siam,siam_silom_line,5).

% Airport Link
dist(phaya_thai_airlink,ratchaprarop,5).
dist(ratchaprarop,makkasan,5).
dist(makkasan,ramkhamhaeng,5).
dist(ramkhamhaeng,hua_mak,5).
dist(hua_mak,ban_thap_chang,5).
dist(ban_thap_chang,latkrabang,5).
dist(latkrabang,suvarnabhumi,5).


% MRT - Blue Line
dist(hua_lamphong,sam_yan,2).
dist(sam_yan,si_lom, 2).
dist(si_lom, lumphini,2).
dist(lumphini,khlong_toei,2).
dist(khlong_toei,queen_sirikit_national_convention_center,2).
dist(queen_sirikit_national_convention_center,sukhumvit,2).
dist(sukhumvit,phetchaburi,2).
dist(phetchaburi,phra_ram_9,2).
dist(phra_ram_9,thailand_cultural_center,2).
dist(thailand_cultural_center,huai_khwang,2).
dist(huai_khwang,sutthisan,2).
dist(sutthisan,ratchadaphisek,2).
dist(ratchadaphisek,lat_phrao,2).
dist(lat_phrao,phahon_yothin,2).
dist(phahon_yothin,chatuchak_park,2).
dist(chatuchak_park,kamphaeng_phet,2).
dist(kamphaeng_phet,bang_sue,2).
dist(bang_sue,tao_poon,2).

% MRT - Purple Line
dist(khlong_bang_phai,talad_bang_yai,1).
dist(talad_bang_yai,sam_yaek,1).
dist(sam_yaek,bang_yai,1).
dist(bang_yai,bang_phlu,1).
dist(bang_phlu,bang_rak_yai,1).
dist(bang_rak_yai,bang_rak_noi_tha_it,1).
dist(bang_rak_noi_tha_it,sai_ma,1).
dist(sai_ma,phra_nang_klao_bridge,1).
dist(phra_nang_klao_bridge,yaek_nonthaburi1,1).
dist(yaek_nonthaburi1,bang_krasor,1).
dist(bang_krasor,nonthaburi_civic_center,1).
dist(nonthaburi_civic_center,ministry_of_public_health,1).
dist(ministry_of_public_health,yaek_tiwanon,1).
dist(yaek_tiwanon,wong_sawang,1).
dist(wong_sawang,bang_son,1).
dist(bang_son,tao_poon_purple,1).

%BTS - Silom Line
dist(national_stadium,siam_silom_line,3).
dist(siam_silom_line,ratchadamri,3).
dist(ratchadamri,sala_daeng,3).
dist(sala_daeng,chong_nonsi,3).
dist(chong_nonsi,surasak,3).
dist(surasak,saphan_taksin,3).
dist(saphan_taksin,krung_thon_buri,3).
dist(krung_thon_buri,wongwian_yai,3).
dist(wongwian_yai,pho_nimit,3).
dist(pho_nimit,talat_phlu,3).
dist(talat_phlu,wutthakat,3).
dist(wutthakat,bang_wa,3).

%BTS - Sukhumvit Line
dist(mo_chit,saphan_kwai,4).
dist(saphan_kwai,ari,4).
dist(ari,sanam_pao,4).
dist(sanam_pao,victory_monument,4).
dist(victory_monument,phaya_thai,4).
dist(phaya_thai,ratchathewi,4).
dist(ratchathewi,siam,4).
dist(siam,chit_lom,4).
dist(chit_lom,ploen_chit,4).
dist(ploen_chit,nana,4).
dist(nana,asok,4).
dist(asok,phrom_phong,4).
dist(phrom_phong,thong_lo,4).
dist(thong_lo,ekkamai,4).
dist(ekkamai,phra_khanong,4).
dist(phra_khanong,on_nut,4).
dist(on_nut,bang_chak,4).
dist(bang_chak,punnawithi,4).
dist(punnawithi,udom_suk,4).
dist(udom_suk,bang_na,4).
dist(bang_na,bearing,4).
dist(bearing,samrong,4).
