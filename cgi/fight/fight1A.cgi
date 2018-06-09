use utf8;
use open IO => ":utf8";
use open ":std";
use Encode;



sub bat1 {
$Nimg1  = $Aimg1;
$Nimg2  = $Aimg2;
$Nimg3  = $Aimg3;
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
$hit2   = $FORM{'hit2'};
$teki2  = $FORM{'teki2'};
$toku2  = $FORM{'toku2'};
$nakama2= $FORM{'nakama2'};
$ktoku2 = $FORM{'ktoku2'};
$hit3   = $FORM{'hit3'};
$teki3  = $FORM{'teki3'};
$toku3  = $FORM{'toku3'};
$nakama3= $FORM{'nakama3'};
$ktoku3 = $FORM{'ktoku3'};
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
$Aimg2   = $FORM{'Aimg2'};
$Acname2 = $FORM{'Acname2'};
$Akou2  = $FORM{'Akou2'};
$Amam2   = $FORM{'Amam2'};
$Asub2   = $FORM{'Asub2'};
$Ahp2    = $FORM{'Ahp2'};
$Amp2    = $FORM{'Amp2'};
$Amhp2   = $FORM{'Amhp2'};
$Ammp2   = $FORM{'Ammp2'};
$Aex2    = $FORM{'Aex2'};
$Amoney2 = $FORM{'Amoney2'};
$Aimg3   = $FORM{'Aimg3'};
$Acname3 = $FORM{'Acname3'};
$Akou3  = $FORM{'Akou3'};
$Amam3   = $FORM{'Amam3'};
$Asub3   = $FORM{'Asub3'};
$Ahp3    = $FORM{'Ahp3'};
$Amp3    = $FORM{'Amp3'};
$Amhp3   = $FORM{'Amhp3'};
$Ammp3   = $FORM{'Ammp3'};
$Aex3    = $FORM{'Aex3'};
$Amoney3 = $FORM{'Amoney3'};
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
$Kimg2  = $FORM{'Kimg2'};
$Kkou2  = $FORM{'Kkou2'};
$Kmam2  = $FORM{'Kmam2'};
$Ksub2  = $FORM{'Ksub2'};
$Khp2   = $FORM{'Khp2'};
$Kmp2   = $FORM{'Kmp2'};
$Kmhp2  = $FORM{'Kmhp2'};
$Kmmp2  = $FORM{'Kmmp2'};
$Kcount2   = $FORM{'Kcount2'};
$Knecount2 = $FORM{'Knecount2'};
$Khaigou2 = $FORM{'Khaigou2'};
$Khai2 = $FORM{'Khaigou2'};
$Klev2  = $FORM{'Klev2'};
$Kmlev2 = $FORM{'Kmlev2'};
$Kimg3  = $FORM{'Kimg3'};
$Kkou3  = $FORM{'Kkou3'};
$Kmam3  = $FORM{'Kmam3'};
$Ksub3  = $FORM{'Ksub3'};
$Khp3   = $FORM{'Khp3'};
$Kmp3   = $FORM{'Kmp3'};
$Kmhp3  = $FORM{'Kmhp3'};
$Kmmp3  = $FORM{'Kmmp3'};
$Kcount3   = $FORM{'Kcount3'};
$Knecount3 = $FORM{'Knecount3'};
$Khaigou3 = $FORM{'Khaigou3'};
$Khai3 = $FORM{'Khaigou3'};
$Klev3  = $FORM{'Klev3'};
$Kmlev3 = $FORM{'Kmlev3'};
$Kkey  = $FORM{'Kkey'};
$Kmoney  = $FORM{'Kmoney'};
$Ssu     = $FORM{'Ssu'};
$Ksei1   = $FORM{'Ksei1'};
$Ksei2   = $FORM{'Ksei2'};
$Ksei3   = $FORM{'Ksei3'};
$Asex[1]   = $FORM{'Asex1'};
$Asex[2]   = $FORM{'Asex2'};
$Asex[3]   = $FORM{'Asex3'};


$Acname = decode( "utf8", $Acname );
$Acname1 = decode( "utf8", $Acname1 );
$Acname2 = decode( "utf8", $Acname2 );
$Acname3 = decode( "utf8", $Acname3 );

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
foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
if($Mimg == $Nimg2){
$Aimg2   = $Nimg2;
$Acname2 = $Mcname;
$Akou2   = int($Mmam * $inkai);
$Amam2   = int($Mmam * $inkai);
$Asub2   = int($Msub * $inkai);
$Ahp2    = int($Mhp * $inkai);
$Amp2    = int($Mmp * $inkai);
$Amhp2   = $Ahp2;
$Ammp2   = $Amp2;
$Aex2    = int($Mex * $inkai);
$Amoney2 = int($Mmoney * $inkai);
}
}
foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
if($Mimg == $Nimg3){
$Aimg3   = $Nimg3;
$Acname3 = $Mcname;
$Akou3   = int($Mmam * $inkai);
$Amam3   = int($Mmam * $inkai);
$Asub3   = int($Msub * $inkai);
$Ahp3    = int($Mhp * $inkai);
$Amp3    = int($Mmp * $inkai);
$Amhp3   = $Ahp3;
$Ammp3   = $Amp3;
$Aex3    = int($Mex * $inkai);
$Amoney3 = int($Mmoney * $inkai);
}
}
if($Acname1 eq $Acname2 && $Acname1 eq $Acname3){
$Acname1 = "$Acname1 A";
$Acname2 = "$Acname2 B";
$Acname3 = "$Acname3 C";
}
if($Acname1 eq $Acname2 && $Acname1 ne $Acname3){
$Acname1 = "$Acname1 A";
$Acname2 = "$Acname2 B";
$Acname3 = "$Acname3";
}
if($Acname1 ne $Acname2 && $Acname1 eq $Acname3){
$Acname1 = "$Acname1 A";
$Acname2 = "$Acname2";
$Acname3 = "$Acname3 B";
}
if($Acname2 eq $Acname3 && $Acname1 ne $Acname2){
$Acname1 = "$Acname1";
$Acname2 = "$Acname2 A";
$Acname3 = "$Acname3 B";
}
}

