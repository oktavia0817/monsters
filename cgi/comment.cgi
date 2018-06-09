use utf8;
use open IO => ":utf8";
use open ":std";
use Encode;

$inname=$FORM{'name'};
$inpass=$FORM{'password'};
$inmes=$FORM{'message'};

$inmes = decode( "utf8", $inmes );

if (length($FORM{'message'}) < 4 or length($FORM{'message'}) > 101)
{ &error("2文字以上、50文字以下で入力して下さい。");}

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    $passcheck = crypt($inpass, $inname);
    if($passcheck ne $Ypass) {&error("パスワードが違います");}
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>$Yplay3<>$Ykey<>$Yimg1<>$Yhai1<>$Ylev1<>$Yimg2<>$Yhai2<>$Ylev2<>$Yimg3<>$Yhai3<>$Ylev3<>$Ymoney<>$inmes<>$turn";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
last;
}
}

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>メッセージは更新されました</B></FONT><BR>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="login">
<INPUT type="hidden" name="name" value="$Yname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="LOGINへ">
</FORM>
<BR><BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOP">
</CENTER>
</FORM>
EOF
&footer;
