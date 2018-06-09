#!C:/perl64/bin/perl
# ↑サーバーに合わせてください

use utf8;
use open IO => ":utf8";
use open ":std";

require './set.cgi';
require './dat/kokoro.cgi';

&decode;

if($FORM{'mode'} eq "")            {  &OPENK; }
elsif($FORM{'mode'} eq "KANRI")    {  &KANRI; }
elsif($FORM{'mode'} eq "DEL")      {  &DEL; }
elsif($FORM{'mode'} eq "NEW")      {  &NEW; }
elsif($FORM{'mode'} eq "NEWPASS")  {  &NEWPASS; }
elsif($FORM{'mode'} eq "ALLDEL")   {  &ALLDEL; }
elsif($FORM{'mode'} eq "FUKUGEN")  {  &FUKUGEN; }
elsif($FORM{'mode'} eq "RESTART")  {  &RESTART; }
elsif($FORM{'mode'} eq "FUKUMON")  {  &FUKUMON; }
elsif($FORM{'mode'} eq "FUKUOK")   {  &FUKUOK; }

#==============#
#  管理モード  #
#==============#

sub OPENK  {

&header;

print <<"EOF";
<BR>
<BR>
<TABLE width="100%" bgcolor="#ff00ff">
<TBODY>
<TR>
<TD bgcolor="#660066"><B><FONT size="+2" color="#FFFFFF">管理モード</FONT></B></TD>
</TR>
</TBODY>
</TABLE>
<BR>
<FORM ACTION="$kanrim" METHOD="POST">
<BLOCKQUOTE><B><FONT size="4">MASTERNAME</FONT></B><BR>
<INPUT type="text" name="mastername"><BR>
<FONT size="+1"><B>MASTERPASSWORD</B></FONT><BR>
<INPUT type="password" name="masterpassword"><BR>
<BR>
<INPUT type="submit" value="管理モード">
<INPUT type="hidden" name="mode" value="KANRI">
</BLOCKQUOTE>
</FORM>
EOF

&footer;

}

