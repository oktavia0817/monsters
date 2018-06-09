use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$Kmoney   = $FORM{'money'};
$seiten   = $FORM{'seiten'};

&open1;
$Tmoney = $Khai[$seiten] * 100;
if($Kmoney < $Tmoney){&error("お金が足りません");}

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>性別変換しますか？</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="変換する">
<INPUT type="hidden" name="mode" value="seitenok">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="Tmoney" value="$Tmoney">
<INPUT type="hidden" name="seiten" value="$seiten">
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
