use utf8;
use open IO => ":utf8";
use open ":std";
use Encode;
require './cgi/fight/fight10B.cgi';


sub wbat {
$Nimg1  = $Aimg1;
$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$monsuu = $FORM{'monsuu'};
$N      = $FORM{'N'};
$G      = $FORM{'G'};
$Gimg   = $FORM{'Gimg'};
$Acname = $FORM{'Acname'};
$inkai  = $FORM{'kai'};
$Iii    = $FORM{'rank'};
$hit1   = $FORM{'hit1'};
$teki1  = $FORM{'teki1'};
$toku1  = $FORM{'toku1'};
$nakama1= $FORM{'nakama1'};
$ktoku1 = $FORM{'ktoku1'};
$Aimg1   = $FORM{'Aimg1'};
$Acname1 = $FORM{'Acname1'};
$Akou1  = $FORM{'Akou1'};
$Amam1   = $FORM{'Amam1'};
$Asub1   = $FORM{'Asub1'};
$Ahp1    = $FORM{'Ahp1'};
$Amp1    = $FORM{'Amp1'};
$Amhp1   = $FORM{'Amhp1'};
$Ammp1   = $FORM{'Ammp1'};
$Aex1    = $FORM{'Aex1'};
$Amoney1 = $FORM{'Amoney1'};
$Kimg1  = $FORM{'Kimg1'};
$Kkou1  = $FORM{'Kkou1'};
$Kmam1  = $FORM{'Kmam1'};
$Ksub1  = $FORM{'Ksub1'};
$Khp1   = $FORM{'Khp1'};
$Kmp1   = $FORM{'Kmp1'};
$Kmhp1  = $FORM{'Kmhp1'};
$Kmmp1  = $FORM{'Kmmp1'};
$Kcount1   = $FORM{'Kcount1'};
$Knecount1 = $FORM{'Knecount1'};
$Khaigou1 = $FORM{'Khaigou1'};
$Khai1 = $FORM{'Khaigou1'};
$Klev1  = $FORM{'Klev1'};
$Kmlev1 = $FORM{'Kmlev1'};
$Kkey  = $FORM{'Kkey'};
$Kmoney  = $FORM{'Kmoney'};
$Ssu     = $FORM{'Ssu'};
$Asex[1]   = $FORM{'Asex1'};

$Acname = decode( "utf8", $Acname );
$Acname1 = decode( "utf8", $Acname1 );

$TD  = '<TD align=center width=200 bgcolor=#ffffff>';
$TD2 = '<TD width=200 bgcolor=#ffffff align=center>';
$TD3 = '<TD align=center width=200 bgcolor=yellow>';

&open2;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    chomp $turn;
    if($turn eq ""){&error("異常が発生しました");}
    if($Yplay2 > time){&error("戦闘の仕切りなおしは出来ません-2");}
    $passcheck = crypt($inpass, $inname);
    if($passcheck ne $Ypass){&error("パスワードが違います");}
    $Kmoney  = $Ymoney;
    $Kkey    = $Ykey;
    $Sturn   = $turn;
    $NEWturn = $turn + 1;
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>$Yplay3<>$Ykey<>$Yimg1<>$Yhai1<>$Ylev1<>$Yimg2<>$Yhai2<>$Ylev2<>$Yimg3<>$Yhai3<>$Ylev3<>$Ymoney<>$Ymes<>$NEWturn\n";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
}
}

if($Sturn == 0){

&open3;

open(FH,"$monsdata") || &error("Can't open $monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
if($Mimg == $Nimg1){
$Aimg1   = $Nimg1;
$Acname1 = $Mcname;
$Akou1   = int($Mmam * $inkai);
$Amam1   = int($Mmam * $inkai);
$Asub1   = int($Msub * $inkai);
$Ahp1    = int($Mhp * $inkai);
$Amp1    = int($Mmp * $inkai);
$Amhp1   = $Ahp1;
$Ammp1   = $Amp1;
$Aex1    = int($Mex * $inkai);
$Amoney1 = int($Mmoney * $inkai);
}
}
}


$BAT = 0;# ザオラル・ザオリクが使用されてない事を宣言
$E   = 0;# 敵の2重攻撃防止


#パターン7 (敵 → 味方1)
$PT = 7;
#パターン1 (味方1 → 敵)
if($Ksub1 >= $Asub1){$PT = 1;}

#パターン1 (味方1 → 敵)
if($PT == 1){
&header2;
&F1;
&A1;
&GETMON;
}#パターン1 終了

#パターン7 (敵 → 味方1)
if($PT == 7){
&header2;
&A1;
&F1;
&GETMON;
}#パターン7 終了

$Fend = 0;

# 引き分け
if($NEWturn >= $maxround){$Fend = 1;}
# 勝利
if($Ahp1 == 0){$Fend = 2;}
# 敗戦
if($Khp1 == 0){$Fend = 3;}

}#サブbat1閉じ


