use utf8;
use open IO => ":utf8";
use open ":std";

&get_cookie2;

if($setimg eq ""){$imgpath = $img;}
if($setimg ne ""){$imgpath = $setimg;}

#========#
# 戦闘用 #
#========#

sub fightC {

print <<"EOF";
<BR><BR>
<CENTER>
<TABLE bgcolor="#ff0000" width="400">
<TBODY>
<TR>
<TD colspan="3" width="400" bgcolor="#000000" align="center">
<BLOCKQUOTE>
<TABLE>
<TBODY>
<TR>
<TD><BR>
EOF
}

sub fightD {

print <<"EOF";
</TD>
</TR>
</TBODY>
</TABLE>
</BLOCKQUOTE>
</TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
EOF
}

sub senaite {

print <<"EOF";

<center>
<FONT color="#FF0000" size="+2"><B>何を行うか決定して下さい！</B></FONT><BR>
<BR>
<TABLE>
<TBODY>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
EOF

for($x=1;$x<=3;$x++){
if(${Khp.$x} != 0){

print <<"EOF";
<td>
<table>
	<tr>
		<TD bgcolor=#ffffff colspan=2 align=center height="150px"><IMG src="$imgpath/${Kimg.$x}.gif" border=0><BR>$itemlist[${Kimg.$x}]</TD>
	</tr>
	<tr>
		$TD2<B>レベル</B></FONT></TD>
		<TD bgcolor=#ffffff align="center"><FONT color=#FF0000><B>${Klev.$x}</B></FONT></TD>
	</tr>
	<tr>
		$TD2<B>HP/MHP</B></FONT></TD>
		<TD bgcolor=#ffffff align="center"><B>${Khp.$x}/${Kmhp.$x}</B></TD>
	</tr>
	<tr>
		$TD2<B>MP/MMP</B></FONT></TD>
		<TD bgcolor=#ffffff align="center"><B>${Kmp.$x}/${Kmmp.$x}</B></TD>
	</tr>
	<tr>
		$TD3 選択して下さい</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="hit$x">
				<option value=1>攻撃する
				<option value=2>防御する
				<option value=3 SELECTED>特殊攻撃使用
				<option value=4>回復魔法使用
			</SELECT>
		</TD>
	</tr>
	<tr>
		$TD3 攻撃相手</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="teki$x">
EOF
				for($i=1;$i<=3;$i++){
					if(${Ahp.$i} != 0){
						print "<option value=$i>${Acname.$i}\n"
					}
				}
print <<"EOF";
			</SELECT>
			</TD>
	</tr>
	<tr>
		$TD3 攻撃魔法</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="toku$x">
				<option value=99 SELECTED>通常攻撃
EOF
				for($t=1;$t<56;$t++){
					$T=$waza[$t];
					if($T != 0 && !($t == 3 or $t == 14 or $t == 37 or $t == 51 or $t == 52)){
						print "<option value=$t>$mtoku[$T] ($mtokump[$T] MP)\n"
					}
				}
print <<"EOF";
			</SELECT>
		</TD>
	</tr>
	<tr>
		$TD3 回復魔法相手</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="nakama$x">
EOF
				for($i=1;$i<=3;$i++){
					if($Ssu >= $i){
						print "<option value=$i>$itemlist[${Kimg.$i}]\n"
					}
				}
print <<"EOF";
			</SELECT>
		</TD>
	</tr>
	<tr>
		$TD3 回復魔法</TD>
		<TD bgcolor=#ffffff>
			<SELECT name="ktoku$x">
				<option value=0 SELECTED>使用しない
EOF
				for($t=1;$t<56;$t++){
					$T=$waza[$t];
					if($T != 0 && ($t == 3 or $t == 14 or $t == 37 or $t == 51 or $t == 52)){
						print "<option value=$t>$mtoku[$T] ($mtokump[$T] MP)\n"
					}
				}
print <<"EOF";
			</SELECT>
		</TD>
	</tr>
</table>
EOF
}#HP判定if
}#for終了

}#sub senaite終了#############################################################################

