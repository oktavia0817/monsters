use utf8;
use open IO => ":utf8";
use open ":std";

#サブルーチン置き場---------------------------------------------------------------------------
sub Ste{
${newhp.$i}       =  ${Khp.$i};
${newmp.$i}       =  ${Kmp.$i};
${newmhp.$i}      =  ${Kmhp.$i};
${newmmp.$i}      =  ${Kmmp.$i};
${newcount.$i}    =  ${Knecount.$i};
${newnecount.$i}  =  ${Knecount.$i};
${newkougeki.$i}  =  ${Kkou.$i};
${newmamori.$i}   =  ${Kmam.$i};
${newsub.$i}      =  ${Ksub.$i};
${newlev.$i}      =  ${Klev.$i};
}

#LVup処理---------------------------------------------------------------------------
sub LVup{
	@monran1 = (0.8,0.9,1.0,1.1,1.2);
	$Hhp = $monran1[int(rand(5))];
	${hp.$i} = int($Hhp * ${newmhp.$i} / ${newlev.$i});
	
	@monran2 = (0.7,0.8,0.9,1.0,1.1);
	$Mmp = $monran2[int(rand(5))];
	${mp.$i} = int($Mmp * ${newmmp.$i} / ${newlev.$i});
	
	@monran3 = (0.8,0.9,1.0,1.1,1.2);
	$Lkou = $monran3[int(rand(5))];
	${kou.$i} = int($Lkou * ${newkougeki.$i} / ${newlev.$i});
	
	@monran4 = (0.7,0.8,0.9,1.0,1.1);
	$Lmam = $monran4[int(rand(5))];
	${mam.$i} = int($Lmam * ${newmamori.$i} / ${newlev.$i});
	
	@monran5 = (0.7,0.8,0.9,1.0,1.1);
	$Lsub = $monran5[int(rand(5))];
	${'sub'.$i} = int($Lsub * ${newsub.$i} / ${newlev.$i});

	${hyouzihp.$i}    =  int(${hp.$i}+(${Khai.$i}*0.1));
	${newmhp.$i}      =  ${hyouzihp.$i} + ${newmhp.$i};

	${hyouzimp.$i}    =  int(${mp.$i}+(${Khai.$i}*0.1));
	${newmmp.$i}      =  ${hyouzimp.$i} + ${newmmp.$i};

	${newcount.$i}    =  ${newcount.$i} - ${newnecount.$i};
	${newnecount.$i}  =  int(${newnecount.$i}*1.15);
	if(${newnecount.$i} >= 99999){${newnecount.$i}  = 99999;}

	${hyouzikougeki.$i} = int(${kou.$i}+(${Khai.$i}*0.1));
	${newkougeki.$i}  =  ${hyouzikougeki.$i} + ${newkougeki.$i};

	${hyouzimamori.$i} = int(${mam.$i}+(${Khai.$i}*0.1));
	${newmamori.$i}   =  ${hyouzimamori.$i} + ${newmamori.$i};

	${hyouzisub.$i}   = int(${'sub'.$i}+(${Khai.$i}*0.1));
	${newsub.$i}      =  ${hyouzisub.$i} + ${newsub.$i};

	${newlev.$i}      =  ${newlev.$i};
	$newmoney         =  $newmoney;

}

#結果出力処理---------------------------------------------------------------------------

sub prR {
print <<"EOF";
<FONT face="Times New Roman" color="#00ffff" size="4p"><B>$itemlist[${Kimg.$i}]</B></FONT><FONT size="4" color="#ffffff">は戦闘に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$log</B></FONT>
<BR>
EOF
if($_[0] != 1) {
print <<"EOF";
<FONT size="4" color="#00ffff"><B>${mon.$i}</B></FONT><FONT size="4" color="#ffff00">ポイント</FONT><FONT size="4" color="#ffffff">の経験値を得た。</FONT>
<BR>
EOF
}
if($i == 1){
print <<"EOF";
<FONT size="4" color="#00ffff"><B>$mmony</B></FONT><FONT size="4" color="#ffff00">ゴールド</FONT><FONT size="4" color="#ffffff">を得た。</FONT><BR>
EOF
}
}

