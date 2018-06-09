use utf8;
use open IO => ":utf8";
use open ":std";

for($m = 1;$m <= 16;$m++){
$Yname[$m] = "";
}

&lock;

open(FH,"${datadir}/$userdata") || &error("Can't open メダル杯");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
$ii++;
$Yname[$ii] = $Yname;
$Yimg1[$ii] = $Yimg1;
$Yimg2[$ii] = $Yimg2;
$Yimg3[$ii] = $Yimg3;
}

open(FH,"dat/time2.cgi");
$newt = <FH>;
close(FH);

($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = localtime($newt);
$mong++;

@KAKIKOMI = "<FONT size=5p color=blue><B>$mong月$mdayg日のメダル獲得杯の結果！</B></FONT><BR><BR>";

&timesyori;

open(FH,"${datadir}/$countdata");
$sou = <FH>;
close(FH);

if($sou >= 16){$sou = 16;}

#1回戦処理(8人に減らす)
if($sou >= 9 && $sou <= 16){
# 1 VS 9
$inname = $Yname[1];
$HP1  = 4;
$KOU1 = 4;
$MAM1 = 4;
$SUB1 = 4;
$inname = $Yname[9];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B><FONT size=4p color=RED>一回戦</FONT><BR>$Yname[1] さん対 $Yname[9]さんの一回戦は$Yname[1]さんが勝利しました</B><BR>";
$Mname[1] = $Yname[9];
$Yname[1] = $Yname[1];
}
if($HP2 > $HP1){
$mes = "<B><FONT size=4p color=RED>一回戦</FONT><BR>$Yname[1]さん 対 $Yname[9]さんの一回戦は$Yname[9]が勝利しました</B><BR>";
$Mname[1] = $Yname[1];
$Yname[1] = $Yname[9];
}
push @KAKIKOMI, $mes;
# 2 対 10
if($Yname[10] eq ""){
$mes = "<B>$Yname[2]さんは一回戦不戦勝でした</B><BR>";
$Yname[2] = $Yname[2];
push @KAKIKOMI, $mes;
}
if($Yname[10] ne ""){
$inname = $Yname[2];
$HP1  = 4;
$KOU1 = 4;
$MAM1 = 4;
$SUB1 = 4;
$inname = $Yname[10];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[2]さん 対 $Yname[10]さんの一回戦は$Yname[2]さんが勝利しました</B><BR>";
$Mname[2] = $Yname[10];
$Yname[2] = $Yname[2];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[2]さん 対 $Yname[10]さんの一回戦は$Yname[10]さんが勝利しました</B><BR>";
$Mname[2] = $Yname[2];
$Yname[2] = $Yname[10];
}
push @KAKIKOMI, $mes;
}
# 3 対 11
if($Yname[11] eq ""){
$mes = "<B>$Yname[3]さんは一回戦不戦勝でした</B><BR>";
$Yname[3] = $Yname[3];
push @KAKIKOMI, $mes;
}
if($Yname[11] ne ""){
$inname = $Yname[3];
$HP1  = 4;
$KOU1 = 4;
$MAM1 = 4;
$SUB1 = 4;
$inname = $Yname[11];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[3]さん 対 $Yname[11]さんの一回戦は$Yname[3]さんが勝利しました</B><BR>";
$Mname[3] = $Yname[11];
$Yname[3] = $Yname[3];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[3]さん 対 $Yname[11]さんの一回戦は$Yname[11]さんが勝利しました</B><BR>";
$Mname[3] = $Yname[3];
$Yname[3] = $Yname[11];
}
push @KAKIKOMI, $mes;
}
# 4 対 12
if($Yname[12] eq ""){
$mes = "<B>$Yname[4]さんは一回戦不戦勝でした</B><BR>";
push @KAKIKOMI, $mes;
}
if($Yname[12] ne ""){
$inname = $Yname[4];
$HP1  = 4;
$KOU1 = 4;
$MAM1 = 4;
$SUB1 = 4;
$inname = $Yname[12];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[4]さん 対 $Yname[12]さんの一回戦は$Yname[4]さんが勝利しました</B><BR>";
$Mname[4] = $Yname[12];
$Yname[4] = $Yname[4];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[4]さん 対 $Yname[12]さんの一回戦は$Yname[12]さんが勝利しました</B><BR>";
$Mname[4] = $Yname[4];
$Yname[4] = $Yname[12];
}
push @KAKIKOMI, $mes;
}
# 5 対 13
if($Yname[13] eq ""){
$mes = "<B>$Yname[5]さんは一回戦不戦勝でした</B><BR>";
push @KAKIKOMI, $mes;
}
if($Yname[13] ne ""){
$inname = $Yname[5];
$HP1  = 4;
$KOU1 = 4;
$MAM1 = 4;
$SUB1 = 4;
$inname = $Yname[13];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[5]さん 対 $Yname[13]さんの一回戦は$Yname[5]さんが勝利しました</B><BR>";
$Mname[5] = $Yname[13];
$Yname[5] = $Yname[5];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[5]さん 対 $Yname[13]さんの一回戦は$Yname[13]さんが勝利しました</B><BR>";
$Mname[5] = $Yname[5];
$Yname[5] = $Yname[13];
}
push @KAKIKOMI, $mes;
}
# 6 対 14
if($Yname[14] eq ""){
$mes = "<B>$Yname[6]さんは一回戦不戦勝でした</B><BR>";
push @KAKIKOMI, $mes;
}
if($Yname[14] ne ""){
$inname = $Yname[6];
$HP1  = 4;
$KOU1 = 4;
$MAM1 = 4;
$SUB1 = 4;
$inname = $Yname[14];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[6]さん 対 $Yname[14]さんの一回戦は$Yname[6]さんが勝利しました</B><BR>";
$Mname[6] = $Yname[14];
$Yname[6] = $Yname[6];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[6]さん 対 $Yname[14]さんの一回戦は$Yname[14]さんが勝利しました</B><BR>";
$Mname[6] = $Yname[6];
$Yname[6] = $Yname[14];
}
push @KAKIKOMI, $mes;
}
# 7 対 15
if($Yname[15] eq ""){
$mes = "<B>$Yname[7]さんは一回戦不戦勝でした</B><BR>";
push @KAKIKOMI, $mes;
}
if($Yname[15] ne ""){
$inname = $Yname[7];
$HP1  = 4;
$KOU1 = 4;
$MAM1 = 4;
$SUB1 = 4;
$inname = $Yname[15];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[7]さん 対 $Yname[15]さんの一回戦は$Yname[7]さんが勝利しました</B><BR>";
$Mname[7] = $Yname[15];
$Yname[7] = $Yname[7];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[7]さん 対 $Yname[15]さんの一回戦は$Yname[15]さんが勝利しました</B><BR>";
$Mname[7] = $Yname[7];
$Yname[7] = $Yname[15];
}
push @KAKIKOMI, $mes;
}
# 8 対 16
if($Yname[16] eq ""){
$mes = "<B>$Yname[8]さんは一回戦不戦勝でした</B><BR><BR>";
push @KAKIKOMI, $mes;
}
if($Yname[16] ne ""){
$inname = $Yname[8];
$HP1  = 4;
$KOU1 = 4;
$MAM1 = 4;
$SUB1 = 4;
$inname = $Yname[16];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[8]さん 対 $Yname[16]さんの一回戦は$Yname[8]さんが勝利しました</B><BR><BR>";
$Mname[8] = $Yname[16];
$Yname[8] = $Yname[8];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[8]さん 対 $Yname[16]さんの一回戦は$Yname[16]さんが勝利しました</B><BR><BR>";
$Mname[8] = $Yname[8];
$Yname[8] = $Yname[16];
}
push @KAKIKOMI, $mes;
}
if($Mname[1] ne ""){
$inname = $Mname[1];
&open3;
$Kdummy = $Kdummy + 1;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[1]さんにはメダル1枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[2] ne ""){
$inname = $Mname[2];
&open3;
$Kdummy = $Kdummy + 1;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[2]さんにはメダル1枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[3] ne ""){
$inname = $Mname[3];
&open3;
$Kdummy = $Kdummy + 1;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[3]さんにはメダル1枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[4] ne ""){
$inname = $Mname[4];
&open3;
$Kdummy = $Kdummy + 1;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[4]さんにはメダル1枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[5] ne ""){
$inname = $Mname[5];
&open3;
$Kdummy = $Kdummy + 1;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[5]さんにはメダル1枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[6] ne ""){
$inname = $Mname[6];
&open3;
$Kdummy = $Kdummy + 1;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[6]さんにはメダル1枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[7] ne ""){
$inname = $Mname[7];
&open3;
$Kdummy = $Kdummy + 1;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[7]さんにはメダル1枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[8] ne ""){
$inname = $Mname[8];
&open3;
$Kdummy = $Kdummy + 1;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[8]さんにはメダル1枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
$sou = 8;
}
#2回戦処理(4人に減らす)
if($sou >= 5 && $sou <= 8){
# 1 対 5
$inname = $Yname[1];
$HP1  = 3;
$KOU1 = 3;
$MAM1 = 3;
$SUB1 = 3;
$inname = $Yname[5];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<BR><BR><B><FONT size=4p color=RED>二回戦</FONT><BR>$Yname[1]さん 対 $Yname[5]さんの二回戦は$Yname[1]さんが勝利しました</B><BR>";
$Mname[9] = $Yname[5];
$Yname[1] = $Yname[1];
}
if($HP2 > $HP1){
$mes = "<BR><BR><B><FONT size=4p color=RED>二回戦</FONT><BR>$Yname[1]さん 対 $Yname[5]さんの二回戦は$Yname[5]さんが勝利しました</B><BR>";
$Mname[9] = $Yname[1];
$Yname[1] = $Yname[5];
}
push @KAKIKOMI, $mes;
# 2 対 6
if($Yname[6] eq ""){
$mes = "<BR><B>$Yname[2]さんは二回戦不戦勝でした</B><BR>";
$Yname[2] = $Yname[2];
push @KAKIKOMI, $mes;
}
if($Yname[6] ne ""){
$inname = $Yname[2];
$HP1  = 3;
$KOU1 = 3;
$MAM1 = 3;
$SUB1 = 3;
$inname = $Yname[6];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[2]さん 対 $Yname[6]さんの二回戦は$Yname[2]さんが勝利しました</B><BR>";
$Mname[10] = $Yname[6];
$Yname[2] = $Yname[2];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[2]さん 対 $Yname[6]さんの二回戦は$Yname[6]さんが勝利しました</B><BR>";
$Mname[10] = $Yname[2];
$Yname[2] = $Yname[6];
}
push @KAKIKOMI, $mes;
}
# 3 対 7
if($Yname[7] eq ""){
$mes = "<B>$Yname[3]さんは二回戦不戦勝でした</B><BR>";
$Yname[3] = $Yname[3];
push @KAKIKOMI, $mes;
}
if($Yname[7] ne ""){
$inname = $Yname[3];
$HP1  = 3;
$KOU1 = 3;
$MAM1 = 3;
$SUB1 = 3;
$inname = $Yname[7];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[3]さん 対 $Yname[7]さんの二回戦は$Yname[3]さんが勝利しました</B><BR>";
$Mname[11] = $Yname[7];
$Yname[3] = $Yname[3];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[3]さん 対 $Yname[7]さんの二回戦は$Yname[7]さんが勝利しました</B><BR>";
$Mname[11] = $Yname[3];
$Yname[3] = $Yname[7];
}
push @KAKIKOMI, $mes;
}
# 4 対 8
if($Yname[8] eq ""){
$mes = "<B>$Yname[4]さんは二回戦不戦勝でした</B><BR><BR>";
$Yname[4] = $Yname[4];
push @KAKIKOMI, $mes;
}
if($Yname[8] ne ""){
$inname = $Yname[4];
$HP1  = 3;
$KOU1 = 3;
$MAM1 = 3;
$SUB1 = 3;
$inname = $Yname[8];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[4]さん 対 $Yname[8]さんの二回戦は$Yname[4]さんが勝利しました</B><BR><BR>";
$Mname[12] = $Yname[8];
$Yname[4] = $Yname[4];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[4]さん 対 $Yname[8]さんの二回戦は$Yname[8]さんが勝利しました</B><BR><BR>";
$Mname[12] = $Yname[4];
$Yname[4] = $Yname[8];
}
push @KAKIKOMI, $mes;
}
if($Mname[9] ne ""){
$inname = $Mname[9];
&open3;
$Kdummy = $Kdummy + 2;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[9]さんにはメダル2枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[10] ne ""){
$inname = $Mname[10];
&open3;
$Kdummy = $Kdummy + 2;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[10]さんにはメダル2枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[11] ne ""){
$inname = $Mname[11];
&open3;
$Kdummy = $Kdummy + 2;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[11]さんにはメダル2枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[12] ne ""){
$inname = $Mname[12];
&open3;
$Kdummy = $Kdummy + 2;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[12]さんにはメダル2枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
$sou = 4;
}
#準決勝処理(2人に減らす)
if($sou >= 3 && $sou <= 4){
# 1 対 3
$inname = $Yname[1];
$HP1  = 2;
$KOU1 = 2;
$MAM1 = 2;
$SUB1 = 2;
$inname = $Yname[3];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<BR><BR><B><FONT size=4p color=RED>準決勝戦</FONT><BR>$Yname[1]さん 対 $Yname[3]さんの準決勝戦は$Yname[1]さんが勝利しました</B><BR>";
$Mname[13] = $Yname[3];
$Yname[1] = $Yname[1];
}
if($HP2 > $HP1){
$mes = "<BR><BR><B><FONT size=4p color=RED>準決勝戦</FONT><BR>$Yname[1]さん 対 $Yname[3]さんの準決勝戦は$Yname[3]さんが勝利しました</B><BR>";
$Mname[13] = $Yname[1];
$Yname[1] = $Yname[3];
}
push @KAKIKOMI, $mes;
# 2 対 4
if($Yname[4] eq ""){
$mes = "<B>$Yname[2]さんは準決勝戦不戦勝でした</B><BR><BR>";
$Yname[2] = $Yname[2];
push @KAKIKOMI, $mes;
}
if($Yname[4] ne ""){
$inname = $Yname[2];
$HP1  = 2;
$KOU1 = 2;
$MAM1 = 2;
$SUB1 = 2;
$inname = $Yname[4];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<B>$Yname[2]さん 対 $Yname[4]さんの準決勝戦は$Yname[2]さんが勝利しました</B><BR><BR>";
$Mname[14] = $Yname[4];
$Yname[2] = $Yname[2];
}
if($HP2 > $HP1){
$mes = "<B>$Yname[2]さん 対 $Yname[4]さんの準決勝戦は$Yname[4]さんが勝利しました</B><BR><BR>";
$Mname[14] = $Yname[2];
$Yname[2] = $Yname[4];
}
push @KAKIKOMI, $mes;
}
if($Mname[13] ne ""){
$inname = $Mname[13];
&open3;
$Kdummy = $Kdummy + 3;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[13]さんにはメダル3枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
if($Mname[14] ne ""){
$inname = $Mname[14];
&open3;
$Kdummy = $Kdummy + 3;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
$mes2 = "$Mname[14]さんにはメダル3枚が与えられました<BR>";
push @KAKIKOMI, $mes2;
}
$sou = 2;
}