sub A1 {

#敵キャラ1攻撃開始
# 味方1・味方2・味方3生存
if($Ahp1 > 0 && $Khp1 > 0) {
$Mam1 = $Kmam1;
if($hit1 == 2){$Mam1 = $Kmam1 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$E = 1;
$war2 = int(($Akou1 * $kou2) - ($Mam1 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp1 = $Khp1 - $war2;
if($Khp1 <= 0 ){$Khp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
# 味方1瀕死 味方2・味方3生存
if($Ahp1 > 0 &&  $Khp2 > 0 && $E != 1) {
$Mam2 = $Kmam2;
if($hit2 == 2){$Mam2 = $Kmam2 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$E = 1;
$war2 = int(($Akou1 * $kou2) - ($Mam2 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp2 = $Khp2 - $war2;
if($Khp2 <= 0 ){$Khp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
# 味方1・味方2瀕死 味方3生存
if($Ahp1 > 0 && $Khp3 > 0 && $E != 1) {
$Mam3 = $Kmam3;
if($hit3 == 2){$Mam3 = $Kmam3 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war2 = int(($Akou1 * $kou2) - ($Mam3 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp3 = $Khp3 - $war2;
if($Khp3 <= 0 ){$Khp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}

#敵キャラ2攻撃開始
# 味方1・味方2・味方3生存
if($Ahp2 > 0 && $Khp1 > 0) {
$Mam1 = $Kmam1;
if($hit1 == 2){$Mam1 = $Kmam1 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$F = 1;
$war2 = int(($Akou2 * $kou2) - ($Mam1 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp1 = $Khp1 - $war2;
if($Khp1 <= 0 ){$Khp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
# 味方1瀕死 味方2・味方3生存
if($Ahp2 > 0 && $Khp2 > 0 && $F != 1) {
$Mam2 = $Kmam2;
if($hit2 == 2){$Mam2 = $Kmam2 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$F = 1;
$war2 = int(($Akou2 * $kou2) - ($Mam2 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp2 = $Khp2 - $war2;
if($Khp2 <= 0 ){$Khp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
# 味方1・味方2瀕死 味方3生存
if($Ahp2 > 0 && $Khp3 > 0 && $F != 1) {
$Mam3 = $Kmam3;
if($hit3 == 2){$Mam3 = $Kmam3 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war2 = int(($Akou2 * $kou2) - ($Mam3 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp3 = $Khp3 - $war2;
if($Khp3 <= 0 ){$Khp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵キャラ3攻撃開始
# 味方1・味方2・味方3生存
if($Ahp3 > 0 && $Khp1 > 0) {
$Mam1 = $Kmam1;
if($hit1 == 2){$Mam1 = $Kmam1 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$H = 1;
$war2 = int(($Akou3 * $kou2) - ($Mam1 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp1 = $Khp1 - $war2;
if($Khp1 <= 0 ){$Khp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
# 味方1瀕死 味方2・味方3生存
if($Ahp3 > 0 && $Khp2 > 0 && $H != 1) {
$Mam2 = $Kmam2;
if($hit2 == 2){$Mam2 = $Kmam2 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$H = 1;
$war2 = int(($Akou3 * $kou2) - ($Mam2 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp2 = $Khp2 - $war2;
if($Khp2 <= 0 ){$Khp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
# 味方1・味方2瀕死 味方3生存
if($Ahp3 > 0 && $Khp3 > 0 && $H != 1) {
$Mam3 = $Kmam3;
if($hit3 == 2){$Mam3 = $Kmam3 * 2;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war2 = int(($Akou3 * $kou2) - ($Mam3 * $kou1));
if($war2 < 0 ) { $war2 = 0; }
$Khp3 = $Khp3 - $war2;
if($Khp3 <= 0 ){$Khp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($war2 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">の</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">をかわした！</FONT><BR>
EOF
}
if($war2 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war2</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}

sub F1 {

#味方1-生存中
if($Khp1 > 0){
### 追加 ###
$KK = 0;
if($Ksei1 == 1 or $Ksei1 == 3 or $Ksei1 == 4 or $Ksei1 == 8 or $Ksei1 == 11 or $Ksei1 == 20 or $Ksei1 == 26){$KK = 1;}
if($Ksei1 == 9 or $Ksei1 == 12 or $Ksei1 == 13 or $Ksei1 == 15 or $Ksei1 == 16 or $Ksei1 == 18 or $Ksei1 == 21 or $Ksei1 == 22 or $Ksei1 == 23 or $Ksei1 == 24 or $Ksei1 == 25 or $Ksei1 == 27){$KK = 2;}
if($KK == 1){
$KK = 0;
@yoi = (1,2,3,4);
$yoiy = $yoi[int(rand(4))];
if($yoiy == 2){$KK = 1;}
}
if($KK == 2){
$KK = 0;
@war = (1,2,3,4);
$waru = $war[int(rand(4))];
if($waru == 1){$KK = 2;}
}
###########
if($hit1 == 1){
#敵1-選択
if($teki1 == 1){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];

#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############

$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK==0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki1 == 2){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1) - ($Amam2 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki1 == 3){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1) - ($Amam3 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit1 - 1終わり
if($hit1 == 2){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
### 追加 ###
if($KK == 1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
if($KK == 2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
}
########
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit1 - 2終わり

#MP切れ及び使用魔法未選択の調査
if($hit1 == 3){
if($toku1 == 0){$hit1 = 6;}
if($toku1 != 0){
$Cmp = $Kmp1 - $mtokump[$toku1];
if($Cmp < 0){$hit1 = 5;}
}
}#調査完了

if($hit1 == 3){
#敵1-選択
if($teki1 == 1){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1 * $mtokuhit[$toku1]) - ($Amam1 * $kou2));
$Kmp1 = $Kmp1 - $mtokump[$toku1];
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki1 == 2){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1 * $mtokuhit[$toku1]) - ($Amam2 * $kou2));
$Kmp1 = $Kmp1 - $mtokump[$toku1];
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki1 == 3){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1 * $mtokuhit[$toku1]) - ($Amam3 * $kou2));
$Kmp1 = $Kmp1 - $mtokump[$toku1];
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit1 - 3終わり

#MP切れ及び使用魔法未選択の調査
if($hit1 == 4){
if($ktoku1 == 0){$hit1 = 6;}
if($ktoku1 != 0){
$Cmp = $Kmp1 - $mtokump[$ktoku1];
if($Cmp < 0){$hit1 = 5;}
}
}#調査完了

if($hit1 == 4){
if($ktoku1 == 3){
if($nakama1 == 1){
$Khp1 = $Khp1 + 30;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが30回復した";
}
if($nakama1 == 2){
if($Khp2 != 0){
$Khp2 = $Khp2 + 30;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが30回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
if($nakama1 == 3){
if($Khp3 != 0){
$Khp3 = $Khp3 + 30;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが30回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku1 == 14){ 
if($nakama1 == 1){
$Khp1 = $Khp1 + 100;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが100回復した";
}
if($nakama1 == 2){
if($Khp2 != 0){
$Khp2 = $Khp2 + 100;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが100回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
if($nakama1 == 3){
if($Khp3 != 0){
$Khp3 = $Khp3 + 100;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが100回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku1 == 37){
if($nakama1 == 1){
$Khp1 = $Kmhp1;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
$MMlog = "$itemlist[$Kimg1]のHPが全回復した";
}
if($nakama1 == 2){
if($Khp2 != 0){
$Khp2 = $Kmhp2;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
$MMlog = "$itemlist[$Kimg2]のHPが全回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
if($nakama1 == 3){
if($Khp3 != 0){
$Khp3 = $Kmhp3;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
$MMlog = "$itemlist[$Kimg3]のHPが全回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku1 == 51){
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($nakama1 == 1){$MMlog = "自分にザオラルは使えません";}
if($nakama1 == 2 && $Khp2 != 0){$MMlog = "$itemlist[$Kimg2]は生きています";}
if($nakama1 == 3 && $Khp3 != 0){$MMlog = "$itemlist[$Kimg3]は生きています";}
if($nakama1 == 2 && $Khp2 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){$MMlog = "$itemlist[$Kimg1]はザオラルを使ったが$itemlist[$Kimg2]は生きかえらなかった";}
if($fuku == 1){
$MMlog = "$itemlist[$Kimg1]はザオラルを使った！$itemlist[$Kimg2]は生きかえった";
$Khp2 = 1;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}
if($nakama1 == 3 && $Khp3 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){
$MMlog = "$itemlist[$Kimg1]はザオラルを使ったが$itemlist[$Kimg3]は生きかえらなかった";
}
if($fuku == 1){
$MMlog = "$itemlist[$Kimg1]はザオラルを使った！$itemlist[$Kimg3]は生きかえった";
$Khp3 = 1;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}
}
if($ktoku1 == 52){
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($nakama1 == 1){
$MMlog = "自分にザオリクは使えません";
}
if($nakama1 == 2 && $Khp2 != 0){
$MMlog = "$itemlist[$Kimg2]は生きています";
}
if($nakama1 == 3 && $Khp3 != 0){
$MMlog = "$itemlist[$Kimg3]は生きています";
}
if($nakama1 == 2 && $Khp2 == 0){
$MMlog = "$itemlist[$Kimg1]はザオリクを使った！$itemlist[$Kimg2]は生きかえった";
$Khp2 = $Kmhp2;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
if($nakama1 == 3 && $Khp3 == 0){
$MMlog = "$itemlist[$Kimg1]はザオリクを使った！$itemlist[$Kimg3]は生きかえった";
$Khp3 = $Kmhp3;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit1 - 4終わり
if($hit1 == 5){
$MMlog = "$itemlist[$Kimg1]のMPが足らなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit1 - 5終わり
if($hit1 == 6){
$MMlog = "使用する魔法が選択されなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit1 - 6終わり
}#味方1-生存中終了
}

sub F2{
#味方1-生存中
if($Khp2 > 0){
### 追加 ###
$KK = 0;
if($Ksei2 == 1 or $Ksei2 == 3 or $Ksei2 == 4 or $Ksei2 == 8 or $Ksei2 == 11 or $Ksei2 == 20 or $Ksei2 == 26){$KK = 1;}
if($Ksei2 == 9 or $Ksei2 == 12 or $Ksei2 == 13 or $Ksei2 == 15 or $Ksei2 == 16 or $Ksei2 == 18 or $Ksei2 == 21 or $Ksei2 == 22 or $Ksei2 == 23 or $Ksei2 == 24 or $Ksei2 == 25 or $Ksei2 == 27){$KK = 2;}
if($KK == 1){
$KK = 0;
@yoi = (1,2,3,4);
$yoiy = $yoi[int(rand(4))];
if($yoiy == 2){$KK = 1;}
}
if($KK == 2){
$KK = 0;
@war = (1,2,3,4);
$waru = $war[int(rand(4))];
if($waru == 1){$KK = 2;}
}
###########
if($hit2 == 1){
#敵1-選択
if($teki2 == 1){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki2 == 2){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1) - ($Amam2 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki2 == 3){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1) - ($Amam3 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit2 - 1終わり
if($hit2 == 2){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
### 追加 ###
if($KK == 1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
if($KK == 2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
}
########
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit2 - 2終わり

#MP切れ及び使用魔法未選択の調査
if($hit2 == 3){
if($toku2 == 0){$hit2 = 6;}
if($toku2 != 0){
$Cmp = $Kmp2 - $mtokump[$toku2];
if($Cmp < 0){$hit2 = 5;}
}
}#調査完了

if($hit2 == 3){
#敵1-選択
if($teki2 == 1){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1 * $mtokuhit[$toku2]) - ($Amam1 * $kou2));
$Kmp2 = $Kmp2 - $mtokump[$toku2];
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki2 == 2){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1 * $mtokuhit[$toku2]) - ($Amam2 * $kou2));
$Kmp2 = $Kmp2 - $mtokump[$toku2];
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki2 == 3){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1 * $mtokuhit[$toku2]) - ($Amam3 * $kou2));
$Kmp2 = $Kmp2 - $mtokump[$toku2];
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit2 - 3終わり

#MP切れ及び使用魔法未選択の調査
if($hit2 == 4){
if($ktoku2 == 0){$hit2 = 6;}
if($ktoku2 != 0){
$Cmp = $Kmp2 - $mtokump[$ktoku2];
if($Cmp < 0){$hit2 = 5;}
}
}#調査完了

if($hit2 == 4){

if($ktoku2 == 3){
if($nakama2 == 2){
$Khp2 = $Khp2 + 30;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが30回復した";
}
if($nakama2 == 1){
if($Khp1 != 0){
$Khp1 = $Khp1 + 30;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが30回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama2 == 3){
if($Khp3 != 0){
$Khp3 = $Khp3 + 30;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが30回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku2 == 14){ 
if($nakama2 == 2){
$Khp2 = $Khp2 + 100;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが100回復した";
}
if($nakama2 == 1){
if($Khp1 != 0){
$Khp1 = $Khp1 + 100;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが100回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama2 == 3){
if($Khp3 != 0){
$Khp3 = $Khp3 + 100;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが100回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku2 == 37){
if($nakama2 == 2){
$Khp2 = $Kmhp2;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
$MMlog = "$itemlist[$Kimg2]のHPが全回復した";
}
if($nakama2 == 1){
if($Khp1 != 0){
$Khp1 = $Kmhp1;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
$MMlog = "$itemlist[$Kimg1]のHPが全回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama2 == 3){
if($Khp3 != 0){
$Khp3 = $Kmhp3;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
$MMlog = "$itemlist[$Kimg3]のHPが全回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku2 == 51){
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($nakama2 == 2){
$MMlog = "自分にザオラルは使えません";
}
if($nakama2 == 1 && $Khp1 != 0){
$MMlog = "$itemlist[$Kimg1]は生きています";
}
if($nakama2 == 3 && $Khp3 != 0){
$MMlog = "$itemlist[$Kimg3]は生きています";
}
if($nakama2 == 1 && $Khp1 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){
$MMlog = "$itemlist[$Kimg2]はザオラルを使ったが$itemlist[$Kimg1]は生きかえらなかった";
}
if($fuku == 1){
$MMlog = "$itemlist[$Kimg2]はザオラルを使った！$itemlist[$Kimg1]は生きかえった";
$Khp1 = 1;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}
if($nakama2 == 3 && $Khp3 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){
$MMlog = "$itemlist[$Kimg2]はザオラルを使ったが$itemlist[$Kimg3]は生きかえらなかった";
}
if($fuku == 1){
$MMlog = "$itemlist[$Kimg2]はザオラルを使った！$itemlist[$Kimg3]は生きかえった";
$Khp3 = 1;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}
}
if($ktoku2 == 52){
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($nakama2 == 2){
$MMlog = "自分にザオリクは使えません";
}
if($nakama2 == 1 && $Khp1 != 0){
$MMlog = "$itemlist[$Kimg1]は生きています";
}
if($nakama2 == 3 && $Khp3 != 0){
$MMlog = "$itemlist[$Kimg3]は生きています";
}
if($nakama2 == 1 && $Khp1 == 0){
$MMlog = "$itemlist[$Kimg2]はザオリクを使った！$itemlist[$Kimg1]は生きかえった";
$Khp1 = $Kmhp1;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
if($nakama2 == 3 && $Khp3 == 0){
$MMlog = "$itemlist[$Kimg2]はザオリクを使った！$itemlist[$Kimg3]は生きかえった";
$Khp3 = $Kmhp3;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit2 - 4終わり
if($hit2 == 5){
$MMlog = "$itemlist[$Kimg2]のMPが足らなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit2 - 5終わり
if($hit2 == 6){
$MMlog = "使用する魔法が選択されなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit2 - 6終わり
}#味方2-生存中終了
}

sub F3 {
#味方1-生存中
if($Khp3 > 0){
### 追加 ###
$KK = 0;
if($Ksei3 == 1 or $Ksei3 == 3 or $Ksei3 == 4 or $Ksei3 == 8 or $Ksei3 == 11 or $Ksei3 == 20 or $Ksei3 == 26){$KK = 1;}
if($Ksei3 == 9 or $Ksei3 == 12 or $Ksei3 == 13 or $Ksei3 == 15 or $Ksei3 == 16 or $Ksei3 == 18 or $Ksei3 == 21 or $Ksei3 == 22 or $Ksei3 == 23 or $Ksei3 == 24 or $Ksei3 == 25 or $Ksei3 == 27){$KK = 2;}
if($KK == 1){
$KK = 0;
@yoi = (1,2,3,4);
$yoiy = $yoi[int(rand(4))];
if($yoiy == 2){$KK = 1;}
}
if($KK == 2){
$KK = 0;
@war = (1,2,3,4);
$waru = $war[int(rand(4))];
if($waru == 1){$KK = 2;}
}
###########
if($hit3 == 1){
#敵1-選択
if($teki3 == 1){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki3 == 2){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1) - ($Amam2 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki3 == 3){
@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1) - ($Amam3 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit3 - 1終わり
if($hit3 == 2){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
### 追加 ###
if($KK == 1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
if($KK == 2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
}
########
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit3 - 2終わり

#MP切れ及び使用魔法未選択の調査
if($hit3 == 3){
if($toku3 == 0){$hit3 = 6;}
if($toku3 != 0){
$Cmp = $Kmp3 - $mtokump[$toku3];
if($Cmp < 0){$hit3 = 5;}
}
}#調査完了

if($hit3 == 3){
#敵1-選択
if($teki3 == 1){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1 * $mtokuhit[$toku3]) - ($Amam1 * $kou2));
$Kmp3 = $Kmp3 - $mtokump[$toku3];
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki3 == 2){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1 * $mtokuhit[$toku3]) - ($Amam2 * $kou2));
$Kmp3 = $Kmp3 - $mtokump[$toku3];
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki3 == 3){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1 * $mtokuhit[$toku3]) - ($Amam3 * $kou2));
$Kmp3 = $Kmp3 - $mtokump[$toku3];
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($KK==2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit3 - 3終わり

#MP切れ及び使用魔法未選択の調査
if($hit3 == 4){
if($ktoku3 == 0){$hit3 = 6;}
if($ktoku3 != 0){
$Cmp = $Kmp3 - $mtokump[$ktoku3];
if($Cmp < 0){$hit3 = 5;}
}
}#調査完了

if($hit3 == 4){

if($ktoku3 == 3){
if($nakama3 == 3){
$Khp3 = $Khp3 + 30;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが30回復した";
}
if($nakama3 == 1){
if($Khp1 != 0){
$Khp1 = $Khp1 + 30;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが30回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama3 == 2){
if($Khp2 != 0){
$Khp2 = $Khp2 + 30;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが30回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
}
if($ktoku3 == 14){ 
if($nakama3 == 3){
$Khp3 = $Khp3 + 100;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが100回復した";
}
if($nakama3 == 1){
if($Khp1 != 0){
$Khp1 = $Khp1 + 100;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが100回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama3 == 2){
if($Khp2 != 0){
$Khp2 = $Khp2 + 100;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが100回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
}
if($ktoku3 == 37){
if($nakama3 == 3){
$Khp3 = $Kmhp3;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$MMlog = "$itemlist[$Kimg1]のHPが全回復した";
}
if($nakama3 == 1){
if($Khp1 != 0){
$Khp1 = $Kmhp1;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$MMlog = "$itemlist[$Kimg1]のHPが全回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama3 == 2){
if($Khp2 != 0){
$Khp2 = $Kmhp2;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$MMlog = "$itemlist[$Kimg2]のHPが全回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
}
if($ktoku3 == 51){
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($nakama3 == 3){
$MMlog = "自分にザオラルは使えません";
}
if($nakama3 == 1 && $Khp1 != 0){
$MMlog = "$itemlist[$Kimg1]は生きています";
}
if($nakama3 == 2 && $Khp2 != 0){
$MMlog = "$itemlist[$Kimg2]は生きています";
}
if($nakama3 == 1 && $Khp1 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){
$MMlog = "$itemlist[$Kimg3]はザオラルを使ったが$itemlist[$Kimg1]は生きかえらなかった";
}
if($fuku == 1){
$MMlog = "$itemlist[$Kimg3]はザオラルを使った！$itemlist[$Kimg1]は生きかえった";
$Khp1 = 1;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}
if($nakama3 == 2 && $Khp2 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){
$MMlog = "$itemlist[$Kimg3]はザオラルを使ったが$itemlist[$Kimg2]は生きかえらなかった";
}
if($fuku == 1){
$MMlog = "$itemlist[$Kimg3]はザオラルを使った！$itemlist[$Kimg2]は生きかえった";
$Khp2 = 1;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}
}
if($ktoku3 == 52){
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($nakama3 == 3){
$MMlog = "自分にザオリクは使えません";
}
if($nakama3 == 1 && $Khp1 != 0){
$MMlog = "$itemlist[$Kimg1]は生きています";
}
if($nakama3 == 2 && $Khp2 != 0){
$MMlog = "$itemlist[$Kimg2]は生きています";
}
if($nakama3 == 1 && $Khp1 == 0){
$MMlog = "$itemlist[$Kimg3]はザオリクを使った！$itemlist[$Kimg1]は生きかえった";
$Khp1 = $Kmhp1;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
if($nakama3 == 2 && $Khp2 == 0){
$MMlog = "$itemlist[$Kimg3]はザオリクを使った！$itemlist[$Kimg2]は生きかえった";
$Khp2 = $Kmhp2;
$BAT  = 1;#ここで復活の場合は復活モンスターは行動無しを宣言
}
}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit3 - 4終わり
if($hit3 == 5){
$MMlog = "$itemlist[$Kimg3]のMPが足らなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit3 - 5終わり
if($hit3 == 6){
$MMlog = "使用する魔法が選択されなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit3 - 6終わり
}#味方3-生存中終了
}

sub F4{
#味方1-ザオラル・ザオリク直後でなければ戦闘可能
if($BAT != 1){
#味方1-生存中
if($Khp1 > 0 && ($Ahp1 > 0 or $Ahp2 > 0 or $Ahp3 > 0)){
### 追加 ###
$KK = 0;
if($Ksei1 == 1 or $Ksei1 == 3 or $Ksei1 == 4 or $Ksei1 == 8 or $Ksei1 == 11 or $Ksei1 == 20 or $Ksei1 == 26){$KK = 1;}
if($Ksei1 == 9 or $Ksei1 == 12 or $Ksei1 == 13 or $Ksei1 == 15 or $Ksei1 == 16 or $Ksei1 == 18 or $Ksei1 == 21 or $Ksei1 == 22 or $Ksei1 == 23 or $Ksei1 == 24 or $Ksei1 == 25 or $Ksei1 == 27){$KK = 2;}
if($KK == 1){
$KK = 0;
@yoi = (1,2,3,4);
$yoiy = $yoi[int(rand(4))];
if($yoiy == 2){$KK = 1;}
}
if($KK == 2){
$KK = 0;
@war = (1,2,3,4);
$waru = $war[int(rand(4))];
if($waru == 1){$KK = 2;}
}
###########
if($hit1 == 1){
#敵1-選択
if($teki1 == 1){
$TY = 0;
if($Ahp1 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki1 == 2){
$TY = 0;
if($Ahp2 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1) - ($Amam2 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki1 == 3){
$TY = 0;
if($Ahp3 ==0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1) - ($Amam3 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit1 - 1終わり
if($hit1 == 2){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
### 追加 ###
if($KK == 1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
if($KK == 2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
}
########
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit1 - 2終わり

#MP切れ及び使用魔法未選択の調査
if($hit1 == 3){
if($toku1 == 0){$hit1 = 6;}
if($toku1 != 0){
$Cmp2 = $Kmp1 - $mtokump[$toku1];
if($Cmp2 < 0){$hit1 = 5;}
}
}#調査完了

if($hit1 == 3){
#敵1-選択
if($teki1 == 1){
$TY = 0;
if($Ahp1 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1 * $mtokuhit[$toku1]) - ($Amam1 * $kou2));
$Kmp1 = $Kmp1 - $mtokump[$toku1];
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki1 == 2){
$TY = 0;
if($Ahp2 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1 * $mtokuhit[$toku1]) - ($Amam2 * $kou2));
$Kmp1 = $Kmp1 - $mtokump[$toku1];
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki1 == 3){
$TY = 0;
if($Ahp3 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou1 * $kou1 * $mtokuhit[$toku1]) - ($Amam2 * $kou2));
$Kmp1 = $Kmp1 - $mtokump[$toku1];
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku1]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit1 - 3終わり

#MP切れ及び使用魔法未選択の調査
if($hit1 == 4){
if($ktoku1 == 0){$hit1 = 6;}
if($ktoku1 != 0){
$Cmp2 = $Kmp2 - $mtokump[$ktoku1];
if($Cmp2 < 0){$hit1 = 5;}
}
}#調査完了

if($hit1 == 4){

if($ktoku1 == 3){
if($nakama1 == 1){
$Khp1 = $Khp1 + 30;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが30回復した";
}
if($nakama1 == 2){
if($Khp2 != 0){
$Khp2 = $Khp2 + 30;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが30回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
if($nakama1 == 3){
if($Khp3 != 0){
$Khp3 = $Khp3 + 30;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが30回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku1 == 14){ 
if($nakama1 == 1){
$Khp1 = $Khp1 + 100;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが100回復した";
}
if($nakama1 == 2){
if($Khp2 != 0){
$Khp2 = $Khp2 + 100;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが100回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
if($nakama1 == 3){
if($Khp3 != 0){
$Khp3 = $Khp3 + 100;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが100回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku1 == 37){
if($nakama1 == 1){
$Khp1 = $Kmhp1;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
$MMlog = "$itemlist[$Kimg1]のHPが全回復した";
}
if($nakama1 == 2){
if($Khp2 != 0){
$Khp2 = $Kmhp2;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
$MMlog = "$itemlist[$Kimg2]のHPが全回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
if($nakama1 == 3){
if($Khp3 != 0){
$Khp3 = $Kmhp3;
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
$MMlog = "$itemlist[$Kimg3]のHPが全回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku1 == 51){
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($nakama1 == 1){$MMlog = "自分にザオラルは使えません";}
if($nakama1 == 2 && $Khp2 != 0){$MMlog = "$itemlist[$Kimg2]は生きています";}
if($nakama1 == 3 && $Khp3 != 0){$MMlog = "$itemlist[$Kimg3]は生きています";}

if($nakama1 == 2 && $Khp2 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){$MMlog = "$itemlist[$Kimg1]はザオラルを使ったが$itemlist[$Kimg2]は生きかえらなかった";}
if($fuku == 1){$MMlog = "$itemlist[$Kimg1]はザオラルを使った！$itemlist[$Kimg2]は生きかえった";$Khp2 = 1;}
}
if($nakama1 == 3 && $Khp3 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){$MMlog = "$itemlist[$Kimg1]はザオラルを使ったが$itemlist[$Kimg3]は生きかえらなかった";}
if($fuku == 1){$MMlog = "$itemlist[$Kimg1]はザオラルを使った！$itemlist[$Kimg3]は生きかえった";$Khp3 = 1;}
}
}
if($ktoku1 == 52){
$Kmp1 = $Kmp1 - $mtokump[$ktoku1];
if($nakama1 == 1){$MMlog = "自分にザオリクは使えません";}
if($nakama1 == 2 && $Khp2 != 0){$MMlog = "$itemlist[$Kimg2]は生きています";}
if($nakama1 == 3 && $Khp3 != 0){$MMlog = "$itemlist[$Kimg3]は生きています";}
if($nakama1 == 2 && $Khp2 == 0){$MMlog = "$itemlist[$Kimg1]はザオリクを使った！$itemlist[$Kimg2]は生きかえった";$Khp1 = $Kmhp1;}
if($nakama1 == 3 && $Khp3 == 0){$MMlog = "$itemlist[$Kimg1]はザオリクを使った！$itemlist[$Kimg3]は生きかえった";$Khp3 = $Kmhp3;}
}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit1 - 4終わり
if($hit1 == 5){
$MMlog = "$itemlist[$Kimg1]のMPが足らなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit1 - 5終わり
if($hit1 == 6){
$MMlog = "使用する魔法が選択されなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou1 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg1]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp1 / $Kmhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp1 / $Kmmp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit1 - 6終わり
}#味方1-生存中終了
}#ザオラル・ザオリク直後で無し終了
}

sub F5{
#味方2-ザオラル・ザオリク直後でなければ戦闘可能
if($BAT != 1){
#味方2-生存中
if($Khp2 > 0 && ($Ahp1 > 0 or $Ahp2 > 0 or $Ahp3 > 0)){
### 追加 ###
$KK = 0;
if($Ksei2 == 1 or $Ksei2 == 3 or $Ksei2 == 4 or $Ksei2 == 8 or $Ksei2 == 11 or $Ksei2 == 20 or $Ksei2 == 26){$KK = 1;}
if($Ksei2 == 9 or $Ksei2 == 12 or $Ksei2 == 13 or $Ksei2 == 15 or $Ksei2 == 16 or $Ksei2 == 18 or $Ksei2 == 21 or $Ksei2 == 22 or $Ksei2 == 23 or $Ksei2 == 24 or $Ksei2 == 25 or $Ksei2 == 27){$KK = 2;}
if($KK == 1){
$KK = 0;
@yoi = (1,2,3,4);
$yoiy = $yoi[int(rand(4))];
if($yoiy == 2){$KK = 1;}
}
if($KK == 2){
$KK = 0;
@war = (1,2,3,4);
$waru = $war[int(rand(4))];
if($waru == 1){$KK = 2;}
}
###########
if($hit2 == 1){
#敵1-選択
if($teki2 == 1){
$TY = 0;
if($Ahp1 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki2 == 2){
$TY = 0;
if($Ahp2 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1) - ($Amam2 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki2 == 3){
$TY = 0;
if($Ahp3 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1) - ($Amam3 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit2 - 1終わり
if($hit2 == 2){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
### 追加 ###
if($KK == 1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
if($KK == 2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
}
########
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit2 - 2終わり

#MP切れ及び使用魔法未選択の調査
if($hit2 == 3){
if($toku2 == 0){$hit2 = 6;}
if($toku2 != 0){
$Cmp2 = $Kmp2 - $mtokump[$toku2];
if($Cmp2 < 0){$hit2 = 5;}
}
}#調査完了

if($hit2 == 3){
#敵1-選択
if($teki2 == 1){
$TY = 0;
if($Ahp1 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1 * $mtokuhit[$toku2]) - ($Amam1 * $kou2));
$Kmp2 = $Kmp2 - $mtokump[$toku2];
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki2 == 2){
$TY = 0;
if($Ahp2 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1 * $mtokuhit[$toku2]) - ($Amam2 * $kou2));
$Kmp2 = $Kmp2 - $mtokump[$toku2];
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki2 == 3){
$TY = 0;
if($Ahp3 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou2 * $kou1 * $mtokuhit[$toku2]) - ($Amam3 * $kou2));
$Kmp2 = $Kmp2 - $mtokump[$toku2];
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku2]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit2 - 3終わり

#MP切れ及び使用魔法未選択の調査
if($hit2 == 4){
if($ktoku2 == 0){$hit2 = 6;}
if($ktoku2 != 0){
$Cmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Cmp2 < 0){$hit2 = 5;}
}
}#調査完了

if($hit2 == 4){

if($ktoku2 == 3){
if($nakama2 == 2){
$Khp2 = $Khp2 + 30;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが30回復した";
}
if($nakama2 == 1){
if($Khp1 != 0){
$Khp1 = $Khp1 + 30;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが30回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama2 == 3){
if($Khp3 != 0){
$Khp3 = $Khp3 + 30;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが30回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku2 == 14){ 
if($nakama2 == 2){
$Khp2 = $Khp2 + 100;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが100回復した";
}
if($nakama2 == 1){
if($Khp1 != 0){
$Khp1 = $Khp1 + 100;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが100回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama2 == 3){
if($Khp3 != 0){
$Khp3 = $Khp3 + 100;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが100回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku2 == 37){
if($nakama2 == 2){
$Khp2 = $Kmhp2;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
$MMlog = "$itemlist[$Kimg2]のHPが全回復した";
}
if($nakama2 == 1){
if($Khp1 != 0){
$Khp1 = $Kmhp1;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
$MMlog = "$itemlist[$Kimg1]のHPが全回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama2 == 3){
if($Khp3 != 0){
$Khp3 = $Kmhp3;
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
$MMlog = "$itemlist[$Kimg3]のHPが全回復した";
}
if($Khp3 == 0){
$MMlog = "$itemlist[$Kimg3]は既に力尽きていた";
}
}
}
if($ktoku2 == 51){
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($nakama2 == 2){$MMlog = "自分にザオラルは使えません";}
if($nakama2 == 1 && $Khp1 != 0){$MMlog = "$itemlist[$Kimg1]は生きています";}
if($nakama2 == 3 && $Khp3 != 0){$MMlog = "$itemlist[$Kimg3]は生きています";}

if($nakama2 == 1 && $Khp1 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){$MMlog = "$itemlist[$Kimg2]はザオラルを使ったが$itemlist[$Kimg1]は生きかえらなかった";}
if($fuku == 1){$MMlog = "$itemlist[$Kimg2]はザオラルを使った！$itemlist[$Kimg1]は生きかえった";$Khp1 = 1;}
}
if($nakama2 == 3 && $Khp3 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){$MMlog = "$itemlist[$Kimg2]はザオラルを使ったが$itemlist[$Kimg3]は生きかえらなかった";}
if($fuku == 1){$MMlog = "$itemlist[$Kimg2]はザオラルを使った！$itemlist[$Kimg3]は生きかえった";$Khp3 = 1;}
}
}
if($ktoku2 == 52){
$Kmp2 = $Kmp2 - $mtokump[$ktoku2];
if($nakama2 == 2){$MMlog = "自分にザオリクは使えません";}
if($nakama2 == 1 && $Khp1 != 0){$MMlog = "$itemlist[$Kimg1]は生きています";}
if($nakama2 == 3 && $Khp3 != 0){$MMlog = "$itemlist[$Kimg3]は生きています";}
if($nakama2 == 1 && $Khp1 == 0){$MMlog = "$itemlist[$Kimg2]はザオリクを使った！$itemlist[$Kimg1]は生きかえった";$Khp1 = $Kmhp1;}
if($nakama2 == 3 && $Khp3 == 0){$MMlog = "$itemlist[$Kimg2]はザオリクを使った！$itemlist[$Kimg3]は生きかえった";$Khp3 = $Kmhp3;}
}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit2 - 4終わり
if($hit2 == 5){
$MMlog = "$itemlist[$Kimg2]のMPが足らなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit2 - 5終わり
if($hit2 == 6){
$MMlog = "使用する魔法が選択されなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou2 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg2]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp2 / $Kmhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp2 / $Kmmp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit2 - 6終わり
}#味方2-生存中終了
}#ザオラル・ザオリク直後で無し終了
}

sub F6{
#味方3-ザオラル・ザオリク直後でなければ戦闘可能
if($BAT != 1){
#味方3-生存中
if($Khp3 > 0 && ($Ahp1 > 0 or $Ahp2 > 0 or $Ahp3 > 0)){
### 追加 ###
$KK = 0;
if($Ksei3 == 1 or $Ksei3 == 3 or $Ksei3 == 4 or $Ksei3 == 8 or $Ksei3 == 11 or $Ksei3 == 20 or $Ksei3 == 26){$KK = 1;}
if($Ksei3 == 9 or $Ksei3 == 12 or $Ksei3 == 13 or $Ksei3 == 15 or $Ksei3 == 16 or $Ksei3 == 18 or $Ksei3 == 21 or $Ksei3 == 22 or $Ksei3 == 23 or $Ksei3 == 24 or $Ksei3 == 25 or $Ksei3 == 27){$KK = 2;}
if($KK == 1){
$KK = 0;
@yoi = (1,2,3,4);
$yoiy = $yoi[int(rand(4))];
if($yoiy == 2){$KK = 1;}
}
if($KK == 2){
$KK = 0;
@war = (1,2,3,4);
$waru = $war[int(rand(4))];
if($waru == 1){$KK = 2;}
}
###########
if($hit3 == 1){
#敵1-選択
if($teki3 == 1){
$TY = 0;
if($Ahp1 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki3 == 2){
$TY = 0;
if($Ahp2 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1) - ($Amam2 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki3 == 3){
$TY = 0;
if($Ahp3 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1) - ($Amam3 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK==1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>懇親の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK==2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに遊んでいる～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit3 - 1終わり
if($hit3 == 2){

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
### 追加 ###
if($KK == 1){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>大防御！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>大防御</B></FONT><FONT size="4" color="#ffffff">している</FONT><BR>
EOF
}
}
if($KK == 2){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに歌っている～♪</FONT><BR>
EOF
}
}
########
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit3 - 2終わり
#MP切れ及び使用魔法未選択の調査
if($hit3 == 3){
if($toku3 == 0){$hit3 = 6;}
if($toku3 != 0){
$Cmp3 = $Kmp3 - $mtokump[$toku3];
if($Cmp3 < 0){$hit3 = 5;}
}
}#調査完了

if($hit3 == 3){
#敵1-選択
if($teki3 == 1){
$TY = 0;
if($Ahp1 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1 * $mtokuhit[$toku3]) - ($Amam1 * $kou2));
$Kmp3 = $Kmp3 - $mtokump[$toku3];
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1 - $war1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg1.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp1 / $Amhp1</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp1 / $Ammp1</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname1</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵2-選択
if($teki3 == 2){
$TY = 0;
if($Ahp2 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1 * $mtokuhit[$toku3]) - ($Amam2 * $kou2));
$Kmp3 = $Kmp3 - $mtokump[$toku3];
if($war1 < 0 ) { $war1 = 0; }
$Ahp2 = $Ahp2 - $war1;
if($Ahp2 <= 0 ) {$Ahp2 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg2.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp2 / $Amhp2</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp2 / $Ammp2</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname2</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
#敵3-選択
if($teki3 == 3){
$TY = 0;
if($Ahp3 == 0){$TY = 1;}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
#### 追加 ###
if($KK == 1){
$kou1 = $kou1 * 2;
}
if($KK == 2){
$kou1 = 0;
}
#############
$war1 = int(($Kkou3 * $kou1 * $mtokuhit[$toku3]) - ($Amam3 * $kou2));
$Kmp3 = $Kmp3 - $mtokump[$toku3];
if($war1 < 0 ) { $war1 = 0; }
$Ahp3 = $Ahp3 - $war1;
if($Ahp3 <= 0 ) {$Ahp3 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"><FONT size="6" color="#ff0000"><B>$NEWturn</B></FONT><FONT face="Times New Roman" color="#ffff00" size="5p"><B>R</B></FONT></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Aimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Ahp3 / $Amhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Amp3 / $Ammp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
EOF
if($KK == 0){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃</B></FONT><FONT size="4" color="#ffffff">しようとしたが既に力尽きていた！</FONT><BR>
EOF
}
}
##### 追加 #####
if($KK == 1){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT size="4" color="#ffffff">しかし</FONT>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">の攻撃は空を斬った！</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT color="yellow" size="4p"><B>会心の一撃！</B></FONT><BR>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT size="4" color="#ffff00"><B>$mtoku[$toku3]</B></FONT><FONT size="4" color="#ffffff">を繰り出し</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$Acname3</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>$war1</B></FONT><FONT size="4" color="#ffffff">ポイントのダメージを与えた！</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>次なる敵</B></FONT><FONT size="4" color="#ffffff">に</FONT><FONT face="Times New Roman" color="#ff0000" size="4p"><B>攻撃準備</B></FONT><FONT size="4" color="#ffffff">を開始した！</FONT><BR>
EOF
}
}
if($KK == 2){
if($TY == 0){
if($war1 == 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
if($war1 != 0){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
if($TY == 1){
print <<"EOF";
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT><FONT size="4" color="#ffffff">は命令を聞かずに踊っている～♪</FONT><BR>
EOF
}
}
#################
print <<"EOF";
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}
}#hit3 - 3終わり

#MP切れ及び使用魔法未選択の調査
if($hit3 == 4){
if($ktoku3 == 0){$hit3 = 6;}
if($ktoku3 != 0){
$Cmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Cmp3 < 0){$hit3 = 5;}
}
}#調査完了

if($hit3 == 4){

if($ktoku3 == 3){
if($nakama3 == 3){
$Khp3 = $Khp3 + 30;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp3 >= $Kmhp3){ $Khp3 = $Kmhp3;}
$MMlog = "$itemlist[$Kimg3]のHPが30回復した";
}
if($nakama3 == 1){
if($Khp1 != 0){
$Khp1 = $Khp1 + 30;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが30回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama3 == 2){
if($Khp2 != 0){
$Khp2 = $Khp2 + 30;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが30回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
}
if($ktoku3 == 14){ 
if($nakama3 == 3){
$Khp3 = $Khp3 + 100;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが100回復した";
}
if($nakama3 == 1){
if($Khp1 != 0){
$Khp1 = $Khp1 + 100;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp1 >= $Kmhp1){ $Khp1 = $Kmhp1;}
$MMlog = "$itemlist[$Kimg1]のHPが100回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama3 == 2){
if($Khp2 != 0){
$Khp2 = $Khp2 + 100;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
if($Khp2 >= $Kmhp2){ $Khp2 = $Kmhp2;}
$MMlog = "$itemlist[$Kimg2]のHPが100回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
}
if($ktoku3 == 37){
if($nakama3 == 3){
$Khp3 = $Kmhp3;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$MMlog = "$itemlist[$Kimg3]のHPが全回復した";
}
if($nakama3 == 1){
if($Khp1 != 0){
$Khp1 = $Kmhp1;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$MMlog = "$itemlist[$Kimg1]のHPが全回復した";
}
if($Khp1 == 0){
$MMlog = "$itemlist[$Kimg1]は既に力尽きていた";
}
}
if($nakama3 == 2){
if($Khp2 != 0){
$Khp2 = $Kmhp2;
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$MMlog = "$itemlist[$Kimg2]のHPが全回復した";
}
if($Khp2 == 0){
$MMlog = "$itemlist[$Kimg2]は既に力尽きていた";
}
}
}
if($ktoku3 == 51){
if($nakama3 == 3){$MMlog = "自分にザオラルは使えません";}
if($nakama3 == 1 && $Khp1 != 0){$MMlog = "$itemlist[$Kimg1]は生きています";}
if($nakama3 == 2 && $Khp2 != 0){$MMlog = "$itemlist[$Kimg2]は生きています";}

if($nakama3 == 1 && $Khp1 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){$MMlog = "$itemlist[$Kimg3]はザオラルを使ったが$itemlist[$Kimg1]は生きかえらなかった";}
if($fuku == 1){$MMlog = "$itemlist[$Kimg3]はザオラルを使った！$itemlist[$Kimg1]は生きかえった";
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$Khp1 = 1;}
}
if($nakama3 == 2 && $Khp2 == 0){

@seizon = (1,0);
$fuku = $seizon[int(rand(2))];
if($fuku == 0){$MMlog = "$itemlist[$Kimg3]はザオラルを使ったが$itemlist[$Kimg2]は生きかえらなかった";}
if($fuku == 1){$MMlog = "$itemlist[$Kimg3]はザオラルを使った！$itemlist[$Kimg2]は生きかえった";
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$Khp2 = 1;}
}
}
if($ktoku3 == 52){
if($nakama3 == 3){$MMlog = "自分にザオリクは使えません";}
if($nakama3 == 1 && $Khp1 != 0){$MMlog = "$itemlist[$Kimg1]は生きています";}
if($nakama3 == 2 && $Khp2 != 0){$MMlog = "$itemlist[$Kimg2]は生きています";}
if($nakama3 == 1 && $Khp1 == 0){$MMlog = "$itemlist[$Kimg3]はザオリクを使った！$itemlist[$Kimg1]は生きかえった";
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$Khp1 = $Kmhp1;}
if($nakama3 == 2 && $Khp2 == 0){$MMlog = "$itemlist[$Kimg3]はザオリクを使った！$itemlist[$Kimg2]は生きかえった";
$Kmp3 = $Kmp3 - $mtokump[$ktoku3];
$Khp2 = $Kmhp2;}
}

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit3 - 4終わり
if($hit3 == 5){
$MMlog = "$itemlist[$Kimg3]のMPが足らなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit3 - 5終わり
if($hit3 == 6){
$MMlog = "使用する魔法が選択されなかった！";

@ransuu1 = (1.0,1.1,1.2,1.3);
$kou1 = $ransuu1[int(rand(4))];
@ransuu2 = (0.9,1.0,1.1,1.2);
$kou2 = $ransuu2[int(rand(4))];
$war1 = int(($Kkou3 * $kou1) - ($Amam1 * $kou2));
if($war1 < 0 ) { $war1 = 0; }
$Ahp1 = $Ahp1;
if($Ahp1 <= 0 ) {$Ahp1 = 0;}
print <<"EOF";
<CENTER>
<TABLE bgcolor="#000000" width="600">
<TBODY>
<TR>
<TD align="center" valign="middle"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><IMG src="$imgpath/$Kimg3.gif" border="0"></TD>
<TD align="center" bgcolor="#ffffff"><FONT face="Times New Roman" color="#0000cc" size="4p"><B>$itemlist[$Kimg3]</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Khp3 / $Kmhp3</FONT></TD>
<TD align="center" bgcolor="#ffffff"><FONT size="4">$Kmp3 / $Kmmp3</FONT></TD>
</TR>
</TBODY>
</TABLE>
</TD>
<TD align="center"></TD>
<TD valign="middle" align="center"><BR>
<TABLE bgcolor="#0000cc" width="250">
<TBODY>
</TBODY>
</TABLE>
</TD>
</TR>
<TR>
<TD colspan="3">
<BLOCKQUOTE>
<FONT face="Times New Roman" color="#0000cc" size="4p"><B>$MMlog</B></FONT><BR>
</BLOCKQUOTE>
</TR>
</TBODY>
</TABLE><BR>
</CENTER>
EOF
}#hit3 - 6終わり
}#味方3-生存中終了
}#ザオラル・ザオリク直後で無し終了
}

sub GETMON{
if($G eq ""){
if($Ahp1 == 0){$Gimg = $Aimg1; $Acname = $Acname1; $Asex = $Asex[1]; $G = 1;}
if($Ahp2 == 0){$Gimg = $Aimg2; $Acname = $Acname2; $Asex = $Asex[2]; $G = 2;}
if($Ahp3 == 0){$Gimg = $Aimg3; $Acname = $Acname3; $Asex = $Asex[3]; $G = 3;}
}
if($G == 1){
if($Ahp2 == 0){$Gimg = $Aimg2; $Acname = $Acname2; $Asex = $Asex[2]; $G = 0;$N = 1;}
if($Ahp3 == 0){$Gimg = $Aimg3; $Acname = $Acname3; $Asex = $Asex[3]; $G = 0;$N = 2;}
}
if($G == 2){
if($Ahp1 == 0){$Gimg = $Aimg1; $Acname = $Acname1; $Asex = $Asex[1]; $G = 0;$N = 1;}
if($Ahp3 == 0){$Gimg = $Aimg3; $Acname = $Acname3; $Asex = $Asex[3]; $G = 0;$N = 3;}
}
if($G == 3){
if($Ahp1 == 0){$Gimg = $Aimg1; $Acname = $Acname1; $Asex = $Asex[1]; $G = 0;$N = 2;}
if($Ahp2 == 0){$Gimg = $Aimg2; $Acname = $Acname2; $Asex = $Asex[2]; $G = 0;$N = 3;}
}
if($G == 0 && $N == 1){
if($Ahp3 == 0){$Gimg = $Aimg3; $Acname = $Acname3; $Asex = $Asex[3];}
}
if($G == 0 && $N == 2){
if($Ahp2 == 0){$Gimg = $Aimg2; $Acname = $Acname2; $Asex = $Asex[2];}
}
if($G == 0 && $N == 3){
if($Ahp1 == 0){$Gimg = $Aimg1; $Acname = $Acname1; $Asex = $Asex[1];}
}
}

1;

__END__
