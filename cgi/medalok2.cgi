use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$Kmoney   = $FORM{'money'};
$kounyu  = 100000000;
$Aimg   = 1;

open(FH,"$monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney) = split(/<>/,$line);
    if($Aimg == $Mimg){
    $Aimg   = $Mimg;
    $Acname = $Mcname;
    $Ahp    = int($Mhp * 2);
    $Amhp   = int($Mhp * 2);
    $Amp    = int($Mmp * 2);
    $Ammp   = int($Mmp * 2);
    $Akou   = int($Mkou * 2);
    $Amam   = int($Mmam * 2);
    $Asub   = int($Msub * 2);
    $Ahai   = 100;
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

$good = 0;

if($Kimg[2] == 0){$pattern = 2; $good = 1;}
if($Kimg[2] != 0 && $Kimg[3] == 0){$pattern = 3; $good = 1;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] == 0){$pattern = 4; $good = 1;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] == 0){$pattern = 5; $good = 1;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] == 0){$pattern = 6; $good = 1;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] == 0){$pattern = 7; $good = 1;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] != 0 && $Kimg[8] == 0){$pattern = 8; $good = 1;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] != 0 && $Kimg[8] != 0 && $Kimg[9] == 0){$pattern = 9; $good = 1;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] != 0 && $Kimg[8] != 0 && $Kimg[9] != 0 && $Kimg[10] == 0){$pattern = 10; $good = 1;}

if($pattern == 2){
$Klev[2] = 1;
$Kmlev[2] = 100;
$Kimg[2]  = $Aimg;
$Khp[2]   = $Ahp;
$Kmhp[2]  = $Ahp;
$Kmp[2]   = $Amp;
$Kmmp[2]  = $Amp;
$Kkou[2]  = $Akou;
$Kmam[2]  = $Amam;
$Ksub[2]  = $Asub;
$Khai[2]  = 100;
$Kcount[2] = 0;
$Knecount[2] = $nextup;
@sexs = (1,2);
$Ksex[2] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[2] = $sei[int(rand(27))];
}
if($pattern == 3){
$Klev[3] = 1;
$Kmlev[3] = 100;
$Kimg[3]  = $Aimg;
$Khp[3]   = $Ahp;
$Kmhp[3]  = $Ahp;
$Kmp[3]   = $Amp;
$Kmmp[3]  = $Amp;
$Kkou[3]  = $Akou;
$Kmam[3]  = $Amam;
$Ksub[3]  = $Asub;
$Khai[3]  = 100;
$Kcount[3] = 0;
$Knecount[3] = $nextup;
@sexs = (1,2);
$Ksex[3] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[3] = $sei[int(rand(27))];
}
if($pattern == 4){
$Klev[4] = 1;
$Kmlev[4] = 100;
$Kimg[4]  = $Aimg;
$Khp[4]   = $Ahp;
$Kmhp[4]  = $Ahp;
$Kmp[4]   = $Amp;
$Kmmp[4]  = $Amp;
$Kkou[4]  = $Akou;
$Kmam[4]  = $Amam;
$Ksub[4]  = $Asub;
$Khai[4]  = 100;
$Kcount[4] = 0;
$Knecount[4] = $nextup;
@sexs = (1,2);
$Ksex[4] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[4] = $sei[int(rand(27))];
}
if($pattern == 5){
$Klev[5] = 1;
$Kmlev[5] = 100;
$Kimg[5]  = $Aimg;
$Khp[5]   = $Ahp;
$Kmhp[5]  = $Ahp;
$Kmp[5]   = $Amp;
$Kmmp[5]  = $Amp;
$Kkou[5]  = $Akou;
$Kmam[5]  = $Amam;
$Ksub[5]  = $Asub;
$Khai[5]  = 100;
$Kcount[5] = 0;
$Knecount[5] = $nextup;
@sexs = (1,2);
$Ksex[5] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[5] = $sei[int(rand(27))];
}
if($pattern == 6){
$Klev[6] = 1;
$Kmlev[6] = 100;
$Kimg[6]  = $Aimg;
$Khp[6]   = $Ahp;
$Kmhp[6]  = $Ahp;
$Kmp[6]   = $Amp;
$Kmmp[6]  = $Amp;
$Kkou[6]  = $Akou;
$Kmam[6]  = $Amam;
$Ksub[6]  = $Asub;
$Khai[6]  = 100;
$Kcount[6] = 0;
$Knecount[6] = $nextup;
@sexs = (1,2);
$Ksex[6] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[6] = $sei[int(rand(27))];
}
if($pattern == 7){
$Klev[7] = 1;
$Kmlev[7] = 100;
$Kimg[7]  = $Aimg;
$Khp[7]   = $Ahp;
$Kmhp[7]  = $Ahp;
$Kmp[7]   = $Amp;
$Kmmp[7]  = $Amp;
$Kkou[7]  = $Akou;
$Kmam[7]  = $Amam;
$Ksub[7]  = $Asub;
$Khai[7]  = 100;
$Kcount[7] = 0;
$Knecount[7] = $nextup;
@sexs = (1,2);
$Ksex[7] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[7] = $sei[int(rand(27))];
}
if($pattern == 8){
$Klev[8] = 1;
$Kmlev[8] = 100;
$Kimg[8]  = $Aimg;
$Khp[8]   = $Ahp;
$Kmhp[8]  = $Ahp;
$Kmp[8]   = $Amp;
$Kmmp[8]  = $Amp;
$Kkou[8]  = $Akou;
$Kmam[8]  = $Amam;
$Ksub[8]  = $Asub;
$Khai[8]  = 100;
$Kcount[8] = 0;
$Knecount[8] = $nextup;
@sexs = (1,2);
$Ksex[8] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[8] = $sei[int(rand(27))];
}
if($pattern == 9){
$Klev[9] = 1;
$Kmlev[9] = 100;
$Kimg[9]  = $Aimg;
$Khp[9]   = $Ahp;
$Kmhp[9]  = $Ahp;
$Kmp[9]   = $Amp;
$Kmmp[9]  = $Amp;
$Kkou[9]  = $Akou;
$Kmam[9]  = $Amam;
$Ksub[9]  = $Asub;
$Khai[9]  = 100;
$Kcount[9] = 0;
$Knecount[9] = $nextup;
@sexs = (1,2);
$Ksex[9] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[9] = $sei[int(rand(27))];
}
if($pattern == 10){
$Klev[10] = 1;
$Kmlev[10] = 100;
$Kimg[10]  = $Aimg;
$Khp[10]   = $Ahp;
$Kmhp[10]  = $Ahp;
$Kmp[10]   = $Amp;
$Kmmp[10]  = $Amp;
$Kkou[10]  = $Akou;
$Kmam[10]  = $Amam;
$Ksub[10]  = $Asub;
$Khai[10]  = 100;
$Kcount[10] = 0;
$Knecount[10] = $nextup;
@sexs = (1,2);
$Ksex[10] = $sexs[int(rand(2))];
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[10] = $sei[int(rand(27))];
}

