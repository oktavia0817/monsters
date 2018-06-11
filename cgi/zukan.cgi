use utf8;
use open IO => ":utf8";
use open ":std";

$inname  = $FORM{'name'};
$inpass  = $FORM{'password'};
$type  = $FORM{'type'};

&header;

if($type == 1){
	$kname = "スライム系";
	@no = (1..20);
	$back = "back1.png"
} elsif ($type == 2){
	$kname = "ドラゴン系";
	@no = (21..45);
	$back = "back2.png"
} elsif ($type == 3){
	$kname = "けもの系";
	@no = (46..70);
	$back = "back3.png"
} elsif ($type == 4){
	$kname = "とり系";
	@no = (71..90);
	$back = "back4.png"
} elsif ($type == 5){
	$kname = "しょくぶつ系";
	@no = (91..110);
	$back = "back5.png"
} elsif ($type == 6){
	$kname = "むし系";
	@no = (111..130);
	$back = "back6.png"
} elsif ($type == 7){
	$kname = "あくま系";
	@no = (131..155);
	$back = "back7.png"
} elsif ($type == 8){
	$kname = "ゾンビ系";
	@no = (156..175);
	$back = "back8.png"
} elsif ($type == 9){
	$kname = "ぶっしつ系";
	@no = (176..200);
	$back = "back9.png"
} elsif ($type == 10){
	$kname = "？？？系";
	@no = (201..215);
	$back = "back10.png"
} elsif ($type == 11){
	$kname = "？？？系2";
	@no = (216..248);
	$back = "back11.png"
}


open(FH,"$monsdata");
@lines = <FH>;
close(FH);

 $mleng = @lines;
 $noleng = @no;

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
	for ($i=0;$i<=$noleng;$i++){
	    if($no[$i] == $Mimg){
	    	$mno[$i]   = $no[$i];
		    $mimg[$i]  = $Mimg;
		    $mname[$i] = $Mcname;
		}
	}
}

open(FH,"zukan/$inname.cgi") || &error("Can't open 図鑑");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   @zukan = split(/<>/,$line);
}


 $get = 0;
	for($i=1;$i<=$mleng;$i++){
		if($zukan[$i]==1){
			$get += 1;
		}
	}

  $s = sprintf('%.2f', $get / $mleng * 100);

print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
	<TBODY>
	<TR><TD width="600" height="70" align="center">
	<HR>
	<FONT color="#00FFFF"><FONT size="5pt"><B>$inname の図鑑</FONT><br>入手したモンスターは$get ／$mleng 匹（$s ％）</B><BR>
	</FONT><HR>
	</TD></TR>
	</TBODY>
</TABLE>

<br>
[<a href="./monster.cgi?mode=zukan&name=$inname&type=1"><b>スライム系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=2"><b>ドラゴン系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=3"><b>けもの系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=4"><b>とり系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=5"><b>しょくぶつ系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=6"><b>むし系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=7"><b>あくま系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=8"><b>ゾンビ系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=9"><b>ぶっしつ系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=10"><b>？？？系</b></a>]
[<a href="./monster.cgi?mode=zukan&name=$inname&type=11"><b>？？？系その2</b></a>]
<br><br>
<table cellspacing="0" cellpadding="0" border="0" width="60%">
	<tr>
		<td colspan="5" align="center"><font color="white" size="5"><b>$kname</b></font>
		</td>
	</tr>
	<tr><td><br></td></tr>

EOF
for ($i=0;$i<$noleng;$i++) {
	print <<"EOF";
	<td>
		<table width="200">
			<tr>
				<td align="center" bgcolor="black" width="20%"><font color="white"><b>$mno[$i]</b></font>
				</td>
			</tr>
EOF
	if($zukan[$no[$i]]==1){
		print <<"EOF";
			<tr>
				<td align="center"  background="$imgpath/$back" width="20%" height="150" valign="bottom"><img src="$imgpath/$mimg[$i].gif"><br>
				</td>
			</tr>
EOF
	} else {
		print <<"EOF";
			<tr>
				<td align="center"  bgcolor="#ffffff" width="20%" height="150" valign="bottom">？？？<br>
				</td>
			</tr>
EOF
	}
print <<"EOF";
			<tr>
				<td align="center" bgcolor="black"><font color="white"><b>$mname[$i]</b></font>
				</td>
			</tr>
		</table>
	</td>
EOF
	$x = ($i+1) % 5;
	if($x==0){
		print "</tr>\n";
		print "<tr>\n";
	}
}
print <<"EOF";
</tr>
</table>
EOF

print <<"EOF";
<br><br>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="">
<INPUT type="submit"  value="TOPへ">
</FORM>
EOF

&footer;
