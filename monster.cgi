#!C:/perl64/bin/perl

use utf8;
use open IO => ":utf8";
use open ":std";

require './set.cgi';
require './dat/kokoro.cgi';
require './dat/mlist.cgi';

if(open(FH,"dat/time2.cgi")){
$newt = <FH>;
close(FH);

if($newt ne ""){
$newt = $newt-time;
if($newt <= 0){
&turn;
}
}
}

############## 禁止IP 追加(2004.2.4) #################

local($match) = 0;
foreach (@noip) {
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) { $match=1; last; }
}
if ($match) {&error("あなたのIPアドレスはアクセス制限にかかってます");}

######################################################

&decode;

$emes = '不正なアクセスです';

if ($ENV{'REQUEST_METHOD'} ne "POST") {
if($FORM{'mode'} eq "change")   {  &error("$emes");}
if($FORM{'mode'} eq "turn")     {  &error("$emes");}
if($FORM{'mode'} eq "MGET")     {  &error("$emes");}
if($FORM{'mode'} eq "KGET")     {  &error("$emes");}
if($FORM{'mode'} eq "Mbye")     {  &error("$emes");}
if($FORM{'mode'} eq "medal")    {  &error("$emes");}
if($FORM{'mode'} eq "medal2")   { &error("$emes");}
if($FORM{'mode'} eq "medal3")   { &error("$emes");}
if($FORM{'mode'} eq "medal4")   { &error("$emes");}
if($FORM{'mode'} eq "medal5")   { &error("$emes");}
if($FORM{'mode'} eq "medal6")   { &error("$emes");}
if($FORM{'mode'} eq "medal7")   { &error("$emes");}
if($FORM{'mode'} eq "medalok")  {  &error("$emes");}
if($FORM{'mode'} eq "medalok2") { &error("$emes");}
if($FORM{'mode'} eq "medalok3") { &error("$emes");}
if($FORM{'mode'} eq "medalok4") { &error("$emes");}
if($FORM{'mode'} eq "medalok5") { &error("$emes");}
if($FORM{'mode'} eq "medalok6") { &error("$emes");}
if($FORM{'mode'} eq "medalok7") { &error("$emes");}
if($FORM{'mode'} eq "fight1")   {  &error("$emes");}
if($FORM{'mode'} eq "fight10")  {  &error("$emes");}
if($FORM{'mode'} eq "fight11")  {  &error("$emes");}
if($FORM{'mode'} eq "aite")     {  &error("$emes");}
if($FORM{'mode'} eq "check")    {  &error("$emes");}
if($FORM{'mode'} eq "check2")   {  &error("$emes");}
if($FORM{'mode'} eq "check3")   {  &error("$emes");}
if($FORM{'mode'} eq "haigou")   {  &error("$emes");}
if($FORM{'mode'} eq "hensin")   {  &error("$emes");}
if($FORM{'mode'} eq "yadoya")   {  &error("$emes");}
if($FORM{'mode'} eq "yadook")   {  &error("$emes");}
if($FORM{'mode'} eq "kyoukai")  {  &error("$emes");}
if($FORM{'mode'} eq "kyoukaiok"){  &error("$emes");}
if($FORM{'mode'} eq "seitenkan"){  &error("$emes");}
if($FORM{'mode'} eq "seitenok") {  &error("$emes");}
if($FORM{'mode'} eq "omiai")    {  &error("$emes");}
if($FORM{'mode'} eq "omisen")   {  &error("$emes");}
if($FORM{'mode'} eq "omik")     {  &error("$emes");}
if($FORM{'mode'} eq "seikou1")  {  &error("$emes");}
if($FORM{'mode'} eq "seikou2")  {  &error("$emes");}
if($FORM{'mode'} eq "fusei1")   {  &error("$emes");}
if($FORM{'mode'} eq "fusei2")   {  &error("$emes");}
if($FORM{'mode'} eq "omiyes")   {  &error("$emes");}
if($FORM{'mode'} eq "omino")    {  &error("$emes");}
if($FORM{'mode'} eq "books")    {  &error("$emes");}
if($FORM{'mode'} eq "readbook") {  &error("$emes");}
if($FORM{'mode'} eq "delete1")  {  &error("$emes");}
if($FORM{'mode'} eq "delete2")  {  &error("$emes");}
}

