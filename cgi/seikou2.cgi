use utf8;
use open IO => ":utf8";
use open ":std";

$inname = $FORM{'name'};
$inpass = $FORM{'password'};
$money  = $FORM{'MONEY2'};

open(FH,"dat/time3.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($login,$name,$otime) = split(/<>/,$line);
}

if($name ne $inname){&error("お見合い所入室タイムオーバーです");}

open(FH,"omiai/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);
}

if($Nimg[2] == 0){&error("移動させるモンスターはいません");}

open(FH,"${datadir}/$inname.cgi") || &error("Can't open open3");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Kname,$Kpass,$Klev1,$Kmlev1,$Kimg1,$Khp1,$Kmhp1,$Kmp1,$Kmmp1,$Kkou1,$Kmam1,$Ksub1,$Khai1,$Kcount1,$Knecount1,$Ksex1,$Ksei1,$Klev2,$Kmlev2,$Kimg2,$Khp2,$Kmhp2,$Kmp2,$Kmmp2,$Kkou2,$Kmam2,$Ksub2,$Khai2,$Kcount2,$Knecount2,$Ksex2,$Ksei2,$Klev3,$Kmlev3,$Kimg3,$Khp3,$Kmhp3,$Kmp3,$Kmmp3,$Kkou3,$Kmam3,$Ksub3,$Khai3,$Kcount3,$Knecount3,$Ksex3,$Ksei3,$Klev4,$Kmlev4,$Kimg4,$Khp4,$Kmhp4,$Kmp4,$Kmmp4,$Kkou4,$Kmam4,$Ksub4,$Khai4,$Kcount4,$Knecount4,$Ksex4,$Ksei4,$Klev5,$Kmlev5,$Kimg5,$Khp5,$Kmhp5,$Kmp5,$Kmmp5,$Kkou5,$Kmam5,$Ksub5,$Khai5,$Kcount5,$Knecount5,$Ksex5,$Ksei5,$Klev6,$Kmlev6,$Kimg6,$Khp6,$Kmhp6,$Kmp6,$Kmmp6,$Kkou6,$Kmam6,$Ksub6,$Khai6,$Kcount6,$Knecount6,$Ksex6,$Ksei6,$Klev7,$Kmlev7,$Kimg7,$Khp7,$Kmhp7,$Kmp7,$Kmmp7,$Kkou7,$Kmam7,$Ksub7,$Khai7,$Kcount7,$Knecount7,$Ksex7,$Ksei7,$Klev8,$Kmlev8,$Kimg8,$Khp8,$Kmhp8,$Kmp8,$Kmmp8,$Kkou8,$Kmam8,$Ksub8,$Khai8,$Kcount8,$Knecount8,$Ksex8,$Ksei8,$Klev9,$Kmlev9,$Kimg9,$Khp9,$Kmhp9,$Kmp9,$Kmmp9,$Kkou9,$Kmam9,$Ksub9,$Khai9,$Kcount9,$Knecount9,$Ksex9,$Ksei9,$Klev10,$Kmlev10,$Kimg10,$Khp10,$Kmhp10,$Kmp10,$Kmmp10,$Kkou10,$Kmam10,$Ksub10,$Khai10,$Kcount10,$Knecount10,$Ksex10,$Ksei10,$Kdummy,$Kkey,$Kmoney) = split(/<>/,$line);}
if($Kmoney < $money){&error("お金が足りません");}
if($Kimg1 != 0 && $Kimg2 != 0 && $Kimg3 != 0 && $Kimg4 != 0 && $Kimg5 != 0 && $Kimg6 != 0 && $Kimg7 != 0 && $Kimg8 != 0 && $Kimg9 != 0 && $Kimg10 != 0){&error("LOGIN画面のモンスターが一杯で戻せません");}

$Nlev2=$Klev2;
$Nmlev2=$Kmlev2;
$Nimg2=$Kimg2;
$Nhp2=$Khp2;
$Nmhp2=$Kmhp2;
$Nmp2=$Kmp2;
$Nmmp2=$Kmmp2;
$Nkou2=$Kkou2;
$Nmam2=$Kmam2;
$Nsub2=$Ksub2;
$Nhai2=$Khai2;
$Ncount2=$Kcount2;
$Nnecount2=$Knecount2;
$Nsex2=$Ksex2;
$Nsei2=$Ksei2;

