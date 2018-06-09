use utf8;
use open IO => ":utf8";
use open ":std";

$inname   = $FORM{'name'};
$inpass   = $FORM{'password'};
$Ssu      = $FORM{'Ssu'};
$cname[1]   = $FORM{'cname1'};
$cname[2]   = $FORM{'cname2'};
$cname[3]   = $FORM{'cname3'};
$cname[4]   = $FORM{'cname4'};
$cname[5]   = $FORM{'cname5'};
$cname[6]   = $FORM{'cname6'};
$cname[7]   = $FORM{'cname7'};
$cname[8]   = $FORM{'cname8'};
$cname[9]   = $FORM{'cname9'};
$cname[10]   = $FORM{'cname10'};

$Ssu++;

for($A=1;$A<$Ssu;$A++){
for($B=$A+1;$B<$Ssu;$B++){
if($cname[$A] == $cname[$B]){&error("並び替えの数値が重なってます");}
}
}

&open1;

### HPバトル専科のDora様より追加 #####
for($A=1;$A<$Ssu;$A++){
if(!$Klev[$A]){&error("その番号のモンスターは所有していません");}
}
##################################

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

for($B=1;$B<11;$B++){
if($cname[1] == $B){
$Nlev[$B]     = $Klev[1];
$Nmlev[$B]    = $Kmlev[1];
$Nimg[$B]     = $Kimg[1];
$Nhp[$B]      = $Khp[1];
$Nmhp[$B]     = $Kmhp[1];
$Nmp[$B]      = $Kmp[1];
$Nmmp[$B]     = $Kmmp[1];
$Nkou[$B]     = $Kkou[1];
$Nmam[$B]     = $Kmam[1];
$Nsub[$B]     = $Ksub[1];
$Nhai[$B]     = $Khai[1];
$Ncount[$B]   = $Kcount[1];
$Nnecount[$B] = $Knecount[1];
$Nsex[$B]     = $Ksex[1];
$Nsei[$B]     = $Ksei[1];
}
if($cname[2] == $B){
$Nlev[$B]     = $Klev[2];
$Nmlev[$B]    = $Kmlev[2];
$Nimg[$B]     = $Kimg[2];
$Nhp[$B]      = $Khp[2];
$Nmhp[$B]     = $Kmhp[2];
$Nmp[$B]      = $Kmp[2];
$Nmmp[$B]     = $Kmmp[2];
$Nkou[$B]     = $Kkou[2];
$Nmam[$B]     = $Kmam[2];
$Nsub[$B]     = $Ksub[2];
$Nhai[$B]     = $Khai[2];
$Ncount[$B]   = $Kcount[2];
$Nnecount[$B] = $Knecount[2];
$Nsex[$B]     = $Ksex[2];
$Nsei[$B]     = $Ksei[2];
}
if($cname[3] == $B){
$Nlev[$B]     = $Klev[3];
$Nmlev[$B]    = $Kmlev[3];
$Nimg[$B]     = $Kimg[3];
$Nhp[$B]      = $Khp[3];
$Nmhp[$B]     = $Kmhp[3];
$Nmp[$B]      = $Kmp[3];
$Nmmp[$B]     = $Kmmp[3];
$Nkou[$B]     = $Kkou[3];
$Nmam[$B]     = $Kmam[3];
$Nsub[$B]     = $Ksub[3];
$Nhai[$B]     = $Khai[3];
$Ncount[$B]   = $Kcount[3];
$Nnecount[$B] = $Knecount[3];
$Nsex[$B]     = $Ksex[3];
$Nsei[$B]     = $Ksei[3];
}
if($cname[4] == $B){
$Nlev[$B]     = $Klev[4];
$Nmlev[$B]    = $Kmlev[4];
$Nimg[$B]     = $Kimg[4];
$Nhp[$B]      = $Khp[4];
$Nmhp[$B]     = $Kmhp[4];
$Nmp[$B]      = $Kmp[4];
$Nmmp[$B]     = $Kmmp[4];
$Nkou[$B]     = $Kkou[4];
$Nmam[$B]     = $Kmam[4];
$Nsub[$B]     = $Ksub[4];
$Nhai[$B]     = $Khai[4];
$Ncount[$B]   = $Kcount[4];
$Nnecount[$B] = $Knecount[4];
$Nsex[$B]     = $Ksex[4];
$Nsei[$B]     = $Ksei[4];
}
if($cname[5] == $B){
$Nlev[$B]     = $Klev[5];
$Nmlev[$B]    = $Kmlev[5];
$Nimg[$B]     = $Kimg[5];
$Nhp[$B]      = $Khp[5];
$Nmhp[$B]     = $Kmhp[5];
$Nmp[$B]      = $Kmp[5];
$Nmmp[$B]     = $Kmmp[5];
$Nkou[$B]     = $Kkou[5];
$Nmam[$B]     = $Kmam[5];
$Nsub[$B]     = $Ksub[5];
$Nhai[$B]     = $Khai[5];
$Ncount[$B]   = $Kcount[5];
$Nnecount[$B] = $Knecount[5];
$Nsex[$B]     = $Ksex[5];
$Nsei[$B]     = $Ksei[5];
}
if($cname[6] == $B){
$Nlev[$B]     = $Klev[6];
$Nmlev[$B]    = $Kmlev[6];
$Nimg[$B]     = $Kimg[6];
$Nhp[$B]      = $Khp[6];
$Nmhp[$B]     = $Kmhp[6];
$Nmp[$B]      = $Kmp[6];
$Nmmp[$B]     = $Kmmp[6];
$Nkou[$B]     = $Kkou[6];
$Nmam[$B]     = $Kmam[6];
$Nsub[$B]     = $Ksub[6];
$Nhai[$B]     = $Khai[6];
$Ncount[$B]   = $Kcount[6];
$Nnecount[$B] = $Knecount[6];
$Nsex[$B]     = $Ksex[6];
$Nsei[$B]     = $Ksei[6];
}
if($cname[7] == $B){
$Nlev[$B]     = $Klev[7];
$Nmlev[$B]    = $Kmlev[7];
$Nimg[$B]     = $Kimg[7];
$Nhp[$B]      = $Khp[7];
$Nmhp[$B]     = $Kmhp[7];
$Nmp[$B]      = $Kmp[7];
$Nmmp[$B]     = $Kmmp[7];
$Nkou[$B]     = $Kkou[7];
$Nmam[$B]     = $Kmam[7];
$Nsub[$B]     = $Ksub[7];
$Nhai[$B]     = $Khai[7];
$Ncount[$B]   = $Kcount[7];
$Nnecount[$B] = $Knecount[7];
$Nsex[$B]     = $Ksex[7];
$Nsei[$B]     = $Ksei[7];
}
if($cname[8] == $B){
$Nlev[$B]     = $Klev[8];
$Nmlev[$B]    = $Kmlev[8];
$Nimg[$B]     = $Kimg[8];
$Nhp[$B]      = $Khp[8];
$Nmhp[$B]     = $Kmhp[8];
$Nmp[$B]      = $Kmp[8];
$Nmmp[$B]     = $Kmmp[8];
$Nkou[$B]     = $Kkou[8];
$Nmam[$B]     = $Kmam[8];
$Nsub[$B]     = $Ksub[8];
$Nhai[$B]     = $Khai[8];
$Ncount[$B]   = $Kcount[8];
$Nnecount[$B] = $Knecount[8];
$Nsex[$B]     = $Ksex[8];
$Nsei[$B]     = $Ksei[8];
}
if($cname[9] == $B){
$Nlev[$B]     = $Klev[9];
$Nmlev[$B]    = $Kmlev[9];
$Nimg[$B]     = $Kimg[9];
$Nhp[$B]      = $Khp[9];
$Nmhp[$B]     = $Kmhp[9];
$Nmp[$B]      = $Kmp[9];
$Nmmp[$B]     = $Kmmp[9];
$Nkou[$B]     = $Kkou[9];
$Nmam[$B]     = $Kmam[9];
$Nsub[$B]     = $Ksub[9];
$Nhai[$B]     = $Khai[9];
$Ncount[$B]   = $Kcount[9];
$Nnecount[$B] = $Knecount[9];
$Nsex[$B]     = $Ksex[9];
$Nsei[$B]     = $Ksei[9];
}
if($cname[10] == $B){
$Nlev[$B]     = $Klev[10];
$Nmlev[$B]    = $Kmlev[10];
$Nimg[$B]     = $Kimg[10];
$Nhp[$B]      = $Khp[10];
$Nmhp[$B]     = $Kmhp[10];
$Nmp[$B]      = $Kmp[10];
$Nmmp[$B]     = $Kmmp[10];
$Nkou[$B]     = $Kkou[10];
$Nmam[$B]     = $Kmam[10];
$Nsub[$B]     = $Ksub[10];
$Nhai[$B]     = $Khai[10];
$Ncount[$B]   = $Kcount[10];
$Nnecount[$B] = $Knecount[10];
$Nsex[$B]     = $Ksex[10];
$Nsei[$B]     = $Ksei[10];
}
}

