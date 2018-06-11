##################################################################
# 　　　                  MONSTER'S　Ver1.8
#                   Copyright (C) 2002 MIKIO
#  このスクリプトはフリーウェアです。二次配布は禁止とします
#  改造・改造版配布は自由ですが、必ず【MONSTER'S 改】と表示して
#  ください。著作権は MIKIO に有ります。
# 【配布元】MIKIO-PALACE  http://park16.wakwak.com/~mikio-palace/
##################################################################

use utf8;
use open IO => ":utf8";
use open ":std";

$cgiurl = './monster.cgi';
$kanrim = './kanri.cgi';
$newurl = './newgame.cgi';
$ncook  = './cook.cgi';
$countdata = 'count.cgi';
$userdata  = 'user.cgi';
$monsdata = 'dat/monsterdat.cgi';
$timedata = 'dat/time.cgi';
$ver = 'Ver1.8';
$titleimg = 'title.gif';
$ENV{'TZ'} = "JST-9";

# ************* 変更する所はここから *******************
# ファイルのロック(Mkdir = 2,Symlink=1,No = 0)
$lockkey  = 2;
# ロックファイル名＆パス
$lockfile = './mons.lock';
# データ格納フォルダ（適当な名前を付けてください）
$datadir = 'mons';
# マスターネーム
$mastername = 'nezirin';
# マスターパスワード
$masterpassword = 'eclipse';
# ＣＧＩへのパス
# http://127.0.0.1/~mikio/monsters/monster.cgiの場合は
# http://127.0.0.1/~mikio/monstersにしてください
$cgipath = "http://127.0.0.1/monsters";
# 画像へのパス
# 実際に画像が入ってるフォルダ名まで
$img = "http://127.0.0.1/monsters/img";
# 掲示板へのＵＲＬ
$bbs = "http://bbs";
# パーミッションを設定
$dirmode = 0777;
# 参加人数を設定（30人以下推奨）
$sankaMAX = 30;#(参加総数の設定です)
$maxshow  = 30;#(TOP画面に表示される数です。)
# データ保存期間
$goodbye = 90;
# 戻り先ＵＲＬ
$homepage = "http://127.0.0.1";
# 戻り先表示文字
$home_title = 'HOME';
# 重複チェックをする時は=1 しない時は=0
$iplog = 1;
# 初期レベルＵＰ値
$nextup = 10;
# 戦闘可能ラウンド数（5以下）
$maxround = 4;
# 戦闘後何分間後に戦闘できるか 30 = 30分後
$nexpplay = 0.1;
# 配合を許可するレベル
$haigoulevel = 1;
# バックアップをとるか　とる=1 とらない=0
$backup = 1;
# バックアップ用フォルダ（適当な名前を付けてください）
$backfolder = 'backup';
# 配合料金（配合回数×$Mmoney）ゴールドになります
$Mmoney = 0;
# 未使用は 0:小型BBS使用 1:
$bbsmode = 1;
# 参加者以外の書込みを許可 1 :参加者以外の書込みを拒否 0
$bbsok = 0;

############################　設定はここまで　########################

############## 禁止IP 追加(2004.2.4) #################

# アクセスを禁止するIPを入力して下さい 
#【例 127.0.0.1の場合は ("127.0.0")と書いて下さい)
# 複数の設定の場合は("127.0.0","211.56.108","61.123.45")の様に,をはさんで" "で囲み入力して下さい。
#アクセス制限をかけない時は必ず半角スペース(" ")を入力しておいて下さい。
@noip = (" ");

############################　追加はここまで　########

&get_cookie2;

if($setimg eq ""){$imgpath = $img;}
if($setimg ne ""){$imgpath = $setimg;}

#========#
# ソート #
#========#

sub ranksort {

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Sname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
    push @points,$Skey;
    }    
    @ranks=sort{$b <=> $a} @points;
    open(FH,"${datadir}/$countdata") || &error("Can't open $countdata");
    $sou = <FH>;
    close(FH);
    $sounin = $sou - 1;
    
    for($i = 0; $i <= $sounin; $i++) {
    foreach $line (@lines) {
    ($Sname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
    $ranking = @ranks[$i];
    if($Skey == $ranking ) {
    push @newrank,$line;
    $line="";
    }
    }
    }
&lock;
open(FH, ">${datadir}/$userdata") || &error("Can't open $userdata");
print FH @newrank;
close(FH);
&unlock;

}

