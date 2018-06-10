use utf8;
use open IO => ":utf8";
use open ":std";

$hensin  = $FORM{'newmonster'};
$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$Omoneys = $FORM{'haimoney'};
$haigou1 = $FORM{'haigou1'};
$haigou2 = $FORM{'haigou2'};
$img1 = $FORM{'img1'};
$img2 = $FORM{'img2'};

&open1;

$passcheck = crypt($inpass, $inname);
if($passcheck ne $Kpass) {&error("パスワードが違います");}
if($Kimg[$haigou1] != $img1 || $Kimg[$haigou2] != $img2){ &error("配合方法が異常です(0)")}
if($Ksex[$haigou1] == $Ksex[$haigou2]){&error("性別が同じで配合出来ません");}
if(($Kimg[$haigou1] != $Kimg[1] && $Kimg[$haigou1] != $Kimg[2] && $Kimg[$haigou1] != $Kimg[3] && $Kimg[$haigou1] != $Kimg[4] && $Kimg[$haigou1] != $Kimg[5] && $Kimg[$haigou1] != $Kimg[6] && $Kimg[$haigou1] != $Kimg[7] && $Kimg[$haigou1] != $Kimg[8] && $Kimg[$haigou1] != $Kimg[9] && $Kimg[$haigou1] != $Kimg[10]) && ($Kimg[$haigou2] != $Kimg[1] && $Kimg[$haigou2] != $Kimg[2] && $Kimg[$haigou2] != $Kimg[3] && $Kimg[$haigou2] != $Kimg[4] && $Kimg[$haigou2] != $Kimg[5] && $Kimg[$haigou2] != $Kimg[6] && $Kimg[$haigou2] != $Kimg[7] && $Kimg[$haigou2] != $Kimg[8] && $Kimg[$haigou2] != $Kimg[9] && $Kimg[$haigou2] != $Kimg[10])){ &error("配合方法が異常です(2)")}

open(FH,"$monsdata") || &error("Can't open $monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
    if($Mimg == $hensin){
    $Nimg = $Mimg;
    $Nkou = $Mkou;
    $Nmam = $Mmam;
    $Nsub = $Msub;
    $Nhp = $Mhp;
    $Nmp = $Mmp;
    $Ntoku = $Mtoku;
}
}

&open2;

$waza[$Ntoku] = $Ntoku;

$NEWWAZA = "$waza[1]<>$waza[2]<>$waza[3]<>$waza[4]<>$waza[5]<>$waza[6]<>$waza[7]<>$waza[8]<>$waza[9]<>$waza[10]<>$waza[11]<>$waza[12]<>$waza[13]<>$waza[14]<>$waza[15]<>$waza[16]<>$waza[17]<>$waza[18]<>$waza[19]<>$waza[20]<>$waza[21]<>$waza[22]<>$waza[23]<>$waza[24]<>$waza[25]<>$waza[26]<>$waza[27]<>$waza[28]<>$waza[29]<>$waza[30]<>$waza[31]<>$waza[32]<>$waza[33]<>$waza[34]<>$waza[35]<>$waza[36]<>$waza[37]<>$waza[38]<>$waza[39]<>$waza[40]<>$waza[41]<>$waza[42]<>$waza[43]<>$waza[44]<>$waza[45]<>$waza[46]<>$waza[47]<>$waza[48]<>$waza[49]<>$waza[50]<>$waza[51]<>$waza[52]";

&lock;
open(FH, ">waza/$inname.cgi") || &error("Can't open!");
print FH $NEWWAZA;
close(FH);
&unlock;

$NEWhai = $Khai[$haigou1] + $Khai[$haigou2];
$NEWhai++;

