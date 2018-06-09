use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};

&open1;

&header;
print <<"EOF";
<CENTER>
<TABLE width="600">
<TBODY>
<TR>
<TD align="center" bgcolor="#ff80ff" height="43"><B><FONT size="+2">性格変更本屋さん</FONT></B></TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
<P align="center">モンスターに本を読ませると性格が変わります。<BR>
現在の性格によっては変わらない場合もあります。<BR>
<BR>
<FONT color="#ff0000"><B>現在のステータス</B></FONT></P>
<CENTER>
<TABLE border="1" bgcolor="#0000ff">
<TBODY>
<TR>
<TD bgcolor="#ffff00" width="150" align="center">1</TD>
<TD bgcolor="#ffff00" width="150" align="center">2</TD>
<TD bgcolor="#ffff00" width="150" align="center">3</TD>
<TD bgcolor="#ffff00" width="150" align="center">4</TD>
<TD bgcolor="#ffff00" width="150" align="center">5</TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[1].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[1]] $seibetu[$Ksex[1]]</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[2].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[2]] $seibetu[$Ksex[2]]</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[3].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[3]] $seibetu[$Ksex[3]]</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[4].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[4]] $seibetu[$Ksex[4]]</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[5].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[5]] $seibetu[$Ksex[5]]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[1]]</TD>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[2]]</TD>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[3]]</TD>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[4]]</TD>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[5]]</TD>
</TR>
<TR>
<TD bgcolor="#ffff00" width="150" align="center">6</TD>
<TD bgcolor="#ffff00" width="150" align="center">7</TD>
<TD bgcolor="#ffff00" width="150" align="center">8</TD>
<TD bgcolor="#ffff00" width="150" align="center">9</TD>
<TD bgcolor="#ffff00" width="150" align="center">10</TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[6].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[6]] $seibetu[$Ksex[6]]</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[7].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[7]] $seibetu[$Ksex[7]]</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[8].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[8]] $seibetu[$Ksex[8]]</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[9].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[9]] $seibetu[$Ksex[9]]</TD>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg[10].gif" border="0" bgcolor="#ffffff"><BR>$itemlist[$Kimg[10]] $seibetu[$Ksex[10]]</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[6]]</TD>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[7]]</TD>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[8]]</TD>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[9]]</TD>
<TD bgcolor="#ffffff" width="150" align="center">$seikaku[$Ksei[10]]</TD>
</TR>
</TBODY>
</TABLE>
<BR>
<FONT color="#ff0000"><B>本一覧</B></FONT></P>
<TABLE bgcolor="#000000">
<TBODY>
<TR>
<TD align="center"  bgcolor="#ffffff" width="120" valign="top">ぼうけんたん<BR>
【1000<B>G</B>】</TD>
<TD align="center"  bgcolor="#ffffff" width="120" valign="top">こわいはなしの本<BR>
【1000<B>G</B>】</TD>
<TD align="center"  bgcolor="#ffffff" width="120" valign="top">やさしくなれる本<BR>
【1000<B>G</B>】</TD>
<TD align="center"  bgcolor="#ffffff" width="120" valign="top">ずるっこの本<BR>
【1000<B>G</B>】</TD>
<TD align="center"  bgcolor="#ffffff" width="120" valign="top">あたまがさえる本<BR>
【1000<B>G</B>】</TD>
<TD align="center"  bgcolor="#ffffff" width="120" valign="top">ユーモアの本<BR>
【1000<B>G</B>】</TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
<FORM ACTION="$cgiurl" METHOD="POST">
<P align="center">モンスターを選択して下さい</P>
<CENTER>
<SELECT name=Mname>
<option value=1 SELECTED>1-$itemlist[$Kimg[1]]
EOF
if($Kimg[2] != 0){
print <<"EOF";
<option value=2>2-$itemlist[$Kimg[2]]
EOF
}
if($Kimg[3] != 0){
print <<"EOF";
<option value=3>3-$itemlist[$Kimg[3]]
EOF
}
if($Kimg[4] != 0){
print <<"EOF";
<option value=4>4-$itemlist[$Kimg[4]]
EOF
}
if($Kimg[5] != 0){
print <<"EOF";
<option value=5>5-$itemlist[$Kimg[5]]
EOF
}
if($Kimg[6] != 0){
print <<"EOF";
<option value=6>6-$itemlist[$Kimg[6]]
EOF
}
if($Kimg[7] != 0){
print <<"EOF";
<option value=7>7-$itemlist[$Kimg[7]]
EOF
}
if($Kimg[8] != 0){
print <<"EOF";
<option value=8>8-$itemlist[$Kimg[8]]
EOF
}
if($Kimg[9] != 0){
print <<"EOF";
<option value=9>9-$itemlist[$Kimg[9]]
EOF
}
if($Kimg[10] != 0){
print <<"EOF";
<option value=10>10-$itemlist[$Kimg[10]]
EOF
}
print <<"EOF";
</SELECT>
<P align="center">
本を選択して下さい</P>
<SELECT name=Bname>
<option value=1 SELECTED>1-ぼうけんたん
<option value=2>2-こわいはなしの本
<option value=3>3-やさしくなれる本
<option value=4>4-ずるっこの本
<option value=5>5-あたまがさえる本
<option value=6>6-ユーモアの本
</SELECT>
<BR>
<BR>
<INPUT type="hidden" name="mode" value="readbook">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit" value="決 定">
</FORM>
<BR>
<BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="キャンセル">
</FORM>
</CENTER>
EOF
&footer;
