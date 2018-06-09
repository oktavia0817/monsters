use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$bpass  = $FORM{'bpass'};
$bname  = $FORM{'bname'};
$bbsno   = $FORM{'DEL'};
$type   = $FORM{'type'};

if($bbsno == 0){ &error("削除するメッセージが選択されていません");}

open(FH,"bbs/$inname.cgi") || &error("Can't open!");
@bbs1 = <FH>;
close(FH);

foreach $line (@bbs1) {
   ($bname1,$bb1,$bname2,$bb2,$bname3,$bb3,$bname4,$bb4,$bname5,$bb5,$bname6,$bb6,$bname7,$bb7,$bname8,$bb8,$bname9,$bb9,$bname10,$bb10)=split(/<>/,$line);
}

$mes = "NO.$bbsnoにはコメントが書かれてません";

if($bbsno == 1){
if($bb1 eq ""){ &error("$mes");}
@nbs1 = "$bname2<>$bb2<>$bname3<>$bb3<>$bname4<>$bb4<>$bname5<>$bb5<>$bname6<>$bb6<>$bname7<>$bb7<>$bname8<>$bb8<>$bname9<>$bb9<>$bname10<>$bb10";
}
if($bbsno == 2){
if($bb2 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname3<>$bb3<>$bname4<>$bb4<>$bname5<>$bb5<>$bname6<>$bb6<>$bname7<>$bb7<>$bname8<>$bb8<>$bname9<>$bb9<>$bname10<>$bb10";
}
if($bbsno == 3){
if($bb3 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname2<>$bb2<>$bname4<>$bb4<>$bname5<>$bb5<>$bname6<>$bb6<>$bname7<>$bb7<>$bname8<>$bb8<>$bname9<>$bb9<>$bname10<>$bb10";
}
if($bbsno == 4){
if($bb4 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname2<>$bb2<>$bname3<>$bb3<>$bname5<>$bb5<>$bname6<>$bb6<>$bname7<>$bb7<>$bname8<>$bb8<>$bname9<>$bb9<>$bname10<>$bb10";
}
if($bbsno == 5){
if($bb5 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname2<>$bb2<>$bname3<>$bb3<>$bname4<>$bb4<>$bname6<>$bb6<>$bname7<>$bb7<>$bname8<>$bb8<>$bname9<>$bb9<>$bname10<>$bb10";
}
if($bbsno == 6){
if($bb6 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname2<>$bb2<>$bname3<>$bb3<>$bname4<>$bb4<>$bname5<>$bb5<>$bname7<>$bb7<>$bname8<>$bb8<>$bname9<>$bb9<>$bname10<>$bb10";
}
if($bbsno == 7){
if($bb7 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname2<>$bb2<>$bname3<>$bb3<>$bname4<>$bb4<>$bname5<>$bb5<>$bname6<>$bb6<>$bname8<>$bb8<>$bname9<>$bb9<>$bname10<>$bb10";
}
if($bbsno == 8){
if($bb8 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname2<>$bb2<>$bname3<>$bb3<>$bname4<>$bb4<>$bname5<>$bb5<>$bname6<>$bb6<>$bname7<>$bb7<>$bname9<>$bb9<>$bname10<>$bb10";
}
if($bbsno == 9){
if($bb9 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname2<>$bb2<>$bname3<>$bb3<>$bname4<>$bb4<>$bname5<>$bb5<>$bname6<>$bb6<>$bname7<>$bb7<>$bname8<>$bb8<>$bname10<>$bb10";
}
if($bbsno == 10){
if($bb10 eq ""){ &error("$mes");}
@nbs1 = "$bname1<>$bb1<>$bname2<>$bb2<>$bname3<>$bb3<>$bname4<>$bb4<>$bname5<>$bb5<>$bname6<>$bb6<>$bname7<>$bb7<>$bname8<>$bb8<>$bname9<>$bb9";
}

&lock;
open(FH, ">bbs/$inname.cgi") || &error("Can't open!");
print FH @nbs1;
close(FH);
&unlock;

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>NO.$bbsnoのコメントを削除しました</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="submit"  value="LOGIN">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="type" value="$type">
<INPUT type="hidden" name="bname" value="$bname">
<INPUT type="hidden" name="bpass" value="$bpass">
</FORM>
<BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOP">
</CENTER>
</FORM>
EOF

&footer;