$Nlev3=$Klev3;
$Nmlev3=$Kmlev3;
$Nimg3=$Kimg3;
$Nhp3=$Khp3;
$Nmhp3=$Kmhp3;
$Nmp3=$Kmp3;
$Nmmp3=$Kmmp3;
$Nkou3=$Kkou3;
$Nmam3=$Kmam3;
$Nsub3=$Ksub3;
$Nhai3=$Khai3;
$Ncount3=$Kcount3;
$Nnecount3=$Knecount3;
$Nsex3=$Ksex3;
$Nsei3=$Ksei3;

$Nlev4=$Klev4;
$Nmlev4=$Kmlev4;
$Nimg4=$Kimg4;
$Nhp4=$Khp4;
$Nmhp4=$Kmhp4;
$Nmp4=$Kmp4;
$Nmmp4=$Kmmp4;
$Nkou4=$Kkou4;
$Nmam4=$Kmam4;
$Nsub4=$Ksub4;
$Nhai4=$Khai4;
$Ncount4=$Kcount4;
$Nnecount4=$Knecount4;
$Nsex4=$Ksex4;
$Nsei4=$Ksei4;

$Nlev5=$Klev5;
$Nmlev5=$Kmlev5;
$Nimg5=$Kimg5;
$Nhp5=$Khp5;
$Nmhp5=$Kmhp5;
$Nmp5=$Kmp5;
$Nmmp5=$Kmmp5;
$Nkou5=$Kkou5;
$Nmam5=$Kmam5;
$Nsub5=$Ksub5;
$Nhai5=$Khai5;
$Ncount5=$Kcount5;
$Nnecount5=$Knecount5;
$Nsex5=$Ksex5;
$Nsei5=$Ksei5;

$Nlev6=$Klev6;
$Nmlev6=$Kmlev6;
$Nimg6=$Kimg6;
$Nhp6=$Khp6;
$Nmhp6=$Kmhp6;
$Nmp6=$Kmp6;
$Nmmp6=$Kmmp6;
$Nkou6=$Kkou6;
$Nmam6=$Kmam6;
$Nsub6=$Ksub6;
$Nhai6=$Khai6;
$Ncount6=$Kcount6;
$Nnecount6=$Knecount6;
$Nsex6=$Ksex6;
$Nsei6=$Ksei6;

$Nlev7=$Klev7;
$Nmlev7=$Kmlev7;
$Nimg7=$Kimg7;
$Nhp7=$Khp7;
$Nmhp7=$Kmhp7;
$Nmp7=$Kmp7;
$Nmmp7=$Kmmp7;
$Nkou7=$Kkou7;
$Nmam7=$Kmam7;
$Nsub7=$Ksub7;
$Nhai7=$Khai7;
$Ncount7=$Kcount7;
$Nnecount7=$Knecount7;
$Nsex7=$Ksex7;
$Nsei7=$Ksei7;

$Nlev8=$Klev8;
$Nmlev8=$Kmlev8;
$Nimg8=$Kimg8;
$Nhp8=$Khp8;
$Nmhp8=$Kmhp8;
$Nmp8=$Kmp8;
$Nmmp8=$Kmmp8;
$Nkou8=$Kkou8;
$Nmam8=$Kmam8;
$Nsub8=$Ksub8;
$Nhai8=$Khai8;
$Ncount8=$Kcount8;
$Nnecount8=$Knecount8;
$Nsex8=$Ksex8;
$Nsei8=$Ksei8;

$Nlev9=$Klev9;
$Nmlev9=$Kmlev9;
$Nimg9=$Kimg9;
$Nhp9=$Khp9;
$Nmhp9=$Kmhp9;
$Nmp9=$Kmp9;
$Nmmp9=$Kmmp9;
$Nkou9=$Kkou9;
$Nmam9=$Kmam9;
$Nsub9=$Ksub9;
$Nhai9=$Khai9;
$Ncount9=$Kcount9;
$Nnecount9=$Knecount9;
$Nsex9=$Ksex9;
$Nsei9=$Ksei9;

