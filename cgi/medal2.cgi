use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$Kmoney   = $FORM{'money'};
$kounyu  = 100000000;

$newmoney = $Kmoney - $kounyu;
if($newmoney < 0) { &error("お金が足りません");}

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="700" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>「1億ゴールド」と「配合100回スライム」を交換出来ます。交換しますか？</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="交換する">
<INPUT type="hidden" name="mode" value="medalok2">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="kounyu" value="$kounyu">
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