#LVup出力処理---------------------------------------------------------------------------
sub prLVup {
print <<"EOF";
<FONT face="Times New Roman" color="yellow" size="4"><B>LEVELUP！</B></FONT><BR>
<FONT face="Times New Roman" color="#00ffff" size="4p"><B>$itemlist[${Kimg.$i}]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4"><B>Lv${Klev.$i}からLv${newlev.$i}</B></FONT><FONT color="#ffffff" size="4">になった！</FONT><BR>
<FONT size="4" color="#ffffff">最大HPが</FONT><FONT size="4" color="#00ffff"><B>${hyouzihp.$i}</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
<FONT size="4" color="#ffffff">最大MPが</FONT><FONT size="4" color="#00ffff"><B>${hyouzimp.$i}</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
<FONT size="4" color="#ffffff">攻撃力が</FONT><FONT size="4" color="#00ffff"><B>${hyouzikougeki.$i}</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
<FONT size="4" color="#ffffff">守備力が</FONT><FONT size="4" color="#00ffff"><B>${hyouzimamori.$i}</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
<FONT size="4" color="#ffffff">素早さが</FONT><FONT size="4" color="#00ffff"><B>${hyouzisub.$i}</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
EOF
}

#鍵獲得処理---------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
sub key {
	if($inkai == $Kkey){
		@KEYSET = (0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,4,4,4,4,4,7,7,7,7,8,8,9,10);
		$KLIST = $KEYSET[int(rand(30))];
	}
	if($KLIST == 1){
		$newkey = $Kkey + 1;
		print <<"EOF";
		<CENTER>
		<TABLE bgcolor="#ff0000" width="400">
		<TBODY>
		<TR>
		<TD colspan="3" width="400" bgcolor="#000000" align="center">
		<BLOCKQUOTE>
		<TABLE>
		<TBODY>
		<TR>
		<TD align="left"><FONT size="4" color="#ffff00">地下$newkey 階への</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>KEY</B><FONT size="4" color="#ffffff">を拾った！</FONT></FONT></TD>
		</TR>
		</TBODY>
		</TABLE>
		</BLOCKQUOTE>
		</TD>
		</TR>
		</TBODY>
		</TABLE>
		</CENTER>
EOF
	}
	if($KLIST == 4){
		$newkey = $Kkey + 3;
		print <<"EOF";
		<CENTER>
		<TABLE bgcolor="#ff0000" width="400">
		<TBODY>
		<TR>
		<TD colspan="3" width="400" bgcolor="#000000" align="center">
		<BLOCKQUOTE>
		<TABLE>
		<TBODY>
		<TR>
		<TD align="left"><FONT size="4" color="#ffff00"><B>幸せのKEY+3</B></FONT><FONT size="4" color="#ffffff">を拾った！ラッキー♪</FONT></FONT></TD>
		</TR>
		</TBODY>
		</TABLE>
		</BLOCKQUOTE>
		</TD>
		</TR>
		</TBODY>
		</TABLE>
		</CENTER>
EOF
	}
	if($KLIST == 7){
		$newkey = $Kkey + 10;
		print <<"EOF";
		<CENTER>
		<TABLE bgcolor="#ff0000" width="400">
		<TBODY>
		<TR>
		<TD colspan="3" width="400" bgcolor="#000000" align="center">
		<BLOCKQUOTE>
		<TABLE>
		<TBODY>
		<TR>
		<TD align="left"><FONT size="4" color="#ffff00"><B>幸運のKEY+10</B></FONT><FONT size="4" color="#ffffff">を拾った！ラッキー♪</FONT></FONT></TD>
		</TR>
		</TBODY>
		</TABLE>
		</BLOCKQUOTE>
		</TD>
		</TR>
		</TBODY>
		</TABLE>
		</CENTER>
EOF
	}
	if($KLIST == 8){
		$newkey = $Kkey + 30;
		print <<"EOF";
		<CENTER>
		<TABLE bgcolor="#ff0000" width="400">
		<TBODY>
		<TR>
		<TD colspan="3" width="400" bgcolor="#000000" align="center">
		<BLOCKQUOTE>
		<TABLE>
		<TBODY>
		<TR>
		<TD align="left"><FONT size="4" color="#ffff00"><B>天運のKEY+30</B></FONT><FONT size="4" color="#ffffff">を拾った！ラッキー♪</FONT></FONT></TD>
		</TR>
		</TBODY>
		</TABLE>
		</BLOCKQUOTE>
		</TD>
		</TR>
		</TBODY>
		</TABLE>
		</CENTER>
EOF
	}
	if($KLIST == 9){
		$newkey = $Kkey + 50;
		print <<"EOF";
		<CENTER>
		<TABLE bgcolor="#ff0000" width="400">
		<TBODY>
		<TR>
		<TD colspan="3" width="400" bgcolor="#000000" align="center">
		<BLOCKQUOTE>
		<TABLE>
		<TBODY>
		<TR>
		<TD align="left"><FONT size="4" color="#ffff00"><B>希望のKEY+50</B></FONT><FONT size="4" color="#ffffff">を拾った！ラッキー♪</FONT></FONT></TD>
		</TR>
		</TBODY>
		</TABLE>
		</BLOCKQUOTE>
		</TD>
		</TR>
		</TBODY>
		</TABLE>
		</CENTER>
EOF
	}
	if($KLIST == 10){
		$newkey = $Kkey + 100;
		print <<"EOF";
		<CENTER>
		<TABLE bgcolor="#ff0000" width="400">
		<TBODY>
		<TR>
		<TD colspan="3" width="400" bgcolor="#000000" align="center">
		<BLOCKQUOTE>
		<TABLE>
		<TBODY>
		<TR>
		<TD align="left"><FONT size="4" color="#ffff00"><B>奇跡のKEY+100</B></FONT><FONT size="4" color="#ffffff">を拾った！ラッキー♪</FONT></FONT></TD>
		</TR>
		</TBODY>
		</TABLE>
		</BLOCKQUOTE>
		</TD>
		</TR>
		</TBODY>
		</TABLE>
		</CENTER>
EOF
	}

}
#勝利時モンスター獲得処理---------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