#決勝処理
if($sou >= 1 && $sou <= 2){

@MEDAL = (7,8,9,10);
$GET = $MEDAL[int(rand(4))];
# 1 対 2
if($Yname[2] eq ""){
$mes = "<BR><BR><B><FONT size=4p color=RED>決勝戦</FONT><BR>$Yname[1]さんは決勝戦不戦勝で優勝しました！メダルが<FONT color=RED>$GET</FONT>個貰えました！<BR></B>";
push @KAKIKOMI, $mes;
}
if($Yname[2] ne ""){
$inname = $Yname[1];
$HP1  = 1;
$KOU1 = 1;
$MAM1 = 1;
$SUB1 = 1;
$inname = $Yname[2];
$HP2  = 1;
$KOU2 = 1;
$MAM2 = 1;
$SUB2 = 1;


@ransuu1 = (1,2,3,4,5,6,7,8,9,10);
$kou1 = $ransuu1[int(rand(10))];
@ransuu2 = (1,2,3,4,5,6,7,8,9,10);
$kou2 = $ransuu2[int(rand(10))];
$war1 = int(($KOU1 + $kou1) - ($MAM2 + $kou2));
$HP2 = $HP2 - $war1;
$war2 = int(($KOU2 + $kou2) - ($MAM1 + $kou1));
$HP1 = $HP1 - $war2;

if($HP1 >= $HP2){
$mes = "<BR><BR><B><FONT size=4p color=RED>決勝戦</FONT><BR>$Yname[1]さん 対 $Yname[2]さんの決勝戦は<FONT color=RED>$Yname[1]</FONT>さんが優勝しました！メダルが<FONT color=RED>$GET</FONT>個貰えました！<BR></B>";
$Mname[16] = $Yname[2];
$Yname[1] = $Yname[1];
}
if($HP2 > $HP1){
$mes = "<BR><B><FONT size=4p color=RED>決勝戦</FONT><BR>$Yname[1]さん 対 $Yname[2]さんの決勝戦は<FONT color=RED>$Yname[2]</FONT>さんが優勝しました！メダルが<FONT color=RED>$GET</FONT>個貰えました！<BR></B>";
$Mname[16] = $Yname[1];
$Yname[1] = $Yname[2];
}
$mes2 = "なお準優勝の$Mname[16]さんにはメダル5枚が与えられました<BR>";
push @KAKIKOMI, $mes;
push @KAKIKOMI, $mes2;

$inname = $Mname[16];
&open3;
$Kdummy = $Kdummy + 5;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);

}
}

$inname = $Yname[1];
&open3;
$Kdummy = $Kdummy + $GET;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);

open(FH, ">dat/turnlog.cgi") || &error("Can't open ");
print FH '&header;';
print FH "\n";
print FH 'print <<"EOF";';
print FH "\n";
print FH @KAKIKOMI;
print FH "\n";
print FH 'EOF';
print FH "\n";
print FH '&footer3;';
close(FH);
&unlock;

&start;
exit;