$BAT = 0;# ザオラル・ザオリクが使用されてない事を宣言
$E   = 0;# 敵1の2重攻撃防止
$F   = 0;# 敵2の2重攻撃防止
$H   = 0;# 敵3の2重攻撃防止

#パターン7 (敵 → 味方1 → 味方2 → 味方3)
$PT = 7;

if ($Ssu == "1"){
	#パターン1 (味方1 → 敵)
	if($Ksub1 >= $Asub1){$PT = 1;}
	$DIE = 7;
	
} elsif ($Ssu == "2") {
	#パターン1 (味方1 → 味方2 → 敵)
	if($Ksub1 >= $Ksub2 && $Ksub2 >= $Asub1){$PT = 1;}
	#パターン3 (味方2 → 味方1 → 敵)
	if($Ksub2 >= $Ksub1 && $Ksub1 >= $Asub1){$PT = 3;}

	if($Khp1 != 0 && $Khp2 == 0){$DIE = 1;}# (戦闘終了後用)戦闘者チェック 1
	if($Khp1 == 0 && $Khp2 != 0){$DIE = 2;}# (戦闘終了後用)戦闘者チェック 2
	if($Khp1 != 0 && $Khp2 != 0){$DIE = 7;}# (戦闘終了後用)戦闘者チェック 全
} else {
	if($Khp1 != 0 && $Khp2 == 0 && $Khp3 == 0){$DIE = 1;}# (戦闘終了後用)戦闘者チェック 1
	if($Khp1 == 0 && $Khp2 != 0 && $Khp3 == 0){$DIE = 2;}# (戦闘終了後用)戦闘者チェック 2
	if($Khp1 == 0 && $Khp2 == 0 && $Khp3 != 0){$DIE = 3;}# (戦闘終了後用)戦闘者チェック 3
	if($Khp1 != 0 && $Khp2 != 0 && $Khp3 == 0){$DIE = 4;}# (戦闘終了後用)戦闘者チェック 1-2
	if($Khp1 != 0 && $Khp2 == 0 && $Khp3 != 0){$DIE = 5;}# (戦闘終了後用)戦闘者チェック 1-3
	if($Khp1 == 0 && $Khp2 != 0 && $Khp3 != 0){$DIE = 6;}# (戦闘終了後用)戦闘者チェック 2-3
	if($Khp1 != 0 && $Khp2 != 0 && $Khp3 != 0){$DIE = 7;}# (戦闘終了後用)戦闘者チェック 全

	#パターン1 (味方1 → 味方2 → 味方3 → 敵)
	if($Ksub1 >= $Ksub2 && $Ksub2 >= $Ksub3 && $Ksub3 >= $Asub1){$PT = 1;}
	#パターン2 (味方1 → 味方3 → 味方2 → 敵)
	if($Ksub1 >= $Ksub3 && $Ksub3 >= $Ksub2 && $Ksub2 >= $Asub1){$PT = 2;}
	#パターン3 (味方2 → 味方1 → 味方3 → 敵)
	if($Ksub2 >= $Ksub1 && $Ksub1 >= $Ksub3 && $Ksub3 >= $Asub1){$PT = 3;}
	#パターン4 (味方2 → 味方3 → 味方1 → 敵)
	if($Ksub2 >= $Ksub3 && $Ksub3 >= $Ksub1 && $Ksub1 >= $Asub1){$PT = 4;}
	#パターン5 (味方3 → 味方1 → 味方2 → 敵)
	if($Ksub3 >= $Ksub1 && $Ksub1 >= $Ksub2 && $Ksub2 >= $Asub1){$PT = 5;}
	#パターン6 (味方3 → 味方2 → 味方1 → 敵)
	if($Ksub3 >= $Ksub2 && $Ksub2 >= $Ksub1 && $Ksub1 >= $Asub1){$PT = 6;}
}