sub mong {

	if($inkai <= 175){
	@MGET = (0,0,1);
	$monlist = $MGET[int(rand(3))];
	}
	if($inkai >= 176 && $inkai <= 200){
	@MGET = (0,0,0,1);
	$monlist = $MGET[int(rand(4))];
	}
	if($inkai >= 201){
	@MGET = (1,0,0,0,0);
	$monlist = $MGET[int(rand(5))];
	}
	if($Gimg >= 201 && $Gimg <= 999 or $Gimg == 110){
	$monlist = 0;
	}

	if($monlist == 1){

	print <<"EOF";
	<CENTER>
	<BR>
	<BR>
	<TABLE border="0">
	<TBODY>
	<TR>
	<TD width="400" colspan="2" align="center">
	<IMG src="$imgpath/$Gimg.gif" border="0">
	<BR><B>$Acname</B>が仲間になりたがっています。
	仲間にしますか？</TD>
	</TR>
	<TR>
	<TD width="200" align="center">
	<FORM ACTION="$cgiurl" METHOD="POST">
	<INPUT type="submit" value="仲間にする">
	<INPUT type="hidden" name="mode" value="MGET">
	<INPUT type="hidden" name="name" value="$inname">
	<INPUT type="hidden" name="password" value="$inpass">
	<INPUT type="hidden" name="Aimg" value="$Gimg">
	<INPUT type="hidden" name="Asex" value="$Asex">
	</FORM>
	</TD>
	<TD width="200" align="center">
	<FORM ACTION="$cgiurl" METHOD="POST">
	<INPUT type="submit" value="無視する">
	<INPUT type="hidden" name="mode" value="login">
	<INPUT type="hidden" name="name" value="$inname">
	<INPUT type="hidden" name="password" value="$inpass">
	</FORM>
	</TD>
	</TR>
	</TBODY>
	</TABLE>
EOF
	}
	
	if($monlist == 0){
	print <<"EOF";
	<FORM ACTION="$cgiurl" METHOD="POST">
	<CENTER>
	<BR><BR>
	<INPUT type="hidden" name="mode" value="login">
	<INPUT type="submit"  value="ログインへ">
	<INPUT type="hidden" name="name" value="$inname">
	<INPUT type="hidden" name="password" value="$inpass">
	</CENTER>
	</FORM>
EOF
	}

}

#戦闘後LVup処理---------------------------------------------------------------------------
#---------------------------------------------------------------------------

