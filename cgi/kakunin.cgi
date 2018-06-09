use utf8;
use open IO => ":utf8";
use open ":std";

$inname   = $FORM{'name'};

open(FH,"omiai/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);
}
if($Nimg[1] == 0){
$Nimg ='-';
}
$MONEY1 = $Nhai[1]*1000;
if($MONEY1 >= 99999){$MONEY1 = 99999;}
if($Nimg[1] != 0){
$Nimg ="$MONEY1ゴールド必要";
}
if($Nimg[2] == 0){
$Nimg2 ='-';
}
$MONEY2 = $Nhai[2]*1000;
if($MONEY2 >= 99999){$MONEY2 = 99999;}
if($Nimg[2] != 0){
$Nimg2 ="$MONEY2ゴールド必要";
}

if($Fimg[1] == 0){
$Fimg ='-';
}
if($Fimg[1] != 0){
$Fimg =$itemlist[$Fimg[1]];
}
if($Fimg[2] == 0){
$Fimg2 ='-';
}
if($Fimg[2] != 0){
$Fimg2 =$itemlist[$Fimg[2]];
}

if($Kimg[1] == 0){ 
$Aname[1] = '未設定';
$mes = '未設定';
}

if($Kimg[1] != 0){ 
$mes = '返事待ち';
}
if($Kimg[2] == 0){
$Aname[2]  = '依頼無し';
}

&header;
print <<"EOF";
<P><B><FONT size="+1">お見合い所 【お見合い料は無料ですが、誕生したモンスターをLOGIN画面に移動するには（配合回数×1000）ゴールド必要です】</FONT></B></P>
<HR>
<P>お見合いに出しているモンスター<BR>
</P>
<TABLE border="1">
<TBODY>
<TR>
<TD bgcolor="#ff0000" align="center"><B>相手ユーザー名</B></TD>
<TD bgcolor="#ff0000" align="center"><B>相手モンスター</B></TD>
<TD bgcolor="#ff0000" align="center"><B>相手モンスター名</B></TD>
<TD bgcolor="#00cccc" align="center"><B>自モンスター</B></TD>
<TD bgcolor="#00cccc" align="center"><B>自モンスター名</B></TD>
<TD rowspan="2" width="73" bgcolor="#ffffff" align="center">$mes</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$Aname[1]</TD>
<TD bgcolor="#ffffff" align="center">
EOF
if($Aimg[1] != 0){
print <<"EOF";
<IMG src="$imgpath/$Aimg[1].gif">
EOF
}
print <<"EOF";
</TD>
<TD bgcolor="#ffffff" align="center">$itemlist[$Aimg[1]] $seibetu[$Asex[1]]<BR>【$seikaku[$Asei[1]]】</TD>
<TD bgcolor="#ffffff" align="center">
EOF
if($Kimg[1] != 0){
print <<"EOF";
<IMG src="$imgpath/$Kimg[1].gif">
EOF
}
print <<"EOF";
</TD>
<TD bgcolor="#ffffff" align="center">$itemlist[$Kimg[1]] $seibetu[$Ksex[1]]<BR>【$seikaku[$Ksei[1]]】</TD>
</TR>
</TBODY>
</TABLE>
<HR>
<P>依頼が来てるモンスター<BR>
</P>
<TABLE border="1">
<TBODY>
<TR>
<TD bgcolor="#ff0000" align="center"><B>相手ユーザー名</B></TD>
<TD bgcolor="#ff0000" align="center"><B>相手モンスター</B></TD>
<TD bgcolor="#ff0000" align="center"><B>相手モンスター名</B></TD>
<TD bgcolor="#00cccc" align="center"><B>自モンスター</B></TD>
<TD bgcolor="#00cccc" align="center"><B>自モンスター名</B></TD>
</TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center">$Aname[2]</TD>
<TD bgcolor="#ffffff" align="center">
EOF
if($Aimg[2] != 0){
print <<"EOF";
<IMG src="$imgpath/$Aimg[2].gif">
EOF
}
print <<"EOF";
</TD>
<TD bgcolor="#ffffff" align="center">$itemlist[$Aimg[2]] $seibetu[$Asex[2]]<BR>【$seikaku[$Asei[2]]】</TD>
<TD bgcolor="#ffffff" align="center">
EOF
if($Kimg[2] != 0){
print <<"EOF";
<IMG src="$imgpath/$Kimg[2].gif">
EOF
}
print <<"EOF";
</TD>
<TD bgcolor="#ffffff" align="center">$itemlist[$Kimg[2]] $seibetu[$Ksex[2]]<BR>【$seikaku[$Ksei[2]]】</TD>
</TR>
</TBODY>
</TABLE>
<BR>
<HR>
<BR>
<BR>
<TABLE border="1">
<TBODY>
<TR>
<TD bgcolor="#ccff00"><B>お見合いで誕生したモンスター 1 </B><BR>$Nimg</TD>
</TR>
<TR>
<TD bgcolor="#00cccc" align="center">
EOF
if($Nimg[1] == 0){
print <<"EOF";
$Nimg
EOF
}
if($Nimg[1] != 0){
print <<"EOF";
<IMG src="$imgpath/$Nimg[1].gif">
EOF
}
print <<"EOF";
</TD>
</TR>
</TBODY>
</TBODY>
</TABLE>
<TABLE border="1">
<TBODY>
<TR>
<TD bgcolor="#ccff00"><B>お見合いで誕生したモンスター 2 </B><BR>$Nimg2</TD>
</TR>
<TR>
<TD bgcolor="#00cccc" align="center">
EOF
if($Nimg[2] == 0){
print <<"EOF";
$Nimg2
EOF
}
if($Nimg[2] != 0){
print <<"EOF";
<IMG src="$imgpath/$Nimg[2].gif">
EOF
}
print <<"EOF";
</TD>
</TR>
</TBODY>
</TABLE>
<HR>
<BR>
<BR>
<TABLE border="1">
<TBODY>
<TR>
<TD bgcolor="#ccff00"><B>お見合い不成立のモンスター 1 <BR></B></TD>
</TR>
<TR>
<TD bgcolor="#00cccc" align="center">
EOF
if($Fimg[1] == 0){
print <<"EOF";
$Fimg
EOF
}
if($Fimg[1] != 0){
print <<"EOF";
<IMG src="$imgpath/$Fimg[1].gif">
EOF
}
print <<"EOF";
</TD>
</TR>
</TBODY>
</TBODY>
</TABLE>
<TABLE border="1">
<TBODY>
<TR>
<TD bgcolor="#ccff00"><B>お見合い不成立のモンスター 2 <BR></B></TD>
</TR>
<TR>
<TD bgcolor="#00cccc" align="center">
EOF
if($Fimg[2] == 0){
print <<"EOF";
$Fimg2
EOF
}
if($Fimg[2] != 0){
print <<"EOF";
<IMG src="$imgpath/$Fimg[2].gif">
EOF
}
print <<"EOF";
</TD>
</TR>
</TBODY>
</TABLE>
<HR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT TYPE="BUTTON" VALUE="CLOSE" onClick="window.close()">
</FORM>
EOF

&footer2;
