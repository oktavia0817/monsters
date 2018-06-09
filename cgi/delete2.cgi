use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};

&open1;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    $passcheck = crypt($inpass, $inname);
    if($passcheck ne $Ypass) {&error("パスワードが違います");}
}
}

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
    $cook = "name\:$inname\,password\:$inpass\,Ikai\:1\,ROOM\:0\,BYE\:8282";
    print "Set-Cookie: MONSTERS=$cook; expires=$date_gmt\n";

open(FH,"${datadir}/$countdata");
$sou = <FH>;
close(FH);
$sou--;

&lock;
open(FH, ">${datadir}/$countdata");
print FH $sou;
close(FH);
&unlock;

open(FH,"${datadir}/$userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Spass,$Sip,$Sbye,$Splay,$Splay2,$Yplay3,$Skey,$Simg1,$Shai1,$Slev1,$Simg2,$Shai2,$Slev2,$Simg3,$Shai3,$Slev3,$Smoney,$Smes,$Sturn) = split(/<>/,$line);
     if($Yname eq $inname) {
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

unlink "${datadir}/$inname.cgi";
unlink "bbs/$inname.cgi";
unlink "waza/$inname.cgi";
unlink "keyset/$inname.cgi";
unlink "omiai/$inname.cgi";
if($backup == 1){
unlink "${backfolder}/$inname.cgi";
}

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="700" height="70" align="center">
<HR>
<FONT size="5pt" color="RED"><B>データは削除されました。ご参加ありがとうございました。</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOP">
</CENTER>
</FORM>
EOF
&footer;