#================#
#  保存期間調査  #
#================#

sub countchange {

open(FH,"${datadir}/$userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($CCname,$CCpass,$CCip,$CCbye,$CCplay,$CCplay2,$Yplay3,$CCkey,$CCimg1,$CChai1,$CClev1,$CCimg2,$CChai2,$CClev2,$CCimg3,$CChai3,$CClev3,$CCmoney,$CCmes,$CCturn) = split(/<>/,$line);
    if($CCbye <= time) {
open(FH,"dat/id.cgi");
@IDlines = <FH>;
close(FH);
foreach $IDline (@IDlines) {
    ($IDname,$IDpass) = split(/<>/,$IDline);
    if($IDname eq $CCname){
    $IDline="";
    }
    &lock;
    open(FH, ">dat/id.cgi");
    print FH @IDlines;
    close(FH);
    &unlock;
    }
    $line="";
    unlink "${datadir}/$CCname.cgi";
    unlink "bbs/$CCname.cgi";
    unlink "waza/$CCname.cgi";
    unlink "keyset/$CCname.cgi";
    unlink "omiai/$CCname.cgi";
    if($backup == 1){
    unlink "${backfolder}/$CCname.cgi";
    }
    &lock;
    open(FH, ">${datadir}/$userdata");
    print FH @lines;
    close(FH);
    &unlock;
    open(FH,"${datadir}/$countdata") || &error("Can't open $countdata");
    $sou = <FH>;
    close(FH);
    $souin = $sou - 1;
    &lock;
    open(FH, ">${datadir}/$countdata") || &error("Can't open $countdata");
    print FH $souin;
    close(FH);
    &unlock;
    }
}
}

#==============#
# モンスゲット #
#==============#

