use utf8;
use open IO => ":utf8";
use open ":std";

#サブルーチン置き場---------------------------------------------------------------------------
sub wSte{
$newhp1       =  $Khp1;
$newmp1       =  $Kmp1;
$newmoney    =  $Kmoney + $mmony;
$newcount1    =  $Knecount1;
$newnecount1  =  $Knecount1;
$newmhp1      =  $Kmhp1;
$newmmp1      =  $Kmmp1;
$newkougeki1  =  $Kkou1;
$newmamori1   =  $Kmam1;
$newsub1      =  $Ksub1;
$newlev1      =  $Klev1;
}

#LVup処理---------------------------------------------------------------------------
sub wLVup{
	@monran1 = (0.8,0.9,1.0,1.1,1.2);
	$Hhp = $monran1[int(rand(5))];
	$hp1 = int($Hhp * $newmhp1 / $newlev1);
	
	@monran2 = (0.7,0.8,0.9,1.0,1.1);
	$Mmp = $monran2[int(rand(5))];
	$mp1 = int($Mmp * $newmmp1 / $newlev1);
	
	@monran3 = (0.8,0.9,1.0,1.1,1.2);
	$Lkou = $monran3[int(rand(5))];
	$kou1 = int($Lkou * $newkougeki1 / $newlev1);
	
	@monran4 = (0.7,0.8,0.9,1.0,1.1);
	$Lmam = $monran4[int(rand(5))];
	$mam1 = int($Lmam * $newmamori1 / $newlev1);
	
	@monran5 = (0.7,0.8,0.9,1.0,1.1);
	$Lsub = $monran5[int(rand(5))];
	$sub1 = int($Lsub * $newsub1 / $newlev1);

	$hyouzihp1    =  int($hp1+($Khai1*0.1));
	$newmhp1      =  $hyouzihp1 + $newmhp1;

	$hyouzimp1    =  int($mp1+($Khai1*0.1));
	$newmmp1      =  $hyouzimp1 + $newmmp1;

	$newcount1    =  $newcount1-$newnecount1;
	$newnecount1  =  int($newnecount1*1.15);
	if($newnecount1 >= 99999){$newnecount1  = 99999;}

	$hyouzikougeki1 = int($kou1+($Khai1*0.1));
	$newkougeki1  =  $hyouzikougeki1 + $newkougeki1;
	
	$hyouzimamori1 = int($mam1+($Khai1*0.1));
	$newmamori1   =  $hyouzimamori1 + $newmamori1;
	
	$hyouzisub1 = int($sub1+($Khai1*0.1));
	$newsub1   =  $hyouzisub1 + $newsub1;

	$newlev1      =  $newlev1;
	$newmoney         =  $newmoney;

}

#結果出力処理---------------------------------------------------------------------------

sub wprR {
print <<"EOF";
<FONT face="Times New Roman" color="#00ffff" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は戦闘に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$log</B></FONT>
<BR>
EOF

if($_[0] != 1) {
print <<"EOF";
<FONT size="4" color="#00ffff"><B>$mon1</B></FONT><FONT size="4" color="#ffff00">ポイント</FONT><FONT size="4" color="#ffffff">の経験値を得た。</FONT>
<BR>
EOF
}

print <<"EOF";
<FONT size="4" color="#00ffff"><B>$mmony</B></FONT><FONT size="4" color="#ffff00">ゴールド</FONT><FONT size="4" color="#ffffff">を得た。</FONT><BR>
EOF
}

#LVup出力処理---------------------------------------------------------------------------
sub wprLVup {
print <<"EOF";
<FONT face="Times New Roman" color="yellow" size="4"><B>LEVELUP！</B></FONT><BR>
<FONT face="Times New Roman" color="#00ffff" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4"><B>Lv$Klev1からLv$newlev1</B></FONT><FONT color="#ffffff" size="4">になった！</FONT><BR>
<FONT size="4" color="#ffffff">最大HPが</FONT><FONT size="4" color="#00ffff"><B>$hyouzihp1</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
<FONT size="4" color="#ffffff">最大MPが</FONT><FONT size="4" color="#00ffff"><B>$hyouzimp1</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
<FONT size="4" color="#ffffff">攻撃力が</FONT><FONT size="4" color="#00ffff"><B>$hyouzikougeki1</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
<FONT size="4" color="#ffffff">守備力が</FONT><FONT size="4" color="#00ffff"><B>$hyouzimamori1</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
<FONT size="4" color="#ffffff">素早さが</FONT><FONT size="4" color="#00ffff"><B>$hyouzisub1</B></FONT><FONT size="4" color="#ffffff">上昇した。</FONT><BR>
EOF
}


#戦闘処理---------------------------------------------------------------------------
#引き分けも勝ちも負けも大体おなじ---------------------------------------------------------------------------

