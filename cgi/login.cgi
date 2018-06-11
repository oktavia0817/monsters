use utf8;
use open IO => ":utf8";
use open ":std";


sub hai {
	for($i=1;$i<=10;$i++){
		if($Klev[$i] >= $haigoulevel){
			print "<option value=$i >0$i: $itemlist[${P.$i}] $seibetu[$Ksex[$i]] LV-$Klev[$i] 配合$Khai[$i]回</OPTION>\n";
		}
	}
}

sub hai2 {
	for($i=1;$i<=10;$i++){
		if($Klev[$i] == 1){
			$ryoukin = $Khai[$i] * 100;
			if($ryoukin >= 99999){$ryoukin = 99999;}
			print "<option value=$i >$itemlist[${P.$i}] $ryoukin ゴールド</OPTION>"
		}
	}
}

$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$bname = $FORM{'name'};
$bpass = $FORM{'password'};
$type = $FORM{'type'};

open(FH,"omiai/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],
$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub
[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],
$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],
$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei
[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],
$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub
[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],
$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],
$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[1]) = split(/<>/,
$line);
}

if($type==1){$bname = $FORM{'bname'};$bpass = $FORM{'bpass'};}
if ($inname eq "") { &error("名前がありません");}
if(!$type==1){
if ($inpass eq "") { &error("パスワードがありません");}}

&open2;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

$login = 0;
    