sub get{

if($pattern == 2){
$Klev[2] = 2;
$Kmlev[2] = 10;
$Kimg[2]  = $Aimg;
$Khp[2]   = $Ahp;
$Kmhp[2]  = $Ahp;
$Kmp[2]   = $Amp;
$Kmmp[2]  = $Amp;
$Kkou[2]  = $Akou;
$Kmam[2]  = $Amam;
$Ksub[2]  = $Asub;
$Khai[2]  = 0;
$Kcount[2] = 0;
$Knecount[2] = $nextup;
$Ksex[2]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[2] = $sei[int(rand(27))];
}
if($pattern == 3){
$Klev[3] = 2;
$Kmlev[3] = 10;
$Kimg[3]  = $Aimg;
$Khp[3]   = $Ahp;
$Kmhp[3]  = $Ahp;
$Kmp[3]   = $Amp;
$Kmmp[3]  = $Amp;
$Kkou[3]  = $Akou;
$Kmam[3]  = $Amam;
$Ksub[3]  = $Asub;
$Khai[3]  = 0;
$Kcount[3] = 0;
$Knecount[3] = $nextup;
$Ksex[3]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[3] = $sei[int(rand(27))];
}
if($pattern == 4){
$Klev[4] = 2;
$Kmlev[4] = 10;
$Kimg[4]  = $Aimg;
$Khp[4]   = $Ahp;
$Kmhp[4]  = $Ahp;
$Kmp[4]   = $Amp;
$Kmmp[4]  = $Amp;
$Kkou[4]  = $Akou;
$Kmam[4]  = $Amam;
$Ksub[4]  = $Asub;
$Khai[4]  = 0;
$Kcount[4] = 0;
$Knecount[4] = $nextup;
$Ksex[4]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[4] = $sei[int(rand(27))];
}
if($pattern == 5){
$Klev[5] = 2;
$Kmlev[5] = 10;
$Kimg[5]  = $Aimg;
$Khp[5]   = $Ahp;
$Kmhp[5]  = $Ahp;
$Kmp[5]   = $Amp;
$Kmmp[5]  = $Amp;
$Kkou[5]  = $Akou;
$Kmam[5]  = $Amam;
$Ksub[5]  = $Asub;
$Khai[5]  = 0;
$Kcount[5] = 0;
$Knecount[5] = $nextup;
$Ksex[5]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[5] = $sei[int(rand(27))];
}
if($pattern == 6){
$Klev[6] = 2;
$Kmlev[6] = 10;
$Kimg[6]  = $Aimg;
$Khp[6]   = $Ahp;
$Kmhp[6]  = $Ahp;
$Kmp[6]   = $Amp;
$Kmmp[6]  = $Amp;
$Kkou[6]  = $Akou;
$Kmam[6]  = $Amam;
$Ksub[6]  = $Asub;
$Khai[6]  = 0;
$Kcount[6] = 0;
$Knecount[6] = $nextup;
$Ksex[6]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[6] = $sei[int(rand(27))];
}
if($pattern == 7){
$Klev[7] = 2;
$Kmlev[7] = 10;
$Kimg[7]  = $Aimg;
$Khp[7]   = $Ahp;
$Kmhp[7]  = $Ahp;
$Kmp[7]   = $Amp;
$Kmmp[7]  = $Amp;
$Kkou[7]  = $Akou;
$Kmam[7]  = $Amam;
$Ksub[7]  = $Asub;
$Khai[7]  = 0;
$Kcount[7] = 0;
$Knecount[7] = $nextup;
$Ksex[7]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[7] = $sei[int(rand(27))];
}
if($pattern == 8){
$Klev[8] = 2;
$Kmlev[8] = 10;
$Kimg[8]  = $Aimg;
$Khp[8]   = $Ahp;
$Kmhp[8]  = $Ahp;
$Kmp[8]   = $Amp;
$Kmmp[8]  = $Amp;
$Kkou[8]  = $Akou;
$Kmam[8]  = $Amam;
$Ksub[8]  = $Asub;
$Khai[8]  = 0;
$Kcount[8] = 0;
$Knecount[8] = $nextup;
$Ksex[8]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[8] = $sei[int(rand(27))];
}
if($pattern == 9){
$Klev[9] = 2;
$Kmlev[9] = 10;
$Kimg[9]  = $Aimg;
$Khp[9]   = $Ahp;
$Kmhp[9]  = $Ahp;
$Kmp[9]   = $Amp;
$Kmmp[9]  = $Amp;
$Kkou[9]  = $Akou;
$Kmam[9]  = $Amam;
$Ksub[9]  = $Asub;
$Khai[9]  = 0;
$Kcount[9] = 0;
$Knecount[9] = $nextup;
$Ksex[9]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[9] = $sei[int(rand(27))];
}
if($pattern == 10){
$Klev[10] = 2;
$Kmlev[10] = 10;
$Kimg[10]  = $Aimg;
$Khp[10]   = $Ahp;
$Kmhp[10]  = $Ahp;
$Kmp[10]   = $Amp;
$Kmmp[10]  = $Amp;
$Kkou[10]  = $Akou;
$Kmam[10]  = $Amam;
$Ksub[10]  = $Asub;
$Khai[10]  = 0;
$Kcount[10] = 0;
$Knecount[10] = $nextup;
$Ksex[10]  = $Asex;
@sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
$Ksei[10] = $sei[int(rand(27))];
}
}

#================#
#  ファイルopen  #
#================#

