use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="700" height="70" align="center">
<HR>
<FONT size="5pt" color="red"><B>本当にゲームを削除して良いですか？30日間登録出来なくなりますよ？</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="承諾して放棄する">
<INPUT type="hidden" name="mode" value="delete2">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
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