#パターン1 (味方1 → 味方2 → 味方3 → 敵)
if($PT == 1){
&header;
&F1;
&F5;
&F6;
&A1;
&GETMON;
}#パターン1 終了

#パターン2 (味方1 → 味方3 → 味方2 → 敵)
if($PT == 2){
&header;
&F1;
&F6;
&F5;
&A1;
&GETMON;
}#パターン2 終了

#パターン3 (味方2 → 味方1 → 味方3 → 敵)
if($PT == 3){
&header;
&F2;
&F4;
&F6;
&A1;
&GETMON;
}#パターン3 終了

#パターン4 (味方2 → 味方3 → 味方1 → 敵)
if($PT == 4){
&header;
&F2;
&F6;
&F4;
&A1;
&GETMON;
}#パターン4 終了

#パターン5 (味方3 → 味方1 → 味方2 → 敵)
if($PT == 5){
&header;
&F3;
&F4;
&F5;
&A1;
&GETMON;
}#パターン5 終了

#パターン6 (味方3 → 味方2 → 味方1 → 敵)
if($PT == 6){
&header;
&F3;
&F5;
&F4;
&A1;
&GETMON;
}#パターン6 終了

#パターン7 (敵 → 味方1 → 味方2 → 味方3)
if($PT == 7){
&header;
&A1;
&F1;
&F5;
&F6;
&GETMON;
}#パターン7 終了

$Fend = 0;

# 引き分け
if($NEWturn >= $maxround){$Fend = 1;}
# 勝利
if($Ahp1 == 0 && $Ahp2 == 0 && $Ahp3 == 0){$Fend = 2;}
# 敗戦
if($Khp1 == 0 && $Khp2 == 0 && $Khp3 == 0){$Fend = 3;}

}


#戦闘継続処理---------------------------------------------------------------------------
#---------------------------------------------------------------------------