sub open1 {

open(FH,"${datadir}/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Kname,$Kpass,$Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Klev[3],$Kmlev[3],$Kimg[3],$Khp[3],$Kmhp[3],$Kmp[3],$Kmmp[3],$Kkou[3],$Kmam[3],$Ksub[3],$Khai[3],$Kcount[3],$Knecount[3],$Ksex[3],$Ksei[3],$Klev[4],$Kmlev[4],$Kimg[4],$Khp[4],$Kmhp[4],$Kmp[4],$Kmmp[4],$Kkou[4],$Kmam[4],$Ksub[4],$Khai[4],$Kcount[4],$Knecount[4],$Ksex[4],$Ksei[4],$Klev[5],$Kmlev[5],$Kimg[5],$Khp[5],$Kmhp[5],$Kmp[5],$Kmmp[5],$Kkou[5],$Kmam[5],$Ksub[5],$Khai[5],$Kcount[5],$Knecount[5],$Ksex[5],$Ksei[5],$Klev[6],$Kmlev[6],$Kimg[6],$Khp[6],$Kmhp[6],$Kmp[6],$Kmmp[6],$Kkou[6],$Kmam[6],$Ksub[6],$Khai[6],$Kcount[6],$Knecount[6],$Ksex[6],$Ksei[6],$Klev[7],$Kmlev[7],$Kimg[7],$Khp[7],$Kmhp[7],$Kmp[7],$Kmmp[7],$Kkou[7],$Kmam[7],$Ksub[7],$Khai[7],$Kcount[7],$Knecount[7],$Ksex[7],$Ksei[7],$Klev[8],$Kmlev[8],$Kimg[8],$Khp[8],$Kmhp[8],$Kmp[8],$Kmmp[8],$Kkou[8],$Kmam[8],$Ksub[8],$Khai[8],$Kcount[8],$Knecount[8],$Ksex[8],$Ksei[8],$Klev[9],$Kmlev[9],$Kimg[9],$Khp[9],$Kmhp[9],$Kmp[9],$Kmmp[9],$Kkou[9],$Kmam[9],$Ksub[9],$Khai[9],$Kcount[9],$Knecount[9],$Ksex[9],$Ksei[9],$Klev[10],$Kmlev[10],$Kimg[10],$Khp[10],$Kmhp[10],$Kmp[10],$Kmmp[10],$Kkou[10],$Kmam[10],$Ksub[10],$Khai[10],$Kcount[10],$Knecount[10],$Ksex[10],$Ksei[10],$Kdummy,$Kkey,$Kmoney) = split(/<>/,$line);}

}

#=================#
#  ファイルopen2  #
#=================#

sub open2 {

open(FH,"waza/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($waza[1],$waza[2],$waza[3],$waza[4],$waza[5],$waza[6],$waza[7],$waza[8],$waza[9],$waza[10],$waza[11],$waza[12],$waza[13],$waza[14],$waza[15],$waza[16],$waza[17],$waza[18],$waza[19],$waza[20],$waza[21],$waza[22],$waza[23],$waza[24],$waza[25],$waza[26],$waza[27],$waza[28],$waza[29],$waza[30],$waza[31],$waza[32],$waza[33],$waza[34],$waza[35],$waza[36],$waza[37],$waza[38],$waza[39],$waza[40],$waza[41],$waza[42],$waza[43],$waza[44],$waza[45],$waza[46],$waza[47],$waza[48],$waza[49],$waza[50],$waza[51],$waza[52]) = split(/<>/,$line);
}
}

#=================#
#  ファイルopen3  #
#=================#

sub open3 {

open(FH,"${datadir}/$inname.cgi") || &error("Can't open open3");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Kname,$Kpass,$Klev1,$Kmlev1,$Kimg1,$Khp1,$Kmhp1,$Kmp1,$Kmmp1,$Kkou1,$Kmam1,$Ksub1,$Khai1,$Kcount1,$Knecount1,$Ksex1,$Ksei1,$Klev2,$Kmlev2,$Kimg2,$Khp2,$Kmhp2,$Kmp2,$Kmmp2,$Kkou2,$Kmam2,$Ksub2,$Khai2,$Kcount2,$Knecount2,$Ksex2,$Ksei2,$Klev3,$Kmlev3,$Kimg3,$Khp3,$Kmhp3,$Kmp3,$Kmmp3,$Kkou3,$Kmam3,$Ksub3,$Khai3,$Kcount3,$Knecount3,$Ksex3,$Ksei3,$Klev4,$Kmlev4,$Kimg4,$Khp4,$Kmhp4,$Kmp4,$Kmmp4,$Kkou4,$Kmam4,$Ksub4,$Khai4,$Kcount4,$Knecount4,$Ksex4,$Ksei4,$Klev5,$Kmlev5,$Kimg5,$Khp5,$Kmhp5,$Kmp5,$Kmmp5,$Kkou5,$Kmam5,$Ksub5,$Khai5,$Kcount5,$Knecount5,$Ksex5,$Ksei5,$Klev6,$Kmlev6,$Kimg6,$Khp6,$Kmhp6,$Kmp6,$Kmmp6,$Kkou6,$Kmam6,$Ksub6,$Khai6,$Kcount6,$Knecount6,$Ksex6,$Ksei6,$Klev7,$Kmlev7,$Kimg7,$Khp7,$Kmhp7,$Kmp7,$Kmmp7,$Kkou7,$Kmam7,$Ksub7,$Khai7,$Kcount7,$Knecount7,$Ksex7,$Ksei7,$Klev8,$Kmlev8,$Kimg8,$Khp8,$Kmhp8,$Kmp8,$Kmmp8,$Kkou8,$Kmam8,$Ksub8,$Khai8,$Kcount8,$Knecount8,$Ksex8,$Ksei8,$Klev9,$Kmlev9,$Kimg9,$Khp9,$Kmhp9,$Kmp9,$Kmmp9,$Kkou9,$Kmam9,$Ksub9,$Khai9,$Kcount9,$Knecount9,$Ksex9,$Ksei9,$Klev10,$Kmlev10,$Kimg10,$Khp10,$Kmhp10,$Kmp10,$Kmmp10,$Kkou10,$Kmam10,$Ksub10,$Khai10,$Kcount10,$Knecount10,$Ksex10,$Ksei10,$Kdummy,$Kkey,$Kmoney) = split(/<>/,$line);}

}