for($A=1;$A<11;$A++){
$Nlev[$A]     = $Klev[$A];
$Nmlev[$A]    = $Kmlev[$A];
$Nimg[$A]     = $Kimg[$A];
$Nhp[$A]      = $Khp[$A];
$Nmhp[$A]     = $Kmhp[$A];
$Nmp[$A]      = $Kmp[$A];
$Nmmp[$A]     = $Kmmp[$A];
$Nkou[$A]     = $Kkou[$A];
$Nmam[$A]     = $Kmam[$A];
$Nsub[$A]     = $Ksub[$A];
$Nhai[$A]     = $Khai[$A];
$Ncount[$A]   = $Kcount[$A];
$Nnecount[$A] = $Knecount[$A];
$Nsex[$A]     = $Ksex[$A];
$Nsei[$A]     = $Ksei[$A];
}

if($haigou1 < $haigou2){$PT = 1;}
if($haigou2 < $haigou1){$PT = 2;}

if($PT == 1){
$Nimg[$haigou1]     = $Nimg;
$Nhai[$haigou1]     = $NEWhai;
$Nlev[$haigou1]     = 1;
$Nmlev[$haigou1]    = int($Klev[$haigou1] + $Klev[$haigou2]);
$Nmhp[$haigou1]     = int($Nhp + $NEWhai);
$Nmmp[$haigou1]     = int($Nmp + $NEWhai);
$Nkou[$haigou1]     = int($Nkou + $NEWhai);
$Nmam[$haigou1]     = int($Nmam + $NEWhai);
$Nsub[$haigou1]     = int($Nsub + $NEWhai);
$Nhp[$haigou1]      = int($Nhp + $NEWhai);
$Nmp[$haigou1]      = int($Nmp + $NEWhai);
$Pmlev    = int($Klev[$haigou1] + $Klev[$haigou2]);
$Pmhp     = int($Nhp + $NEWhai);
$Pmmp     = int($Nmp + $NEWhai);
$Pkou     = int($Nkou + $NEWhai);
$Pmam     = int($Nmam + $NEWhai);
$Psub     = int($Nsub + $NEWhai);
$Ncount[$haigou1]   = 0;
$Nnecount[$haigou1] = $nextup;

@sexs = (1,2);
$Nsex[$haigou1] = $sexs[int(rand(2))];
$Psex     = $Nsex[$haigou1];

@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Nsei[$haigou1] = $sei[int(rand(27))];
$Psei     = $Nsei[$haigou1];

$Nimg[$haigou2]     = 0;
$Nhai[$haigou2]     = 0;
$Nlev[$haigou2]     = 0;
$Nmlev[$haigou2]    = 0;
$Nmhp[$haigou2]     = 0;
$Nmmp[$haigou2]     = 0;
$Nhp[$haigou2]      = 0;
$Nmp[$haigou2]      = 0;
$Nkou[$haigou2]     = 0;
$Nmam[$haigou2]     = 0;
$Nsub[$haigou2]     = 0;
$Ncount[$haigou2]   = 0;
$Nnecount[$haigou2] = 0;
$Nsex[$haigou2]     = 0;
$Nsei[$haigou2]     = 0;
}
if($PT == 2){
$Nimg[$haigou2]     = $Nimg;
$Nhai[$haigou2]     = $NEWhai;
$Nlev[$haigou2]     = 1;
$Nmlev[$haigou2]    = int($Klev[$haigou1] + $Klev[$haigou2]);
$Nmhp[$haigou2]     = int($Nhp + $NEWhai);
$Nmmp[$haigou2]     = int($Nmp + $NEWhai);
$Nkou[$haigou2]     = int($Nkou + $NEWhai);
$Nmam[$haigou2]     = int($Nmam + $NEWhai);
$Nsub[$haigou2]     = int($Nsub + $NEWhai);
$Nhp[$haigou2]      = int($Nhp + $NEWhai);
$Nmp[$haigou2]      = int($Nmp + $NEWhai);
$Ncount[$haigou2]   = 0;
$Nnecount[$haigou2] = $nextup;

@sexs = (1,2);
$Nsex[$haigou2] = $sexs[int(rand(2))];
$Psex     = $Nsex[$haigou2];

@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Nsei[$haigou2] = $sei[int(rand(27))];
$Psei     = $Nsei[$haigou2];

$Pmlev    = int($Klev[$haigou1] + $Klev[$haigou2]);
$Pmhp     = int($Nhp + $NEWhai);
$Pmmp     = int($Nmp + $NEWhai);
$Pkou     = int($Nkou + $NEWhai);
$Pmam     = int($Nmam + $NEWhai);
$Psub     = int($Nsub + $NEWhai);
$Nimg[$haigou1]     = 0;
$Nhai[$haigou1]     = 0;
$Nlev[$haigou1]     = 0;
$Nmlev[$haigou1]    = 0;
$Nmhp[$haigou1]     = 0;
$Nmmp[$haigou1]     = 0;
$Nhp[$haigou1]      = 0;
$Nmp[$haigou1]      = 0;
$Nkou[$haigou1]     = 0;
$Nmam[$haigou1]     = 0;
$Nsub[$haigou1]     = 0;
$Ncount[$haigou1]   = 0;
$Nnecount[$haigou1] = 0;
$Nsex[$haigou1]     = 0;
$Nsei[$haigou1]     = 0;
}
for($C=2;$C<11;$C++){
$D = $C + 1;
if($Nimg[$C]==0){
$Nlev[$C]     = $Nlev[$D];
$Nmlev[$C]    = $Nmlev[$D];
$Nimg[$C]     = $Nimg[$D];
$Nhp[$C]      = $Nhp[$D];
$Nmhp[$C]     = $Nmhp[$D];
$Nmp[$C]      = $Nmp[$D];
$Nmmp[$C]     = $Nmmp[$D];
$Nkou[$C]     = $Nkou[$D];
$Nmam[$C]     = $Nmam[$D];
$Nsub[$C]     = $Nsub[$D];
$Nhai[$C]     = $Nhai[$D];
$Ncount[$C]   = $Ncount[$D];
$Nnecount[$C] = $Nnecount[$D];
$Nsex[$C]     = $Nsex[$D];
$Nsei[$C]     = $Nsei[$D];
$Nimg[$D]     = 0;
$Nhai[$D]     = 0;
$Nlev[$D]     = 0;
$Nmlev[$D]    = 0;
$Nmhp[$D]     = 0;
$Nmmp[$D]     = 0;
$Nhp[$D]      = 0;
$Nmp[$D]      = 0;
$Nkou[$D]     = 0;
$Nmam[$D]     = 0;
$Nsub[$D]     = 0;
$Ncount[$D]   = 0;
$Nnecount[$D] = 0;
$Nsex[$D]     = 0;
$Nsei[$D]     = 0;
}
}
$Nimg[10]     = 0;
$Nhai[10]     = 0;
$Nlev[10]     = 0;
$Nmlev[10]    = 0;
$Nmhp[10]     = 0;
$Nmmp[10]     = 0;
$Nhp[10]      = 0;
$Nmp[10]      = 0;
$Nkou[10]     = 0;
$Nmam[10]     = 0;
$Nsub[10]     = 0;
$Ncount[10]   = 0;
$Nnecount[10] = 0;
$Nsex[10]     = 0;
$Nsei[10]     = 0;
$Nmoney      = $Kmoney - $Omoneys;

