use utf8;
use open IO => ":utf8";
use open ":std";

$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$BBNAME   = $FORM{'BBNAME'};

open(FH,"dat/time3.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($login,$name,$otime) = split(/<>/,$line);
}

if($name ne $inname){&error("お見合い所入室タイムオーバーです");}

&lock;

if($BBNAME eq non){

open(FH,"omiai/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);}

if($Kimg[1] == 0){&error("お見合いの設定はされていません");}
if($Fimg[1] != 0 && $Fimg[2] != 0){&error("先にお見合い不成立のモンスターをLOGIN画面に戻して下さい");}

$Vname = $Aname[1];

open(FH,"omiai/$Vname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);}

if($Fimg[1] != 0 && $Fimg[2] != 0){&error("$Vnameさんのお見合い不成立のモンスターがLOGIN画面に戻るまで解除出来ません");}

if($Fimg[1] == 0){
$newline = "$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Aname[1]<>$Alev[1]<>$Amlev[1]<>$Aimg[1]<>$Ahp[1]<>$Amhp[1]<>$Amp[1]<>$Ammp[1]<>$Akou[1]<>$Amam[1]<>$Asub[1]<>$Ahai[1]<>$Acount[1]<>$Anecount[1]<>$Asex[1]<>$Asei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";
}

if($Fimg[1] != 0 && $Fimg[2] == 0){
$newline = "$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Aname[1]<>$Alev[1]<>$Amlev[1]<>$Aimg[1]<>$Ahp[1]<>$Amhp[1]<>$Amp[1]<>$Ammp[1]<>$Akou[1]<>$Amam[1]<>$Asub[1]<>$Ahai[1]<>$Acount[1]<>$Anecount[1]<>$Asex[1]<>$Asei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[1]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]";
}


open(FH, ">omiai/$Vname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);


open(FH,"omiai/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);}


if($Fimg[1] == 0){
$newline = "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Aname[2]<>$Alev[2]<>$Amlev[2]<>$Aimg[2]<>$Ahp[2]<>$Amhp[2]<>$Amp[2]<>$Ammp[2]<>$Akou[2]<>$Amam[2]<>$Asub[2]<>$Ahai[2]<>$Acount[2]<>$Anecount[2]<>$Asex[2]<>$Asei[2]<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";
}

if($Fimg[1] != 0 && $Fimg[2] == 0){
$newline = "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Aname[2]<>$Alev[2]<>$Amlev[2]<>$Aimg[2]<>$Ahp[2]<>$Amhp[2]<>$Amp[2]<>$Ammp[2]<>$Akou[2]<>$Amam[2]<>$Asub[2]<>$Ahai[2]<>$Acount[2]<>$Anecount[2]<>$Asex[2]<>$Asei[2]<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[1]<>$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Fsei[1]";
}

open(FH, ">omiai/$inname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>設定を解除しました</B>
</FONT>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="LOGINへ">
</FORM>
<BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOPへ">
</FORM>
</CENTER>
EOF
}

if($BBNAME ne non){

if($BBNAME eq $inname){&error("設定が自分になってます");}

open(FH,"omiai/$BBNAME.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);}

if($Kimg[2] != 0){&error("$BBNAMEさんのモンスターは順番待ちです");}

sub hai3 {

open(FH,"${datadir}/$inname.cgi") || &error("Can't open open3");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Kname,$Kpass,$Klev1,$Kmlev1,$Kimg1,$Khp1,$Kmhp1,$Kmp1,$Kmmp1,$Kkou1,$Kmam1,$Ksub1,$Khai1,$Kcount1,$Knecount1,$Ksex1,$Ksei1,$Klev2,$Kmlev2,$Kimg2,$Khp2,$Kmhp2,$Kmp2,$Kmmp2,$Kkou2,$Kmam2,$Ksub2,$Khai2,$Kcount2,$Knecount2,$Ksex2,$Ksei2,$Klev3,$Kmlev3,$Kimg3,$Khp3,$Kmhp3,$Kmp3,$Kmmp3,$Kkou3,$Kmam3,$Ksub3,$Khai3,$Kcount3,$Knecount3,$Ksex3,$Ksei3,$Klev4,$Kmlev4,$Kimg4,$Khp4,$Kmhp4,$Kmp4,$Kmmp4,$Kkou4,$Kmam4,$Ksub4,$Khai4,$Kcount4,$Knecount4,$Ksex4,$Ksei4,$Klev5,$Kmlev5,$Kimg5,$Khp5,$Kmhp5,$Kmp5,$Kmmp5,$Kkou5,$Kmam5,$Ksub5,$Khai5,$Kcount5,$Knecount5,$Ksex5,$Ksei5,$Klev6,$Kmlev6,$Kimg6,$Khp6,$Kmhp6,$Kmp6,$Kmmp6,$Kkou6,$Kmam6,$Ksub6,$Khai6,$Kcount6,$Knecount6,$Ksex6,$Ksei6,$Klev7,$Kmlev7,$Kimg7,$Khp7,$Kmhp7,$Kmp7,$Kmmp7,$Kkou7,$Kmam7,$Ksub7,$Khai7,$Kcount7,$Knecount7,$Ksex7,$Ksei7,$Klev8,$Kmlev8,$Kimg8,$Khp8,$Kmhp8,$Kmp8,$Kmmp8,$Kkou8,$Kmam8,$Ksub8,$Khai8,$Kcount8,$Knecount8,$Ksex8,$Ksei8,$Klev9,$Kmlev9,$Kimg9,$Khp9,$Kmhp9,$Kmp9,$Kmmp9,$Kkou9,$Kmam9,$Ksub9,$Khai9,$Kcount9,$Knecount9,$Ksex9,$Ksei9,$Klev10,$Kmlev10,$Kimg10,$Khp10,$Kmhp10,$Kmp10,$Kmmp10,$Kkou10,$Kmam10,$Ksub10,$Khai10,$Kcount10,$Knecount10,$Ksex10,$Ksei10,$Kdummy,$Kkey,$Kmoney) = split(/<>/,$line);}

if($Kimg4 != 0){
print <<"EOF";
<option value=4 >$itemlist[$Kimg4] $seibetu[$Ksex4] LEVEL-$Klev4 【$seikaku[$Ksei4]】</OPTION>
EOF
}
if($Kimg5 != 0){
print <<"EOF";
<option value=5 >$itemlist[$Kimg5] $seibetu[$Ksex5] LEVEL-$Klev5 【$seikaku[$Ksei5]】</OPTION>
EOF
}
if($Kimg6 != 0){
print <<"EOF";
<option value=6 >$itemlist[$Kimg6] $seibetu[$Ksex6] LEVEL-$Klev6 【$seikaku[$Ksei6]】</OPTION>
EOF
}
if($Kimg7 != 0){
print <<"EOF";
<option value=7 >$itemlist[$Kimg7] $seibetu[$Ksex7] LEVEL-$Klev7 【$seikaku[$Ksei7]】</OPTION>
EOF
}
if($Kimg8 != 0){
print <<"EOF";
<option value=8 >$itemlist[$Kimg8] $seibetu[$Ksex8] LEVEL-$Klev8 【$seikaku[$Ksei8]】</OPTION>
EOF
}
if($Kimg9 != 0){
print <<"EOF";
<option value=9 >$itemlist[$Kimg9] $seibetu[$Ksex9] LEVEL-$Klev9 【$seikaku[$Ksei9]】</OPTION>
EOF
}
if($Kimg10 != 0){
print <<"EOF";
<option value=10 >$itemlist[$Kimg10] $seibetu[$Ksex10] LEVEL-$Klev10 【$seikaku[$Ksei10]】</OPTION>
EOF
}
}

sub hai4 {

open(FH,"${datadir}/$BBNAME.cgi") || &error("Can't open open3");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Kname,$Kpass,$Klev1,$Kmlev1,$Kimg1,$Khp1,$Kmhp1,$Kmp1,$Kmmp1,$Kkou1,$Kmam1,$Ksub1,$Khai1,$Kcount1,$Knecount1,$Ksex1,$Ksei1,$Klev2,$Kmlev2,$Kimg2,$Khp2,$Kmhp2,$Kmp2,$Kmmp2,$Kkou2,$Kmam2,$Ksub2,$Khai2,$Kcount2,$Knecount2,$Ksex2,$Ksei2,$Klev3,$Kmlev3,$Kimg3,$Khp3,$Kmhp3,$Kmp3,$Kmmp3,$Kkou3,$Kmam3,$Ksub3,$Khai3,$Kcount3,$Knecount3,$Ksex3,$Ksei3,$Klev4,$Kmlev4,$Kimg4,$Khp4,$Kmhp4,$Kmp4,$Kmmp4,$Kkou4,$Kmam4,$Ksub4,$Khai4,$Kcount4,$Knecount4,$Ksex4,$Ksei4,$Klev5,$Kmlev5,$Kimg5,$Khp5,$Kmhp5,$Kmp5,$Kmmp5,$Kkou5,$Kmam5,$Ksub5,$Khai5,$Kcount5,$Knecount5,$Ksex5,$Ksei5,$Klev6,$Kmlev6,$Kimg6,$Khp6,$Kmhp6,$Kmp6,$Kmmp6,$Kkou6,$Kmam6,$Ksub6,$Khai6,$Kcount6,$Knecount6,$Ksex6,$Ksei6,$Klev7,$Kmlev7,$Kimg7,$Khp7,$Kmhp7,$Kmp7,$Kmmp7,$Kkou7,$Kmam7,$Ksub7,$Khai7,$Kcount7,$Knecount7,$Ksex7,$Ksei7,$Klev8,$Kmlev8,$Kimg8,$Khp8,$Kmhp8,$Kmp8,$Kmmp8,$Kkou8,$Kmam8,$Ksub8,$Khai8,$Kcount8,$Knecount8,$Ksex8,$Ksei8,$Klev9,$Kmlev9,$Kimg9,$Khp9,$Kmhp9,$Kmp9,$Kmmp9,$Kkou9,$Kmam9,$Ksub9,$Khai9,$Kcount9,$Knecount9,$Ksex9,$Ksei9,$Klev10,$Kmlev10,$Kimg10,$Khp10,$Kmhp10,$Kmp10,$Kmmp10,$Kkou10,$Kmam10,$Ksub10,$Khai10,$Kcount10,$Knecount10,$Ksex10,$Ksei10,$Kdummy,$Kkey,$Kmoney) = split(/<>/,$line);}

if($Kimg4 != 0){
print <<"EOF";
<option value=4 >$itemlist[$Kimg4] $seibetu[$Ksex4] LEVEL-$Klev4 【$seikaku[$Ksei4]】</OPTION>
EOF
}
if($Kimg5 != 0){
print <<"EOF";
<option value=5 >$itemlist[$Kimg5] $seibetu[$Ksex5] LEVEL-$Klev5 【$seikaku[$Ksei5]】</OPTION>
EOF
}
if($Kimg6 != 0){
print <<"EOF";
<option value=6 >$itemlist[$Kimg6] $seibetu[$Ksex6] LEVEL-$Klev6 【$seikaku[$Ksei6]】</OPTION>
EOF
}
if($Kimg7 != 0){
print <<"EOF";
<option value=7 >$itemlist[$Kimg7] $seibetu[$Ksex7] LEVEL-$Klev7 【$seikaku[$Ksei7]】</OPTION>
EOF
}
if($Kimg8 != 0){
print <<"EOF";
<option value=8 >$itemlist[$Kimg8] $seibetu[$Ksex8] LEVEL-$Klev8 【$seikaku[$Ksei8]】</OPTION>
EOF
}
if($Kimg9 != 0){
print <<"EOF";
<option value=9 >$itemlist[$Kimg9] $seibetu[$Ksex9] LEVEL-$Klev9 【$seikaku[$Ksei9]】</OPTION>
EOF
}
if($Kimg10 != 0){
print <<"EOF";
<option value=10 >$itemlist[$Kimg10] $seibetu[$Ksex10] LEVEL-$Klev10 【$seikaku[$Ksei10]】</OPTION>
EOF
}
}



&header;
print <<"EOF";
<P><B><FONT size="+2">お見合いモンスター設定</FONT></B></P>
<BR>
設定完了後、相手が了承するとお見合いが成立します。
<BR>
<HR>
<FORM ACTION="$cgiurl" METHOD="POST">
<P>どのモンスターをお見合いさせますか？<BR>
</P>
自分のモンスターの選択
<SELECT name=KMONS>
EOF
&hai3;
print <<"EOF";
</SELECT>
<BR>
<P>$BBNAMEさんのどのモンスターとお見合いさせますか？<BR>
</P>
相手のモンスターの選択
<SELECT name=AMONS>
EOF
&hai4;
print <<"EOF";
</SELECT>
<INPUT type="submit" value=" 決  定 ">
<INPUT type="hidden" name="mode" value="omik">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="aname" value="$BBNAME">
</FORM>
<HR>
<BR>
<CENTER>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="omiai">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="お見合い所へ">
</FORM>
<BR>
</CENTER>
EOF
}

&unlock;

&footer;
