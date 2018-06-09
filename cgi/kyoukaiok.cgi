use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$kyoukaidai  = $FORM{'kyoukaidai'};

&open1;

for($A=1;$A<11;$A++){
$Nhp[$A]      = $Khp[$A];
$Nmp[$A]      = $Kmp[$A];
if($Kimg[$A] != 0 && $Khp[$A] == 0){$Nhp[$A] = $Kmhp[$A];$Nmp[$A] = $Kmmp[$A];}
}
$newmoney = $Kmoney - $kyoukaidai;
$newline = "$Kname<>$Kpass<>$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Nhp[1]<>$Kmhp[1]<>$Nmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Nhp[2]<>$Kmhp[2]<>$Nmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>$Klev[3]<>$Kmlev[3]<>$Kimg[3]<>$Nhp[3]<>$Kmhp[3]<>$Nmp[3]<>$Kmmp[3]<>$Kkou[3]<>$Kmam[3]<>$Ksub[3]<>$Khai[3]<>$Kcount[3]<>$Knecount[3]<>$Ksex[3]<>$Ksei[3]<>$Klev[4]<>$Kmlev[4]<>$Kimg[4]<>$Nhp[4]<>$Kmhp[4]<>$Nmp[4]<>$Kmmp[4]<>$Kkou[4]<>$Kmam[4]<>$Ksub[4]<>$Khai[4]<>$Kcount[4]<>$Knecount[4]<>$Ksex[4]<>$Ksei[4]<>$Klev[5]<>$Kmlev[5]<>$Kimg[5]<>$Nhp[5]<>$Kmhp[5]<>$Nmp[5]<>$Kmmp[5]<>$Kkou[5]<>$Kmam[5]<>$Ksub[5]<>$Khai[5]<>$Kcount[5]<>$Knecount[5]<>$Ksex[5]<>$Ksei[5]<>$Klev[6]<>$Kmlev[6]<>$Kimg[6]<>$Nhp[6]<>$Kmhp[6]<>$Nmp[6]<>$Kmmp[6]<>$Kkou[6]<>$Kmam[6]<>$Ksub[6]<>$Khai[6]<>$Kcount[6]<>$Knecount[6]<>$Ksex[6]<>$Ksei[6]<>$Klev[7]<>$Kmlev[7]<>$Kimg[7]<>$Nhp[7]<>$Kmhp[7]<>$Nmp[7]<>$Kmmp[7]<>$Kkou[7]<>$Kmam[7]<>$Ksub[7]<>$Khai[7]<>$Kcount[7]<>$Knecount[7]<>$Ksex[7]<>$Ksei[7]<>$Klev[8]<>$Kmlev[8]<>$Kimg[8]<>$Nhp[8]<>$Kmhp[8]<>$Nmp[8]<>$Kmmp[8]<>$Kkou[8]<>$Kmam[8]<>$Ksub[8]<>$Khai[8]<>$Kcount[8]<>$Knecount[8]<>$Ksex[8]<>$Ksei[8]<>$Klev[9]<>$Kmlev[9]<>$Kimg[9]<>$Nhp[9]<>$Kmhp[9]<>$Nmp[9]<>$Kmmp[9]<>$Kkou[9]<>$Kmam[9]<>$Ksub[9]<>$Khai[9]<>$Kcount[9]<>$Knecount[9]<>$Ksex[9]<>$Ksei[9]<>$Klev[10]<>$Kmlev[10]<>$Kimg[10]<>$Nhp[10]<>$Kmhp[10]<>$Nmp[10]<>$Kmmp[10]<>$Kkou[10]<>$Kmam[10]<>$Ksub[10]<>$Khai[10]<>$Kcount[10]<>$Knecount[10]<>$Ksex[10]<>$Ksei[10]<>$Kdummy<>$Kkey<>$newmoney";


&lock;
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open!");
print FH $newline;
close(FH);
&unlock;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    $passcheck = crypt($inpass, $inname);
    if($passcheck ne $Ypass) {&error("パスワードが違います");}
    $newmoney = $Ymoney - $kyoukaidai;
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>$Yplay3<>$Ykey<>$Yimg1<>$Yhai1<>$Ylev1<>$Yimg2<>$Yhai2<>$Ylev2<>$Yimg3<>$Yhai3<>$Ylev3<>$newmoney<>$Ymes<>$turn";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
}
}

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>お祈りが天にとどきました</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="LOGINへ">
</FORM>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOP">
</CENTER>
</FORM>
EOF
&footer;