#===========#
# ヘッダー  #
#===========#

sub header {

print <<"EOF";
Content-type: text/html;

<HTML>
<HEAD>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=utf-8">
<TITLE>MONSTER'S</TITLE>
</HEAD>
<BODY bgcolor=#0066FF>
<LINK REL="stylesheet" HREF="style.css" TYPE="text/css">
<style type="text/css">
<!--
A:Link,A:Visited{color:white;text-decoration:none;}
A:hover{color:crimson;text-decoration:none;}
-->
</style>
EOF

}

#============#
# ヘッダー2  #
#============#

sub header2 {

print <<"EOF";
Content-type: text/html;

<HTML>
<HEAD>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=utf-8">
<TITLE>MONSTER'S</TITLE>
</HEAD>
<BODY  background="$imgpath/back.gif">
<LINK REL="stylesheet" HREF="style.css" TYPE="text/css">
<style type="text/css">
<!--
A:Link,A:Visited{color:white;text-decoration:none;}
A:hover{color:crimson;text-decoration:none;}
-->
</style>
EOF

}

#============#
#  フッター  #
#============#

sub footer {

print <<"EOF";
<DIV align="right">
<BR>
<TABLE>
<TBODY>
<TR>
<TD colspan="2" align="center"><FONT color=#ff3333><B>MONSTER'S $ver </B></FONT></TD>
</TR>
<TR>
<TD><B>【サポート・修正】</B></TD>
<TD><A href="http://ayasoft.hmc6.net/">AYA'sCafe【サポ専】</A></TD>
</TR>
<TR>
<TD><B>【作成・配布】</B></TD>
<TD><A href="http://park16.wakwak.com/~mikio-palace/">MIKIO-PALACE</A></TD>
</TR>
<TR>
<TD><B>【ADVISER】</B></TD>
<TD>RYUJIN・あばかぶ</TD>
</TR>
<TR>
<TD colspan="2"><B>Copyright (C) 2002-2004：MIKIO</B></TD>
</TR>
</TBODY>
</TABLE>
</DIV>
</BODY>
</HTML>
EOF

}

#=============#
#  フッター2  #
#=============#