if($Nhp[1] == 0){&error("No.1は必ず生存中のモンスターを設定をしてください");}

$newline = "$Kname<>$Kpass<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Nlev[3]<>$Nmlev[3]<>$Nimg[3]<>$Nhp[3]<>$Nmhp[3]<>$Nmp[3]<>$Nmmp[3]<>$Nkou[3]<>$Nmam[3]<>$Nsub[3]<>$Nhai[3]<>$Ncount[3]<>$Nnecount[3]<>$Nsex[3]<>$Nsei[3]<>$Nlev[4]<>$Nmlev[4]<>$Nimg[4]<>$Nhp[4]<>$Nmhp[4]<>$Nmp[4]<>$Nmmp[4]<>$Nkou[4]<>$Nmam[4]<>$Nsub[4]<>$Nhai[4]<>$Ncount[4]<>$Nnecount[4]<>$Nsex[4]<>$Nsei[4]<>$Nlev[5]<>$Nmlev[5]<>$Nimg[5]<>$Nhp[5]<>$Nmhp[5]<>$Nmp[5]<>$Nmmp[5]<>$Nkou[5]<>$Nmam[5]<>$Nsub[5]<>$Nhai[5]<>$Ncount[5]<>$Nnecount[5]<>$Nsex[5]<>$Nsei[5]<>$Nlev[6]<>$Nmlev[6]<>$Nimg[6]<>$Nhp[6]<>$Nmhp[6]<>$Nmp[6]<>$Nmmp[6]<>$Nkou[6]<>$Nmam[6]<>$Nsub[6]<>$Nhai[6]<>$Ncount[6]<>$Nnecount[6]<>$Nsex[6]<>$Nsei[6]<>$Nlev[7]<>$Nmlev[7]<>$Nimg[7]<>$Nhp[7]<>$Nmhp[7]<>$Nmp[7]<>$Nmmp[7]<>$Nkou[7]<>$Nmam[7]<>$Nsub[7]<>$Nhai[7]<>$Ncount[7]<>$Nnecount[7]<>$Nsex[7]<>$Nsei[7]<>$Nlev[8]<>$Nmlev[8]<>$Nimg[8]<>$Nhp[8]<>$Nmhp[8]<>$Nmp[8]<>$Nmmp[8]<>$Nkou[8]<>$Nmam[8]<>$Nsub[8]<>$Nhai[8]<>$Ncount[8]<>$Nnecount[8]<>$Nsex[8]<>$Nsei[8]<>$Nlev[9]<>$Nmlev[9]<>$Nimg[9]<>$Nhp[9]<>$Nmhp[9]<>$Nmp[9]<>$Nmmp[9]<>$Nkou[9]<>$Nmam[9]<>$Nsub[9]<>$Nhai[9]<>$Ncount[9]<>$Nnecount[9]<>$Nsex[9]<>$Nsei[9]<>$Nlev[10]<>$Nmlev[10]<>$Nimg[10]<>$Nhp[10]<>$Nmhp[10]<>$Nmp[10]<>$Nmmp[10]<>$Nkou[10]<>$Nmam[10]<>$Nsub[10]<>$Nhai[10]<>$Ncount[10]<>$Nnecount[10]<>$Nsex[10]<>$Nsei[10]<>$Kdummy<>$Kkey<>$Kmoney";
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
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>$Yplay3<>$Ykey<>$Nimg[1]<>$Nhai[1]<>$Nlev[1]<>$Nimg[2]<>$Nhai[2]<>$Nlev[2]<>$Nimg[3]<>$Nhai[3]<>$Nlev[3]<>$Ymoney<>$Ymes<>$turn";

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
<FONT size="5pt" color="#0000FF"><B>並べ替えが完了しました</B>
</FONT>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$Kname">
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
&footer;