sub taktak {
if($Fend == 1 || $Fend == 2 || $Fend == 3){
	&Ste;
	if ($Fend == 1){
		$log ="引き分けた";
		$s = 0.5;
	} elsif ($Fend == 2){
		$log ="勝利した";
		$s = 1;
	} elsif ($Fend == 3){
		$log ="負けた";
		$s = 0.5;	
	}
	
	$mon1 = int(($Aex1 + $Aex2 + $Aex3) * $s /$Ssu);
	$mon2 = $mon1;
	$mon3 = $mon1;
	$mmony = $Amoney1 + $Amoney2 + $Amoney3;
	$newkey = $Kkey;
	$newmoney    =  $Kmoney + $mmony;


for ($i=1;$i<=$Ssu;$i++){

	#レベル限界判定
	if(${Klev.$i} == ${Kmlev.$i}) {

		&fightC;

		&prR(1);

		&fightD;

	}#レベル限界判定閉じ
	else {

		${newcount.$i}    =  ${Kcount.$i} + ${mon.$i};

		#LvUP判定
		if(${newcount.$i} >= ${newnecount.$i}) {
			Label0:

			${newlev.$i}++;
			&LVup;

			#成長限界判定
			if(${newlev.$i} == ${Kmlev.$i}) {

				${newmhp.$i}      =  15 + ${Khai.$i};
				if(${newhp.$i} > ${newmhp.$i}){${newhp.$i} = ${newmhp.$i};}
				${newmmp.$i}      =  14 + ${Khai.$i};
				if(${newmp.$i} > ${newmmp.$i}){${newmp.$i} = ${newmmp.$i};}
				${newcount.$i}    =  ${Knecount.$i};
				${newnecount.$i}  =  ${Knecount.$i};
				${newkougeki.$i}  =  25 + ${Khai.$i};
				${newmamori.$i}   =  24 + ${Khai.$i};
				${newsub.$i}      =  24 + ${Khai.$i};

				&fightC;

				&prR(0);

				print <<"EOF";
				<FONT face="Times New Roman" color="yellow" size="4"><B>LEVELUP！</B></FONT><BR>
				<FONT face="Times New Roman" color="#00ffff" size="4p"><B>$itemlist[${Kimg.$i}]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#00ffff" size="4"><B>Lv${Klev.$i}からLv${newlev.$i}</B></FONT><FONT color="#ffffff" size="4">になった！</FONT><BR>
				<BR><FONT size="4" color="#ff0000"><B>成長の限界に達した。</B></FONT>
				<BR><FONT size="4" color="#ff0000"><B>年老いた為、$itemlist[${Kimg.$i}]の力は激減した。</B></FONT></TD>
EOF

				&fightD;

			}#成長限界判定閉じ
			else {

				#続けてLVUP判定
				if(${newcount.$i} >= ${newnecount.$i}){
					goto Label0;
				}

				&fightC;

				&prR(0);

				#合計上昇値計算
				${hyouzihp.$i}       =  ${newmhp.$i} - ${Kmhp.$i};
				${hyouzimp.$i}       =  ${newmmp.$i} - ${Kmmp.$i};
				${hyouzikougeki.$i}  =  ${newkougeki.$i} - ${Kkou.$i};
				${hyouzimamori.$i}   =  ${newmamori.$i} - ${Kmam.$i};
				${hyouzisub.$i}      =  ${newsub.$i} - ${Ksub.$i};

				&prLVup;

				&fightD;

			}#成長限界判定else閉じ
		}#LvUP判定閉じ
		else {

			&fightC;

			&prR(0);

			&fightD;

		}#LvUP判定else閉じ
	}#レベル限界判定else閉じ
}#for閉じ


#戦闘後処理↓---------------
if($Fend == 2){
	&key;
} elsif ($Fend == 3){
	&haisen;
	if($Khp1 == 0 && $Khp2 == 0 && $Khp3 == 0){$newhp1 = 1;}
}

if($newmoney >= 199999999999){ $newmoney = 199999999999;}

&open3;

$newline = "$Kname<>$Kpass<>$newlev1<>$Kmlev1<>$Kimg1<>$newhp1<>$newmhp1<>$newmp1<>$newmmp1<>$newkougeki1<>$newmamori1<>$newsub1<>$Khai1<>$newcount1<>$newnecount1<>$Ksex1<>$Ksei1<>$newlev2<>$Kmlev2<>$Kimg2<>$newhp2<>$newmhp2<>$newmp2<>$newmmp2<>$newkougeki2<>$newmamori2<>$newsub2<>$Khai2<>$newcount2<>$newnecount2<>$Ksex2<>$Ksei2<>$newlev3<>$Kmlev3<>$Kimg3<>$newhp3<>$newmhp3<>$newmp3<>$newmmp3<>$newkougeki3<>$newmamori3<>$newsub3<>$Khai3<>$newcount3<>$newnecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$newkey<>$newmoney";
&lock;
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
&unlock;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    &get_ip;
    $newbye   =  (time + ($goodbye * 24 * 60 * 60));
    $newplay  =  (time + ($nexpplay * 60));
	if($Fend == 2){ $mg = 2;} else {$mg = $Yplay3; }
    $line = "$Yname<>$Ypass<>$host<>$newbye<>$newplay<>$newplay<>$mg<>$newkey<>$Kimg1<>$Khai1<>$newlev1<>$Kimg2<>$Khai2<>$newlev2<>$Kimg3<>$Khai3<>$newlev3<>$newmoney<>$Ymes<>$turn";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
}
}

&ranksort;
&backup;

if($Fend == 2){
	&mong;
	} else {
	print <<"EOF";
	<FORM ACTION="$cgiurl" METHOD="POST">
	<CENTER>
	<BR><BR>
	<INPUT type="hidden" name="mode" value="login">
	<INPUT type="submit"  value="ログインへ">
	<INPUT type="hidden" name="name" value="$inname">
	<INPUT type="hidden" name="password" value="$inpass">
	</CENTER>
	</FORM>
EOF
}

}#勝利or負けor引き分け分岐閉じ

}#関数taktak閉じ


1;