use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$kyoukaidai  = $FORM{'kyoukaidai'};
$Kmoney   = $FORM{'money'};

$newmoney = $Kmoney - $kyoukaidai;
if($newmoney < 0) { &error("お金が足りません");}

if($kyoukaidai == 0){&error("現在お祈りする必要はありません");}

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>お祈りしますか？</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="お祈りする">
<INPUT type="hidden" name="mode" value="kyoukaiok">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="kyoukaidai" value="$kyoukaidai">
</FORM>
<BR>
<BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="キャンセル">
</FORM>
EOF
&footer;
