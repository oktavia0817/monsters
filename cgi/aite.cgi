use utf8;
use open IO => ":utf8";
use open ":std";

&countchange;

sub kai {

$keitou = $FORM{'keitou'};

if($keitou == 0){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (1,2,3,21,22,23,46,47,48,71,72,91,92,111,112,131,132,133,156,157,176,177,178);
$ten = $ransu[(rand(23))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (3,4,5,24,25,26,49,50,51,73,74,93,94,113,114,134,135,136,158,159,179,180,181);
$ten = $ransu[(rand(23))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (5,6,7,27,28,29,52,53,54,75,76,95,96,115,116,137,138,139,160,161,182,183,184);
$ten = $ransu[(rand(23))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (7,8,9,30,31,32,55,56,57,77,78,97,98,117,118,140,141,142,162,163,185,186,187);
$ten = $ransu[(rand(23))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (9,10,11,33,34,35,58,59,60,79,80,99,100,119,120,143,144,145,164,165,188,189,190);
$ten = $ransu[(rand(23))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (11,12,13,36,37,38,61,62,63,81,82,101,102,121,122,146,147,148,166,167,191,192,193);
$ten = $ransu[(rand(23))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (13,14,15,39,40,41,64,65,66,83,84,103,104,123,124,125,149,150,151,168,169,194,195,196);
$ten = $ransu[(rand(24))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (16,17,18,42,43,67,68,85,86,87,105,106,107,126,127,128,152,153,170,171,172,173,197,198);
$ten = $ransu[(rand(24))];
}
if($inkai >= 201 && $inkai <= 500) {
@ransu = (19,20,44,45,69,70,88,89,90,108,109,110,129,130,154,155,174,175,199,200);
$ten = $ransu[(rand(20))];
}
if($inkai >= 501 && $inkai <= 1000) {
@ransu = (215,201,202,203,204,205,206,207,208,209,210,211,212,213,214,110);
$ten = $ransu[(rand(16))];
}
if($inkai >= 1001) {
@ransu = (220,221,222,223,224,225);
$ten = $ransu[(rand(6))];
}
}

if($keitou == 1){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (1,2,3);
$ten = $ransu[(rand(3))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (3,4,5);
$ten = $ransu[(rand(3))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (5,6,7);
$ten = $ransu[(rand(3))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (7,8,9);
$ten = $ransu[(rand(3))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (9,10,11);
$ten = $ransu[(rand(3))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (11,12,13);
$ten = $ransu[(rand(3))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (13,14,15);
$ten = $ransu[(rand(3))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (16,17,18);
$ten = $ransu[(rand(3))];
}
if($inkai >= 201 && $$inkai <= 500) {
@ransu = (19,20);
$ten = $ransu[(rand(2))];
}
if($inkai >= 501) {
@ransu = (217,218,219);
$ten = $ransu[(rand(3))];
}
}

if($keitou == 2){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (21,22,23);
$ten = $ransu[(rand(3))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (24,25,26);
$ten = $ransu[(rand(3))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (27,28,29);
$ten = $ransu[(rand(3))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (30,31,32);
$ten = $ransu[(rand(3))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (33,34,35);
$ten = $ransu[(rand(3))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (36,37,38);
$ten = $ransu[(rand(3))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (39,40,41);
$ten = $ransu[(rand(3))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (42,43);
$ten = $ransu[(rand(2))];
}
if($inkai >= 201) {
@ransu = (44,45);
$ten = $ransu[(rand(2))];
}

}

if($keitou == 3){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (46,47,48);
$ten = $ransu[(rand(3))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (49,50,51);
$ten = $ransu[(rand(3))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (52,53,54);
$ten = $ransu[(rand(3))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (55,56,57);
$ten = $ransu[(rand(3))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (58,59,60);
$ten = $ransu[(rand(3))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (61,62,63);
$ten = $ransu[(rand(3))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (64,65,66);
$ten = $ransu[(rand(3))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (67,68);
$ten = $ransu[(rand(2))];
}
if($inkai >= 201) {
@ransu = (69,70);
$ten = $ransu[(rand(2))];
}
}

if($keitou == 4){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (71,72);
$ten = $ransu[(rand(2))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (73,74);
$ten = $ransu[(rand(2))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (75,76);
$ten = $ransu[(rand(2))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (77,78);
$ten = $ransu[(rand(2))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (79,80);
$ten = $ransu[(rand(2))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (81,82);
$ten = $ransu[(rand(2))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (83,84);
$ten = $ransu[(rand(2))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (85,86,87);
$ten = $ransu[(rand(3))];
}
if($inkai >= 201) {
@ransu = (88,89,90);
$ten = $ransu[(rand(3))];
}
}

if($keitou == 5){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (91,92);
$ten = $ransu[(rand(2))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (93,94);
$ten = $ransu[(rand(2))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (95,96);
$ten = $ransu[(rand(2))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (97,98);
$ten = $ransu[(rand(2))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (99,100);
$ten = $ransu[(rand(2))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (101,102);
$ten = $ransu[(rand(2))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (103,104);
$ten = $ransu[(rand(2))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (105,106,107);
$ten = $ransu[(rand(3))];
}
if($inkai >= 201) {
@ransu = (108,109,110);
$ten = $ransu[(rand(3))];
}
}

if($keitou == 6){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (111,112);
$ten = $ransu[(rand(2))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (113,114);
$ten = $ransu[(rand(2))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (115,116);
$ten = $ransu[(rand(2))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (117,118);
$ten = $ransu[(rand(2))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (119,120);
$ten = $ransu[(rand(2))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (121,122);
$ten = $ransu[(rand(2))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (123,124,125);
$ten = $ransu[(rand(3))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (126,127,128);
$ten = $ransu[(rand(3))];
}
if($inkai >= 201) {
@ransu = (129,130);
$ten = $ransu[(rand(2))];
}
}

if($keitou == 7){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (131,132,133);
$ten = $ransu[(rand(3))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (134,135,136);
$ten = $ransu[(rand(3))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (137,138,139);
$ten = $ransu[(rand(3))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (140,141,142);
$ten = $ransu[(rand(3))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (143,144,145);
$ten = $ransu[(rand(3))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (146,147,148);
$ten = $ransu[(rand(3))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (149,150,151);
$ten = $ransu[(rand(3))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (152,153);
$ten = $ransu[(rand(2))];
}
if($inkai >= 201) {
@ransu = (154,155);
$ten = $ransu[(rand(2))];
}
if($inkai == 501) { @ransu = (154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,155,154,238); 
$ten = $ransu[(rand(40))]; }
}

if($keitou == 8){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (156,157);
$ten = $ransu[(rand(2))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (158,159);
$ten = $ransu[(rand(2))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (160,161);
$ten = $ransu[(rand(2))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (162,163);
$ten = $ransu[(rand(2))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (164,165);
$ten = $ransu[(rand(2))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (166,167);
$ten = $ransu[(rand(2))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (168,169);
$ten = $ransu[(rand(2))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (170,171,172,173);
$ten = $ransu[(rand(4))];
}
if($inkai >= 201 && $$inkai <= 1000) {
@ransu = (174,175);
$ten = $ransu[(rand(2))];
}
if($inkai >= 1001) {
@ransu = (238,239,240,241,242);
$ten = $ransu[(rand(5))];
}
}

if($keitou == 9){

if($inkai >= 1 && $inkai <= 25) {
@ransu = (176,177,178);
$ten = $ransu[(rand(3))];
}
if($inkai >= 26 && $inkai <= 50) {
@ransu = (179,180,181);
$ten = $ransu[(rand(3))];
}
if($inkai >= 51 && $inkai <= 75) {
@ransu = (182,183,184);
$ten = $ransu[(rand(3))];
}
if($inkai >= 76 && $$inkai <= 100) {
@ransu = (185,186,187);
$ten = $ransu[(rand(3))];
}
if($inkai >= 101 && $inkai <= 125) {
@ransu = (188,189,190);
$ten = $ransu[(rand(3))];
}
if($inkai >= 126 && $inkai <= 150) {
@ransu = (191,192,193);
$ten = $ransu[(rand(3))];
}
if($inkai >= 151 && $inkai <= 175) {
@ransu = (194,195,196);
$ten = $ransu[(rand(3))];
}
if($inkai >= 176 && $$inkai <= 200) {
@ransu = (197,198);
$ten = $ransu[(rand(2))];
}
if($inkai >= 201) {
@ransu = (199,200);
$ten = $ransu[(rand(2))];
}
}

if($keitou == 10){

if($inkai >= 1 && $inkai <= 500) {
@ransu = (201,202,203,204,205,206,207);
$ten = $ransu[(rand(7))];
}
if($inkai >= 501 && $inkai <= 1000) {
@ransu = (208,209,210,211,212,213,214,215);
$ten = $ransu[(rand(8))];
}
if($inkai >= 1001) {
@ransu = (226,227,228,229,232,233,234,235,236,237);
$ten = $ransu[(rand(10))];
}
}

}

$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$Ypass  = $FORM{'loginpass'};
$inkai  = $FORM{'kai'};
$Iii    = $FORM{'rank'};
$Ssu    = $FORM{'Ssu'};

$Yname = $inname;
$Ikai  = $inkai;
$ROOM  = $FORM{'keitou'};

&set_cookie;

if($inkai eq ""){&error("まだクッキーに保存されてません");}

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass1,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    $passcheck = crypt($Ypass, $inname);
    if($passcheck ne $Ypass1) {&error("パスワードが違います");}
    if($Yplay > time){&error("戦闘の仕切りなおしは出来ません");}
    $Kkey     = $Ykey;
    $newbye   =  (time + ($goodbye * 24 * 60 * 60));
    $newplay  =  (time + ($nexpplay * 60));
    $line = "$Yname<>$Ypass1<>$Yip<>$Ybye<>$newplay<>$Yplay2<>0<>$Ykey<>$Yimg1<>$Yhai1<>$Ylev1<>$Yimg2<>$Yhai2<>$Ylev2<>$Yimg3<>$Yhai3<>$Ylev3<>$Ymoney<>$Ymes<>0\n";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
}
}


########################################################################


@ransu7 = (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
$med = $ransu7[(rand(30))];
if($med == 1){

@ransu8 = (1,0,0);
$med2 = $ransu8[(rand(3))];
if($med2 == 1){

open(FH,"keyset/$inname.cgi");
@keyset1 = <FH>;
close(FH);
foreach $line5 (@keyset1) {
   ($fusi[1],$fusi[2],$fusi[3],$fusi[4],$fusi[5],$fusi[6],$fusi[7],$fusi[8],$fusi[9],$fusi[10])=split(/<>/,$line5);
}

if($fusi[1]==1 && $fusi[2]==2 && $fusi[3]==3 && $fusi[4]==4 && $fusi[5]==5 && $fusi[6]==6 && $fusi[7]==7 && $fusi[8]==8 && $fusi[9]==9 && $fusi[10]==10){
$med2=0;}
}

if($med2 == 1){

&open1;

$Kimg1 = $Kimg[1];
$Kimg2 = $Kimg[2];
$Kimg3 = $Kimg[3];

&open2;

$TD  = '<TD align=center width=150 bgcolor=#ffffff>';
$TD2 = '<TD width=150 bgcolor=#ffffff align=center><FONT color=#000000>';
$TD3 = '<TD align=center width=150 bgcolor=yellow>';

open(FH,"$monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
    if(1 == $Mimg){
    $Aimg[1]   = $Mimg;
    $Acname[1] = $Mcname;
    $Ahp[1]    = int($Mhp * $inkai+30);
    $Amhp[1]   = int($Mhp * $inkai+30);
    $Amp[1]    = int($Mmp * $inkai+30);
    $Ammp[1]   = int($Mmp * $inkai+30);
    $Akou[1]   = $Mkou * $inkai+30;
    $Amam[1]   = $Mmam * $inkai+30;
    $Amoney[1] = $Mmoney;
    $Aex[1]    = $Mex;
    @sexs = (1,2);
    $Asex[1] = $sexs[int(rand(2))];
}
}

&header;


print <<"EOF";
<BODY  background="$imgpath/back.gif">
<P align="center"><BR>
<FONT color="#FF0000" size="+2"><B>スライムの不思議な城に迷い込んだ！</B></FONT></P>
<CENTER>
<TABLE border="1">
<TBODY>
<TR>
<TD nowrap valign="top">
<CENTER>
<TABLE>
<TBODY>
<TR>
$TD<IMG src="$imgpath/$Aimg[1].gif" border=0><BR><B><FONT color=#0033CC>$Acname[1] - $seibetu[$Asex[1]]</FONT></B>が現れた！</TD>
</TR>
<TR>
$TD<FONT color=#FF0000><B>HP/MHP </B></FONT><B>  $Amhp[1]/$Amhp[1]</B></TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
</TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<BR>
<FONT color="#FF0000" size="+2"><B>勝利すれば不思議な鍵が貰えます！</B></FONT><BR>
<BR>
<TABLE border="1">
<TBODY>
<TR>
<TD>
<CENTER>
<TABLE>
<TBODY>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor=#ffffff colspan=\"2\" align=center><IMG src="$imgpath/$Kimg[1].gif" border=0><BR>$itemlist[$Kimg1]</TD>
</TR>
<TR>
$TD2<B>レベル</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><FONT color=#FF0000><B>$Klev[1]</B></FONT></TD>
</TR>
<TR>
$TD2<B>HP/MHP</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><B>$Khp[1]/$Kmhp[1]</B></TD>
</TR>
<TR>
$TD2<B>MP/MMP</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><B>$Kmp[1]/$Kmmp[1]</B></TD>
</TR>
<TR>

$TD3
選択して下さい
</TD>
<TD bgcolor=#ffffff>
<SELECT name="hit1">
<option value=1 SELECTED>攻撃する
</SELECT>
</TD>
</TR>
<TR>
$TD3
攻撃相手
</TD>
<TD bgcolor=#ffffff>
<SELECT name="teki1">
<option value=1 SELECTED>$Acname[1]
</SELECT>
</TD>
</TR>
<TR>
<TD colspan="7" bgcolor="#ffffff" align="center">
<BR>
<INPUT type="submit" name="medok" value="決定">
<INPUT type="hidden" name="mode" value="check3">
<INPUT type="hidden" name="monsuu" value="$monsuu">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$Ypass">
<INPUT type="hidden" name="Aimg1" value="$Aimg[1]">
<INPUT type="hidden" name="kai" value="$inkai">
<INPUT type="hidden" name="rank" value="$Iii">
<INPUT type="hidden" name="Ssu" value="$Ssu">
<INPUT type="hidden" name="Asex1" value="$Asex[1]">
<BR>
</FORM>
</TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
EOF
}

if($med2 == 0){

&open1;

$Kimg1 = $Kimg[1];
$Kimg2 = $Kimg[2];
$Kimg3 = $Kimg[3];

&open2;

$TD  = '<TD align=center width=150 bgcolor=#ffffff>';
$TD2 = '<TD width=150 bgcolor=#ffffff align=center><FONT color=#000000>';
$TD3 = '<TD align=center width=150 bgcolor=yellow>';

open(FH,"$monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
    if(110 == $Mimg){
    $Aimg[1]   = $Mimg;
    $Acname[1] = $Mcname;
    $Ahp[1]    = int($Mhp * $inkai);
    $Amhp[1]   = int($Mhp * $inkai);
    $Amp[1]    = int($Mmp * $inkai);
    $Ammp[1]   = int($Mmp * $inkai);
    $Akou[1]   = $Mkou * $inkai;
    $Amam[1]   = $Mmam * $inkai;
    $Amoney[1] = $Mmoney;
    $Aex[1]    = $Mex;
@sexs = (1,2);
$Asex[1] = $sexs[int(rand(2))];
}
}

&header;

print <<"EOF";
<BODY  background="$imgpath/back.gif">
<P align="center"><BR>
<FONT color="#FF0000" size="+2"><B>わたぼうのメダル城に迷い込んだ！</B></FONT></P>
<CENTER>
<TABLE border="1">
<TBODY>
<TR>
<TD nowrap valign="top">
<CENTER>
<TABLE>
<TBODY>
<TR>
$TD<IMG src="$imgpath/$Aimg[1].gif" border=0><BR><B><FONT color=#0033CC>$Acname[1] - $seibetu[$Asex[1]]</FONT></B>が現れた！</TD>
</TR>
<TR>
$TD<FONT color=#FF0000><B>HP/MHP </B></FONT><B>  $Amhp[1]/$Amhp[1]</B></TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
</TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<BR>
<FONT color="#FF0000" size="+2"><B>勝利すればメダルが3枚貰えます！</B></FONT><BR>
<BR>
<TABLE border="1">
<TBODY>
<TR>
<TD>
<CENTER>
<TABLE>
<TBODY>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor=#ffffff colspan=\"2\" align=center><IMG src="$imgpath/$Kimg[1].gif" border=0><BR>$itemlist[$Kimg1]</TD>
</TR>
<TR>
$TD2<B>レベル</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><FONT color=#FF0000><B>$Klev[1]</B></FONT></TD>
</TR>
<TR>
$TD2<B>HP/MHP</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><B>$Khp[1]/$Kmhp[1]</B></TD>
</TR>
<TR>
$TD2<B>MP/MMP</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><B>$Kmp[1]/$Kmmp[1]</B></TD>
</TR>
<TR>

$TD3
選択して下さい
</TD>
<TD bgcolor=#ffffff>
<SELECT name="hit1">
<option value=1 SELECTED>攻撃する
</SELECT>
</TD>
</TR>
<TR>
$TD3
攻撃相手
</TD>
<TD bgcolor=#ffffff>
<SELECT name="teki1">
<option value=1 SELECTED>$Acname[1]
</SELECT>
</TD>
</TR>
<TR>
<TD colspan="7" bgcolor="#ffffff" align="center">
<BR>
<INPUT type="submit" name="medok" value="決定">
<INPUT type="hidden" name="mode" value="check2">
<INPUT type="hidden" name="monsuu" value="$monsuu">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$Ypass">
<INPUT type="hidden" name="Aimg1" value="$Aimg[1]">
<INPUT type="hidden" name="kai" value="$inkai">
<INPUT type="hidden" name="rank" value="$Iii">
<INPUT type="hidden" name="Ssu" value="$Ssu">
<INPUT type="hidden" name="Asex1" value="$Asex[1]">
<BR>
</FORM>
</TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
EOF
}
}

if($med == 0){

########################################################################

&open1;

$Kimg1 = $Kimg[1];
$Kimg2 = $Kimg[2];
$Kimg3 = $Kimg[3];

$Ksei1 = $Ksei[1];
$Ksei2 = $Ksei[2];
$Ksei3 = $Ksei[3];

if($inkai>$Kkey){&error("既にその階のKEYは持っていません");}

if($Ssu >= 3 ){$Ssu = 3;}

&open2;

$TD  = '<TD align=center width=150 bgcolor=#ffffff>';
$TD2 = '<TD width=150 bgcolor=#ffffff align=center><FONT color=#000000>';
$TD3 = '<TD align=center width=150 bgcolor=yellow>';


@ransu0 = (1,1,1,2,2,3);
$monsuu = $ransu0[(rand(6))];


for($mo=1;$mo<=$monsuu;$mo++){

&kai;

open(FH,"$monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
    if($ten == $Mimg){
    $Aimg[$mo]   = $Mimg;
    $Acname[$mo] = $Mcname;
    $Ahp[$mo]    = int($Mhp * $inkai);
    $Amhp[$mo]   = int($Mhp * $inkai);
    $Amp[$mo]    = int($Mmp * $inkai);
    $Ammp[$mo]   = int($Mmp * $inkai);
    $Akou[$mo]   = $Mkou * $inkai;
    $Amam[$mo]   = $Mmam * $inkai;
    $Amoney[$mo] = $Mmoney;
    @sexs = (1,2);
    $Asex[$mo] = $sexs[int(rand(2))];
    $Aex[$mo]    = $Mex;
    last;}
}
}

if($Acname[1] eq $Acname[2] && $Acname[1] eq $Acname[3]){
$Acname[1] = "$Acname[1] A";
$Acname[2] = "$Acname[2] B";
$Acname[3] = "$Acname[3] C";
}
if($Acname[1] eq $Acname[2] && $Acname[1] ne $Acname[3]){
$Acname[1] = "$Acname[1] A";
$Acname[2] = "$Acname[2] B";
$Acname[3] = "$Acname[3]";
}
if($Acname[1] ne $Acname[2] && $Acname[1] eq $Acname[3]){
$Acname[1] = "$Acname[1] A";
$Acname[2] = "$Acname[2]";
$Acname[3] = "$Acname[3] B";
}
if($Acname[2] eq $Acname[3] && $Acname[1] ne $Acname[2]){
$Acname[1] = "$Acname[1]";
$Acname[2] = "$Acname[2] A";
$Acname[3] = "$Acname[3] B";
}

#@back = (1..11);
#$backl = $back[int(rand(11))];
#$backimg = "back$backl.png";

&header;

print <<"EOF";
<BODY>
<P align="center"><BR>
<FONT color="#FF0000" size="+2"><B>モンスターが$monsuu 体現れた！</B></FONT></P>
<CENTER>
<TABLE border="1">
<TBODY>
<TR>
<TD nowrap valign="top">
<CENTER>
<TABLE>
<TBODY>
<TR>
$TD<IMG src="$imgpath/$Aimg[1].gif" border=0><BR><B><FONT color=#0033CC>$Acname[1] - $seibetu[$Asex[1]]</FONT></B>が現れた！</TD>
EOF
if($monsuu == 2 or $monsuu == 3){
print <<"EOF";
$TD<IMG src="$imgpath/$Aimg[2].gif" border=0><BR><B><FONT color=#0033CC>$Acname[2] - $seibetu[$Asex[2]]</FONT></B>が現れた！</TD>
EOF
}
if($monsuu == 3){
print <<"EOF";
$TD<IMG src="$imgpath/$Aimg[3].gif" border=0><BR><B><FONT color=#0033CC>$Acname[3] - $seibetu[$Asex[3]]</FONT></B>が現れた！</TD>
EOF
}
print "</TR>\n";
print "<TR>\n";
print "$TD<FONT color=#FF0000><B>HP/MHP </B></FONT><B>  $Amhp[1]/$Amhp[1]</B></TD>\n";
if($monsuu == 2 or $monsuu == 3){
print "$TD<FONT color=#FF0000><B>HP/MHP </B></FONT><B>  $Amhp[2]/$Amhp[2]</B></TD>\n";
}
if($monsuu == 3){
print "$TD<FONT color=#FF0000><B>HP/MHP </B></FONT><B>  $Amhp[3]/$Amhp[3]</B></TD>\n";
}
print "</TR>\n";
print "<TR>\n";
print "$TD<B><FONT color=#FF0000>MP/MMP </FONT></B><B>  $Ammp[1]/$Ammp[1]</B></TD>\n";
if($monsuu == 2 or $monsuu == 3){
print "$TD<B><FONT color=#FF0000>MP/MMP </FONT></B><B>  $Ammp[2]/$Ammp[2]</B></TD>\n";
}
if($monsuu == 3){
print "$TD<B><FONT color=#FF0000>MP/MMP </FONT></B><B>  $Ammp[3]/$Ammp[3]</B></TD>\n";
}
print "</TR>\n";
print <<"EOF";
</TR>
</TBODY>
</TABLE>
</CENTER>
</TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<BR>
<FONT color="#FF0000" size="+2"><B>何を行うか決定して下さい！</B></FONT><BR>
<BR>
<TABLE>
<TBODY>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
EOF
for($x=1;$x<=3;$x++){
if($Khp[$x] != 0){

print <<"EOF";
<td>
<table>
	<tr>
		<TD colspan=2 align=center height="150px" valign="bottom"><IMG src="$imgpath/$Kimg[$x].gif" border=0><BR><font  color="white">$itemlist[${Kimg.$x}]</font></TD>
	</tr>
	<tr>
		$TD2<B>レベル</B></FONT></TD>
		<TD bgcolor=#ffffff align="center"><FONT color=#FF0000><B>$Klev[$x]</B></FONT></TD>
	</tr>
	<tr>
		$TD2<B>HP/MHP</B></FONT></TD>
		<TD bgcolor=#ffffff align="center"><B>$Khp[$x]/$Kmhp[$x]</B></TD>
	</tr>
	<tr>
		$TD2<B>MP/MMP</B></FONT></TD>
		<TD bgcolor=#ffffff align="center"><B>$Kmp[$x]/$Kmmp[$x]</B></TD>
	</tr>
	<tr>
		$TD3 選択して下さい</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="hit$x">
				<option value=1>攻撃する
				<option value=2>防御する
				<option value=3 SELECTED>特殊攻撃使用
				<option value=4>回復魔法使用
			</SELECT>
		</TD>
	</tr>
	<tr>
		$TD3 攻撃相手</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="teki$x">
EOF
				for($i=1;$i<=3;$i++){
					if($Ahp[$i] != 0){
						print "<option value=$i>$Acname[$i]\n"
					}
				}
print <<"EOF";
			</SELECT>
			</TD>
	</tr>
	<tr>
		$TD3 攻撃魔法</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="toku$x">
				<option value=99 SELECTED>通常攻撃
EOF
				for($t=1;$t<56;$t++){
					$T=$waza[$t];
					if($T != 0 && !($t == 3 or $t == 14 or $t == 37 or $t == 51 or $t == 52)){
						print "<option value=$t>$mtoku[$T] ($mtokump[$T] MP)\n"
					}
				}
print <<"EOF";
			</SELECT>
		</TD>
	</tr>
	<tr>
		$TD3 回復魔法相手</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="nakama$x">
EOF
				for($i=1;$i<=3;$i++){
					if($Ssu >= $i){
						print "<option value=$i>$itemlist[${Kimg.$i}]\n"
					}
				}
print <<"EOF";
			</SELECT>
		</TD>
	</tr>
	<tr>
		$TD3 回復魔法</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="ktoku$x">
				<option value=0 SELECTED>使用しない
EOF
				for($t=1;$t<56;$t++){
					$T=$waza[$t];
					if($T != 0 && ($t == 3 or $t == 14 or $t == 37 or $t == 51 or $t == 52)){
						print "<option value=$t>$mtoku[$T] ($mtokump[$T] MP)\n"
					}
				}
print <<"EOF";
			</SELECT>
		</TD>
	</tr>
</table>
EOF
}#HP判定if
}#for終了



print <<"EOF";
</TR>
<TR>
<TD colspan="7" align="center">
<BR>
<INPUT type="submit" name="monok" value="決定">
<INPUT type="hidden" name="mode" value="check">
<INPUT type="hidden" name="monsuu" value="$monsuu">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$Ypass">
<INPUT type="hidden" name="Aimg1" value="$Aimg[1]">
<INPUT type="hidden" name="Aimg2" value="$Aimg[2]">
<INPUT type="hidden" name="Aimg3" value="$Aimg[3]">
<INPUT type="hidden" name="kai" value="$inkai">
<INPUT type="hidden" name="rank" value="$Iii">
<INPUT type="hidden" name="Ssu" value="$Ssu">
<INPUT type="hidden" name="Ksei1" value="$Ksei1">
<INPUT type="hidden" name="Ksei2" value="$Ksei2">
<INPUT type="hidden" name="Ksei3" value="$Ksei3">
<INPUT type="hidden" name="Asex1" value="$Asex[1]">
<INPUT type="hidden" name="Asex2" value="$Asex[2]">
<INPUT type="hidden" name="Asex3" value="$Asex[3]">
<BR>
</FORM>
</TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
EOF

}######################################

&footer;