if($FORM{'mode'} eq "")            {  &start; exit; }
elsif($FORM{'mode'} eq "change")   {  &change; }
elsif($FORM{'mode'} eq "turn")     {  &turn; }
elsif($FORM{'mode'} eq "turnlog")  {  &turnlog; }
elsif($FORM{'mode'} eq "MGET")     {  &MGET; }
elsif($FORM{'mode'} eq "KGET")     {  &KGET; }
elsif($FORM{'mode'} eq "Mbye")     {  &Mbye; }
elsif($FORM{'mode'} eq "medal")    {  &medal;  }
elsif($FORM{'mode'} eq "medal2")   {  &medal2; }
elsif($FORM{'mode'} eq "medal3")   {  &medal3; }
elsif($FORM{'mode'} eq "medal4")   {  &medal4; }
elsif($FORM{'mode'} eq "medal5")   {  &medal5; }
elsif($FORM{'mode'} eq "medal6")   {  &medal6; }
elsif($FORM{'mode'} eq "medal7")   {  &medal7; }
elsif($FORM{'mode'} eq "medalok")  {  &medalok;  }
elsif($FORM{'mode'} eq "medalok2") {  &medalok2; }
elsif($FORM{'mode'} eq "medalok3") {  &medalok3; }
elsif($FORM{'mode'} eq "medalok4") {  &medalok4; }
elsif($FORM{'mode'} eq "medalok5") {  &medalok5; }
elsif($FORM{'mode'} eq "medalok6") {  &medalok6; }
elsif($FORM{'mode'} eq "medalok7") {  &medalok7; }
elsif($FORM{'mode'} eq "fight1")   {  &fight1; }
elsif($FORM{'mode'} eq "fight10")  {  &fight10; }
elsif($FORM{'mode'} eq "fight11")  {  &fight11; }
elsif($FORM{'mode'} eq "login")    {  &login; }
elsif($FORM{'mode'} eq "logout")   {  &logout; }
elsif($FORM{'mode'} eq "bbsmode")  {  &bbsmode; }
elsif($FORM{'mode'} eq "bbs2")     {  &bbs2; }
elsif($FORM{'mode'} eq "bbs3")     {  &bbs3; }
elsif($FORM{'mode'} eq "bbsdel")   {  &bbsdel; }
elsif($FORM{'mode'} eq "aite")     {  &aite; }
elsif($FORM{'mode'} eq "check")    {  &check; }
elsif($FORM{'mode'} eq "check2")   {  &check2; }
elsif($FORM{'mode'} eq "check3")   {  &check3; }
elsif($FORM{'mode'} eq "haigou")   {  &haigou; }
elsif($FORM{'mode'} eq "comment")  {  &comment; }
elsif($FORM{'mode'} eq "hensin")   {  &hensin; }
elsif($FORM{'mode'} eq "yadoya")   {  &yadoya;}
elsif($FORM{'mode'} eq "yadook")   {  &yadook;}
elsif($FORM{'mode'} eq "kyoukai")  {  &kyoukai;}
elsif($FORM{'mode'} eq "kyoukaiok"){  &kyoukaiok;}
elsif($FORM{'mode'} eq "seitenkan"){  &seitenkan;}
elsif($FORM{'mode'} eq "seitenok") {  &seitenok;}
elsif($FORM{'mode'} eq "omiai" )   {  &omiai;}
elsif($FORM{'mode'} eq "omisen" )  {  &omisen;}
elsif($FORM{'mode'} eq "omik" )    {  &omik;}
elsif($FORM{'mode'} eq "seikou1")  {  &seikou1;}
elsif($FORM{'mode'} eq "seikou2")  {  &seikou2;}
elsif($FORM{'mode'} eq "fusei1")   {  &fusei1;}
elsif($FORM{'mode'} eq "fusei2")   {  &fusei2;}
elsif($FORM{'mode'} eq "omiyes")   {  &omiyes;}
elsif($FORM{'mode'} eq "omino")    {  &omino;}
elsif($FORM{'mode'} eq "kakunin")  {  &kakunin;}
elsif($FORM{'mode'} eq "books")    {  &books;}
elsif($FORM{'mode'} eq "readbook") {  &readbook;}
elsif($FORM{'mode'} eq "delete1")  {  &delete1;}
elsif($FORM{'mode'} eq "delete2")  {  &delete2;}

#=============#
#  START画面  #
#=============#