$KLINE = "$Kname<>$Kpass<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Nlev[3]<>$Nmlev[3]<>$Nimg[3]<>$Nhp[3]<>$Nmhp[3]<>$Nmp[3]<>$Nmmp[3]<>$Nkou[3]<>$Nmam[3]<>$Nsub[3]<>$Nhai[3]<>$Ncount[3]<>$Nnecount[3]<>$Nsex[3]<>$Nsei[3]<>$Nlev[4]<>$Nmlev[4]<>$Nimg[4]<>$Nhp[4]<>$Nmhp[4]<>$Nmp[4]<>$Nmmp[4]<>$Nkou[4]<>$Nmam[4]<>$Nsub[4]<>$Nhai[4]<>$Ncount[4]<>$Nnecount[4]<>$Nsex[4]<>$Nsei[4]<>$Nlev[5]<>$Nmlev[5]<>$Nimg[5]<>$Nhp[5]<>$Nmhp[5]<>$Nmp[5]<>$Nmmp[5]<>$Nkou[5]<>$Nmam[5]<>$Nsub[5]<>$Nhai[5]<>$Ncount[5]<>$Nnecount[5]<>$Nsex[5]<>$Nsei[5]<>$Nlev[6]<>$Nmlev[6]<>$Nimg[6]<>$Nhp[6]<>$Nmhp[6]<>$Nmp[6]<>$Nmmp[6]<>$Nkou[6]<>$Nmam[6]<>$Nsub[6]<>$Nhai[6]<>$Ncount[6]<>$Nnecount[6]<>$Nsex[6]<>$Nsei[6]<>$Nlev[7]<>$Nmlev[7]<>$Nimg[7]<>$Nhp[7]<>$Nmhp[7]<>$Nmp[7]<>$Nmmp[7]<>$Nkou[7]<>$Nmam[7]<>$Nsub[7]<>$Nhai[7]<>$Ncount[7]<>$Nnecount[7]<>$Nsex[7]<>$Nsei[7]<>$Nlev[8]<>$Nmlev[8]<>$Nimg[8]<>$Nhp[8]<>$Nmhp[8]<>$Nmp[8]<>$Nmmp[8]<>$Nkou[8]<>$Nmam[8]<>$Nsub[8]<>$Nhai[8]<>$Ncount[8]<>$Nnecount[8]<>$Nsex[8]<>$Nsei[8]<>$Nlev[9]<>$Nmlev[9]<>$Nimg[9]<>$Nhp[9]<>$Nmhp[9]<>$Nmp[9]<>$Nmmp[9]<>$Nkou[9]<>$Nmam[9]<>$Nsub[9]<>$Nhai[9]<>$Ncount[9]<>$Nnecount[9]<>$Nsex[9]<>$Nsei[9]<>$Nlev[10]<>$Nmlev[10]<>$Nimg[10]<>$Nhp[10]<>$Nmhp[10]<>$Nmp[10]<>$Nmmp[10]<>$Nkou[10]<>$Nmam[10]<>$Nsub[10]<>$Nhai[10]<>$Ncount[10]<>$Nnecount[10]<>$Nsex[10]<>$Nsei[10]<>$Kdummy<>$Kkey<>$Nmoney";

