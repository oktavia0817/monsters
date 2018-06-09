use utf8;
use open IO => ":utf8";
use open ":std";

$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$KEYGET   = $FORM{'KEYGET'};

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay1,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    if($turn == 66){
    if($Yplay3 == 55){ &error("KEYの不正取得です");}
}
}
}

open(FH,"keyset/$inname.cgi");
@keyset1 = <FH>;
close(FH);
foreach $line5 (@keyset1) {
   ($fusi[1],$fusi[2],$fusi[3],$fusi[4],$fusi[5],$fusi[6],$fusi[7],$fusi[8],$fusi[9],$fusi[10])=split(/<>/,$line5);
}

if($KEYGET==1){
$fusi[1] = 1;
}
if($KEYGET==2){
$fusi[2] = 2;
}
if($KEYGET==3){
$fusi[3] = 3;
}
if($KEYGET==4){
$fusi[4] = 4;
}
if($KEYGET==5){
$fusi[5] = 5;
}
if($KEYGET==6){
$fusi[6] = 6;
}
if($KEYGET==7){
$fusi[7] = 7;
}
if($KEYGET==8){
$fusi[8] = 8;
}
if($KEYGET==9){
$fusi[9] = 9;
}
if($KEYGET==10){
$fusi[10] = 10;
}

@nbs1 = "$fusi[1]<>$fusi[2]<>$fusi[3]<>$fusi[4]<>$fusi[5]<>$fusi[6]<>$fusi[7]<>$fusi[8]<>$fusi[9]<>$fusi[10]";

&lock;
open(FH, ">keyset/$inname.cgi") || &error("Can't open!");
print FH @nbs1;
close(FH);
&unlock;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    $line = "$Yname<>$Ypass<>Yip<>$Ybye<>$Yplay<>$Yplay2<>55<>$Ykey<>$Yimg1<>$Yhai1<>$Ylev1<>$Yimg2<>$Yhai2<>$Ylev2<>$Yimg3<>$Yhai3<>$Ylev3<>$Ymoney<>$Ymes<>$turn";

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
<FONT size="5pt" color="#0000FF"><B>$keylist[$KEYGET] を入手した！</B></FONT><BR>
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