sub start {

$menu = $FORM{'menu'};

if($menu eq ""){$mode = 0;}
if($menu ne ""){$mode = 1;}

$ii = 0;

open(FH,"${datadir}/$countdata");
$sou = <FH>;
close(FH);

open(FH,"dat/time2.cgi");
$newt2 = <FH>;
close(FH);

($secg2,$ming2,$hourg2,$mdayg2,$mong2,$yearg2,$wdayg2,$ydayg2,$isdstg2) = localtime($newt2);
$mong2++;
$newt2 = $newt2 - time;

&header;
&get_cookie;

print <<"EOF";
<TABLE width="100%" bgcolor="#ff00ff">
  <TBODY>
    <TR>
      <TD bgcolor="#660066"><FONT color="#FFFFFF"><B>[ <A href="$homepage">$home_title</A> ] [ <A href="http:/park16.wakwak.com/~mikio-palace/mon176.html" target="_blank">PLAYMANUAL</A> ] [ <A href="$bbs" target="_blank">BBS</A> ]
      [ <A href="http:/park16.wakwak.com/~mikio-palace/haigou.html" target="_blank">配合表\</A> ] [ <A href="$cgipath/$kanrim" target="_blank">管理モード</A> ] [ <A href="$cgipath/$ncook" target="_blank"><font color=red>画像設定</font></A> ]</B></FONT></TD>
      <TD bgcolor="#660066" align="center"><FONT size="+2" color="#FFFFFF"><B>MONSTER'S</B></FONT><FONT size="+2"><B> </B></FONT><FONT size="+1" color="#FF0000"><B>$ver</B></FONT></TD>
</TR>
</TBODY>
</TABLE>
<TABLE>
<TBODY>
<TR>
<TD><FONT color="#000000"><B><FONT color="#000000"><BR>
参加数は【最高<FONT color="red">$sankaMAX</FONT><FONT color="#000000">人で現在</FONT><FONT color="red">$sou</FONT>人】です!</FONT>戦闘を行うと<FONT color="red">$nexpplay</FONT>分後にしか戦闘が出来ません。<BR>
配合レベルは</B></FONT><FONT color="#FF0000"><B>$haigoulevel</B></FONT><FONT color="#000000"><B>の設定です。次のメダル獲得杯は<FONT color="red">$mong2</FONT>月<FONT color=red>$mdayg2</FONT>日で出場権利は<FONT color="red">16</FONT>位までの人です。</B></FONT><BR>
<BR>
<TABLE>
<TBODY>
<TR>
<TD>
<FORM name="RemainForm"><INPUT name="RemainTime" size="35" type="text" readonly></FORM>
<SCRIPT language="JavaScript">
<!--
nextTurn = $newt2; loadDate = new Date();
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
return "次のメダル獲得杯まで " + hour + ":" + min + ":" + sec;}
/-->
</SCRIPT>
</TD>
<TD valign="top">
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="前大会の結果">
<INPUT TYPE="hidden" NAME="mode" VALUE="turnlog">
</FORM>
</TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD valign="top">
<BR>
<TABLE bgcolor="#000000">
<TBODY>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD><FONT color="#FFFFFF"><B>USER-ID</B></FONT></TD>
<TD><INPUT type="text" size="14" name="name" value="$Yname"></TD>
</TR>
<TR>
<TD><FONT color="#FFFFFF"><B>PASSWORD</B></FONT></TD>
<TD><INPUT type="password" size="14" name="password" value="$Ypass"></TD>
</TR>
<TR>
<TD></TD>
<TD><INPUT type="submit" value="LOGIN"></TD>
<INPUT type="hidden" name="mode" value="login">
</FORM>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
</TBODY>
</TABLE>
<HR size="5">
<TABLE>
<TBODY>
<TR>
<TD valign="middle" width="562"><FONT color="#000000"><B>初めての方は</B></FONT><FONT color="#FFFF00"><B>NEWGAME</B></FONT><FONT color="#000000"><B>から参加してください。</B></FONT><FONT color="#000000"><B>登録後はLOGINからお願いします。</B></FONT></TD>
EOF
if($sou < $sankaMAX){
print <<"EOF";
<TD align="center" bgcolor="#000000" width="98" height="30">
<B><FONT color="#FFFFFF" size="+1"><FONT color="#FFFFFF"><A href="$cgipath/$newurl">NEWGAME</FONT></TD>
EOF
}
if($sou >= $sankaMAX){
print <<"EOF";
<TD height="21" align="center" bgcolor="#000000">
<font color=white>登録数が最大です</font></TD>
EOF
}
print <<"EOF";
</TR>
</TBODY>
</TABLE>
<BR>
EOF

