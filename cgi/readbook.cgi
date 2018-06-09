use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$Mname  = $FORM{'Mname'};
$Bname  = $FORM{'Bname'};

&open1;

if($Mname == 1){$Msei = $Ksei[1];}
if($Mname == 2){$Msei = $Ksei[2];}
if($Mname == 3){$Msei = $Ksei[3];}
if($Mname == 4){$Msei = $Ksei[4];}
if($Mname == 5){$Msei = $Ksei[5];}
if($Mname == 6){$Msei = $Ksei[6];}
if($Mname == 7){$Msei = $Ksei[7];}
if($Mname == 8){$Msei = $Ksei[8];}
if($Mname == 9){$Msei = $Ksei[9];}
if($Mname == 10){$Msei = $Ksei[10];}

$newmoney = $Kmoney - 1000;
if($newmoney < 0){&error("お金が足りません");}
$Newsei = $Msei;

open(FH,"dat/book.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($book,$seikaku,$Nsei,$dummy) = split(/<>/,$line);
    if($book == $Bname && $Msei == $seikaku){$Newsei = $Nsei;}
}

if($Mname == 1){$Ksei[1] = $Newsei;}
if($Mname == 2){$Ksei[2] = $Newsei;}
if($Mname == 3){$Ksei[3] = $Newsei;}
if($Mname == 4){$Ksei[4] = $Newsei;}
if($Mname == 5){$Ksei[5] = $Newsei;}
if($Mname == 6){$Ksei[6] = $Newsei;}
if($Mname == 7){$Ksei[7] = $Newsei;}
if($Mname == 8){$Ksei[8] = $Newsei;}
if($Mname == 9){$Ksei[9] = $Newsei;}
if($Mname == 10){$Ksei[10] = $Newsei;}

$newline = "$Kname<>$Kpass<>$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>$Klev[3]<>$Kmlev[3]<>$Kimg[3]<>$Khp[3]<>$Kmhp[3]<>$Kmp[3]<>$Kmmp[3]<>$Kkou[3]<>$Kmam[3]<>$Ksub[3]<>$Khai[3]<>$Kcount[3]<>$Knecount[3]<>$Ksex[3]<>$Ksei[3]<>$Klev[4]<>$Kmlev[4]<>$Kimg[4]<>$Khp[4]<>$Kmhp[4]<>$Kmp[4]<>$Kmmp[4]<>$Kkou[4]<>$Kmam[4]<>$Ksub[4]<>$Khai[4]<>$Kcount[4]<>$Knecount[4]<>$Ksex[4]<>$Ksei[4]<>$Klev[5]<>$Kmlev[5]<>$Kimg[5]<>$Khp[5]<>$Kmhp[5]<>$Kmp[5]<>$Kmmp[5]<>$Kkou[5]<>$Kmam[5]<>$Ksub[5]<>$Khai[5]<>$Kcount[5]<>$Knecount[5]<>$Ksex[5]<>$Ksei[5]<>$Klev[6]<>$Kmlev[6]<>$Kimg[6]<>$Khp[6]<>$Kmhp[6]<>$Kmp[6]<>$Kmmp[6]<>$Kkou[6]<>$Kmam[6]<>$Ksub[6]<>$Khai[6]<>$Kcount[6]<>$Knecount[6]<>$Ksex[6]<>$Ksei[6]<>$Klev[7]<>$Kmlev[7]<>$Kimg[7]<>$Khp[7]<>$Kmhp[7]<>$Kmp[7]<>$Kmmp[7]<>$Kkou[7]<>$Kmam[7]<>$Ksub[7]<>$Khai[7]<>$Kcount[7]<>$Knecount[7]<>$Ksex[7]<>$Ksei[7]<>$Klev[8]<>$Kmlev[8]<>$Kimg[8]<>$Khp[8]<>$Kmhp[8]<>$Kmp[8]<>$Kmmp[8]<>$Kkou[8]<>$Kmam[8]<>$Ksub[8]<>$Khai[8]<>$Kcount[8]<>$Knecount[8]<>$Ksex[8]<>$Ksei[8]<>$Klev[9]<>$Kmlev[9]<>$Kimg[9]<>$Khp[9]<>$Kmhp[9]<>$Kmp[9]<>$Kmmp[9]<>$Kkou[9]<>$Kmam[9]<>$Ksub[9]<>$Khai[9]<>$Kcount[9]<>$Knecount[9]<>$Ksex[9]<>$Ksei[9]<>$Klev[10]<>$Kmlev[10]<>$Kimg[10]<>$Khp[10]<>$Kmhp[10]<>$Kmp[10]<>$Kmmp[10]<>$Kkou[10]<>$Kmam[10]<>$Ksub[10]<>$Khai[10]<>$Kcount[10]<>$Knecount[10]<>$Ksex[10]<>$Ksei[10]<>$Kdummy<>$Kkey<>$newmoney";


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
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>$Yplay3<>$Ykey<>$Yimg1<>$Yhai1<>$Ylev1<>$Yimg2<>$Yhai2<>$Ylev2<>$Yimg3<>$Yhai3<>$Ylev3<>$newmoney<>$Ymes<>$turn";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
}
}

if($Msei == $Newsei){ $mes = "モンスターの性格は変わらなかった";}
if($Msei != $Newsei){ $mes = "性格が【$seikaku[$Msei]】から【$seikaku[$Newsei]】に変わった";}

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>$mes</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="books">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="本屋へ戻る">
</FORM>
<BR><BR><BR>
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