sub footer2 {

print <<"EOF";
<DIV align="right">
<BR>
<TABLE>
<TBODY>
<TR>
<TD colspan="2" align="center"><FONT color=#ff3333><B>MONSTER'S $ver </B></FONT></TD>
</TR>
<TR>
<TD><B>【サポート・修正】</B></TD>
<TD><A href="http://ayasoft.hmc6.net/">AYA'sCafe【サポ専】</A></TD>
</TR>
<TR>
<TD><B>【作成・配布】</B></TD>
<TD><A href="http://park16.wakwak.com/~mikio-palace/">MIKIO-PALACE</A></TD>
</TR>
<TR>
<TD><B>【ADVISER】</B></TD>
<TD>RYUJIN・あばかぶ</TD>
</TR>
<TR>
<TD colspan="2"><B>Copyright (C) 2002-2004：MIKIO</B></TD>
</TR>
</TBODY>
</TABLE>
</DIV>
</BODY>
</HTML>
EOF

}

#=============#
#  フッター3  #
#=============#

sub footer3 {

print <<"EOF";
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOP">
</CENTER>
</FORM>
<DIV align="right">
<TABLE>
<TBODY>
<TR>
<TD colspan="2" align="center"><FONT color=#ff3333><B>MONSTER'S $ver </B></FONT></TD>
</TR>
<TR>
<TD><B>【サポート・修正】</B></TD>
<TD><A href="http://ayasoft.hmc6.net/">AYA'sCafe【サポ専】</A></TD>
</TR>
<TR>
<TD><B>【作成・配布】</B></TD>
<TD><A href="http://park16.wakwak.com/~mikio-palace/">MIKIO-PALACE</A></TD>
</TR>
<TR>
<TD><B>【ADVISER】</B></TD>
<TD>RYUJIN・あばかぶ</TD>
</TR>
<TR>
<TD colspan="2"><B>Copyright (C) 2002-2004：MIKIO</B></TD>
</TR>
</TBODY>
</TABLE>
</DIV>
</BODY>
</HTML>
EOF

}

#==============#
# デコード処理 #
#==============#

sub decode  {

    if ($ENV{'REQUEST_METHOD'} eq "POST") {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
        @pairs = split(/&/, $buffer);
    }
    else {
    @pairs = split(/&/, $ENV{'QUERY_STRING'});
    }

    foreach $pair (@pairs) {
       ($name, $value) = split(/=/, $pair);
        $name =~ tr/+/ /;
        $name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

        $value =~ s/</&lt;/g;
        $value =~ s/>/&gt;/g;
        $value =~ s/\,/，/g;
        $value =~ s/\r\n/<br>/g;
        $value =~ s/\r/<br>/g;
        $value =~ s/\n/<br>/g;

        $FORM{$name} = $value;
    }
}

#=============#
# クッキーSET #
#=============#