sub nend {
if($Fend == 0){

&senaite;

print <<"EOF";
</TR>
<TR>
<TD colspan="6" bgcolor="#ffffff" align="center">
<BR>
<INPUT type="submit" name="monok" value="決定">
<INPUT type="hidden" name="mode" value="fight1">

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

<INPUT type="hidden" name="Aimg2" value="$Aimg2">
<INPUT type="hidden" name="Acname2" value="$Acname2">
<INPUT type="hidden" name="Akou2" value="$Akou2">
<INPUT type="hidden" name="Amam2" value="$Amam2">
<INPUT type="hidden" name="Asub2" value="$Asub2">
<INPUT type="hidden" name="Ahp2" value="$Ahp2">
<INPUT type="hidden" name="Amp2" value="$Amp2">
<INPUT type="hidden" name="Amhp2" value="$Amhp2">
<INPUT type="hidden" name="Ammp2" value="$Ammp2">
<INPUT type="hidden" name="Aex2" value="$Aex2">
<INPUT type="hidden" name="Amoney2" value="$Amoney2">

<INPUT type="hidden" name="Aimg3" value="$Aimg3">
<INPUT type="hidden" name="Acname3" value="$Acname3">
<INPUT type="hidden" name="Akou3" value="$Akou3">
<INPUT type="hidden" name="Amam3" value="$Amam3">
<INPUT type="hidden" name="Asub3" value="$Asub3">
<INPUT type="hidden" name="Ahp3" value="$Ahp3">
<INPUT type="hidden" name="Amp3" value="$Amp3">
<INPUT type="hidden" name="Amhp3" value="$Amhp3">
<INPUT type="hidden" name="Ammp3" value="$Ammp3">
<INPUT type="hidden" name="Aex3" value="$Aex3">
<INPUT type="hidden" name="Amoney3" value="$Amoney3">

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

<INPUT type="hidden" name="Kimg2" value="$Kimg2">
<INPUT type="hidden" name="Kkou2" value="$Kkou2">
<INPUT type="hidden" name="Kmam2" value="$Kmam2">
<INPUT type="hidden" name="Ksub2" value="$Ksub2">
<INPUT type="hidden" name="Khp2" value="$Khp2">
<INPUT type="hidden" name="Kmp2" value="$Kmp2">
<INPUT type="hidden" name="Kmhp2" value="$Kmhp2">
<INPUT type="hidden" name="Kmmp2" value="$Kmmp2">
<INPUT type="hidden" name="Kcount2" value="$Kcount2">
<INPUT type="hidden" name="Knecount2" value="$Knecount2">
<INPUT type="hidden" name="Khaigou2" value="$Khai2">
<INPUT type="hidden" name="Klev2" value="$Klev2">
<INPUT type="hidden" name="Kmlev2" value="$Kmlev2">

<INPUT type="hidden" name="Kimg3" value="$Kimg3">
<INPUT type="hidden" name="Kkou3" value="$Kkou3">
<INPUT type="hidden" name="Kmam3" value="$Kmam3">
<INPUT type="hidden" name="Ksub3" value="$Ksub3">
<INPUT type="hidden" name="Khp3" value="$Khp3">
<INPUT type="hidden" name="Kmp3" value="$Kmp3">
<INPUT type="hidden" name="Kmhp3" value="$Kmhp3">
<INPUT type="hidden" name="Kmmp3" value="$Kmmp3">
<INPUT type="hidden" name="Kcount3" value="$Kcount3">
<INPUT type="hidden" name="Knecount3" value="$Knecount3">
<INPUT type="hidden" name="Khaigou3" value="$Khai3">
<INPUT type="hidden" name="Klev3" value="$Klev3">
<INPUT type="hidden" name="Kmlev3" value="$Kmlev3">

<INPUT type="hidden" name="Kmoney" value="$Kmoney">
<INPUT type="hidden" name="kai" value="$inkai">
<INPUT type="hidden" name="rank" value="$Iii">
<INPUT type="hidden" name="Kkey" value="$Kkey">
<INPUT type="hidden" name="Ssu" value="$Ssu">

<INPUT type="hidden" name="Ksei1" value="$Ksei1">
<INPUT type="hidden" name="Ksei2" value="$Ksei2">
<INPUT type="hidden" name="Ksei3" value="$Ksei3">
<INPUT type="hidden" name="Asex1" value="$Asex[1]">
<INPUT type="hidden" name="Asex2" value="$Asex[2]">
<INPUT type="hidden" name="Asex3" value="$Asex[3]">
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

$newlev2      =  $Klev2;
$newhp2       =  $Khp2;
$newmhp2      =  $Kmhp2;
$newmp2       =  $Kmp2;
$newmmp2      =  $Kmmp2;
$newkougeki2  =  $Kkou2;
$newmamori2   =  $Kmam2;
$newsub2      =  $Ksub2;
$newcount2    =  $Kcount2;
$newnecount2  =  $Knecount2;

$newlev3      =  $Klev3;
$newhp3       =  $Khp3;
$newmhp3      =  $Kmhp3;
$newmp3       =  $Kmp3;
$newmmp3      =  $Kmmp3;
$newkougeki3  =  $Kkou3;
$newmamori3   =  $Kmam3;
$newsub3      =  $Ksub3;
$newcount3    =  $Kcount3;
$newnecount3  =  $Knecount3;

}




1;