&lock;
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $KLINE;
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
    $Kkey        = $Ykey;
    $Nmoney      = $Ymoney - $Omoneys;
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>$Yplay3<>$Ykey<>$Nimg[1]<>$Nhai[1]<>$Nlev[1]<>$Nimg[2]<>$Nhai[2]<>$Nlev[2]<>$Nimg[3]<>$Nhai[3]<>$Nlev[3]<>$Nmoney<>$Ymes<>$turn";
&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
}
}

open(FH,"waza/$inname.cgi") || &error("Can't open!");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($waza1,$waza2,$waza3,$waza4,$waza5,$waza6,$waza7,$waza8,$waza9,$waza10,$waza11,$waza12,$waza13,$waza14,$waza15,$waza16,$waza17,$waza18,$waza19,$waza20,$waza21,$waza22,$waza23,$waza24,$waza25,$waza26,$waza27,$waza28,$waza29,$waza30,$waza31,$waza32,$waza33,$waza34,$waza35,$waza36,$waza37,$waza38,$waza39,$waza40,$waza41,$waza42,$waza43,$waza44,$waza45,$waza46,$waza47,$waza48,$waza49,$waza50,$waza51,$waza52) = split(/<>/,$line);
}

&header;

print <<"EOF";
<P align="center">
<FONT face="Times New Roman" color="#0000cc" size="6"><B>NEW MONSTER!</B></FONT>
</P>
<HR>
<BR>
<CENTER>
<TABLE cellspacing="3" cellpadding="1" width="700" bgcolor="black" border="0">
<TBODY>
<TR>
<TD width="150" bgcolor="#339999">
<DIV align="center"><FONT face="Times New Roman">Level</FONT></DIV>
</TD>
<TD width="150" bgcolor="#339999">
<DIV align="center"><FONT face="Times New Roman">H P</FONT></DIV>
</TD>
<TD width="150" bgcolor="#339999">
<DIV align="center"><FONT face="Times New Roman">M P</FONT></DIV>
</TD>
<TD width="150" bgcolor="#339999">
<DIV align="center">攻撃力</DIV>
</TD>
<TD width="150" bgcolor="#339999">
<DIV align="center">守備力</DIV>
</TD>
<TD width="150" bgcolor="#339999">
<DIV align="center">素早さ</DIV>
</TD>
</TR>
<TR>
<TD width="150" bgcolor="white">
<DIV align="center"><FONT face="Times New Roman">1 / $Pmlev</FONT></DIV>
</TD>
<TD width="150" bgcolor="white">
<DIV align="center"><FONT face="Times New Roman">$Pmhp / $Pmhp</FONT></DIV>
</TD>
<TD width="150" bgcolor="white">
<DIV align="center"><FONT face="Times New Roman">$Pmmp / $Pmmp</FONT></DIV>
</TD>
<TD width="150" bgcolor="white">
<DIV align="center"><FONT face="Times New Roman">$Pkou</FONT></DIV>
</TD>
<TD width="150" bgcolor="white">
<DIV align="center"><FONT face="Times New Roman">$Pmam</FONT></DIV>
</TD>
<TD width="150" bgcolor="white">
<DIV align="center"><FONT face="Times New Roman">$Psub</FONT></TD>
</TR>
<TR>
<TD rowspan="2" width="150" bgcolor="#ffffff" align="center"><IMG src="$imgpath/$Nimg.gif" border="0" bgcolor="#ffffff"></TD>
<TD bgcolor="#339999" width="150" align="center">モンスター名</TD>
<TD width="150" bgcolor="#339999" align="center">経験値</TD>
<TD width="150" bgcolor="#339999" align="center">配合数</TD>
<TD width="150" bgcolor="#339999" align="center">所持金</TD>
<TD width="150" bgcolor="#339999">最深階</TD>
</TR>
<TR>
<TD bgcolor="white" width="150" align="center">$itemlist[$Nimg] $seibetu[$Psex]<BR>$seikaku[$Psei]</TD>
<TD width="150" bgcolor="#ffffff" align="center">0 / $nextup</TD>
<TD width="150" bgcolor="white" align="center">$NEWhai 回</TD>
<TD width="150" bgcolor="white" align="center">$Nmoney ゴールド</TD>
<TD width="150" bgcolor="white" align="center"><FONT face="Times New Roman">地下$Kkey 階</FONT></TD>
</TR>
<TR>
<TD bgcolor="#339999" colspan="6" align="center">特殊攻撃</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza1]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza2]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza3]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza4]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza5]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza6]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza7]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza8]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza9]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza10]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza11]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza12]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza13]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza14]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza15]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza16]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza17]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza18]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza19]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza20]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza21]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza22]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza23]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza24]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza25]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza26]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza27]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza28]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza29]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza30]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza31]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza32]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza33]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza34]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza35]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza36]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza37]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza38]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza39]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza40]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza41]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza42]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza43]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza44]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza45]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza46]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza47]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza48]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza49]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza50]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza51]</TD>
<TD bgcolor="#ffffff" align="center">$mtoku[$waza52]</TD>
<TD bgcolor="#ffffff" align="center">□</TD>
<TD bgcolor="#ffffff" align="center">□</TD>
</TR>
</TBODY>
</TABLE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="LOGINへ">
</FORM>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="  TOP  ">
</FORM>
</CENTER>
EOF

&footer;
