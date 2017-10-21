% MRT - Blue Line
%--------------------------------------------------------------
train(hua_lamphong,mrt_blue_line).
train(sam_yan,mrt_blue_line).
train(si_lom,mrt_blue_line).
train(lumphini,mrt_blue_line).
train(klong_toei,mrt_blue_line).
train(queen_sirkit_national_covention_center,mrt_blue_line).
train(sukhumvit,mrt_blue_line).
train(phetchaburi,mrt_blue_line).
train(phra_ram_9,mrt_blue_line).
train(thailand_cultural_center,mrt_blue_line).
train(huai_kwang,mrt_blue_line).
train(sutthisan,mrt_blue_line).
train(ratchadaphisek,mrt_blue_line).
train(lat_phrao,mrt_blue_line).
train(phahon_yothin,mrt_blue_line).
train(chatuchak_park,mrt_blue_line).
train(kamphaen_phet,mrt_blue_line).
train(bang_sue,mrt_blue_line).
train(tao_poon,mrt_blue_line).

% MRT - Purple Line
%--------------------------------------------------------------
train(khlong_bang_phai,mrt_purple_line).
train(talad_bang_yai,mrt_purple_line).
train(sam_yaek,mrt_purple_line).
train(bang_yai,mrt_purple_line).
train(bang_phlu,mrt_purple_line).
train(bang_rak_yai,mrt_purple_line).
train(bang_rak_noi_tha_it,mrt_purple_line).
train(sai_ma,mrt_purple_line).
train(phra_nang_klao_bridge,mrt_purple_line).
train(yaek_nonthaburi1,mrt_purple_line).
train(bang_krasor,mrt_purple_line).
train(nonthaburi_civic_center,mrt_purple_line).
train(ministry_of_public_health,mrt_purple_line).
train(yaek_tiwanon,mrt_purple_line).
train(wong_sawang,mrt_purple_line).
train(bang_son,mrt_purple_line).
train(tao_poon_purple,mrt_purple_line).

% BTS - Sukhumvit Line
%--------------------------------------------------------------
train(mo_chit,bts_sukhumvit_line).
train(saphan_kwai,bts_sukhumvit_line).
train(ari,bts_sukhumvit_line).
train(sanam_pao,bts_sukhumvit_line).
train(victory_monument,bts_sukhumvit_line).
train(phaya_thai,bts_sukhumvit_line).
train(ratchathewi,bts_sukhumvit_line).
train(siam,bts_sukhumvit_line).
train(chit_lom,bts_sukhumvit_line).
train(ploen_chit,bts_sukhumvit_line).
train(nana,bts_sukhumvit_line).
train(asok,bts_sukhumvit_line).
train(phrom_phong,bts_sukhumvit_line).
train(thong_lo,bts_sukhumvit_line).
train(ekkamai,bts_sukhumvit_line).
train(phra_khanong,bts_sukhumvit_line).
train(on_nut,bts_sukhumvit_line).
train(bang_chak,bts_sukhumvit_line).
train(punnawithi,bts_sukhumvit_line).
train(udom_suk,bts_sukhumvit_line).
train(bang_na,bts_sukhumvit_line).
train(bearing,bts_sukhumvit_line).
train(samrong,bts_sukhumvit_line).

% BTS - Silom Line
%--------------------------------------------------------------
train(national_stadium,bts_silom_line).
train(siam_silom_line,bts_silom_line).
train(ratchadamri,bts_silom_line).
train(sala_daeng,bts_silom_line).
train(chong_nonsi,bts_silom_line).
train(surasak,bts_silom_line).
train(saphan_taksin,bts_silom_line).
train(krung_thon_buri,bts_silom_line).
train(wongwian_yai,bts_silom_line).
train(pho_nimit,bts_silom_line).
train(talat_phlu,bts_silom_line).
train(wutthakat,bts_silom_line).
train(bang_wa,bts_silom_line).

% BTS - Airlink Line
%--------------------------------------------------------------
train(phaya_thai_airlink,airlink).
train(ratchaprarop,airlink).
train(makkasan,airlink).
train(ramkhamhaeng,airlink).
train(hua_mak,airlink).
train(ban_thap_chang,airlink).
train(latkrabang,airlink).
train(suvarnabhumi,airlink).

% different train database
%--------------------------------------------------------------
checkDifferent(mrt_blue_line, mrt_purple_line).
checkDifferent(mrt_blue_line, bts_sukhumvit_line).
checkDifferent(mrt_blue_line,bts_silom_line).
checkDifferent(mrt_blue_line,airlink).
checkDifferent(mrt_purple_line,bts_sukhumvit_line).
checkDifferent(mrt_purple_line,bts_silom_line).
checkDifferent(mrt_purple_line,airlink).
checkDifferent(bts_sukhumvit_line,bts_silom_line).o
checkDifferent(bts_sukhumvit_line,airlink).
checkDifferent(bts_silom_line,airlink).


% Code
%--------------------------------------------------------------------------------------------------------------------------------------------------
% theTrain(train_list, Return)
theTrainIs(Lst, Return) :- whichTrain(Lst, [], Return).

whichTrain([], Return, Return).
whichTrain([T|Lst], Result, Return) :- train(T, BMA), append([BMA], Result, RR1), whichTrain(Lst, RR1, Return).

% includeWalk(train_list, Return)
includeWalk(Lst, Return) :- checkWalk(Lst,[],Return).

checkWalk([],Return, Return).
checkWalk([H|T], Result,Return) :- isDifferent(H,T) -> append(Result, [walk], X), checkWalk(T, X, Return)
                                                                                ;append(Result, [H],X),checkWalk(T,X,Return).

isDifferent(X,[Y|T]) :- checkDifferent(X,Y),!.
isDifferent(X,[Y|T]) :- checkDifferent(Y,X),!.

