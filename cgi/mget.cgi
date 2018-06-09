use utf8;
use open IO => ":utf8";
use open ":std";


$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$Aimg   = $FORM{'Aimg'};
$Asex   = $FORM{'Asex'};

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    if($Yplay3 != 2){&error("仲間の不正取得は出来ません");}
    $ntime = time;
    if($Yplay < $ntime){&error("タイムオーバーのため さみしく帰っていった");}
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
    $Ahp    = int($Mhp * 2);
    $Amhp   = int($Mhp * 2);
    $Amp    = int($Mmp * 2);
    $Ammp   = int($Mmp * 2);
    $Akou   = int($Mkou * 2);
    $Amam   = int($Mmam * 2);
    $Asub   = int($Msub * 2);
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

&get;

if($pattern != 0){

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

if($good == 0){

&header;
print <<"EOF";
<SCRIPT LANGUAGE="JavaScript">
<!--
 Images = new Array();
    Images[0] = new Image();
    Images[1] = new Image();
    Images[2] = new Image();
    Images[3] = new Image();
    Images[4] = new Image();
    Images[5] = new Image();
    Images[6] = new Image();
    Images[7] = new Image();
    Images[8] = new Image();
    Images[9] = new Image();
    Images[10] = new Image();
    
    Images[0].src = "$imgpath/$Aimg.gif";
    Images[1].src = "$imgpath/$Kimg[1].gif";
    Images[2].src = "$imgpath/$Kimg[2].gif";
    Images[3].src = "$imgpath/$Kimg[3].gif";
    Images[4].src = "$imgpath/$Kimg[4].gif";
    Images[5].src = "$imgpath/$Kimg[5].gif";
    Images[6].src = "$imgpath/$Kimg[6].gif";
    Images[7].src = "$imgpath/$Kimg[7].gif";
    Images[8].src = "$imgpath/$Kimg[8].gif";
    Images[9].src = "$imgpath/$Kimg[9].gif";
    Images[10].src = "$imgpath/$Kimg[10].gif";    
    
    function change_img() {
  form1.img1.src = Images[ form1.MNAME.selectedIndex ].src;
 }
 //--->
 </SCRIPT>
<CENTER>
<TABLE border="1" height="122">
<TBODY>
<TR>
<TD align="center" width="600">モンスターが一杯です。<BR>
誰を仲間から外しますか？<BR>
<FORM name=form1 ACTION="./monster.cgi" METHOD="POST">
<SELECT name="MNAME" onClick="change_img()">
<option value=0 SELECTED>新しいモンスター : $itemlist[$Aimg] $seibetu[$Asex]</option>
<option value=1>01: $itemlist[$P1] $seibetu[$Ksex[1]] LV-$Klev[1] 配合$Khai[1]回</option>
<option value=2>02: $itemlist[$P2] $seibetu[$Ksex[2]] LV-$Klev[2] 配合$Khai[2]回</option>
<option value=3>03: $itemlist[$P3] $seibetu[$Ksex[3]] LV-$Klev[3] 配合$Khai[3]回</option>
<option value=4>04: $itemlist[$P4] $seibetu[$Ksex[4]] LV-$Klev[4] 配合$Khai[4]回</option>
<option value=5>05: $itemlist[$P5] $seibetu[$Ksex[5]] LV-$Klev[5] 配合$Khai[5]回</option>
<option value=6>06: $itemlist[$P6] $seibetu[$Ksex[6]] LV-$Klev[6] 配合$Khai[6]回</option>
<option value=7>07: $itemlist[$P7] $seibetu[$Ksex[7]] LV-$Klev[7] 配合$Khai[7]回</option>
<option value=8>08: $itemlist[$P8] $seibetu[$Ksex[8]] LV-$Klev[8] 配合$Khai[8]回</option>
<option value=9>09: $itemlist[$P9] $seibetu[$Ksex[9]] LV-$Klev[9] 配合$Khai[9]回</option>
<option value=10>10: $itemlist[$P10] $seibetu[$Ksex[10]] LV-$Klev[10] 配合$Khai[10]回</option>
</SELECT>
<INPUT type="submit" value="仲間から外す">
<INPUT type="hidden" name="mode" value="Mbye">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="Aimg" value="$Aimg">
<INPUT type="hidden" name="Asex" value="$Asex">
<BR>
<BR>
<IMG NAME="img1" SRC="$imgpath/$Aimg.gif">
</FORM>
</TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
EOF

}

&footer;