sub wtaktak {
if($Fend == 1 || $Fend == 2 || $Fend == 3){
	&wSte;
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
	
	$mon1 = int(($Aex1 + $Aex2 + $Aex3) * $s);
	$mmony = $Amoney1 + $Amoney2 + $Amoney3;
	$newkey = $Kkey;
	$newmoney    =  $Kmoney + $mmony;

	#レベル限界判定
	if($Klev1 == $Kmlev1) {

		&fightC;

		&wprR(1);

		&fightD;

	}#レベル限界判定閉じ
	else {

		$newcount1    =  $Kcount1 + $mon1;

		#LvUP判定
		if($newcount1 >= $newnecount1) {
			Label0:

			$newlev1++;
			&wLVup;

			#成長限界判定
				if($newlev1 == $Kmlev1) {

				$newmhp1      =  15 + $Khai1;
				if($newhp1 > $newmhp1){$newhp1 = $newmhp1;}
				$newmmp1      =  14 + $Khai1;
				if($newmp1 > $newmmp1){$newmp1 = $newmmp1;}
				$newcount1    =  $Knecount1;
				$newnecount1  =  $Knecount1;
				$newkougeki1  =  25 + $Khai1;
				$newmamori1   =  24 + $Khai1;
				$newsub1   =  24 + $Khai1;

				&fightC;

				&wprR(0);

				print <<"EOF";
				<FONT face="Times New Roman" color="yellow" size="4"><B>LEVELUP！</B></FONT><BR>
				<FONT face="Times New Roman" color="#00ffff" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は戦闘に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$log</B></FONT>
				<BR><FONT size="4" color="#ff0000"><B>成長の限界に達した。</B></FONT>
				<BR><FONT size="4" color="#ff0000"><B>年老いた為、$itemlist[$Kimg1]の力は激減した。</B></FONT></TD>
EOF

				&fightD;

			}#成長限界判定閉じ
			else {

				#続けてLVUP判定
				if($newcount1 >= $newnecount1){
					goto Label0;
				}

				&fightC;

				&wprR(0);

				#合計上昇値計算
				$hyouzihp1       =  $newmhp1 - $Kmhp1;
				$hyouzimp1       =  $newmmp1 - $Kmmp1;
				$hyouzikougeki1  =  $newkougeki1 - $Kkou1;
				$hyouzimamori1   =  $newmamori1 - $Kmam1;
				$hyouzisub1      =  $newsub1 - $Ksub1;

				&wprLVup;

				&fightD;

			}#成長限界判定else閉じ
		}#LvUP判定閉じ
		else {

			&fightC;

			&wprR(0);

			&fightD;

		}#LvUP判定else閉じ
	}#レベル限界判定else閉じ


#戦闘後処理↓---------------

if($Khp1 == 0){$newhp1 = 1;}
if($newmoney >= 199999999999){ $newmoney = 199999999999;}

&open3;

if($_[0]==1 && $Fend == 2){#わたぼう判定
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
<TD align="left"><FONT size="4" color="#ffff00"><B>メダル</B></FONT><FONT size="4" color="#ffffff">を3枚ゲットした！ラッキー♪</FONT></FONT></TD>
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

$Kdummy = $Kdummy + 3;
}#わたぼう判定閉じ

if($_[0]==2 && $Fend == 2){#スライム城判定
open(FH,"keyset/$inname.cgi");
@keyset1 = <FH>;
close(FH);
foreach $line5 (@keyset1) {
   ($fusi[1],$fusi[2],$fusi[3],$fusi[4],$fusi[5],$fusi[6],$fusi[7],$fusi[8],$fusi[9],$fusi[10])=split(/<>/,$line5);
}

print <<"EOF";
<CENTER>
<BR>
<BR>
<TABLE border="0">
<TBODY>
<TR>
<TD width="400" colspan="2" align="center">
<BR><B>どのKEYを取得しますか？</B></TD>
</TR>
<TR>
<TD width="200" align="center">
<FORM ACTION="$cgiurl" METHOD="POST">
<SELECT name=KEYGET>
EOF
if($fusi[1]==0){
print "<option value=1>$keyname[1]\n";
}
if($fusi[2]==0){
print "<option value=2>$keyname[2]\n";
}
if($fusi[3]==0){
print "<option value=3>$keyname[3]\n";
}
if($fusi[4]==0){
print "<option value=4>$keyname[4]\n";
}
if($fusi[5]==0){
print "<option value=5>$keyname[5]\n";
}
if($fusi[6]==0){
print "<option value=6>$keyname[6]\n";
}
if($fusi[7]==0){
print "<option value=7>$keyname[7]\n";
}
if($fusi[8]==0){
print "<option value=8>$keyname[8]\n";
}
if($fusi[9]==0){
print "<option value=9>$keyname[9]\n";
}
if($fusi[10]==0){
print "<option value=10>$keyname[10]\n";
}
print <<"EOF";
</SELECT>
<INPUT type="submit" value="取得する">
<INPUT type="hidden" name="mode" value="KGET">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
</FORM>
</TD>
<TD width="200" align="center">
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="取得しない">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
</FORM>
</TD>
</TR>
</TBODY>
</TABLE>
EOF
EOF

}#スライム城判定閉じ




$newline = "$Kname<>$Kpass<>$newlev1<>$Kmlev1<>$Kimg1<>$newhp1<>$newmhp1<>$newmp1<>$newmmp1<>$newkougeki1<>$newmamori1<>$newsub1<>$Khai1<>$newcount1<>$newnecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$newkey<>$newmoney";
&lock;
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
&unlock;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay1,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    &get_ip;
    $newbye   =  (time + ($goodbye * 24 * 60 * 60));
    $newplay  =  (time + ($nexpplay * 60));
    $line = "$Yname<>$Ypass<>$host<>$newbye<>$newplay<>$newplay<>$Yplay3<>$newkey<>$Kimg1<>$Khai1<>$newlev1<>$Yimg2<>$Yhai2<>$Ylev2<>$Yimg3<>$Yhai3<>$Ylev3<>$newmoney<>$Ymes<>$turn";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
}
}

&ranksort;
&backup;

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

}#勝利or負けor引き分け分岐閉じ

}#関数taktak閉じ



1;