sub set_cookie {
    # クッキーは30日間有効
    ($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = gmtime(time + 30*24*60*60);
    $yearg += 1900;
    if ($secg  < 10) { $secg  = "0$secg";  }
    if ($ming  < 10) { $ming  = "0$ming";  }
    if ($hourg < 10) { $hourg = "0$hourg"; }
    if ($mdayg < 10) { $mdayg = "0$mdayg"; }
    $month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
    $youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
    $date_gmt = "$youbi, $mdayg\-$month\-$yearg $hourg:$ming:$secg GMT";
    $cook = "name\:$Yname\,password\:$Ypass\,Ikai\:$Ikai\,ROOM\:$ROOM\,BYE\:8181";
    print "Set-Cookie: MONSTERS=$cook; expires=$date_gmt\n";
}

sub set_cookie2 {
    # クッキーは30日間有効
    ($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = gmtime(time + 30*24*60*60);
    $yearg += 1900;
    if ($secg  < 10) { $secg  = "0$secg";  }
    if ($ming  < 10) { $ming  = "0$ming";  }
    if ($hourg < 10) { $hourg = "0$hourg"; }
    if ($mdayg < 10) { $mdayg = "0$mdayg"; }
    $month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
    $youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
    $date_gmt = "$youbi, $mdayg\-$month\-$yearg $hourg:$ming:$secg GMT";
    $cook2 = "setimg<>$setimg";
    print "Set-Cookie: MONSTERS2=$cook2; expires=$date_gmt\n";
}

#=============#
# クッキーGET #
#=============#

sub get_cookie { 

    @pairs = split(/\;/,$ENV{'HTTP_COOKIE'});
    foreach $pair (@pairs) {
        local($name, $value) = split(/\=/, $pair);
        $name =~ s/ //g;
        $DUMMY{$name} = $value;
    }
    @pairs = split(/\,/,$DUMMY{'MONSTERS'});
    foreach $pair (@pairs) {
        local($name, $value) = split(/\:/, $pair);
        $COOKIE{$name} = $value;
    }
    $Yname = $COOKIE{'name'};
    $Ypass = $COOKIE{'password'};
    $Ikai  = $COOKIE{'Ikai'};
    $ROOM  = $COOKIE{'ROOM'};
    $BYE   = $COOKIE{'BYE'};

    if ($FORM{'name'})     { $Yname = $FORM{'name'}; }
    if ($FORM{'passwoed'}) { $Ypass = $FORM{'password'}; }
    if ($FORM{'Ikai'})     { $Ikai  = $FORM{'Ikai'}; }
    if ($FORM{'ROOM'})     { $ROOM  = $FORM{'ROOM'}; }
    if ($FORM{'BYE'})      { $BYE   = $FORM{'BYE'}; }
}

sub get_cookie2 { 

    @pairs = split(/\;/,$ENV{'HTTP_COOKIE'});
    foreach $pair (@pairs) {
        local($name, $value) = split(/\=/, $pair);
        $name =~ s/ //g;
        $DUMMY{$name} = $value;
    }
    @pairs = split(/\,/,$DUMMY{'MONSTERS2'});
    foreach $pair (@pairs) {
        local($name, $value) = split(/<>/, $pair);
        $COOKIE{$name} = $value;
    }
    $setimg = $COOKIE{'setimg'};

    if ($FORM{'setimg'})     { $setimg = $FORM{'setimg'}; }

}

#========#
# IP取得 #
#========#

sub get_ip {

    $host = $ENV{'REMOTE_HOST'};
    $addr = $ENV{'REMOTE_ADDR'};

    if ($get_remotehost) {
        if ($host eq "" || $host eq "$addr") {
            $host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
        }
    }
    if ($host eq "") { $host = $addr; }
}

#========#
# エラー #
#========#

sub error {
&unlock;
&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#FF0033"><B><B>$_[0]</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOP">
</FORM>
</CENTER>
EOF
&footer;
exit;
}

#--------------#
#  ロック処理  #
#--------------#
sub lock {
	# 古いロックは削除
	if (-e $lockfile) {
		local($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 30) { &unlock; }
	}
	local($retry) = 5;
	# symlink関数式ロック
	if ($lockkey == 1) {
		while (!symlink(".", $lockfile)) {
			if (--$retry <= 0) { &error('現在、サーバが混み合っています'); }
			sleep(1);
		}
	# mkdir関数式ロック
	} elsif ($lockkey == 2) {
		while (!mkdir($lockfile, 0755)) {
			if (--$retry <= 0) { &error('現在、サーバが混み合っています'); }
			sleep(1);
		}
	}
	$lockflag=1;
}

#--------------#
#  ロック解除  #
#--------------#
sub unlock {
	if ($lockkey == 1) { unlink($lockfile); }
	elsif ($lockkey == 2) { rmdir($lockfile); }

	$lockflag=0;
}

#==================#
#  パス暗号化処理  #
#==================#

sub pass {

$crypted = crypt($Ypass, $Yname);

}

#==================#
#  パス暗号化処理  #
#==================#

sub passan {

$inpass = crypt($inpass, $inname);

}

#==========#
# 時間取得 #
#==========#

sub gettime {

if($timelog == 1){
$del  =  $Ybye - time;
$mday = int($del/86400)+1;
}
elsif($timelog == 2){
($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = localtime(time);
$yearg += 1900;
$mong++;
if ($ming  < 10) { $ming  = "0$ming";  }
if ($hourg < 10) { $hourg = "0$hourg"; }
if ($mdayg < 10) { $mdayg = "0$mdayg"; }
$Ktime = "[$yearg.$mong.$mdayg($hourg:$ming)]";
}
elsif($timelog == 5){
($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = localtime($endtime);
$yearg += 1900;
$mong++;
if ($ming  < 10) { $ming  = "0$ming";  }
if ($hourg < 10) { $hourg = "0$hourg"; }
if ($mdayg < 10) { $mdayg = "0$mdayg"; }
$logtime = "$yearg年$mong月$mdayg日($hourg:$ming)";
}

}

#==============#
# バックアップ #
#==============#

sub backup {

if($backup == 1){
open(FH,"${datadir}/$inname.cgi") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

&lock;
open(FH, ">${backfolder}/$Kname.cgi") || &error("Can't open ");
print FH @lines;
close(FH);
&unlock;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

&lock;
open(FH, ">${backfolder}/$userdata") ;
print FH @lines;
close(FH);
&unlock;

open(FH,"${datadir}/$countdata") || &error("Can't open!");
@lines = <FH>;
close(FH);

&lock;
open(FH, ">${backfolder}/$countdata") ;
print FH @lines;
close(FH);
&unlock;
}
}

#============#
#  敗戦処理  #
#============#

sub haisen {

@syori = (1,1,1,1,1,2,2,2,2,3);
$mai = $syori[int(rand(10))];

if($Kkey <= 4 && $inkai <= 10){
$mai = 1;
}
if($Kkey <= 3){
$mai = 0;
}

if($mai == 1){
$newkey = $Kkey - 1;
print <<"EOF";
<CENTER>
<TABLE bgcolor="#ff0000" width="400">
<TBODY>
<TR>
<TD colspan="3" width="400" bgcolor="#000000" align="center">
<BLOCKQUOTE>
<TABLE>
<TBODY>
<TR>
<TD align="left"><FONT size="4" color="#ffff00"><B>不幸のKEY-1</B></FONT><FONT size="4" color="#ffffff">を拾ってしまった！</FONT></FONT></TD>
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

if($mai == 2){
$newkey = $Kkey - 3;
print <<"EOF";
<CENTER>
<TABLE bgcolor="#ff0000" width="400">
<TBODY>
<TR>
<TD colspan="3" width="400" bgcolor="#000000" align="center">
<BLOCKQUOTE>
<TABLE>
<TBODY>
<TR>
<TD align="left"><FONT size="4" color="#ffff00"><B>不幸のKEY-3</B></FONT><FONT size="4" color="#ffffff">を拾ってしまった！</FONT></FONT></TD>
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

if($mai == 3){
$logkey = int($Kkey / 5);
$newkey = $Kkey - $logkey;
print <<"EOF";
<CENTER>
<TABLE bgcolor="#ff0000" width="400">
<TBODY>
<TR>
<TD colspan="3" width="400" bgcolor="#000000" align="center">
<BLOCKQUOTE>
<TABLE>
<TBODY>
<TR>
<TD align="left"><FONT size="4" color="#ffff00"><B>超不幸のKEY-$logkey</B></FONT><FONT size="4" color="#ffffff">を拾ってしまった！！</FONT></FONT></TD>
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

}

#====================#
#  メダル杯初期時間  #
#====================#

sub timesyori{

($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = localtime(time);
$yearg += 1900;
$mong++;

if($mdayg >= 1 && $mdayg <= 10 && E != 1){
$day = 11;
$mon = $mong;
$year= $yearg;
$E   = 1;
}
if($mdayg >= 11 && $mdayg <= 20 && E != 1){
$day = 21;
$mon = $mong;
$year= $yearg;
$E   = 1;
}
if($mdayg >= 21 && $mdayg <= 31 && E != 1){
$day = 1;
$mon = $mong +1;
$year= $yearg;
if($mon == 13){
$mon = 1;
$year++;
$E   = 1;
}
}
$year -=1900;
$mon -=1;

use Time::Local;
$time2 = timelocal(0,0,0,$day,$mon,$year); 
open(FH, ">dat/time2.cgi") ;
print FH $time2;
close(FH);

}


1;

__END__
