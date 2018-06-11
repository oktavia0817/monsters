#!C:/perl64/bin/perl
# ↑サーバーに合わせてください

use utf8;
use open IO => ":utf8";
use open ":std";

require './set.cgi';

&decode;

&get_cookie;

if($BYE == 8181){ &error("重複登録の可能\性\がある為参加出来ません。");}
if($BYE == 8282){ &error("放棄後30日間は登録出来ません。");}

if($FORM{'mode'} eq "")            {  &newgame; exit; }
elsif($FORM{'mode'} eq "sinki")    {  &sinki; }



sub newgame {

open(FH,"${datadir}/$countdata");
$sou = <FH>;
close(FH);

$toplog = $sankaMAX - $sou;
if(!$toplog != 0 ) { &error("参加数が最大です。登録できません。");}

&header;

print <<"EOF";
<BR>
<BR>
<TABLE width="100%" bgcolor="#ff00ff">
<TBODY>
<TR>
<TD bgcolor="#660066"><B><FONT size="+2" color="#FFFFFF">NEW-GAME</FONT></B></TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<BR>
<TABLE>
<TBODY>
<TR>
<TD align="center" bgcolor="black">
<FORM ACTION="$newurl" METHOD="POST">
<B><FONT color="#ffff00" size="5">UserName・Password</FONT><FONT  color="#ffffff" size="4">を設定してください</FONT></B></TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<TABLE>
<TBODY>
<TR>
<TD><B><FONT color="#ffff00" size="4">UserName</FONT></B>（半角英数4文字～8文字）
<BR>
<INPUT type="text" size="14" name="name" value="">
<BR>
<BR>
<B><FONT color="#ffff00" size="4">Password</FONT></B>（半角英数4文字～8文字）
<BR>
<INPUT type="password" size="14" name="password" value="">
<BR>
<BR>
<INPUT type="submit" mode="sinki" value="　登　　録　">
<INPUT type="hidden" name="mode" value="sinki">
</TD>
</TR>
</TBODY>
</TABLE>
</FORM>
<BR>
<BR>
</CENTER>
EOF

&footer;

}

sub sinki {

open(FH,"${datadir}/$countdata");
$sou = <FH>;
close(FH);

$toplog = $sankaMAX - $sou;
if(!$toplog != 0 ) { &error("参加数が最大です。登録できません。");}

if ($FORM{'name'} =~ m/[^0-9a-zA-Z]/)
{&error("ユーザー名に半角英数字以外の文字が含まれています。"); }
if ($FORM{'password'} =~ m/[^0-9a-zA-Z]/)
{&error("パスワードに半角英数字以外の文字が含まれています。"); }

if ($FORM{'name'} eq "") { &error("名前がありません");}
if ($FORM{'password'} eq "") { &error("パスワードがありません");}
if ($FORM{'name'} eq $FORM{'password'}) { &error("IDとパスワードは違うものにして下さい");}

if (length($FORM{'name'}) < 4 or length($FORM{'name'}) > 8)
{ &error("ユーザー名は、4文字以上、8文字以下で入力して下さい。");}
if (length($FORM{'password'}) < 4 or length($FORM{'password'}) > 8) 
{ &error("パスワードは、4文字以上、8文字以下で入力して下さい。");} 

if(!open(FH,"$datadir/$countdata")) { &makeDF; }
if(open(FH,"$datadir/$FORM{'name'}.cgi")) {&error("その名前は既に登録されています");}

open(FH,"${datadir}/$userdata");
@lines = <FH>;
close(FH);

    if($iplog == 1){
    &get_ip;
foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($host eq $Yip) { &error("重複登録の可能\性\があります。現在の設定では参加出来ません。")}
    }
}

&makeNEW;

&header;

