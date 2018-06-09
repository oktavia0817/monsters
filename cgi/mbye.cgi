use utf8;
use open IO => ":utf8";
use open ":std";


$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$Mno    = $FORM{'MNAME'};
$Aimg   = $FORM{'Aimg'};
$Acname = $FORM{'Acname'};
$Asex   = $FORM{'Asex'};

open(FH,"$monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney) = split(/<>/,$line);
    if($Aimg == $Mimg){
    $Aimg   = $Mimg;
    $Acname = $Mcname;
    $Ahp    = int($Mhp);
    $Amhp   = int($Mhp);
    $Amp    = int($Mmp);
    $Ammp   = int($Mmp);
    $Akou   = int($Mkou);
    $Amam   = int($Mmam);
    $Asub   = int($Msub);
}
}

&open1;

$P1 = $Kimg[1]; 
$P2 = $Kimg[2]; 
$P3 = $Kimg[3]; 
$P4 = $Kimg[4]; 
$P5 = $Kimg[5]; 
$P6 = $Kimg[6]; 
$P7 = $Kimg[7]; 
$P8 = $Kimg[8]; 
$P9 = $Kimg[9]; 
$P10 = $Kimg[10]; 


if($Mno == 0){$mes = "$Acnameはさみしそうにさっていった";}
if($Mno == 1){
$mes = "$Acnameが加わり$itemlist[$P1]はさっていった";
$pattern = 1;
}
if($Mno == 2){$mes = "$Acnameが加わり$itemlist[$P2]はさっていった";
$pattern = 2;
}
if($Mno == 3){$mes = "$Acnameが加わり$itemlist[$P3]はさっていった";
$pattern = 3;
}
if($Mno == 4){$mes = "$Acnameが加わり$itemlist[$P4]はさっていった";
$pattern = 4;
}
if($Mno == 5){$mes = "$Acnameが加わり$itemlist[$P5]はさっていった";
$pattern = 5;
}
if($Mno == 6){$mes = "$Acnameが加わり$itemlist[$P6]はさっていった";
$pattern = 6;
}
if($Mno == 7){$mes = "$Acnameが加わり$itemlist[$P7]はさっていった";
$pattern = 7;
}
if($Mno == 8){$mes = "$Acnameが加わり$itemlist[$P8]はさっていった";
$pattern = 8;
}
if($Mno == 9){$mes = "$Acnameが加わり$itemlist[$P9]はさっていった";
$pattern = 9;
}
if($Mno == 10){$mes = "$Acnameが加わり$itemlist[$P10]はさっていった";
$pattern = 10;
}

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    if($Yplay3 != 2){&error("仲間の不正取得は出来ません");}
}
}

open(FH,"$monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney) = split(/<>/,$line);
    if($Aimg == $Mimg){
    $Aimg   = $Mimg;
    $Acname = $Mcname;
    $Ahp    = int($Mhp);
    $Amhp   = int($Mhp);
    $Amp    = int($Mmp);
    $Ammp   = int($Mmp);
    $Akou   = int($Mkou);
    $Amam   = int($Mmam);
    $Asub   = int($Msub);
}
}

&open1;

if($pattern == 1){
$Klev[1] = 1;
$Kmlev[1] = 10;
$Kimg[1]  = $Aimg;
$Khp[1]   = $Ahp;
$Kmhp[1]  = $Ahp;
$Kmp[1]   = $Amp;
$Kmmp[1]  = $Amp;
$Kkou[1]  = $Akou;
$Kmam[1]  = $Amam;
$Ksub[1]  = $Asub;
$Khai[1]  = 0;
$Kcount[1] = 0;
$Knecount[1] = $nextup;
$Ksex[2] = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[2] = $sei[int(rand(27))];
}

&get;

open(FH,"${datadir}/$inname.cgi");
@lines = <FH>;
close(FH);
$newline = "$Kname<>$Kpass<>$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>$Klev[3]<>$Kmlev[3]<>$Kimg[3]<>$Khp[3]<>$Kmhp[3]<>$Kmp[3]<>$Kmmp[3]<>$Kkou[3]<>$Kmam[3]<>$Ksub[3]<>$Khai[3]<>$Kcount[3]<>$Knecount[3]<>$Ksex[3]<>$Ksei[3]<>$Klev[4]<>$Kmlev[4]<>$Kimg[4]<>$Khp[4]<>$Kmhp[4]<>$Kmp[4]<>$Kmmp[4]<>$Kkou[4]<>$Kmam[4]<>$Ksub[4]<>$Khai[4]<>$Kcount[4]<>$Knecount[4]<>$Ksex[4]<>$Ksei[4]<>$Klev[5]<>$Kmlev[5]<>$Kimg[5]<>$Khp[5]<>$Kmhp[5]<>$Kmp[5]<>$Kmmp[5]<>$Kkou[5]<>$Kmam[5]<>$Ksub[5]<>$Khai[5]<>$Kcount[5]<>$Knecount[5]<>$Ksex[5]<>$Ksei[5]<>$Klev[6]<>$Kmlev[6]<>$Kimg[6]<>$Khp[6]<>$Kmhp[6]<>$Kmp[6]<>$Kmmp[6]<>$Kkou[6]<>$Kmam[6]<>$Ksub[6]<>$Khai[6]<>$Kcount[6]<>$Knecount[6]<>$Ksex[6]<>$Ksei[6]<>$Klev[7]<>$Kmlev[7]<>$Kimg[7]<>$Khp[7]<>$Kmhp[7]<>$Kmp[7]<>$Kmmp[7]<>$Kkou[7]<>$Kmam[7]<>$Ksub[7]<>$Khai[7]<>$Kcount[7]<>$Knecount[7]<>$Ksex[7]<>$Ksei[7]<>$Klev[8]<>$Kmlev[8]<>$Kimg[8]<>$Khp[8]<>$Kmhp[8]<>$Kmp[8]<>$Kmmp[8]<>$Kkou[8]<>$Kmam[8]<>$Ksub[8]<>$Khai[8]<>$Kcount[8]<>$Knecount[8]<>$Ksex[8]<>$Ksei[8]<>$Klev[9]<>$Kmlev[9]<>$Kimg[9]<>$Khp[9]<>$Kmhp[9]<>$Kmp[9]<>$Kmmp[9]<>$Kkou[9]<>$Kmam[9]<>$Ksub[9]<>$Khai[9]<>$Kcount[9]<>$Knecount[9]<>$Ksex[9]<>$Ksei[9]<>$Klev[10]<>$Kmlev[10]<>$Kimg[10]<>$Khp[10]<>$Kmhp[10]<>$Kmp[10]<>$Kmmp[10]<>$Kkou[10]<>$Kmam[10]<>$Ksub[10]<>$Khai[10]<>$Kcount[10]<>$Knecount[10]<>$Ksex[10]<>$Ksei[10]<>$Kdummy<>$Kkey<>$Kmoney";
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
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>1<>$Ykey<>$Kimg[1]<>$Khai[1]<>$Klev[1]<>$Kimg[2]<>$Khai[2]<>$Klev[2]<>$Kimg[3]<>$Khai[3]<>$Klev[3]<>$Ymoney<>$Ymes<>$turn";
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
<FONT size="5pt" color="#0000FF"><B>$mes</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$inname">
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