if($pattern != 0){

open(FH,"${datadir}/$inname.cgi");
@lines = <FH>;
close(FH);

$newmoney = $Kmoney - $kounyu;
$newline = "$Kname<>$Kpass<>$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>$Klev[3]<>$Kmlev[3]<>$Kimg[3]<>$Khp[3]<>$Kmhp[3]<>$Kmp[3]<>$Kmmp[3]<>$Kkou[3]<>$Kmam[3]<>$Ksub[3]<>$Khai[3]<>$Kcount[3]<>$Knecount[3]<>$Ksex[3]<>$Ksei[3]<>$Klev[4]<>$Kmlev[4]<>$Kimg[4]<>$Khp[4]<>$Kmhp[4]<>$Kmp[4]<>$Kmmp[4]<>$Kkou[4]<>$Kmam[4]<>$Ksub[4]<>$Khai[4]<>$Kcount[4]<>$Knecount[4]<>$Ksex[4]<>$Ksei[4]<>$Klev[5]<>$Kmlev[5]<>$Kimg[5]<>$Khp[5]<>$Kmhp[5]<>$Kmp[5]<>$Kmmp[5]<>$Kkou[5]<>$Kmam[5]<>$Ksub[5]<>$Khai[5]<>$Kcount[5]<>$Knecount[5]<>$Ksex[5]<>$Ksei[5]<>$Klev[6]<>$Kmlev[6]<>$Kimg[6]<>$Khp[6]<>$Kmhp[6]<>$Kmp[6]<>$Kmmp[6]<>$Kkou[6]<>$Kmam[6]<>$Ksub[6]<>$Khai[6]<>$Kcount[6]<>$Knecount[6]<>$Ksex[6]<>$Ksei[6]<>$Klev[7]<>$Kmlev[7]<>$Kimg[7]<>$Khp[7]<>$Kmhp[7]<>$Kmp[7]<>$Kmmp[7]<>$Kkou[7]<>$Kmam[7]<>$Ksub[7]<>$Khai[7]<>$Kcount[7]<>$Knecount[7]<>$Ksex[7]<>$Ksei[7]<>$Klev[8]<>$Kmlev[8]<>$Kimg[8]<>$Khp[8]<>$Kmhp[8]<>$Kmp[8]<>$Kmmp[8]<>$Kkou[8]<>$Kmam[8]<>$Ksub[8]<>$Khai[8]<>$Kcount[8]<>$Knecount[8]<>$Ksex[8]<>$Ksei[8]<>$Klev[9]<>$Kmlev[9]<>$Kimg[9]<>$Khp[9]<>$Kmhp[9]<>$Kmp[9]<>$Kmmp[9]<>$Kkou[9]<>$Kmam[9]<>$Ksub[9]<>$Khai[9]<>$Kcount[9]<>$Knecount[9]<>$Ksex[9]<>$Ksei[9]<>$Klev[10]<>$Kmlev[10]<>$Kimg[10]<>$Khp[10]<>$Kmhp[10]<>$Kmp[10]<>$Kmmp[10]<>$Kkou[10]<>$Kmam[10]<>$Ksub[10]<>$Khai[10]<>$Kcount[10]<>$Knecount[10]<>$Ksex[10]<>$Ksei[10]<>$Kdummy<>$Kkey<>$newmoney";
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
    $Ymoney = $newmoney;
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>$Yplay3<>$Ykey<>$Kimg[1]<>$Khai[1]<>$Klev[1]<>$Kimg[2]<>$Khai[2]<>$Klev[2]<>$Kimg[3]<>$Khai[3]<>$Klev[3]<>$Ymoney<>$Ymes<>$turn";
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
<FONT size="5pt" color="#0000FF"><IMG src="$imgpath/$Aimg.gif" border="0"><B>$Acname が仲間に加わりました</B></FONT><BR>
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

}
if($good == 0){&error("モンスターが一杯です！");}