$Nlev10=$Klev10;
$Nmlev10=$Kmlev10;
$Nimg10=$Kimg10;
$Nhp10=$Khp10;
$Nmhp10=$Kmhp10;
$Nmp10=$Kmp10;
$Nmmp10=$Kmmp10;
$Nkou10=$Kkou10;
$Nmam10=$Kmam10;
$Nsub10=$Ksub10;
$Nhai10=$Khai10;
$Ncount10=$Kcount10;
$Nnecount10=$Knecount10;
$Nsex10=$Ksex10;
$Nsei10=$Ksei10;

if($Kimg2 == 0){
$Nlev2=$Nlev[2];
$Nmlev2=$Nmlev[2];
$Nimg2=$Nimg[2];
$Nhp2=$Nhp[2];
$Nmhp2=$Nmhp[2];
$Nmp2=$Nmp[2];
$Nmmp2=$Nmmp[2];
$Nkou2=$Nkou[2];
$Nmam2=$Nmam[2];
$Nsub2=$Nsub[2];
$Nhai2=$Nhai[2];
$Ncount2=$Ncount[2];
$Nnecount2=$Nnecount[2];
$Nsex2=$Nsex[2];
$Nsei2=$Nsei[2];
}
if($Kimg2 != 0 && $Kimg3 == 0){
$Nlev3=$Nlev[2];
$Nmlev3=$Nmlev[2];
$Nimg3=$Nimg[2];
$Nhp3=$Nhp[2];
$Nmhp3=$Nmhp[2];
$Nmp3=$Nmp[2];
$Nmmp3=$Nmmp[2];
$Nkou3=$Nkou[2];
$Nmam3=$Nmam[2];
$Nsub3=$Nsub[2];
$Nhai3=$Nhai[2];
$Ncount3=$Ncount[2];
$Nnecount3=$Nnecount[2];
$Nsex3=$Nsex[2];
$Nsei3=$Nsei[2];
}
if($Kimg2 != 0 && $Kimg3 != 0 && $Kimg4 == 0){
$Nlev4=$Nlev[2];
$Nmlev4=$Nmlev[2];
$Nimg4=$Nimg[2];
$Nhp4=$Nhp[2];
$Nmhp4=$Nmhp[2];
$Nmp4=$Nmp[2];
$Nmmp4=$Nmmp[2];
$Nkou4=$Nkou[2];
$Nmam4=$Nmam[2];
$Nsub4=$Nsub[2];
$Nhai4=$Nhai[2];
$Ncount4=$Ncount[2];
$Nnecount4=$Nnecount[2];
$Nsex4=$Nsex[2];
$Nsei4=$Nsei[2];
}
if($Kimg2 != 0 && $Kimg3 != 0 && $Kimg4 != 0 && $Kimg5 == 0){
$Nlev5=$Nlev[2];
$Nmlev5=$Nmlev[2];
$Nimg5=$Nimg[2];
$Nhp5=$Nhp[2];
$Nmhp5=$Nmhp[2];
$Nmp5=$Nmp[2];
$Nmmp5=$Nmmp[2];
$Nkou5=$Nkou[2];
$Nmam5=$Nmam[2];
$Nsub5=$Nsub[2];
$Nhai5=$Nhai[2];
$Ncount5=$Ncount[2];
$Nnecount5=$Nnecount[2];
$Nsex5=$Nsex[2];
$Nsei5=$Nsei[2];
}
if($Kimg2 != 0 && $Kimg3 != 0 && $Kimg4 != 0 && $Kimg5 != 0 && $Kimg6 == 0){
$Nlev6=$Nlev[2];
$Nmlev6=$Nmlev[2];
$Nimg6=$Nimg[2];
$Nhp6=$Nhp[2];
$Nmhp6=$Nmhp[2];
$Nmp6=$Nmp[2];
$Nmmp6=$Nmmp[2];
$Nkou6=$Nkou[2];
$Nmam6=$Nmam[2];
$Nsub6=$Nsub[2];
$Nhai6=$Nhai[2];
$Ncount6=$Ncount[2];
$Nnecount6=$Nnecount[2];
$Nsex6=$Nsex[2];
$Nsei6=$Nsei[2];
}
if($Kimg2 != 0 && $Kimg3 != 0 && $Kimg4 != 0 && $Kimg5 != 0 && $Kimg6 != 0 && $Kimg7 == 0){
$Nlev7=$Nlev[2];
$Nmlev7=$Nmlev[2];
$Nimg7=$Nimg[2];
$Nhp7=$Nhp[2];
$Nmhp7=$Nmhp[2];
$Nmp7=$Nmp[2];
$Nmmp7=$Nmmp[2];
$Nkou7=$Nkou[2];
$Nmam7=$Nmam[2];
$Nsub7=$Nsub[2];
$Nhai7=$Nhai[2];
$Ncount7=$Ncount[2];
$Nnecount7=$Nnecount[2];
$Nsex7=$Nsex[2];
$Nsei7=$Nsei[2];
}
if($Kimg2 != 0 && $Kimg3 != 0 && $Kimg4 != 0 && $Kimg5 != 0 && $Kimg6 != 0 && $Kimg7 != 0 && $Kimg8 == 0){
$Nlev8=$Nlev[2];
$Nmlev8=$Nmlev[2];
$Nimg8=$Nimg[2];
$Nhp8=$Nhp[2];
$Nmhp8=$Nmhp[2];
$Nmp8=$Nmp[2];
$Nmmp8=$Nmmp[2];
$Nkou8=$Nkou[2];
$Nmam8=$Nmam[2];
$Nsub8=$Nsub[2];
$Nhai8=$Nhai[2];
$Ncount8=$Ncount[2];
$Nnecount8=$Nnecount[2];
$Nsex8=$Nsex[2];
$Nsei8=$Nsei[2];
}
if($Kimg2 != 0 && $Kimg3 != 0 && $Kimg4 != 0 && $Kimg5 != 0 && $Kimg6 != 0 && $Kimg7 != 0 && $Kimg8 != 0 && $Kimg9 == 0){
$Nlev9=$Nlev[2];
$Nmlev9=$Nmlev[2];
$Nimg9=$Nimg[2];
$Nhp9=$Nhp[2];
$Nmhp9=$Nmhp[2];
$Nmp9=$Nmp[2];
$Nmmp9=$Nmmp[2];
$Nkou9=$Nkou[2];
$Nmam9=$Nmam[2];
$Nsub9=$Nsub[2];
$Nhai9=$Nhai[2];
$Ncount9=$Ncount[2];
$Nnecount9=$Nnecount[2];
$Nsex9=$Nsex[2];
$Nsei9=$Nsei[2];
}
if($Kimg2 != 0 && $Kimg3 != 0 && $Kimg4 != 0 && $Kimg5 != 0 && $Kimg6 != 0 && $Kimg7 != 0 && $Kimg8 != 0 && $Kimg9 != 0 && $Kimg10 == 0){
$Nlev10=$Nlev[2];
$Nmlev10=$Nmlev[2];
$Nimg10=$Nimg[2];
$Nhp10=$Nhp[2];
$Nmhp10=$Nmhp[2];
$Nmp10=$Nmp[2];
$Nmmp10=$Nmmp[2];
$Nkou10=$Nkou[2];
$Nmam10=$Nmam[2];
$Nsub10=$Nsub[2];
$Nhai10=$Nhai[2];
$Ncount10=$Ncount[2];
$Nnecount10=$Nnecount[2];
$Nsex10=$Nsex[2];
$Nsei10=$Nsei[2];
}
$Nmoney = $Kmoney - $money;
$newline = "$Kname<>$Kpass<>$Klev1<>$Kmlev1<>$Kimg1<>$Khp1<>$Kmhp1<>$Kmp1<>$Kmmp1<>$Kkou1<>$Kmam1<>$Ksub1<>$Khai1<>$Kcount1<>$Knecount1<>$Ksex1<>$Ksei1<>$Nlev2<>$Nmlev2<>$Nimg2<>$Nhp2<>$Nmhp2<>$Nmp2<>$Nmmp2<>$Nkou2<>$Nmam2<>$Nsub2<>$Nhai2<>$Ncount2<>$Nnecount2<>$Nsex2<>$Nsei2<>$Nlev3<>$Nmlev3<>$Nimg3<>$Nhp3<>$Nmhp3<>$Nmp3<>$Nmmp3<>$Nkou3<>$Nmam3<>$Nsub3<>$Nhai3<>$Ncount3<>$Nnecount3<>$Nsex3<>$Nsei3<>$Nlev4<>$Nmlev4<>$Nimg4<>$Nhp4<>$Nmhp4<>$Nmp4<>$Nmmp4<>$Nkou4<>$Nmam4<>$Nsub4<>$Nhai4<>$Ncount4<>$Nnecount4<>$Nsex4<>$Nsei4<>$Nlev5<>$Nmlev5<>$Nimg5<>$Nhp5<>$Nmhp5<>$Nmp5<>$Nmmp5<>$Nkou5<>$Nmam5<>$Nsub5<>$Nhai5<>$Ncount5<>$Nnecount5<>$Nsex5<>$Nsei5<>$Nlev6<>$Nmlev6<>$Nimg6<>$Nhp6<>$Nmhp6<>$Nmp6<>$Nmmp6<>$Nkou6<>$Nmam6<>$Nsub6<>$Nhai6<>$Ncount6<>$Nnecount6<>$Nsex6<>$Nsei6<>$Nlev7<>$Nmlev7<>$Nimg7<>$Nhp7<>$Nmhp7<>$Nmp7<>$Nmmp7<>$Nkou7<>$Nmam7<>$Nsub7<>$Nhai7<>$Ncount7<>$Nnecount7<>$Nsex7<>$Nsei7<>$Nlev8<>$Nmlev8<>$Nimg8<>$Nhp8<>$Nmhp8<>$Nmp8<>$Nmmp8<>$Nkou8<>$Nmam8<>$Nsub8<>$Nhai8<>$Ncount8<>$Nnecount8<>$Nsex8<>$Nsei8<>$Nlev9<>$Nmlev9<>$Nimg9<>$Nhp9<>$Nmhp9<>$Nmp9<>$Nmmp9<>$Nkou9<>$Nmam9<>$Nsub9<>$Nhai9<>$Ncount9<>$Nnecount9<>$Nsex9<>$Nsei9<>$Nlev10<>$Nmlev10<>$Nimg10<>$Nhp10<>$Nmhp10<>$Nmp10<>$Nmmp10<>$Nkou10<>$Nmam10<>$Nsub10<>$Nhai10<>$Ncount10<>$Nnecount10<>$Nsex10<>$Nsei10<>$Kdummy<>$Kkey<>$Nmoney";
&lock;
open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
&unlock;