if($mode == 0){

if($sou <= $maxshow){$hyouzi = $sou;}
if($sou > $maxshow){
$MAX = $maxshow+1;
$hyouzi = $maxshow;
print <<"EOF";
<TD valign="top">
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="$MAX位以降">
<INPUT TYPE="hidden" NAME="mode" VALUE="">
<INPUT TYPE="hidden" NAME="menu" VALUE="1">
</FORM>
</TD>
<BR>
EOF
}
print <<"EOF";
<TABLE width="100%" bgcolor="#ff00ff">
<TBODY>
<TR>
<TD bgcolor="#660066"><B><FONT size="+2" color="#FFFFFF">RANKING [1位～$hyouzi位]</FONT></B></TD>
</TR>
</TBODY>
</TABLE>
EOF
}

if($mode == 1){
$hyouzi = $maxshow+1;
print <<"EOF";
</TR>
</TBODY>
</TABLE>
<BR>
<TD valign="top">
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="1位～$maxshow位">
<INPUT TYPE="hidden" NAME="mode" VALUE="">
<INPUT TYPE="hidden" NAME="menu" VALUE="">
</FORM>
</TD>
<BR>
<TABLE width="100%" bgcolor="#ff00ff">
<TBODY>
<TR>
<TD bgcolor="#660066"><B><FONT size="+2" color="#FFFFFF">RANKING [$hyouzi位～$sou位]</FONT></B></TD>
</TR>
</TBODY>
</TABLE>
EOF

}

open(FH,"${datadir}/$userdata");
@lines = <FH>;
close(FH);
print <<"EOF";
<BR>
<BR>
<DIV align="center">
<TABLE border="0" bgcolor="black" class="table-css">
<TBODY>
<TR>
<TH align="center" nowrap="nowrap" bgcolor="black"><FONT color="#FFFFFF">Rank</FONT></TH>
<TH align="center" nowrap="nowrap" bgcolor="#0000cc" ><FONT color="#FFFFFF">User</FONT></TH>
<TH align="center" nowrap="nowrap" bgcolor="#0000cc" colspan="6"><FONT color="#FFFFFF">手持ち</FONT></TH>
</TR>
EOF