foreach $line (@lines) {
    ($Yname1,$Ypass1,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,
$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    $Krank++;
    if($inname eq $Yname1) {
    $Kmes = $Ymes;
    $Kkey = $Ykey;
    $Kmoney = $Ymoney;
    
    $passcheck = crypt($inpass, $inname);
    if(!$type==1){
    if($passcheck ne $Ypass1) { &error("パスワードが違います");  }
    }
    $Yplaytime = $Yplay - time;
    $login = 1; last;
    }
}
if(!$login){ &error("あなたは未登録かパスワードエラーです！");  }

&open1;

$Slev[1] = $Klev[1];

for($A=1;$A<11;$A++){
if($Kimg[$A] != 0){$Ssu++;}
if($Khp[$A]  != 0){$SSsu++;}
}
$P1       = $Kimg[1];
$P2       = $Kimg[2];
$P3       = $Kimg[3];
$P4       = $Kimg[4];
$P5       = $Kimg[5];
$P6       = $Kimg[6];
$P7       = $Kimg[7];
$P8       = $Kimg[8];
$P9       = $Kimg[9];
$P10       = $Kimg[10];

for($im=2;$im<11;$im++){
$Slev[$im] = $Klev[$im];
if($Kimg[$im]==0){
$Klev[$im] = '-';
$KKlev[$im] = 0;
$Kmlev[$im] = '-';
$Khp[$im] = '-';
$Kmhp[$im] = '-';
$Kmp[$im] = '-';
$Kmmp[$im] = '-';
$Kkou[$im] = '-';
$Kmam[$im] = '-';
$Ksub[$im] = '-';
$Khai[$im] = '-';
$Kcount[$im] = '-';
$Knecount[$im] = '-';
$Ksex[$im] = '-';
$Ksei[$im] = '-';
}
}
for($Y=1;$Y<11;$Y++){
if($Kmhp[$Y] != 0 && $Khp[$Y] != 0){
$yado = $yado + $Kmhp[$Y]-$Khp[$Y] + $Kmmp[$Y]-$Kmp[$Y];
}
}
$yadoya = $yado;
if($yadoya >= 99999){$yadoya = 99999;}

for($Y=1;$Y<11;$Y++){
if($Kmhp[$Y] != 0 && $Khp[$Y] == 0){
$kyoukai = $kyoukai + $Kmhp[$Y] + $Kmmp[$Y];
}
}
$kyoukai = $kyoukai * 2;
if($kyoukai eq ""){$kyoukai = 0;}
if($kyoukai >= 99999){$kyoukai = 99999;}

$haigoudai = $Khaigou * $Mmoney;
if($haigoudai >= 99999) { $haigoudai = 99999;}

$namelog = "$KnameさんのLOGINメニュー";
if($type == 1){
$namelog = "$KnameさんのLOGIN内容";
}

open(FH,"keyset/$inname.cgi");
@keyset1 = <FH>;
close(FH);
foreach $line5 (@keyset1) {
   ($fusi[1],$fusi[2],$fusi[3],$fusi[4],$fusi[5],$fusi[6],$fusi[7],$fusi[8],$fusi[9],$fusi[10])=split(/<>/,$line5);
}


open(FH,"$monsdata");
@lines99 = <FH>;
close(FH);

 $mleng = @lines99;

open(FH,"zukan/$inname.cgi") || goto Label0;
@lines98 = <FH>;
close(FH);
goto Label1;

Label0:
&lock;
open(FH,">>zukan/$inname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>";
close(FH);
&unlock;

Label1:
foreach $line (@lines98) {
   @zukan = split(/<>/,$line);
}


 $get = 0;
	for($i=1;$i<=$mleng;$i++){
		if($zukan[$i]==1){
			$get += 1;
		}
	}

  $s = sprintf('%.2f', $get / $mleng * 100);

&header;

print <<"EOF";
<CENTER>
<TABLE>
<TBODY>
<TR>
<TD align="center"><FONT color="#FFFFFF"><B>[ <A href="$homepage">$home_title</A> ] 
      [ <A href="http://oktavia.sakura.ne.jp/monsters/haigou.html" target="_blank">配合表\</A> ] [ <A href="http://oktavia.sakura.ne.jp/monsters/kaizou.html" target="_blank">改造点・新モンスター配合表\</A> ]
[ <A href="$cgipath/$kanrim" target="_blank">管理モード</A> ]
</B></FONT></TD>
</TR>
</TBODY>
</TABLE>
<TABLE border="0" width="700" bgcolor="black">
<TBODY>
<TR>
<TD colspan="6" align="center"><font color="white" size="4"><b>$namelog</b></font></TD>
</TR>
<TR>
<TD align="center" bgcolor="#00cccc">所持金</TD>
<TD align="center" bgcolor="#00cccc">KEY</TD>
<TD align="center" bgcolor="#00cccc">ランク</TD>
<TD align="center" bgcolor="#00cccc">メダル</TD>
<TD align="center" width="338" bgcolor="#00cccc">コメント</TD>
<TR>
<TD align="center" bgcolor="#ffffff">$Kmoney ゴールド</TD>
<TD align="center" bgcolor="#ffffff">地下$Kkey 階</TD>
<TD align="center" bgcolor="#ffffff">$Krank 位</TD>
<TD align="center" bgcolor="#ffffff">$Kdummy 個</TD>
<TD align="left" width="338" bgcolor="#ffffff">$Kmes</TD>
</TR>
<TR>
<TD align="center" bgcolor="#00cccc">
[<a href="./monster.cgi?mode=zukan&name=$inname&type=1"><b>魔物図鑑</b></a>]
</TD>
</TR>
<TR>
<TD align="center" bgcolor="white">
<FONT color="black">$get ／$mleng 匹（$s ％）
</TD>
</TR>
</FORM>
<FORM ACTION="$cgiurl" METHOD="POST">
</TR>
</TBODY>
</TABLE>
<TABLE border="0" width="700" bgcolor="black">
<TBODY>
<TR>
<TD align="center" bgcolor="#00cccc">NO</TD>
<TD align="center" bgcolor="#00cccc">キャラ</TD>
<TD align="center" bgcolor="#00cccc">配合</TD>
<TD align="center" bgcolor="#00cccc">LV<BR>
最大LV</TD>
<TD width="70" align="center" bgcolor="#00cccc">HP<BR>
最大HP</TD>
<TD width="70" align="center" bgcolor="#00cccc">MP<BR>
最大MP</TD>
<TD width="70" align="center" bgcolor="#00cccc">攻撃力</TD>
<TD width="70" align="center" bgcolor="#00cccc">守備力</TD>
<TD width="70" align="center" bgcolor="#00cccc">素早さ</TD>
<TD width="70" align="center" bgcolor="#00cccc">経験値<BR>
UP経験値</TD>
</TR>
EOF
for($g=1;$g<11;$g++){
if($g >= 1 && $g <= 3) { $col = 'yellow';}
if($g >= 4 && $g <= 10){ $col = '#ffffff';}
print <<"EOF";
<TR>
<TD align="center" bgcolor="$col">
EOF
if($Ssu >= 1 && $type == 1){
print <<"EOF";
$g
EOF
}

if($Kimg[$g] != 0 && $Ssu >= 1 && $type != 1){
	$tex ="";
	for ($i=1;$i<=10;$i++) {
		for ($x=1;$x<=$i;$x++) {
			if($Ssu == $i && $g == $x){
				$tex = "<SELECT name=cname$x>\n";
				for ($n=1;$n<=$i;$n++) {
					if($x==$n) {
						$tex .= "<option value=$n SELECTED>$n</option>\n";
					} else {
						$tex .= "<option value=$n>$n</option>\n";
					}
				}
				$tex .= "</SELECT>\n";
			}
		}
	}
	print $tex;
}

print <<"EOF";
</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[$g].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[$g]] - 
 $seibetu[$Ksex[$g]]<BR>【$seikaku[$Ksei[$g]]】</TD>
<TD align="center" bgcolor="$col">$Khai[$g]回</TD>
<TD align="center" bgcolor="$col">$Klev[$g]<BR>
$Kmlev[$g]</TD>
<TD align="center" bgcolor="$col">$Khp[$g]<BR>
$Kmhp[$g]</TD>
<TD align="center" bgcolor="$col">$Kmp[$g]<BR>
$Kmmp[$g]</TD>
<TD align="center" bgcolor="$col">$Kkou[$g]</TD>
<TD align="center" bgcolor="$col">$Kmam[$g]</TD>
<TD align="center" bgcolor="$col">$Ksub[$g]</TD>
<TD align="center" bgcolor="$col">$Kcount[$g]<BR>
$Knecount[$g]</TD>
</TR>
EOF
}
print <<"EOF";
<TR>
<TD align="center" colspan="4">
EOF
if($Ssu >= 2 && $type != 1){
print <<"EOF";
<BR>
<INPUT type="submit" value="並び替えOK">
<INPUT type="hidden" name="mode"  value="change">
<INPUT type="hidden" name="Ssu"   value="$Ssu">
<INPUT type="hidden" name="name"  value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
</FORM>
EOF
}
print <<"EOF";
</TD>
<TD colspan="6" align="center">
<FONT color=white><B>No.1からNo.3迄のモンスターが戦闘を行います</B></FONT>
</TD>
</TR>
</TBODY>
</TABLE>

<TABLE border="0" width="700" bgcolor="black">
<TBODY>
<TR>
<TD colspan="5" align="center" bgcolor="#00cccc"><a href="javascript:bo('u2')" class="menu">▼系統の鍵一覧▼</a></TD>
</TR>
</table>
<div id="u2">
<TABLE border="0" width="700" bgcolor="black">
<TR>
EOF
for($k=1;$k<6;$k++){
$K=$fusi[$k];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$keylist[$K]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($k=6;$k<11;$k++){
$K=$fusi[$k];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$keylist[$K]</TD>
EOF
}
print <<"EOF";
</TR>
</table>
</div>
<TABLE border="0" width="700" bgcolor="black">
<TR>
<TD colspan="5" align="center" bgcolor="#00cccc"><a href="javascript:bo('u3')" class="menu">▼取得特殊攻撃一覧▼</a></TD>
</TR>
</table>
<div id="u3">
<TABLE border="0" width="700" bgcolor="black">
<TR>
EOF
for($t=1;$t<6;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=6;$t<11;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=11;$t<16;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=16;$t<21;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=21;$t<26;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=26;$t<31;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=31;$t<36;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=36;$t<41;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=41;$t<46;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=46;$t<51;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
<TR>
EOF
for($t=51;$t<56;$t++){
$T=$waza[$t];
print <<"EOF";
<TD width="140" align="center" bgcolor="#ffffff">$mtoku[$T]</TD>
EOF
}
print <<"EOF";
</TR>
</TBODY>
</TABLE>
</div>
<BR>
EOF
if(!$type == 1){

&get_cookie;
print <<"EOF";
<P align="center">
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT size="80" type="text" name="message" value="">
<INPUT type="hidden" name="mode" value="comment">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit" value="コメント変更">
</P>
</FORM>
</td>
</tr> 
</table>
<FORM name="RemainForm"><INPUT name="RemainTime" size="30" type="text" readonly></FORM><SCRIPT language="JavaScript">
<!--
nextTurn = $Yplaytime; loadDate = new Date();
timerID = setTimeout('dispRemainTime()', 100);
function dispRemainTime() { clearTimeout(timerID);
document.RemainForm.RemainTime.value = getRemainTime();
timerID = setTimeout('dispRemainTime()', 1000);}
function getRemainTime() {
now = new Date();msec = now.getTime() - loadDate.getTime();
msec -= msec % 1000; msec /= 1000;msec = nextTurn - msec;
if (msec < 0) {msec = 0;}
sec = msec % 60; msec = (msec - sec) / 60;
min = msec % 60; hour = (msec - min) / 60;
if (hour < 10) {hour = "0" + hour;}
if (min < 10) {min = "0" + min;}
if (sec < 10) {sec = "0" + sec;}
return "戦闘OKまで " + hour + ":" + min + ":" + sec;}
//-->
</SCRIPT>
<TABLE bgcolor="#000000" width="90%">
<TBODY>
<TR>
<TD bgcolor="#000000" height="30" align="center"><FONT color="#ff0000" size="+1"><B>戦　闘</B></FONT></TD>
<TD bgcolor="#000000"><FONT color="#ffffff">KEYやモンスターが入手出来ます。KEYは一番深い階層を選択した時にしか出現しま
せん。</FONT></TD>
</TR>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【最 深 階】</TD>
<TD bgcolor="#99ccff">
<SELECT name="keitou">
<option value=0>通常の部屋
EOF
if($fusi[1]==1){
print "<option value=1>$keyname[1]\n";
}
if($fusi[2]==2){
print "<option value=2>$keyname[2]\n";
}
if($fusi[3]==3){
print "<option value=3>$keyname[3]\n";
}
if($fusi[4]==4){
print "<option value=4>$keyname[4]\n";
}
if($fusi[5]==5){
print "<option value=5>$keyname[5]\n";
}
if($fusi[6]==6){
print "<option value=6>$keyname[6]\n";
}
if($fusi[7]==7){
print "<option value=7>$keyname[7]\n";
}
if($fusi[8]==8){
print "<option value=8>$keyname[8]\n";
}
if($fusi[9]==9){
print "<option value=9>$keyname[9]\n";
}
if($fusi[10]==10){
print "<option value=10>$keyname[10]\n";
}
print <<"EOF";
</SELECT>
<FONT color="#000000">の地下</FONT> 
<input type="text" name="kai" value="$Kkey" size="5">
EOF
print <<"EOF";
</SELECT>
<FONT color="#000000">Fに </FONT>
<INPUT type="submit" value="戦闘に行く！">
<INPUT type="hidden" name="mode" value="aite">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$Kpass">
<INPUT type="hidden" name="loginpass" value="$inpass">
<INPUT type="hidden" name="rank" value="$Krank">
<INPUT type="hidden" name="Ssu"   value="$Ssu">
</TD>
</TR>
</FORM>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【前対戦階】</TD>
<TD bgcolor="#99ccff">
<SELECT name="keitou">
<option value=0>通常の部屋
EOF
for($i = 1 ; $i <= 10; $i++) {
if($ROOM == $i) {
$sel = 'SELECTED';
}
else {
$sel = '';
}
if($fusi[$i] == $i){
print "<option value=$i $sel>$keyname[$i]\n";
}
}
print <<"EOF";
</SELECT>
<FONT color="#000000">の地下 </FONT>
<input type="text" name="kai" value="$Ikai" size="5">
EOF

print <<"EOF";
</SELECT>
<FONT color="#000000">Fに</FONT> 
<INPUT type="submit" value="戦闘に行く！">
<INPUT type="hidden" name="mode" value="aite">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$Kpass">
<INPUT type="hidden" name="loginpass" value="$inpass">
<INPUT type="hidden" name="rank" value="$Krank">
<INPUT type="hidden" name="Ssu"   value="$Ssu">
</TD>
</TR>
</FORM>
<TR>
<TD colspan="2">
<HR size="5">
</TD>
</TR>
<TR>
<TD bgcolor="#000000" height="30" align="center"><FONT color="#ff0000" size="+1"><B>本屋さん</B></FONT></TD>
<TD bgcolor="#000000"><FONT color="#ffffff">モンスターに本を読ませて性格を変更させる事が出来ます。</FONT></TD>
</TR>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【本屋に入室】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="本屋に入室">
<INPUT type="hidden" name = "mode" value = "books">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<TD colspan="2">
<HR size="5">
<TR>
<TD bgcolor="#000000" height="30" align="center"><FONT color="#ff0000" size="+1"><B>宿　屋</B></FONT></TD>
<TD bgcolor="#000000"><FONT color="#ffffff">表\示\されたゴールドを支払って宿屋に宿泊します。HP・MPが完全に回復します。
</FONT></TD>
</TR>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【宿泊料金】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="$yadoya ゴールド">
<INPUT type="hidden" name = "mode" value = "yadoya">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="yadodai" value="$yadoya">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<TD colspan="2">
<HR size="5">
</TD>
</TR>
<TR>
<TD height="30" align="center"><FONT color="#ff0000" size="+1"><B>教 会</B></FONT></TD>
<TD><FONT color="#ffffff">表\示\されたゴールドを支払って教会でお祈りします。HP・MPが完全に回復して復活します。</FONT>
</TD>
</TR>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【お祈り料】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="$kyoukai ゴールド">
<INPUT type="hidden" name = "mode" value = "kyoukai">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="kyoukaidai" value="$kyoukai">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<TD colspan="2">
<HR size="5">
</TD>
</TR>
<TR>
<TD bgcolor="#000000" height="30" align="center"><FONT color="#ff0000" size="+1"><B>メダル交換所</B></FONT></TD>
<TD bgcolor="#000000"><FONT color="#ffffff">貯めたメダルでレアモンスターをGET出来ます！</FONT></TD>
</TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【メダル30枚でVIPSスライム】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="交換所入室">
<INPUT type="hidden" name = "mode" value = "medal3">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
</TD>
</TR>
</FORM>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【メダル50枚でわたぼう】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="交換所入室">
<INPUT type="hidden" name = "mode" value = "medal">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
</TD>
</TR>
</FORM>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【1億ゴールドで配合100回スライム】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="交換所入室">
<INPUT type="hidden" name = "mode" value = "medal2">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【3000万ゴールドでちのせいれい】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="交換所入室">
<INPUT type="hidden" name = "mode" value = "medal4">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【3000万ゴールドでみずのせいれい】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="交換所入室">
<INPUT type="hidden" name = "mode" value = "medal5">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【3000万ゴールドでひのせいれい】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="交換所入室">
<INPUT type="hidden" name = "mode" value = "medal6">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【3000万ゴールドでかぜのせいれい】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="交換所入室">
<INPUT type="hidden" name = "mode" value = "medal7">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<TD colspan="2">
<HR size="5">
</TD>
</TR>
<TR>
<TD bgcolor="#000000" height="30" align="center"><FONT color="#ff0000" size="+1"><B>配　合</B></FONT></TD>
<TD bgcolor="#000000"><FONT color="#ffffff">配合料金は配合させる2匹のモンスターの【（レベル＋レベル）×10ゴールド】で
す。</FONT></TD>
</TR>
<TR>

<SCRIPT LANGUAGE="JavaScript">
<!--

var m =0;

function bo(x){

 if(document.getElementById){

  if(m!=0 && m==x){
   document.getElementById(m).style.display="none";
   m=0;
  }
  else{
   if(m!=0){
    document.getElementById(m).style.display="none";
   }
   document.getElementById(x).style.display="block";
   m=x;
  }
 }

 else if(document.all){
  if(m!=0 && m==x){
   document.all(m).style.display ="none";
   m=0;
  }
  else{
   if(m!=0){
    document.all(m).style.display = "none";
   }
   document.all(x).style.display = "block";
   m=x;
  }
 }
}
 Images = new Array();
    Images[0] = new Image();
    Images[1] = new Image();
    Images[2] = new Image();
    Images[3] = new Image();
    Images[4] = new Image();
    Images[5] = new Image();
    Images[6] = new Image();
    Images[7] = new Image();
    Images[8] = new Image();
    Images[9] = new Image();
    Images[10] = new Image();
    
    Images[0].src = "$imgpath/blank.gif";
    Images[1].src = "$imgpath/$Kimg[1].gif";
    Images[2].src = "$imgpath/$Kimg[2].gif";
    Images[3].src = "$imgpath/$Kimg[3].gif";
    Images[4].src = "$imgpath/$Kimg[4].gif";
    Images[5].src = "$imgpath/$Kimg[5].gif";
    Images[6].src = "$imgpath/$Kimg[6].gif";
    Images[7].src = "$imgpath/$Kimg[7].gif";
    Images[8].src = "$imgpath/$Kimg[8].gif";
    Images[9].src = "$imgpath/$Kimg[9].gif";
    Images[10].src = "$imgpath/$Kimg[10].gif";

    var i = 0

    if($Slev[1] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[2].gif";
	    Images[i+2].src = "$imgpath/$Kimg[3].gif";
	    Images[i+3].src = "$imgpath/$Kimg[4].gif";
	    Images[i+4].src = "$imgpath/$Kimg[5].gif";
	    Images[i+5].src = "$imgpath/$Kimg[6].gif";
	    Images[i+6].src = "$imgpath/$Kimg[7].gif";
	    Images[i+7].src = "$imgpath/$Kimg[8].gif";
	    Images[i+8].src = "$imgpath/$Kimg[9].gif";
	    Images[i+9].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    if($Slev[2] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[3].gif";
	    Images[i+2].src = "$imgpath/$Kimg[4].gif";
	    Images[i+3].src = "$imgpath/$Kimg[5].gif";
	    Images[i+4].src = "$imgpath/$Kimg[6].gif";
	    Images[i+5].src = "$imgpath/$Kimg[7].gif";
	    Images[i+6].src = "$imgpath/$Kimg[8].gif";
	    Images[i+7].src = "$imgpath/$Kimg[9].gif";
	    Images[i+8].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    if($Slev[3] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[4].gif";
	    Images[i+2].src = "$imgpath/$Kimg[5].gif";
	    Images[i+3].src = "$imgpath/$Kimg[6].gif";
	    Images[i+4].src = "$imgpath/$Kimg[7].gif";
	    Images[i+5].src = "$imgpath/$Kimg[8].gif";
	    Images[i+6].src = "$imgpath/$Kimg[9].gif";
	    Images[i+7].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    if($Slev[4] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[5].gif";
	    Images[i+2].src = "$imgpath/$Kimg[6].gif";
	    Images[i+3].src = "$imgpath/$Kimg[7].gif";
	    Images[i+4].src = "$imgpath/$Kimg[8].gif";
	    Images[i+5].src = "$imgpath/$Kimg[9].gif";
	    Images[i+6].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    if($Slev[5] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[6].gif";
	    Images[i+2].src = "$imgpath/$Kimg[7].gif";
	    Images[i+3].src = "$imgpath/$Kimg[8].gif";
	    Images[i+4].src = "$imgpath/$Kimg[9].gif";
	    Images[i+5].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    if($Slev[6] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[7].gif";
	    Images[i+2].src = "$imgpath/$Kimg[8].gif";
	    Images[i+3].src = "$imgpath/$Kimg[9].gif";
	    Images[i+4].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    if($Slev[7] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[8].gif";
	    Images[i+2].src = "$imgpath/$Kimg[9].gif";
	    Images[i+3].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    if($Slev[8] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[9].gif";
	    Images[i+2].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    if($Slev[9] < $haigoulevel){
	    Images[i+1].src = "$imgpath/$Kimg[10].gif";
    } else {
    	i = i+1
    }

    function change_img1() {
    form1.img1.src = Images[ form1.haigou1.selectedIndex ].src;
    }
    function change_img2() {
    form1.img2.src = Images[ form1.haigou2.selectedIndex ].src;
    }
  
 //--->
 </SCRIPT>
<FORM name=form1 ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【配合可能\のみ表\示\】</TD>
<TD bgcolor="#99ccff">ベース- 
<SELECT name=haigou1 onClick="change_img1()">
<option value=0 SELECTED>選 択</OPTION>
EOF
&hai;
print <<"EOF";
</SELECT>
<IMG NAME="img1" SRC="$imgpath/blank.gif">
<BR>
材 料-- 
<SELECT name=haigou2 onClick="change_img2()">
<option value=0 SELECTED>選 択</OPTION>
EOF
&hai;
print <<"EOF";
</SELECT> 
<IMG NAME="img2" SRC="$imgpath/blank.gif">

----
<INPUT type="submit" value="配合する"><BR>
<INPUT type="hidden" name="mode" value="haigou">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="money" value="$Kmoney">
<BR>
<img src="$imgpath/110.gif"> <A href="http://park16.wakwak.com/~mikio-palace/haigou.html" target=_blank>配合表\</a>だよ。よく考えて配合してね
</TD>
</TR>
</FORM>
<TR>
<TD colspan="2">
<HR size="5">
</TD>
</TR>
<TR>
<TD bgcolor="#000000" height="30" align="center"><FONT color="#ff0000" size="+1"><B>陰陽変換所</B></FONT></TD>
<TD bgcolor="#000000"><FONT color="#ffffff">陰陽変換料金はモンスターの【配合回数×100ゴールド】です。（上限は99999ゴー
ルド）</FONT></TD>
</TR>

<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【陰陽変換可能\のみ表\示\】</TD>
<TD bgcolor="#99ccff">
<SELECT name=seiten>
<option value="no">選 択</OPTION>
EOF
&hai2;
print <<"EOF";
</SELECT> 
<INPUT type="submit" value="陰陽変換する"><BR>
<INPUT type="hidden" name="mode" value="seitenkan">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="money" value="$Kmoney">
</TD>
</TR>
</FORM>
<TR>
<TD colspan="2">
<HR size="5">
</TD>
</TR>
<TR>
<TD bgcolor="#000000" height="30" align="center"><FONT color="#ff0000" size="+1"><B>お見合い所へ行く</B></FONT></TD>
<TD bgcolor="#000000"><FONT color="#ffffff">お見合いの相手を選択したり、お見合いの依頼状況を確認出来ます。</FONT></TD>
</TR>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
EOF
if($Aimg[2] == 0){
print <<"EOF";
<TD bgcolor="#99ccff" height="30">
【お見合い所】
EOF
}
if($Aimg[2] != 0){
print <<"EOF";
<TD bgcolor="white" height="30" align="center">
<IMG src="$imgpath/irai.gif">
EOF
}
print <<"EOF";
</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="入室する">
<INPUT type="hidden" name = "mode" value = "omiai">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
</FORM>
</TD>
</TR>
<TR>
<TD colspan="2">
<HR size="5">
<TR>
<TD bgcolor="#000000" height="30" align="center"><FONT color="#ff0000" size="+1"><B>ゲームの放棄</B></FONT></TD>
<TD bgcolor="#000000"><FONT color="#ffffff">ゲームを放棄する際にはご利用下さい。放棄後30日間は新規登録出来ません。
</FONT></TD>
</TR>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor="#99ccff" height="30">【ゲーム放棄】</TD>
<TD bgcolor="#99ccff">
<INPUT type="submit" value="放棄する">
<INPUT type="hidden" name = "mode" value = "delete1">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
</TD>
</TR>
</FORM>
</TBODY>
</TABLE>
</DIV>
<BR>
EOF
}

if($bbsmode == 1){

open(FH,"bbs/$inname.cgi") || &error("Can't open!");
@bbs1 = <FH>;
close(FH);
foreach $line (@bbs1) {
   ($bname[1],$bb[1],$bname[2],$bb[2],$bname[3],$bb[3],$bname[4],$bb[4],$bname[5],$bb[5],$bname[6],$bb[6],$bname[7],
$bb[7],$bname[8],$bb[8],$bname[9],$bb[9],$bname[10],$bb[10],$bname[11],$bb[11],$bname[12],$bb[12],$bname[13],$bb[13],
$bname[14],$bb[14],$bname[15],$bb[15])=split(/<>/,$line);
}
print <<"EOF";
<BR>
<HR size="5">
<CENTER>
<TABLE bgcolor="#000000" width="70%">
<TBODY>
<TR>
<TD bgcolor="#99ccff" align="center"><FONT color="red"><B>【注意】</B></FONT><FONT color="black"><B> </B>パスワードが
違うと書き込めません</FONT></TD>
</TR>
<TR>
<TD bgcolor="#99ccff" align="center">
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT size="20" type="text" name="bname" value="$bname">
<INPUT size="10" type="password" name="bpass" value="$bpass">
<INPUT type="hidden" name="type" value="$type">
<INPUT type="hidden" name="mode" value="bbsmode">
<INPUT type="hidden" name="kname" value="$Kname">
<INPUT type="submit"  value="書込み">
<BR>
<INPUT size="77" type="text" name="bbs">
</TD>
</TR>
</FORM>
EOF
if($Kname eq $bname){
print <<"EOF";
<TR>
<TD bgcolor="#99ccff" align="center" valign="top">
<FORM ACTION="$cgiurl" METHOD="POST">
<SELECT name=DEL>
<option value=0>選択</OPTION>
EOF
for($D=1;$D<11;$D++){
print <<"EOF";
<option value=$D>$D</OPTION>
EOF
}
print <<"EOF";
</SELECT>
<INPUT type="submit" value="削除"> 
<INPUT type="hidden" name="mode" value="bbsdel">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="bname" value="$bname">
<INPUT type="hidden" name="bpass" value="$bpass">
<INPUT type="hidden" name="type" value="$type">
<FONT color="black">オーナーのみが削除出来ます</FONT>
</TD>
</TR>
</FORM>
EOF
}
print <<"EOF";
</TBODY>
</TABLE>
EOF
#############################
if($type != 1){
print <<"EOF";
<BR>
<FORM ACTION="$cgiurl" METHOD="POST" target="_blank">
<FONT size="3pt"> 記帳したい人のBBSを開く</FONT>
<SELECT name=BBNAME>
EOF
open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line1 (@lines) {
    ($Sname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,
$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line1);
print "<option value=$Sname >$Sname\n";
}
print <<"EOF";
</SELECT>
<INPUT type="submit" value="BBS-OPEN">
<INPUT type="hidden" name="mode" value="bbs2">
<INPUT size="20" type="hidden" name="bname" value="$bname">
<INPUT size="10" type="hidden" name="bpass" value="$bpass">
<INPUT type="hidden" name="type" value="$type">
<INPUT type="hidden" name="kname" value="$Kname">
</FORM>
EOF
}
#############################
print <<"EOF";
<BR>
<TABLE border="0" bgcolor="#000000">
<TBODY>
EOF
for($B=1;$B<11;$B++){
print <<"EOF";
<TR>
<TD bgcolor="#ffffff" align="center"><B>$B</B></TD>
<TD bgcolor="#99ccff" width="100"><FONT color="black" size="3">$bname[$B]</FONT></TD>
<TD bgcolor="#99ccff" width="600"><FONT color="black" size="3">$bb[$B]</FONT></TD>
</TR>
EOF
}
print <<"EOF";
</TBODY>
</TABLE>
</CENTER>
EOF
}

print <<"EOF";
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="  TOP  ">
</FORM>
<CENTER>
EOF


&footer;