sub KANRI {

$inmastername     = $FORM{'mastername'};
$inmasterpassword = $FORM{'masterpassword'};

if($inmastername eq "") { &error("MASTERNAMEが有りません");}
if($inmasterpassword eq "") { &error("MASTERPASSWORDが有りません");}
if($inmastername ne $mastername) { &error("MASTERNAMEが違います");}
if($inmasterpassword ne $masterpassword) { &error("MASTERPASSWORDが違います");}

open(FH,"${datadir}/$userdata");
@lines = <FH>;
close(FH);

&header;

print <<"EOF";
<P><B><FONT size="6pt">管理モード</FONT></B></P>

<HR>
<P><FONT size="4pt">消滅モンスターの復活</FONT></P>
<FORM ACTION="$kanrim" METHOD="POST">
<FONT size="4pt"> 対象ユーザーを選択して下さい </FONT><BR>
<SELECT name=FUKUNAME>
<option value="no">対象の人を選択
EOF
foreach $line (@lines) {
    ($Sname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
print "<option value=$Sname >$Sname\n";
}
print <<"EOF";
</SELECT>
<INPUT type="submit" value="ユーザー決定">
<INPUT type="hidden" name="mode" value="FUKUMON">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
</FORM>
<HR>
<P><FONT size="4pt">ユーザーデータの復元</FONT></P>
<FORM ACTION="$kanrim" METHOD="POST">
<INPUT type="submit" value="復元する">
<INPUT type="hidden" name="mode" value="FUKUGEN">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
</FORM>
<HR>
<P><FONT size="4pt">再スタート</FONT></P>
<FORM ACTION="$kanrim" METHOD="POST">
<INPUT type="submit" value="RESTART">
<INPUT type="hidden" name="mode" value="RESTART">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
</FORM>
<HR>
<P><FONT size="4pt">データ一括削除・メダル杯の記録もクリアーされます</FONT></P>
<FORM ACTION="$kanrim" METHOD="POST">
<INPUT type="submit" value="全部削除">
<INPUT type="hidden" name="mode" value="ALLDEL">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
</FORM>
<HR>
<FORM ACTION="$kanrim" METHOD="POST">
<FONT size="4pt"> ルール違反者と思われる人の削除を行います </FONT><BR>
<SELECT name=DELNAME>
<option value="no">対象の人を選択
EOF
foreach $line (@lines) {
    ($Sname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
print "<option value=$Sname >$Sname\n";
}
print <<"EOF";
</SELECT>
<BR>
<BR>
<INPUT type="submit" value="管理削除">
<BR>
<INPUT type="hidden" name="mode" value="DEL">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
</FORM>
</TD>
<BR>
<HR>
<FORM ACTION="$kanrim" METHOD="POST">
<FONT size="4pt"> パスワードの変更 </FONT><BR>
<SELECT name=NEWNAME>
<option value="no">対象の人を選択
EOF
foreach $line (@lines) {
    ($Sname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
print "<option value=$Sname >$Sname\n";
}
print <<"EOF";
</SELECT>
<BR>
<BR>
<INPUT type=text name=newpass>NEWパスワード
<BR>
<INPUT type="submit" value="パスワード決定">
<BR>
<INPUT type="hidden" name="mode" value="NEWPASS">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
</FORM>
</TD>
<HR>
<BR>
<FORM ACTION="$kanrim" METHOD="POST">
<FONT size="4pt"> 重複の対象のためエラーが出る人を新規登録します </FONT><BR>
<BR>
<INPUT type=text name=rename >登録ユーザー名
<BR>
<BR>
<INPUT type=password name=repassword>登録パスワード
<BR>
<BR>
<INPUT type="submit" value="管理登録">
<INPUT type="hidden" name="mode" value="NEW">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
</FORM>
</BLOCKQUOTE>
</TD>
EOF

&footer;

}

#==================#
# 管理MODE(全削除) #
#==================#

sub ALLDEL {

$inmastername     = $FORM{'mastername'};
$inmasterpassword = $FORM{'masterpassword'};

open(FH,"${datadir}/$userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
    unlink "${datadir}/$Yname.cgi";
    unlink "bbs/$Yname.cgi";
    unlink "waza/$Yname.cgi";
    unlink "omiai/$Yname.cgi";
    unlink "keyset/$Yname.cgi";
    unlink "dat/id.cgi";

    if($backup == 1){
    unlink "${backfolder}/$Yname.cgi";
    }
    }

    unlink "${datadir}/$userdata";
    unlink "${datadir}/$countdata";

    if($backup == 1){
    unlink "${backfolder}/$userdata";
    unlink "${backfolder}/$countdata";
    }


rmdir $datadir;

if($backup == 1){
rmdir $backfolder;
}

open(FH, ">dat/turnlog.cgi") || &error("Can't open ");
print FH '&header;';
print FH "\n";
print FH 'print <<"EOF";';
print FH "\n";
print FH "<FONT size=4p><B>まだ大会は一度も開かれていません</B></FONT><BR><BR><BR><BR>";
print FH "\n";
print FH 'EOF';
print FH "\n";
print FH '&footer3;';
close(FH);

&header;
print <<"EOF";
<CENTER>
<HR width='80%'>
<FONT size=5pt color=#0033FF><B>全データを削除しました</B></FONT>
<BR><BR><BR>
<FORM ACTION="$kanrim" METHOD="POST">
<INPUT type="hidden" name="mode" value="KANRI">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
<INPUT type="submit"  value="管理モードへ">
</FORM>
<hr width='80%'>
</CENTER>
EOF
&footer;

}

#================#
# 管理MODE(削除) #
#================#

sub DEL {

$inmastername     = $FORM{'mastername'};
$inmasterpassword = $FORM{'masterpassword'};

open(FH,"${datadir}/$countdata");
$sou = <FH>;
close(FH);
$sou--;

&lock;
open(FH, ">${datadir}/$countdata");
print FH $sou;
close(FH);
&unlock;

$krname = $FORM{'DELNAME'};

open(FH,"${datadir}/$userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
     if($Yname eq $krname) {
     $line = "";
&lock;
open(FH, ">${datadir}/$userdata");
print FH @lines;
close(FH);
&unlock;
     }
}

open(FH,"dat/id.cgi");
@IDlines = <FH>;
close(FH);
foreach $IDline (@IDlines) {
    ($IDname,$IDpass) = split(/<>/,$IDline);
    if($IDname eq $krname){
    $IDline="";
    }
    &lock;
    open(FH, ">dat/id.cgi");
    print FH @IDlines;
    close(FH);
    &unlock;
    }

unlink "${datadir}/$krname.cgi";
unlink "bbs/$krname.cgi";
unlink "waza/$krname.cgi";
unlink "keyset/$krname.cgi";
unlink "omiai/$krname.cgi";
if($backup == 1){
unlink "${backfolder}/$krname.cgi";
}

&header;
print <<"EOF";
<CENTER>
<HR width='80%'>
<FONT size=5pt color=#0033FF><B>管理モードで強制削除しました</B></FONT>
<BR><BR><BR>
<FORM ACTION="$kanrim" METHOD="POST">
<INPUT type="hidden" name="mode" value="KANRI">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
<INPUT type="submit"  value="管理モードへ">
</FORM>
</CENTER>
EOF
&footer;

}

#================#
# 管理MODE(登録) #
#================#

sub NEW {

$inmastername     = $FORM{'mastername'};
$inmasterpassword = $FORM{'masterpassword'};

open(FH,"${datadir}/$countdata");
$sou = <FH>;
close(FH);
$sou++;

&lock;
open(FH, ">${datadir}/$countdata");
print FH $sou;
close(FH);
&unlock;

@monset = (1,21,46,71,91,111,131,156,176);
$monster = $monset[int(rand(9))];
@sexs = (1,2);
$sex = $sexs[int(rand(2))];


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
$Yname = $FORM{'rename'};
$Ypass = $FORM{'repassword'};
&pass;

$Yip = '管理者登録';
$Ybye = (time + ($goodbye * 24 * 60 * 60));
$Yplay = time;
$Ymes = '未登録';
$Ysex = $sex;

$Nsei = 14;

open(FH,">>dat/id.cgi");
print FH "$Yname<>$crypted\n";
close(FH);

&lock;
open(FH,">>${datadir}/$userdata");
print FH "$Yname<>$crypted<>$Yip<>$Ybye<>$Yplay<>$Yplay<>$Yplay<>$Ykey<>$Yimg<>0<>1<>0<>0<>0<>0<>0<>0<>10<>$Ymes<>0\n";
close(FH);
&unlock;

&lock;
open(FH,">>${datadir}/$Yname.cgi");
print FH "$Yname<>$crypted<>1<>10<>$Yimg<>$Yhp<>$Ymhp<>$Ymp<>$Ymmp<>$Ykou<>$Ymam<>$Ysub<>0<>0<>$nextup<>$Ysex<>$Nsei<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$nextup<>0<>0<>0<>$Ykey<>10";
close(FH);
&unlock;

&lock;
open(FH,">>bbs/$Yname.cgi");
print FH "<><><><><><><><><><><><><><><><><><><>";
close(FH);
&unlock;

&lock;
open(FH,">>waza/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0";
close(FH);
&unlock;

open(FH,">>omiai/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0";
close(FH);

&lock;
open(FH,">>keyset/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0";
close(FH);
&unlock;

&header;
print <<"EOF";
<CENTER>
<HR width='80%'>
<CENTER>
<FONT size=5pt color=#0033FF><B>管理モードで新規登録しました</B></FONT>
<BR><BR><BR>
<FORM ACTION="$kanrim" METHOD="POST">
<INPUT type="hidden" name="mode" value="KANRI">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
<INPUT type="submit"  value="管理モードへ">
</FORM>
</CENTER>
EOF
&footer;

}

#==============#
# 管理MODE(RE) #
#==============#

sub RESTART {

$inmastername     = $FORM{'mastername'};
$inmasterpassword = $FORM{'masterpassword'};

open(FH,"${datadir}/$userdata");
@Ulines = <FH>;
close(FH);

foreach $Uline (@Ulines) {
    ($Yname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$Uline);
$Ybye = (time + ($goodbye * 24 * 60 * 60));
$Yplay = time;
$Uline = "$Yname<>$Spass<>$Sip<>$Ybye<>$Yplay<>$Yplay<>$Yplay<>1<>1<>0<>1<>0<>0<>0<>0<>0<>0<>10<>$Smes<>$Sturn";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @Ulines;
close(FH);
&unlock;
}

foreach $Uline (@Ulines) {
    ($Yname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$Uline);

open(FH,"${datadir}/$Yname.cgi");
@Klines = <FH>;
close(FH);

foreach $Kline (@Klines) {
   ($Kname,$Kpass,$Klev1,$Kmlev1,$Kimg1,$Khp1,$Kmhp1,$Kmp1,$Kmmp1,$Kkou1,$Kmam1,$Ksub1,$Khai1,$Kcount1,$Knecount1,$Ksex1,$Ksei1,$Klev2,$Kmlev2,$Kimg2,$Khp2,$Kmhp2,$Kmp2,$Kmmp2,$Kkou2,$Kmam2,$Ksub2,$Khai2,$Kcount2,$Knecount2,$Ksex2,$Ksei2,$Klev3,$Kmlev3,$Kimg3,$Khp3,$Kmhp3,$Kmp3,$Kmmp3,$Kkou3,$Kmam3,$Ksub3,$Khai3,$Kcount3,$Knecount3,$Ksex3,$Ksei3,$Klev4,$Kmlev4,$Kimg4,$Khp4,$Kmhp4,$Kmp4,$Kmmp4,$Kkou4,$Kmam4,$Ksub4,$Khai4,$Kcount4,$Knecount4,$Ksex4,$Ksei4,$Klev5,$Kmlev5,$Kimg5,$Khp5,$Kmhp5,$Kmp5,$Kmmp5,$Kkou5,$Kmam5,$Ksub5,$Khai5,$Kcount5,$Knecount5,$Ksex5,$Ksei5,$Klev6,$Kmlev6,$Kimg6,$Khp6,$Kmhp6,$Kmp6,$Kmmp6,$Kkou6,$Kmam6,$Ksub6,$Khai6,$Kcount6,$Knecount6,$Ksex6,$Ksei6,$Klev7,$Kmlev7,$Kimg7,$Khp7,$Kmhp7,$Kmp7,$Kmmp7,$Kkou7,$Kmam7,$Ksub7,$Khai7,$Kcount7,$Knecount7,$Ksex7,$Ksei7,$Klev8,$Kmlev8,$Kimg8,$Khp8,$Kmhp8,$Kmp8,$Kmmp8,$Kkou8,$Kmam8,$Ksub8,$Khai8,$Kcount8,$Knecount8,$Ksex8,$Ksei8,$Klev9,$Kmlev9,$Kimg9,$Khp9,$Kmhp9,$Kmp9,$Kmmp9,$Kkou9,$Kmam9,$Ksub9,$Khai9,$Kcount9,$Knecount9,$Ksex9,$Ksei9,$Klev10,$Kmlev10,$Kimg10,$Khp10,$Kmhp10,$Kmp10,$Kmmp10,$Kkou10,$Kmam10,$Ksub10,$Khai10,$Kcount10,$Knecount10,$Ksex10,$Ksei10,$Kdummy,$Kkey,$Kmoney) = split(/<>/,$Kline);

$Kline = "$Kname<>$Kpass<>1<>10<>1<>1<>2<>1<>3<>3<>3<>3<>0<>0<>10<>1<>14<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>1<>10";}

&lock;
open(FH, ">${datadir}/$Yname.cgi") || &error("Can't open!");
print FH @Klines;
close(FH);
&unlock;
}

foreach $Uline (@Ulines) {
    ($Yname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$Uline);

&lock;
open(FH,">keyset/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0";
close(FH);
&unlock;

}

foreach $Uline (@Ulines) {
    ($Yname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$Uline);

&lock;
open(FH,">waza/$Yname.cgi");
print FH "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0";
close(FH);
&unlock;

}

&header;
print <<"EOF";
<CENTER>
<HR width='80%'>
<FONT size=5pt color=#0033FF><B>RESTARTの準備が完了しました</B></FONT>
<BR><BR><BR>
<FORM ACTION="$kanrim" METHOD="POST">
<INPUT type="hidden" name="mode" value="KANRI">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
<INPUT type="submit"  value="管理モードへ">
</FORM>
</CENTER>
EOF
&footer;

}

#================#
# 管理MODE(変更) #
#================#

sub NEWPASS {

$inmastername     = $FORM{'mastername'};
$inmasterpassword = $FORM{'masterpassword'};

$NEWname = $FORM{'NEWNAME'};
$NEWpass = $FORM{'newpass'};
$Yname = $NEWname;
$Ypass = $NEWpass;
&pass;

open(FH,"${datadir}/$userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
     if($Yname eq $NEWname) {
     $line = "$Yname<>$crypted<>$Sip<>$Sbye<>$Splay<>$Splay2<>$Yplay3<>$Skey<>$Simg1<>$Shai1<>$Slev1<>$Simg2<>$Shai2<>$Slev2<>$Simg3<>$Shai3<>$Slev3<>$Smoney<>$Smes<>$Sturn";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
}
}

open(FH,"${datadir}/$NEWname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Kname,$Kpass,$Klev1,$Kmlev1,$Kimg1,$Khp1,$Kmhp1,$Kmp1,$Kmmp1,$Kkou1,$Kmam1,$Ksub1,$Khai1,$Kcount1,$Knecount1,$Ksex1,$Ksei1,$Klev2,$Kmlev2,$Kimg2,$Khp2,$Kmhp2,$Kmp2,$Kmmp2,$Kkou2,$Kmam2,$Ksub2,$Khai2,$Kcount2,$Knecount2,$Ksex2,$Ksei2,$Klev3,$Kmlev3,$Kimg3,$Khp3,$Kmhp3,$Kmp3,$Kmmp3,$Kkou3,$Kmam3,$Ksub3,$Khai3,$Kcount3,$Knecount3,$Ksex3,$Ksei3,$Klev4,$Kmlev4,$Kimg4,$Khp4,$Kmhp4,$Kmp4,$Kmmp4,$Kkou4,$Kmam4,$Ksub4,$Khai4,$Kcount4,$Knecount4,$Ksex4,$Ksei4,$Klev5,$Kmlev5,$Kimg5,$Khp5,$Kmhp5,$Kmp5,$Kmmp5,$Kkou5,$Kmam5,$Ksub5,$Khai5,$Kcount5,$Knecount5,$Ksex5,$Ksei5,$Klev6,$Kmlev6,$Kimg6,$Khp6,$Kmhp6,$Kmp6,$Kmmp6,$Kkou6,$Kmam6,$Ksub6,$Khai6,$Kcount6,$Knecount6,$Ksex6,$Ksei6,$Klev7,$Kmlev7,$Kimg7,$Khp7,$Kmhp7,$Kmp7,$Kmmp7,$Kkou7,$Kmam7,$Ksub7,$Khai7,$Kcount7,$Knecount7,$Ksex7,$Ksei7,$Klev8,$Kmlev8,$Kimg8,$Khp8,$Kmhp8,$Kmp8,$Kmmp8,$Kkou8,$Kmam8,$Ksub8,$Khai8,$Kcount8,$Knecount8,$Ksex8,$Ksei8,$Klev9,$Kmlev9,$Kimg9,$Khp9,$Kmhp9,$Kmp9,$Kmmp9,$Kkou9,$Kmam9,$Ksub9,$Khai9,$Kcount9,$Knecount9,$Ksex9,$Ksei9,$Klev10,$Kmlev10,$Kimg10,$Khp10,$Kmhp10,$Kmp10,$Kmmp10,$Kkou10,$Kmam10,$Ksub10,$Khai10,$Kcount10,$Knecount10,$Ksex10,$Ksei10,$Kdummy,$Kkey,$Kmoney) = split(/<>/,$line);

    $line = "$Kname<>$crypted<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Klev2<>$Kmlev2<>$Kimg2<>$Khp2<>$Kmhp2<>$Kmp2<>$Kmmp2<>$Kkou2<>$Kmam2<>$Ksub2<>$Khai2<>$Kcount2<>$Knecount2<>$Ksex2<>$Ksei2<>$Klev3<>$Kmlev3<>$Kimg3<>$Khp3<>$Kmhp3<>$Kmp3<>$Kmmp3<>$Kkou3<>$Kmam3<>$Ksub3<>$Khai3<>$Kcount3<>$Knecount3<>$Ksex3<>$Ksei3<>$Klev4<>$Kmlev4<>$Kimg4<>$Khp4<>$Kmhp4<>$Kmp4<>$Kmmp4<>$Kkou4<>$Kmam4<>$Ksub4<>$Khai4<>$Kcount4<>$Knecount4<>$Ksex4<>$Ksei4<>$Klev5<>$Kmlev5<>$Kimg5<>$Khp5<>$Kmhp5<>$Kmp5<>$Kmmp5<>$Kkou5<>$Kmam5<>$Ksub5<>$Khai5<>$Kcount5<>$Knecount5<>$Ksex5<>$Ksei5<>$Klev6<>$Kmlev6<>$Kimg6<>$Khp6<>$Kmhp6<>$Kmp6<>$Kmmp6<>$Kkou6<>$Kmam6<>$Ksub6<>$Khai6<>$Kcount6<>$Knecount6<>$Ksex6<>$Ksei6<>$Klev7<>$Kmlev7<>$Kimg7<>$Khp7<>$Kmhp7<>$Kmp7<>$Kmmp7<>$Kkou7<>$Kmam7<>$Ksub7<>$Khai7<>$Kcount7<>$Knecount7<>$Ksex7<>$Ksei7<>$Klev8<>$Kmlev8<>$Kimg8<>$Khp8<>$Kmhp8<>$Kmp8<>$Kmmp8<>$Kkou8<>$Kmam8<>$Ksub8<>$Khai8<>$Kcount8<>$Knecount8<>$Ksex8<>$Ksei8<>$Klev9<>$Kmlev9<>$Kimg9<>$Khp9<>$Kmhp9<>$Kmp9<>$Kmmp9<>$Kkou9<>$Kmam9<>$Ksub9<>$Khai9<>$Kcount9<>$Knecount9<>$Ksex9<>$Ksei9<>$Klev10<>$Kmlev10<>$Kimg10<>$Khp10<>$Kmhp10<>$Kmp10<>$Kmmp10<>$Kkou10<>$Kmam10<>$Ksub10<>$Khai10<>$Kcount10<>$Knecount10<>$Ksex10<>$Ksei10<>$Kdummy<>$Kkey<>$Kmoney";}

&lock;
open(FH, ">${datadir}/$NEWname.cgi") || &error("Can't open!");
print FH @lines;
close(FH);
&unlock;

&header;
print <<"EOF";
<CENTER>
<HR width='80%'>
<FONT size=5pt color=#0033FF><B>管理モードでパスワードを変更しました</B></FONT>
<BR><BR><BR>
<FORM ACTION="$kanrim" METHOD="POST">
<INPUT type="hidden" name="mode" value="KANRI">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
<INPUT type="submit"  value="管理モードへ">
</FORM>
</CENTER>
EOF
&footer;

}

#====================#
# ユーザーデータ復元 #
#====================#

sub FUKUGEN {

open(FH,"dat/id.cgi");
@IDlines = <FH>;
close(FH);

foreach $IDline (@IDlines) {
   ($IDname,$IDpass) = split(/<>/,$IDline);

open(FH,"${datadir}/$IDname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Kname,$Kpass,$Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Klev[3],$Kmlev[3],$Kimg[3],$Khp[3],$Kmhp[3],$Kmp[3],$Kmmp[3],$Kkou[3],$Kmam[3],$Ksub[3],$Khai[3],$Kcount[3],$Knecount[3],$Ksex[3],$Ksei[3],$Klev[4],$Kmlev[4],$Kimg[4],$Khp[4],$Kmhp[4],$Kmp[4],$Kmmp[4],$Kkou[4],$Kmam[4],$Ksub[4],$Khai[4],$Kcount[4],$Knecount[4],$Ksex[4],$Ksei[4],$Klev[5],$Kmlev[5],$Kimg[5],$Khp[5],$Kmhp[5],$Kmp[5],$Kmmp[5],$Kkou[5],$Kmam[5],$Ksub[5],$Khai[5],$Kcount[5],$Knecount[5],$Ksex[5],$Ksei[5],$Klev[6],$Kmlev[6],$Kimg[6],$Khp[6],$Kmhp[6],$Kmp[6],$Kmmp[6],$Kkou[6],$Kmam[6],$Ksub[6],$Khai[6],$Kcount[6],$Knecount[6],$Ksex[6],$Ksei[6],$Klev[7],$Kmlev[7],$Kimg[7],$Khp[7],$Kmhp[7],$Kmp[7],$Kmmp[7],$Kkou[7],$Kmam[7],$Ksub[7],$Khai[7],$Kcount[7],$Knecount[7],$Ksex[7],$Ksei[7],$Klev[8],$Kmlev[8],$Kimg[8],$Khp[8],$Kmhp[8],$Kmp[8],$Kmmp[8],$Kkou[8],$Kmam[8],$Ksub[8],$Khai[8],$Kcount[8],$Knecount[8],$Ksex[8],$Ksei[8],$Klev[9],$Kmlev[9],$Kimg[9],$Khp[9],$Kmhp[9],$Kmp[9],$Kmmp[9],$Kkou[9],$Kmam[9],$Ksub[9],$Khai[9],$Kcount[9],$Knecount[9],$Ksex[9],$Ksei[9],$Klev[10],$Kmlev[10],$Kimg[10],$Khp[10],$Kmhp[10],$Kmp[10],$Kmmp[10],$Kkou[10],$Kmam[10],$Ksub[10],$Khai[10],$Kcount[10],$Knecount[10],$Ksex[10],$Ksei[10],$Kdummy,$Kkey,$Kmoney) = split(/<>/,$line);

$now = time;
$bye = time + ($goodbye * 60 * 60 *24);

$Nline = "$Kname<>$Kpass<>255.255.255.0<>$bye<>$now<>$now<>0<>$Kkey<>$Kimg[1]<>$Khai[1]<>$Klev[1]<>$Kimg[2]<>$Khai[2]<>$Klev[2]<>$Kimg[3]<>$Khai[3]<>$Klev[3]<>$Kmoney<>未登録<>0\n";

push @NNline,$Nline;
}
}

&lock;
open(FH, ">>${datadir}/$userdata") ;
print FH @NNline;
close(FH);
&unlock;

&header;
print <<"EOF";
<CENTER>
<FONT size=5pt color=#0033FF><B>ユーザーデータは復元しました</B></FONT>
<BR><BR><BR>
EOF
&footer;

}

#====================#
# 消滅モンスター復活 #
#====================#

sub FUKUMON {

$inmastername     = $FORM{'mastername'};
$inmasterpassword = $FORM{'masterpassword'};
$FUKUNAME = $FORM{'FUKUNAME'};

&header;

print <<"EOF";
<P><B><FONT size="6pt">消滅モンスターの復活</FONT></B></P>

<HR>
<P><FONT size="4pt">対象ユーザーは $FUKUNAME さんです</FONT></P>
<FORM ACTION="$kanrim" METHOD="POST">
<FONT size="4pt"> 復活するモンスター決定 </FONT><BR>
<SELECT name=MONNAME>
<option value="no">選択してください
EOF
for($i=1;$i<216;$i++){
print "<option value=$i >$itemlist[$i]\n";
}
print <<"EOF";
</SELECT>
<BR>
<BR>
<FONT size="4pt"> 復活するモンスター性別決定 </FONT><BR>
<SELECT name=SEX>
<option value="no">選択してください
EOF
print "<option value=1 >♂\n";
print "<option value=2 >♀\n";
print <<"EOF";
</SELECT>
<BR>
<BR>
<FONT size="4pt"> 復活するモンスターMAXレベル決定 </FONT><BR>
<INPUT type="txt" name="MAXLEVEL" >
<BR>
<BR>
<FONT size="4pt"> 復活するモンスター現在レベル決定 </FONT><BR>
<INPUT type="txt" name="LEVEL" >
<BR>
<BR>
<FONT size="4pt"> 復活するモンスター配合回数 </FONT><BR>
<INPUT type="txt" name="HAIGOU" >
<BR>
<BR>
<INPUT type="submit" value="復活処理開始">
<INPUT type="hidden" name="mode" value="FUKUOK">
<INPUT type="hidden" name="FUKUNAME" value="$FUKUNAME">
<INPUT type="hidden" name="mastername" value="$inmastername">
<INPUT type="hidden" name="masterpassword" value="$inmasterpassword">
</FORM>
</BLOCKQUOTE>
</TD>
EOF

&footer;

}

#====================#
# 消滅モンス復元処理 #
#====================#

sub FUKUOK {

$inmastername     = $FORM{'mastername'};
$inmasterpassword = $FORM{'masterpassword'};
$FUKUNAME         = $FORM{'FUKUNAME'};
$MONNAME          = $FORM{'MONNAME'};
$SEX              = $FORM{'SEX'};
$LEVEL            = $FORM{'LEVEL'};
$MAXLEVEL         = $FORM{'MAXLEVEL'};
$HAIGOU           = $FORM{'HAIGOU'};

if($MONNAME eq "no") { &error("モンスターを選択してください");}
if($SEX eq "no")     { &error("性別を選択してください");}
if($MAXLEVEL eq '')  { &error("MAXレベルを入力してください");}
if($LEVEL eq '')     { &error("現在レベルを入力してください");}
if($HAIGOU eq '')    { &error("配合回数を入力してください");}
if($MAXLEVEL <= $LEVEL) { &error("最大レベルと同じまたは超さない数字を入力してください");}

open(FH,"$monsdata") || &error("Can't open $monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
    if($Mimg == $MONNAME){
    $Nimg = $Mimg;
    $Nkou = int(($Mkou + $HAIGOU) * $LEVEL);
    $Nmam = int(($Mmam + $HAIGOU) * $LEVEL);
    $Nsub = int(($Msub + $HAIGOU) * $LEVEL);
    $Nhp = int(($Mhp + $HAIGOU) * $LEVEL);
    $Nmp = int(($Mmp + $HAIGOU) * $LEVEL);
}
}

open(FH,"${datadir}/$FUKUNAME.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Kname,$Kpass,$Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Klev[3],$Kmlev[3],$Kimg[3],$Khp[3],$Kmhp[3],$Kmp[3],$Kmmp[3],$Kkou[3],$Kmam[3],$Ksub[3],$Khai[3],$Kcount[3],$Knecount[3],$Ksex[3],$Ksei[3],$Klev[4],$Kmlev[4],$Kimg[4],$Khp[4],$Kmhp[4],$Kmp[4],$Kmmp[4],$Kkou[4],$Kmam[4],$Ksub[4],$Khai[4],$Kcount[4],$Knecount[4],$Ksex[4],$Ksei[4],$Klev[5],$Kmlev[5],$Kimg[5],$Khp[5],$Kmhp[5],$Kmp[5],$Kmmp[5],$Kkou[5],$Kmam[5],$Ksub[5],$Khai[5],$Kcount[5],$Knecount[5],$Ksex[5],$Ksei[5],$Klev[6],$Kmlev[6],$Kimg[6],$Khp[6],$Kmhp[6],$Kmp[6],$Kmmp[6],$Kkou[6],$Kmam[6],$Ksub[6],$Khai[6],$Kcount[6],$Knecount[6],$Ksex[6],$Ksei[6],$Klev[7],$Kmlev[7],$Kimg[7],$Khp[7],$Kmhp[7],$Kmp[7],$Kmmp[7],$Kkou[7],$Kmam[7],$Ksub[7],$Khai[7],$Kcount[7],$Knecount[7],$Ksex[7],$Ksei[7],$Klev[8],$Kmlev[8],$Kimg[8],$Khp[8],$Kmhp[8],$Kmp[8],$Kmmp[8],$Kkou[8],$Kmam[8],$Ksub[8],$Khai[8],$Kcount[8],$Knecount[8],$Ksex[8],$Ksei[8],$Klev[9],$Kmlev[9],$Kimg[9],$Khp[9],$Kmhp[9],$Kmp[9],$Kmmp[9],$Kkou[9],$Kmam[9],$Ksub[9],$Khai[9],$Kcount[9],$Knecount[9],$Ksex[9],$Ksei[9],$Klev[10],$Kmlev[10],$Kimg[10],$Khp[10],$Kmhp[10],$Kmp[10],$Kmmp[10],$Kkou[10],$Kmam[10],$Ksub[10],$Khai[10],$Kcount[10],$Knecount[10],$Ksex[10],$Ksei[10],$Kdummy,$Kkey,$Kmoney) = split(/<>/,$line);
}

if($Kimg[2] == 0){ $pt = 2;}
if($Kimg[2] != 0 && $Kimg[3] == 0){ $pt = 3;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] == 0){ $pt = 4;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] == 0){ $pt = 5;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] == 0){ $pt = 6;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] == 0){ $pt = 7;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] != 0 && $Kimg[8] == 0){ $pt = 8;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] != 0 && $Kimg[8] != 0 && $Kimg[9] == 0){ $pt = 9;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] != 0 && $Kimg[8] != 0 && $Kimg[9] != 0 && $Kimg[10] == 0){ $pt = 10;}
if($Kimg[2] != 0 && $Kimg[3] != 0 && $Kimg[4] != 0 && $Kimg[5] != 0 && $Kimg[6] != 0 && $Kimg[7] != 0 && $Kimg[8] != 0 && $Kimg[9] != 0 && $Kimg[10] != 0){ &error("モンスターが10体いる\場合はこの機能\は使用出来ません");}

$Klev[$pt] = $LEVEL;
$Kmlev[$pt] = $MAXLEVEL;
$Kimg[$pt] = $Nimg;
$Khp[$pt] = $Nhp;
$Kmhp[$pt] = $Nhp;
$Kmp[$pt] = $Nmp;
$Kmmp[$pt] = $Nmp;
$Kkou[$pt] = $Nkou;
$Kmam[$pt] = $Nmam;
$Ksub[$pt] = $Nsub;
$Khai[$pt] = $HAIGOU;
$Kcount[$pt] = 1;
for($E = 1;$E < $LEVEL;$E++){
if($kai eq ""){$kai = 10;}
$kai = int($kai*1.15);
}
if($kai >=99999){$kai = 99999;}
$Knecount[$pt] = $kai;
$Ksex[$pt] = $SEX;
$Ksei[$pt] = 14;

$newline = "$Kname<>$Kpass<>$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>$Klev[3]<>$Kmlev[3]<>$Kimg[3]<>$Khp[3]<>$Kmhp[3]<>$Kmp[3]<>$Kmmp[3]<>$Kkou[3]<>$Kmam[3]<>$Ksub[3]<>$Khai[3]<>$Kcount[3]<>$Knecount[3]<>$Ksex[3]<>$Ksei[3]<>$Klev[4]<>$Kmlev[4]<>$Kimg[4]<>$Khp[4]<>$Kmhp[4]<>$Kmp[4]<>$Kmmp[4]<>$Kkou[4]<>$Kmam[4]<>$Ksub[4]<>$Khai[4]<>$Kcount[4]<>$Knecount[4]<>$Ksex[4]<>$Ksei[4]<>$Klev[5]<>$Kmlev[5]<>$Kimg[5]<>$Khp[5]<>$Kmhp[5]<>$Kmp[5]<>$Kmmp[5]<>$Kkou[5]<>$Kmam[5]<>$Ksub[5]<>$Khai[5]<>$Kcount[5]<>$Knecount[5]<>$Ksex[5]<>$Ksei[5]<>$Klev[6]<>$Kmlev[6]<>$Kimg[6]<>$Khp[6]<>$Kmhp[6]<>$Kmp[6]<>$Kmmp[6]<>$Kkou[6]<>$Kmam[6]<>$Ksub[6]<>$Khai[6]<>$Kcount[6]<>$Knecount[6]<>$Ksex[6]<>$Ksei[6]<>$Klev[7]<>$Kmlev[7]<>$Kimg[7]<>$Khp[7]<>$Kmhp[7]<>$Kmp[7]<>$Kmmp[7]<>$Kkou[7]<>$Kmam[7]<>$Ksub[7]<>$Khai[7]<>$Kcount[7]<>$Knecount[7]<>$Ksex[7]<>$Ksei[7]<>$Klev[8]<>$Kmlev[8]<>$Kimg[8]<>$Khp[8]<>$Kmhp[8]<>$Kmp[8]<>$Kmmp[8]<>$Kkou[8]<>$Kmam[8]<>$Ksub[8]<>$Khai[8]<>$Kcount[8]<>$Knecount[8]<>$Ksex[8]<>$Ksei[8]<>$Klev[9]<>$Kmlev[9]<>$Kimg[9]<>$Khp[9]<>$Kmhp[9]<>$Kmp[9]<>$Kmmp[9]<>$Kkou[9]<>$Kmam[9]<>$Ksub[9]<>$Khai[9]<>$Kcount[9]<>$Knecount[9]<>$Ksex[9]<>$Ksei[9]<>$Klev[10]<>$Kmlev[10]<>$Kimg[10]<>$Khp[10]<>$Kmhp[10]<>$Kmp[10]<>$Kmmp[10]<>$Kkou[10]<>$Kmam[10]<>$Ksub[10]<>$Khai[10]<>$Kcount[10]<>$Knecount[10]<>$Ksex[10]<>$Ksei[10]<>$Kdummy<>$Kkey<>$Kmoney";

&lock;
open(FH, ">${datadir}/$FUKUNAME.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
&unlock;

&header;
print <<"EOF";
<CENTER>
<FONT size=5pt color=#0033FF><B>モンスター復活完了しました</B></FONT>
<BR><BR><BR>
EOF
&footer;

}