print <<"EOF";
<CENTER><B><FONT color="#ffff00" size="5">UserName・Password</FONT><FONT color="#0000cc" size="+3">OK！</FONT></B>
<HR>
<CENTER>
<TABLE width="700" bgcolor="#000000">
<TBODY>
<TR>
<TD align="center"><B><FONT color="#FF0000" size="4">以下の内容で登録が完了しました。</FONT></B><BR>
<BR>
<TABLE cellspacing="3" cellpadding="1" width="697" bgcolor="black" border="0">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff" colspan="3" rowspan="4"><IMG src="$imgpath/$Yimg.gif" border="0"></TD>
<TD bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">LEVEL</FONT></B></DIV>
</TD>
<TD bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">H P</FONT></B></DIV>
</TD>
<TD bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">M P</FONT></B></DIV>
</TD>
<TD bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">攻 撃 力</FONT></B></DIV>
</TD>
<TD bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">守 備 力</FONT></B></DIV>
</TD>
<TD bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">経 験 値</FONT></B></DIV>
</TD>
</TR>
<TR>
<TD align="center" width="70" bgcolor="white">1 / 10</FONT></TD>
<TD width="67" bgcolor="white" align="center">$Yhp / $Ymhp</FONT></TD>
<TD width="61" bgcolor="white" align="center">$Ymp / $Ymmp</FONT></TD>
<TD width="90" bgcolor="white" align="center">$Ykou</FONT></TD>
<TD width="96" bgcolor="white" align="center">$Ymam</FONT></TD>
<TD width="87" bgcolor="white" align="center">0 / $nextup</FONT></TD>
</TR>
<TR>
<TD width="70" bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">配 合 数</FONT></B></DIV>
</TD>
<TD width="67" bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">所 持 金</FONT></B></DIV>
</TD>
<TD width="61" bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">鍵入手</FONT></B></DIV>
</TD>
<TD width="90" bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">特 殊</FONT></B></DIV>
</TD>
<TD width="96" bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">特 殊</FONT></B></DIV>
</TD>
<TD width="87" bgcolor="#339999">
<DIV align="center"><B><FONT color="#ffffff">特 殊</FONT></B></DIV>
</TD>
</TR>
<TR>
<TD width="70" bgcolor="white" align="center">0回</FONT></TD>
<TD width="67" bgcolor="white" align="center">10</FONT></TD>
<TD width="61" bgcolor="white" align="center">地下1階</FONT></TD>
<TD width="90" bgcolor="white" align="center">覚えてない</FONT></TD>
<TD align="center" width="96" bgcolor="white">覚えてない</FONT></TD>
<TD align="center" width="87" bgcolor="white">覚えてない</FONT></TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<TABLE border="1" bgcolor="#ffff00">
<TBODY>
<TR>
<TD align="center" bgcolor="#000000"><B><FONT color="#ffff00" size="4">UserName</FONT></B></TD>
<TD align="center" bgcolor="#000000"><B><FONT color="#ffff00" size="4">Password</FONT></B></TD>
</TR>
<TR>
<TD align="center" bgcolor="#000000"><B><FONT color="#ffffff" size="4">$FORM{'name'}</FONT></B></TD>
<TD align="center" bgcolor="#000000"><B><FONT color="#ffffff" size="4">$FORM{'password'}</FONT></B></TD>
</TR>
</TBODY>
</TABLE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="hidden" name=name value="$FORM{'name'}">
<INPUT type="hidden" name=password value="$FORM{'pass'}">
<INPUT type="submit" value="  T O P  "><BR><BR>
</FORM>
</TD>
</TR>
</TBODY>
</TABLE>
</CENTER>
EOF

&footer;

}

sub makeNEW {

open(FH,"dat/time2.cgi");
$time2 = <FH>;
close(FH);

chomp $time2;

if($time2 eq ""){&timesyori;}

open(FH,"${datadir}/$countdata");
$sou = <FH>;
close(FH);
$sou++;

&lock;
open(FH, ">${datadir}/$countdata");
print FH $sou;
close(FH);
&unlock;

&get_ip;

$Yname = $FORM{'name'};
$Ypass = $FORM{'password'};
&pass;

$Ybye = (time + ($goodbye * 24 * 60 * 60));
$Yplay = time ;
$Ymes = '未登録';


@monset = (1,21,46,71,91,111,131,156,176);
$monster = $monset[int(rand(9))];
@sexs = (1,2);
$sex = $sexs[int(rand(2))];
$Nsei = 14;

if($monster == 1)     {$Yimg=1;  $Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}
elsif($monster == 21) {$Yimg=21; $Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}
elsif($monster == 46) {$Yimg=46; $Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}
elsif($monster == 71) {$Yimg=71; $Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}
elsif($monster == 91) {$Yimg=91; $Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}
elsif($monster == 111){$Yimg=111;$Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}
elsif($monster == 131){$Yimg=131;$Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}
elsif($monster == 156){$Yimg=156;$Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}
elsif($monster == 176){$Yimg=176;$Yhp=5 ;$Ymhp=5 ;$Ymp=5;$Ymmp=5;$Ykou=5;$Ymam=5;$Ysub=5;}

$Ykey = 1;

&lock;
open(FH,">>${datadir}/$userdata");
print FH "$Yname<>$crypted<>$host<>$Ybye<>$Yplay<>$Yplay<>$Yplay<>$Ykey<>$Yimg<>0<>1<>0<>0<>0<>0<>0<>0<>10<>$Ymes<>0\n";
close(FH);

open(FH,">>dat/id.cgi");
print FH "$Yname<>$crypted\n";
close(FH);

open(FH,">>${datadir}/$Yname.cgi");
print FH "$Yname<>$crypted<>1<>10<>$Yimg<>$Yhp<>$Ymhp<>$Ymp<>$Ymmp<>$Ykou<>$Ymam<>$Ysub<>0<>0<>$nextup<>$sex<>$Nsei<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>$Ykey<>10";
close(FH);

open(FH,">>bbs/$Yname.cgi");
print FH "<><><><><><><><><><><><><><><><><><><>";
close(FH);

open(FH,">>keyset/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0";
close(FH);

open(FH,">>omiai/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0";
close(FH);

open(FH,">>waza/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0";
close(FH);

open(FH,">>zukan/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>";
close(FH);

&unlock;

&set_cookie;

}

#================#
#  フォルダ作成  #
#================#

sub makeDF {

mkdir($datadir, $dirmode);
open(FH,">$datadir/$countdata");
print FH "0";
close(FH);

if($backup == 1){
mkdir($backfolder, $dirmode);
}

}

