use utf8;
use open IO => ":utf8";
use open ":std";

$Kname  = $FORM{'kname'};
$bpass  = $FORM{'bpass'};
$bname  = $FORM{'bname'};
$type   = $FORM{'type'};
$inname = $FORM{'BBNAME'};

&header;

open(FH,"bbs/$inname.cgi") || &error("Can't open! $inname");
@bbs1 = <FH>;
close(FH);
foreach $line (@bbs1) {
   ($bname[1],$bb[1],$bname[2],$bb[2],$bname[3],$bb[3],$bname[4],$bb[4],$bname[5],$bb[5],$bname[6],$bb[6],$bname[7],$bb[7],$bname[8],$bb[8],$bname[9],$bb[9],$bname[10],$bb[10])=split(/<>/,$line);
}

print <<"EOF";
<CENTER>
<BR>
<FONT size="5pt"><B>$innameさんの掲示板</B></FONT>
<BR><BR>
<TABLE bgcolor="#000000" width="70%">
<TBODY>
<TR>
<TD bgcolor="#99ccff" align="center"><FONT color="red"><B>【注意】</B></FONT><FONT color="black"><B> </B>パスワードが違うと書き込めません</FONT></TD>
</TR>
<TR>
<TD bgcolor="#99ccff" align="center">
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT size="20" type="text" name="bname" value="$bname">
<INPUT size="10" type="password" name="bpass" value="$bpass">
<INPUT type="hidden" name="type" value="$type">
<INPUT type="hidden" name="mode" value="bbs3">
<INPUT type="hidden" name="kname" value="$Kname">
<INPUT type="hidden" name="BBNAME" value="$inname">
<INPUT type="submit"  value="書込み">
<BR>
<INPUT size="77" type="text" name="bbs">
</TD>
</TR>
</FORM>
</TBODY>
</TABLE>
<BR>
<TABLE border="0" bgcolor="#000000">
<TBODY>
EOF
for($B=1;$B<11;$B++){
print <<"EOF";
<TR>
<TD bgcolor="#ffffff" align="center"><B>$B</B></TD>
<TD bgcolor="#99ccff" width="100"><FONT color="black" size="3">$bname[$B]</FONT></TD>
<TD bgcolor="#99ccff" width="600"><FONT color="black" size="3">$bb[$B]</FONT></TD>
</TR>
EOF
}
print <<"EOF";
</TBODY>
</TABLE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT TYPE="BUTTON" VALUE="CLOSE" onClick="window.close()">
</FORM>
</CENTER>
</BODY>
</HTML>
EOF