open(FH,"omiai/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);}

$newline = "$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>$Aname[1]<>$Alev[1]<>$Amlev[1]<>$Aimg[1]<>$Ahp[1]<>$Amhp[1]<>$Amp[1]<>$Ammp[1]<>$Akou[1]<>$Amam[1]<>$Asub[1]<>$Ahai[1]<>$Acount[1]<>$Anecount[1]<>$Asex[1]<>$Asei[1]<>$Aname[2]<>$Alev[2]<>$Amlev[2]<>$Aimg[2]<>$Ahp[2]<>$Amhp[2]<>$Amp[2]<>$Ammp[2]<>$Akou[2]<>$Amam[2]<>$Asub[2]<>$Ahai[2]<>$Acount[2]<>$Anecount[2]<>$Asex[2]<>$Asei[2]<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[1]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";
&lock;
open(FH, ">omiai/$inname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
&unlock;

open(FH,"${datadir}/$userdata") || &error("Can't open $userdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Yname,$Ypass,$Yip,$Ybye,$Yplay,$Yplay2,$Yplay3,$Ykey,$Yimg1,$Yhai1,$Ylev1,$Yimg2,$Yhai2,$Ylev2,$Yimg3,$Yhai3,$Ylev3,$Ymoney,$Ymes,$turn) = split(/<>/,$line);
    if($inname eq $Yname) {
    $passcheck = crypt($inpass, $inname);
    if($passcheck ne $Ypass) {&error("パスワードが違います");}
    $line = "$Yname<>$Ypass<>$Yip<>$Ybye<>$Yplay<>$Yplay2<>$Yplay3<>$Ykey<>$Yimg1<>$Yhai1<>$Ylev1<>$Yimg2<>$Yhai2<>$Ylev2<>$Yimg3<>$Yhai3<>$Ylev3<>$Nmoney<>$Ymes<>$turn";

&lock;
open(FH, ">${datadir}/$userdata") ;
print FH @lines;
close(FH);
&unlock;
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
<FONT size="5pt" color="#0000FF"><B>LOGIN画面に移動しました</B>
</FONT>
<HR>
</TD>
</TR>
</TBODY>
</TABLE>
<BR><BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="omiai">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="お見合い所へ">
</FORM>
<BR>
</CENTER>
EOF

&footer;
