use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$yadodai  = $FORM{'yadodai'};
$Kmoney   = $FORM{'money'};

if($yadodai == 0){&error("現在宿泊する必要はありません");}

$newmoney = $Kmoney - $yadodai;
if($newmoney < 0) { &error("お金が足りません");}

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>宿泊しますか？</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="宿泊する">
<INPUT type="hidden" name="mode" value="yadook">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="yadodai" value="$yadodai">
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