#戦闘継続処理---------------------------------------------------------------------------
#---------------------------------------------------------------------------

sub wnend {
if($Fend == 0){

print <<"EOF";
<center>
<FONT color="#FF0000" size="+2"><B>何を行うか決定して下さい！</B></FONT><BR>
<BR>
<TABLE border="1">
<TBODY>
<TR>
<TD>
<CENTER>
<TABLE>
<TBODY>
<TR>
<FORM ACTION="$cgiurl" METHOD="POST">
<TD bgcolor=#ffffff colspan=\"2\" align=center><IMG src="$imgpath/$Kimg1.gif" border=0><BR>$itemlist[$Kimg1]</TD>
</TR>
<TR>
$TD2<B>レベル</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><FONT color=#FF0000><B>$Klev1</B></FONT></TD>
</TR>
<TR>
$TD2<B>HP/MHP</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><B>$Khp1/$Kmhp1</B></TD>
</TR>
<TR>
$TD2<B>MP/MMP</B></FONT></TD><TD bgcolor=#ffffff align=\"center\"><B>$Kmp1/$Kmmp1</B></TD>
</TR>
<TR>

$TD3
選択して下さい
</TD>
<TD bgcolor=#ffffff>
<SELECT name="hit1">
<option value=1 SELECTED>攻撃する
</SELECT>
</TD>
</TR>
<TR>
$TD3
攻撃相手
</TD>
<TD bgcolor=#ffffff>
<SELECT name="teki1">
<option value=1 SELECTED>$Acname1
</SELECT>
</TD>
</TR>

</TR>
<TR>
<TD colspan="5" bgcolor="#ffffff" align="center">
<BR>
<INPUT type="submit" name="monok" value="決定">
<INPUT type="hidden" name="mode" value="$_[0]">
<INPUT type="hidden" name="N" value="$N">
<INPUT type="hidden" name="G" value="$G">
<INPUT type="hidden" name="Gimg" value="$Gimg">
<INPUT type="hidden" name="Acname" value="$Acname">
<INPUT type="hidden" name="monsuu" value="$monsuu">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="hidden" name="Aimg1" value="$Aimg1">
<INPUT type="hidden" name="Acname1" value="$Acname1">
<INPUT type="hidden" name="Akou1" value="$Akou1">
<INPUT type="hidden" name="Amam1" value="$Amam1">
<INPUT type="hidden" name="Asub1" value="$Asub1">
<INPUT type="hidden" name="Ahp1" value="$Ahp1">
<INPUT type="hidden" name="Amp1" value="$Amp1">
<INPUT type="hidden" name="Amhp1" value="$Amhp1">
<INPUT type="hidden" name="Ammp1" value="$Ammp1">
<INPUT type="hidden" name="Aex1" value="$Aex1">
<INPUT type="hidden" name="Amoney1" value="$Amoney1">
<INPUT type="hidden" name="Kimg1" value="$Kimg1">
<INPUT type="hidden" name="Kkou1" value="$Kkou1">
<INPUT type="hidden" name="Kmam1" value="$Kmam1">
<INPUT type="hidden" name="Ksub1" value="$Ksub1">
<INPUT type="hidden" name="Khp1" value="$Khp1">
<INPUT type="hidden" name="Kmp1" value="$Kmp1">
<INPUT type="hidden" name="Kmhp1" value="$Kmhp1">
<INPUT type="hidden" name="Kmmp1" value="$Kmmp1">
<INPUT type="hidden" name="Kcount1" value="$Kcount1">
<INPUT type="hidden" name="Knecount1" value="$Knecount1">
<INPUT type="hidden" name="Khaigou1" value="$Khai1">
<INPUT type="hidden" name="Klev1" value="$Klev1">
<INPUT type="hidden" name="Kmlev1" value="$Kmlev1">
<INPUT type="hidden" name="Kmoney" value="$Kmoney">
<INPUT type="hidden" name="kai" value="$inkai">
<INPUT type="hidden" name="rank" value="$Iii">
<INPUT type="hidden" name="Kkey" value="$Kkey">
<INPUT type="hidden" name="Ssu" value="$Ssu">
<INPUT type="hidden" name="Asex1" value="$Asex[1]">
<BR>
</FORM>
</TD>
</TR>
</TBODY>
</TABLE>
</TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
EOF
}

$newlev1      =  $Klev1;
$newhp1       =  $Khp1;
$newmhp1      =  $Kmhp1;
$newmp1       =  $Kmp1;
$newmmp1      =  $Kmmp1;
$newkougeki1  =  $Kkou1;
$newmamori1   =  $Kmam1;
$newsub1      =  $Ksub1;
$newcount1    =  $Kcount1;
$newnecount1  =  $Knecount1;


}#サブnend閉じ




1;