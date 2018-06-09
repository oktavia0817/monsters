use utf8;
use open IO => ":utf8";
use open ":std";
use Encode;

$Kname  = $FORM{'kname'};
$bpass  = $FORM{'bpass'};
$bname  = $FORM{'bname'};
$bbs    = $FORM{'bbs'};
$type   = $FORM{'type'};

$bbs = decode( "utf8", $bbs );

if($bname eq ''){&error("名前がありません");}
if($bpass eq ''){&error("パスワードがありません");}
$login = $bbsok;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($bname eq $Yname) {
    $passcheck = crypt($bpass, $bname);
    if($passcheck ne $Ypass) {&error("パスワードが違います");}
    $Kpass = $bpass;
    $login = 1; last;
}
}

if($login == 0){&error("参加者以外の人は書き込めません");}

$check = '<>';
$posi = index $bbs,$check;
if($posi ne -1 ){&error("$posi=posi【<>】この文字は使えません");}
if (length($FORM{'bbs'}) < 4 or length($FORM{'bbs'}) > 72){ &error("2文字以上、35文字以下で入力して下さい。");}

open(FH,"bbs/$Kname.cgi") || &error("Can't open!");
@bbs1 = <FH>;
close(FH);

foreach $line (@bbs1) {
   ($bname1,$bb1,$bname2,$bb2,$bname3,$bb3,$bname4,$bb4,$bname5,$bb5,$bname6,$bb6,$bname7,$bb7,$bname8,$bb8,$bname9,$bb9,$bname10,$bb10)=split(/<>/,$line);
}

$timelog = 2;
&gettime;

push @bbs,$bbs;
push @bbs,$Ktime;

@nbs1 = "$bname<>@bbs<>$bname1<>$bb1<>$bname2<>$bb2<>$bname3<>$bb3<>$bname4<>$bb4<>$bname5<>$bb5<>$bname6<>$bb6<>$bname7<>$bb7<>$bname8<>$bb8<>$bname9<>$bb9";

&lock;
open(FH, ">bbs/$Kname.cgi") || &error("Can't open!");
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
<FONT size="5pt" color="#0000FF"><B>書込みは正常終了しました</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$Kname">
<INPUT type="hidden" name="password" value="$Kpass">
<INPUT type="hidden" name="bname" value="$bname">
<INPUT type="hidden" name="bpass" value="$bpass">
<INPUT type="hidden" name="type" value="$type">
<INPUT type="submit"  value="LOGIN">
</FORM>
<BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOP">
</CENTER>
</FORM>
EOF

&footer;