if($mode == 0){

foreach $line (@lines) {
    ($Yyname,$Yypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
if ($ii >= $maxshow){last;} 
$ii++;
if($Yplay <= time){
$good = '<font color="#00FFCC"><FONT face="Times New Roman">O K!</FONT>';}
else {
$good = '<font color="#FF0066"><FONT face="Times New Roman">N O!</FONT>';}
$timelog = 1;
&gettime;
$delday = $mday;
print <<"EOF";
<TR>
<TH align="center" nowrap="nowrap" rowspan="3" bgcolor="#CC00CC"><FONT color="#FFFFFF" size="4p">$ii</FONT></TH>
<TH align=right nowrap=nowrap bgcolor="blue" rowspan="2">
<FONT color = white><FONT size=2>ユーザー名：</FONT></FONT><A HREF="$cgiurl?mode=login&name=$Yyname&type=1&bname=$Yname&bpass=$Ypass" target="_blank"><FONT size="4p">$Yyname</A></FONT><BR>
<FONT color = white><FONT size=2>最深部：</FONT></FONT><FONT color = white>地下<FONT color = red>$Ykey</font>階<FONT><BR>
<FONT color = white><FONT size=2>所持金：</FONT></FONT><FONT color = white>$Ymoneyゴールド<FONT><BR>
<FONT color = white><FONT size=2>おみあい状況：</FONT></FONT><A HREF="$cgiurl?mode=kakunin&name=$Yyname" target="_blank"><FONT>確認</A></FONT><BR>
<FONT color = white><FONT size=2>戦闘：</FONT></FONT>$good<BR>
<FONT color = white><FONT size=2>データ保存期間：</FONT></FONT>あと$delday日<BR>
</TH>
<TH align=center valign=bottom nowrap=nowrap bgcolor="#ffffff" height="40"  valign="bottom" colspan="2" rowspan="2">
<IMG src="$imgpath/$Yimg1.gif" border="0"><BR>
<FONT size = 2>$itemlist[$Yimg1] Lv<FONT color = red>$Ylev1</FONT></FONT><BR>
<FONT size = 2>配合<FONT color = red>$Yhai1</FONT>回</FONT></FONT><BR>
</TH>
<TH align=center valign=bottom nowrap=nowrap bgcolor="#ffffff" height="40"  valign="bottom" colspan="2" rowspan="2">
<IMG src="$imgpath/$Yimg2.gif" border="0"><BR>
<FONT size = 2>$itemlist[$Yimg2] Lv<FONT color = red>$Ylev2</FONT></FONT><BR>
<FONT size = 2>配合<FONT color = red>$Yhai2</FONT>回</FONT></FONT><BR>
</TH>
<TH align=center valign=bottom nowrap=nowrap bgcolor="#ffffff" height="40"  valign="bottom" colspan="2" rowspan="2"> 
<IMG src="$imgpath/$Yimg3.gif" border="0"><BR>
<FONT size = 2>$itemlist[$Yimg3] Lv<FONT color = red>$Ylev3</FONT></FONT><BR>
<FONT size = 2>配合<FONT color = red>$Yhai3</FONT>回</FONT></FONT><BR>
</TH>
</TR>
<TR>
</TR>
<TR>
<TH bgcolor="#0000cc"><FONT color="#FFFFFF">COMMENT</FONT></TH>
<TH colspan="6" align="left" bgcolor="#ffffff">  $Ymes</TH>
</TR>
EOF
}
}

if($mode == 1){

foreach $line (@lines) {
    ($Yyname,$Yypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
$ii++;
if($ii > $maxshow){
if($Yplay <= time){
$good = '<font color="#00FFCC"><FONT face="Times New Roman">O K!</FONT>';}
else {
$good = '<font color="#FF0066"><FONT face="Times New Roman">N O!</FONT>';}
$timelog = 1;
&gettime;
$delday = $mday;
print <<"EOF";
<TR>
<TH align="center" nowrap="nowrap" rowspan="3" bgcolor="#CC00CC"><FONT color="#FFFFFF" size="4p">$ii</FONT></TH>
<TH align=right nowrap=nowrap bgcolor="blue" rowspan="2">
<FONT color = white><FONT size=2>ユーザー名：</FONT></FONT><A HREF="$cgiurl?mode=login&name=$Yyname&type=1&bname=$Yname&bpass=$Ypass" target="_blank"><FONT size="4p">$Yyname</A></FONT><BR>
<FONT color = white><FONT size=2>最深部：</FONT></FONT><FONT color = white>地下<FONT color = red>$Ykey</font>階<FONT><BR>
<FONT color = white><FONT size=2>所持金：</FONT></FONT><FONT color = white>$Ymoneyゴールド<FONT><BR>
<FONT color = white><FONT size=2>おみあい状況：</FONT></FONT><A HREF="$cgiurl?mode=kakunin&name=$Yyname" target="_blank"><FONT>確認</A></FONT><BR>
<FONT color = white><FONT size=2>戦闘：</FONT></FONT>$good<BR>
<FONT color = white><FONT size=2>データ保存期間：</FONT></FONT>あと$delday日<BR>
</TH>
<TH align=center valign=bottom nowrap=nowrap bgcolor="#ffffff" height="40"  valign="bottom" colspan="2" rowspan="2">
<IMG src="$imgpath/$Yimg1.gif" border="0"><BR>
<FONT size = 2>$itemlist[$Yimg1] Lv<FONT color = red>$Ylev1</FONT></FONT><BR>
<FONT size = 2>配合<FONT color = red>$Yhai1</FONT>回</FONT></FONT><BR>
</TH>
<TH align=center valign=bottom nowrap=nowrap bgcolor="#ffffff" height="40"  valign="bottom" colspan="2" rowspan="2">
<IMG src="$imgpath/$Yimg2.gif" border="0"><BR>
<FONT size = 2>$itemlist[$Yimg2] Lv<FONT color = red>$Ylev2</FONT></FONT><BR>
<FONT size = 2>配合<FONT color = red>$Yhai2</FONT>回</FONT></FONT><BR>
</TH>
<TH align=center valign=bottom nowrap=nowrap bgcolor="#ffffff" height="40"  valign="bottom" colspan="2" rowspan="2"> 
<IMG src="$imgpath/$Yimg3.gif" border="0"><BR>
<FONT size = 2>$itemlist[$Yimg3] Lv<FONT color = red>$Ylev3</FONT></FONT><BR>
<FONT size = 2>配合<FONT color = red>$Yhai3</FONT>回</FONT></FONT><BR>
</TH>
</TR>
<TR>
</TR>
<TR>
<TH bgcolor="#0000cc"><FONT color="#FFFFFF">COMMENT</FONT></TH>
<TH colspan="6" align="left" bgcolor="#ffffff">  $Ymes</TH>
</TR>
EOF
}
}
}

print <<"EOF";
</TBODY>
</TABLE>
</DIV>
EOF

&footer2;

}

#==============#
#  お見合い所  #
#==============#

sub omiai {
require './cgi/omiai.cgi';
}

sub omisen {
require './cgi/omisen.cgi';
}

sub omik {
require './cgi/omik.cgi';
}

sub  seikou1 {
require './cgi/seikou1.cgi';
}

sub  seikou2 {
require './cgi/seikou2.cgi';
}

sub  fusei1 {
require './cgi/fusei1.cgi';
}

sub  fusei2 {
require './cgi/fusei2.cgi';
}

sub  omiyes {
require './cgi/omiyes.cgi';
}

sub  omino {
require './cgi/omino.cgi';
}

sub  kakunin {
require './cgi/kakunin.cgi';
}

#====================#
#  メダル獲得杯処理  #
#====================#

sub turn {

require './cgi/turn.cgi';

}

sub turnlog {

require './dat/turnlog.cgi';

}

#================#
#  放棄コマンド  #
#================#

sub delete1 {

require './cgi/delete1.cgi';

}

sub delete2 {

require './cgi/delete2.cgi';

}

#============#
#  本屋さん  #
#============#

sub books {

require './cgi/books.cgi';

}

sub readbook {

require './cgi/readbook.cgi';

}

#========#
#  戦闘  #
#========#

sub aite {

require './cgi/aite.cgi';

}

sub check{

$monsuu = $FORM{'monsuu'};
$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$Aimg1  = $FORM{'Aimg1'};
$Aimg2  = $FORM{'Aimg2'};
$Aimg3  = $FORM{'Aimg3'};
$inkai  = $FORM{'kai'};
$Iii    = $FORM{'rank'};
$Ssu    = $FORM{'Ssu'};
$hit1   = $FORM{'hit1'};
$teki1  = $FORM{'teki1'};
$toku1  = $FORM{'toku1'};
$nakama1= $FORM{'nakama1'};
$ktoku1 = $FORM{'ktoku1'};
$hit2   = $FORM{'hit2'};
$teki2  = $FORM{'teki2'};
$toku2  = $FORM{'toku2'};
$nakama2= $FORM{'nakama2'};
$ktoku2 = $FORM{'ktoku2'};
$hit3   = $FORM{'hit3'};
$teki3  = $FORM{'teki3'};
$toku3  = $FORM{'toku3'};
$nakama3= $FORM{'nakama3'};
$ktoku3 = $FORM{'ktoku3'};

require './dat/data.cgi';
require './cgi/fight/fight1.cgi';
}

#######################################

sub check2{

$monsuu = $FORM{'monsuu'};
$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$Aimg1  = $FORM{'Aimg1'};
$inkai  = $FORM{'kai'};
$Iii    = $FORM{'rank'};
$Ssu    = $FORM{'Ssu'};
$hit1   = $FORM{'hit1'};
$teki1  = $FORM{'teki1'};
$toku1  = $FORM{'toku1'};
$nakama1= $FORM{'nakama1'};
$ktoku1 = $FORM{'ktoku1'};

require './dat/data.cgi';
require './cgi/fight/fight10.cgi';

}

sub check3{

$monsuu = $FORM{'monsuu'};
$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$Aimg1  = $FORM{'Aimg1'};
$inkai  = $FORM{'kai'};
$Iii    = $FORM{'rank'};
$Ssu    = $FORM{'Ssu'};
$hit1   = $FORM{'hit1'};
$teki1  = $FORM{'teki1'};
$toku1  = $FORM{'toku1'};
$nakama1= $FORM{'nakama1'};
$ktoku1 = $FORM{'ktoku1'};

require './dat/data.cgi';
require './cgi/fight/fight11.cgi';

}

#######################################

sub fight1 {
require './dat/data.cgi';
require './cgi/fight/fight1.cgi';
}
sub fight10 {
require './dat/data.cgi';
require './cgi/fight/fight10.cgi';
}
sub fight11 {
require './dat/data.cgi';
require './cgi/fight/fight11.cgi';
}
sub MGET {
require './cgi/mget.cgi';
}
sub KGET {
require './cgi/kget.cgi';
}
sub Mbye {
require './cgi/mbye.cgi';
}

#=============#
#  LOGIN画面  #
#=============#

sub login {
require './cgi/login.cgi';
}

sub change {
require './cgi/change.cgi';
}

sub logout {

$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$bname = $FORM{'name'};
$bpass = $FORM{'password'};
$type = $FORM{'type'};

$now = time;

&lock;
open(FH,">dat/time3.cgi");
print FH "0<>noname<>$now";
close(FH);
&unlock;

login;

}

#=============#
#  BBSモード  #
#=============#

sub bbsmode {
require './cgi/bbs.cgi';
}

sub bbs2 {
require './cgi/bbs2.cgi';
}

sub bbs3 {
require './cgi/bbs3.cgi';
}

sub bbsdel {
require './cgi/bbsdel.cgi';
}

#========#
#  配合  #
#========#

sub haigou {
require './cgi/haigou.cgi';
}

sub hensin {
require './cgi/hensin.cgi';
}

#============#
#メダル交換所#
#============#

sub medal {

require './cgi/medal.cgi';

}
sub medal2 {

require './cgi/medal2.cgi';

}
sub medal3 {

require './cgi/medal3.cgi';

}
sub medal4 {

require './cgi/medal4.cgi';

}
sub medal5 {

require './cgi/medal5.cgi';

}
sub medal6 {

require './cgi/medal6.cgi';

}
sub medal7 {

require './cgi/medal7.cgi';

}

#==============#
# メダル交換所 #
#==============#

sub medalok {

require './cgi/medalok.cgi';

}
sub medalok2 {

require './cgi/medalok2.cgi';

}
sub medalok3 {

require './cgi/medalok3.cgi';

}
sub medalok4 {

require './cgi/medalok4.cgi';

}
sub medalok5 {

require './cgi/medalok5.cgi';

}
sub medalok6 {

require './cgi/medalok6.cgi';

}
sub medalok7 {

require './cgi/medalok7.cgi';

}

#==========#
# 宿屋開始 #
#==========#

sub yadoya {

require './cgi/yadoya.cgi';

}

#==========#
# 宿屋終了 #
#==========#

sub yadook {

require './cgi/yadook.cgi';

}

#==========#
# 性転換所 #
#==========#

sub seitenkan {

require './cgi/seitenkan.cgi';

}

#==========#
# 性転終了 #
#==========#

sub seitenok {

require './cgi/seitenok.cgi';

}

#==========#
# 教会開始 #
#==========#

sub kyoukai {

require './cgi/kyoukai.cgi';

}

#==========#
# 教会終了 #
#==========#

sub kyoukaiok {

require './cgi/kyoukaiok.cgi';

}

#================#
#  コメント更新  #
#================#

sub comment {

require './cgi/comment.cgi';

}

#==============#
# 新規登録開始 #
#==============#

sub newgame {

require './cgi/newgame.cgi';

}

#==============#
#  NEW-GAME用  #
#==============#

sub makeNEW {

require './cgi/makenew.cgi';

}

#================#
#  新規登録完了  #
#================#

sub sinki {

require './cgi/sinki.cgi';

}


#====================#
#  メダル杯初期時間  #
#====================#

sub timesyori{

($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = localtime(time);
$yearg += 1900;
$mong++;

if($mdayg >= 1 && $mdayg <= 10 && E != 1){
$day = 11;
$mon = $mong;
$year= $yearg;
$E   = 1;
}
if($mdayg >= 11 && $mdayg <= 20 && E != 1){
$day = 21;
$mon = $mong;
$year= $yearg;
$E   = 1;
}
if($mdayg >= 21 && $mdayg <= 31 && E != 1){
$day = 1;
$mon = $mong +1;
$year= $yearg;
if($mon == 13){
$mon = 1;
$year++;
$E   = 1;
}
}
$year -=1900;
$mon -=1;

use Time::Local;
$time2 = timelocal(0,0,0,$day,$mon,$year); 
open(FH, ">dat/time2.cgi") ;
print FH $time2;
close(FH);

}

