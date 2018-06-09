use utf8;
use open IO => ":utf8";
use open ":std";

$inname   = $FORM{'name'};
$inpass   = $FORM{'password'};
$BBNAME   = $FORM{'aname'};
$KMONS    = $FORM{'KMONS'};
$AMONS    = $FORM{'AMONS'};

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
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);}

if($Kimg[1] != 0){&error("お見合いは既に設定されてます。解除してから申し込んで下さい");}

open(FH,"${datadir}/$inname.cgi") || &error("Can't open open3");
@Klines = <FH>;
close(FH);

foreach $Kline (@Klines) {
   ($Kname,$Kpass,$Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Klev[3],$Kmlev[3],$Kimg[3],$Khp[3],$Kmhp[3],$Kmp[3],$Kmmp[3],$Kkou[3],$Kmam[3],$Ksub[3],$Khai[3],$Kcount[3],$Knecount[3],$Ksex[3],$Ksei[3],$Klev[4],$Kmlev[4],$Kimg[4],$Khp[4],$Kmhp[4],$Kmp[4],$Kmmp[4],$Kkou[4],$Kmam[4],$Ksub[4],$Khai[4],$Kcount[4],$Knecount[4],$Ksex[4],$Ksei[4],$Klev[5],$Kmlev[5],$Kimg[5],$Khp[5],$Kmhp[5],$Kmp[5],$Kmmp[5],$Kkou[5],$Kmam[5],$Ksub[5],$Khai[5],$Kcount[5],$Knecount[5],$Ksex[5],$Ksei[5],$Klev[6],$Kmlev[6],$Kimg[6],$Khp[6],$Kmhp[6],$Kmp[6],$Kmmp[6],$Kkou[6],$Kmam[6],$Ksub[6],$Khai[6],$Kcount[6],$Knecount[6],$Ksex[6],$Ksei[6],$Klev[7],$Kmlev[7],$Kimg[7],$Khp[7],$Kmhp[7],$Kmp[7],$Kmmp[7],$Kkou[7],$Kmam[7],$Ksub[7],$Khai[7],$Kcount[7],$Knecount[7],$Ksex[7],$Ksei[7],$Klev[8],$Kmlev[8],$Kimg[8],$Khp[8],$Kmhp[8],$Kmp[8],$Kmmp[8],$Kkou[8],$Kmam[8],$Ksub[8],$Khai[8],$Kcount[8],$Knecount[8],$Ksex[8],$Ksei[8],$Klev[9],$Kmlev[9],$Kimg[9],$Khp[9],$Kmhp[9],$Kmp[9],$Kmmp[9],$Kkou[9],$Kmam[9],$Ksub[9],$Khai[9],$Kcount[9],$Knecount[9],$Ksex[9],$Ksei[9],$Klev[10],$Kmlev[10],$Kimg[10],$Khp[10],$Kmhp[10],$Kmp[10],$Kmmp[10],$Kkou[10],$Kmam[10],$Ksub[10],$Khai[10],$Kcount[10],$Knecount[10],$Ksex[10],$Ksei[10],$Kdummy,$Kkey,$Kmoney) = split(/<>/,$Kline);}

if($Klev[$KMONS] < $haigoulevel){&error("自分のモンスターが配合レベルに達していません");}
if($Kimg[2] == 0){&error("所持モンスターが1体の時は設定出来ません");}

if($KMONS >= 1 && $KMONS <= 3){&error("NO.1～NO.3のモンスターは選択出来ません");}
if($AMONS >= 1 && $AMONS <= 3){&error("NO.1～NO.3のモンスターは選択出来ません");}
open(FH,"${datadir}/$BBNAME.cgi") || &error("Can't open open3");
@Alines = <FH>;
close(FH);

foreach $Aline (@Alines) {
   ($Aname,$Apass,$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Alev[3],$Amlev[3],$Aimg[3],$Ahp[3],$Amhp[3],$Amp[3],$Ammp[3],$Akou[3],$Amam[3],$Asub[3],$Ahai[3],$Acount[3],$Anecount[3],$Asex[3],$Asei[3],$Alev[4],$Amlev[4],$Aimg[4],$Ahp[4],$Amhp[4],$Amp[4],$Ammp[4],$Akou[4],$Amam[4],$Asub[4],$Ahai[4],$Acount[4],$Anecount[4],$Asex[4],$Asei[4],$Alev[5],$Amlev[5],$Aimg[5],$Ahp[5],$Amhp[5],$Amp[5],$Ammp[5],$Akou[5],$Amam[5],$Asub[5],$Ahai[5],$Acount[5],$Anecount[5],$Asex[5],$Asei[5],$Alev[6],$Amlev[6],$Aimg[6],$Ahp[6],$Amhp[6],$Amp[6],$Ammp[6],$Akou[6],$Amam[6],$Asub[6],$Ahai[6],$Acount[6],$Anecount[6],$Asex[6],$Asei[6],$Alev[7],$Amlev[7],$Aimg[7],$Ahp[7],$Amhp[7],$Amp[7],$Ammp[7],$Akou[7],$Amam[7],$Asub[7],$Ahai[7],$Acount[7],$Anecount[7],$Asex[7],$Asei[7],$Alev[8],$Amlev[8],$Aimg[8],$Ahp[8],$Amhp[8],$Amp[8],$Ammp[8],$Akou[8],$Amam[8],$Asub[8],$Ahai[8],$Acount[8],$Anecount[8],$Asex[8],$Asei[8],$Alev[9],$Amlev[9],$Aimg[9],$Ahp[9],$Amhp[9],$Amp[9],$Ammp[9],$Akou[9],$Amam[9],$Asub[9],$Ahai[9],$Acount[9],$Anecount[9],$Asex[9],$Asei[9],$Alev[10],$Amlev[10],$Aimg[10],$Ahp[10],$Amhp[10],$Amp[10],$Ammp[10],$Akou[10],$Amam[10],$Asub[10],$Ahai[10],$Acount[10],$Anecount[10],$Asex[10],$Asei[10],$Adummy,$Akey,$Amoney) = split(/<>/,$Aline);}

if($Alev[$AMONS] < $haigoulevel){&error("相手のモンスターが配合レベルに達していません");}
if($Aimg[2] == 0){&error("相手の所持モンスターが1体の時は設定出来ません");}
if($Asex[$AMONS] == $Ksex[$KMONS]){&error("性別が同じです");}

open(FH,"${datadir}/$inname.cgi") || &error("Can't open open3");
@Klines = <FH>;
close(FH);

foreach $Kline (@Klines) {
   ($Kname,$Kpass,$Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Klev[3],$Kmlev[3],$Kimg[3],$Khp[3],$Kmhp[3],$Kmp[3],$Kmmp[3],$Kkou[3],$Kmam[3],$Ksub[3],$Khai[3],$Kcount[3],$Knecount[3],$Ksex[3],$Ksei[3],$Klev[4],$Kmlev[4],$Kimg[4],$Khp[4],$Kmhp[4],$Kmp[4],$Kmmp[4],$Kkou[4],$Kmam[4],$Ksub[4],$Khai[4],$Kcount[4],$Knecount[4],$Ksex[4],$Ksei[4],$Klev[5],$Kmlev[5],$Kimg[5],$Khp[5],$Kmhp[5],$Kmp[5],$Kmmp[5],$Kkou[5],$Kmam[5],$Ksub[5],$Khai[5],$Kcount[5],$Knecount[5],$Ksex[5],$Ksei[5],$Klev[6],$Kmlev[6],$Kimg[6],$Khp[6],$Kmhp[6],$Kmp[6],$Kmmp[6],$Kkou[6],$Kmam[6],$Ksub[6],$Khai[6],$Kcount[6],$Knecount[6],$Ksex[6],$Ksei[6],$Klev[7],$Kmlev[7],$Kimg[7],$Khp[7],$Kmhp[7],$Kmp[7],$Kmmp[7],$Kkou[7],$Kmam[7],$Ksub[7],$Khai[7],$Kcount[7],$Knecount[7],$Ksex[7],$Ksei[7],$Klev[8],$Kmlev[8],$Kimg[8],$Khp[8],$Kmhp[8],$Kmp[8],$Kmmp[8],$Kkou[8],$Kmam[8],$Ksub[8],$Khai[8],$Kcount[8],$Knecount[8],$Ksex[8],$Ksei[8],$Klev[9],$Kmlev[9],$Kimg[9],$Khp[9],$Kmhp[9],$Kmp[9],$Kmmp[9],$Kkou[9],$Kmam[9],$Ksub[9],$Khai[9],$Kcount[9],$Knecount[9],$Ksex[9],$Ksei[9],$Klev[10],$Kmlev[10],$Kimg[10],$Khp[10],$Kmhp[10],$Kmp[10],$Kmmp[10],$Kkou[10],$Kmam[10],$Ksub[10],$Khai[10],$Kcount[10],$Knecount[10],$Ksex[10],$Ksei[10],$Kdummy,$Kkey,$Kmoney) = split(/<>/,$Kline);}

for($A=1;$A<11;$A++){
$Nlev[$A]     = $Klev[$A];
$Nmlev[$A]    = $Kmlev[$A];
$Nimg[$A]     = $Kimg[$A];
$Nhp[$A]      = $Khp[$A];
$Nmhp[$A]     = $Kmhp[$A];
$Nmp[$A]      = $Kmp[$A];
$Nmmp[$A]     = $Kmmp[$A];
$Nkou[$A]     = $Kkou[$A];
$Nmam[$A]     = $Kmam[$A];
$Nsub[$A]     = $Ksub[$A];
$Nhai[$A]     = $Khai[$A];
$Ncount[$A]   = $Kcount[$A];
$Nnecount[$A] = $Knecount[$A];
$Nsex[$A]     = $Ksex[$A];
$Nsei[$A]     = $Ksei[$A];
}

$Slev[1]     = $Klev[$KMONS];
$Smlev[1]    = $Kmlev[$KMONS];
$Simg[1]     = $Kimg[$KMONS];
$Shp[1]      = $Khp[$KMONS];
$Smhp[1]     = $Kmhp[$KMONS];
$Smp[1]      = $Kmp[$KMONS];
$Smmp[1]     = $Kmmp[$KMONS];
$Skou[1]     = $Kkou[$KMONS];
$Smam[1]     = $Kmam[$KMONS];
$Ssub[1]     = $Ksub[$KMONS];
$Shai[1]     = $Khai[$KMONS];
$Scount[1]   = $Kcount[$KMONS];
$Snecount[1] = $Knecount[$KMONS];
$Ssex[1]     = $Ksex[$KMONS];
$Ssei[1]     = $Ksei[$KMONS];

$Nlev[10]     = 0;
$Nmlev[10]    = 0;
$Nimg[10]     = 0;
$Nhp[10]      = 0;
$Nmhp[10]     = 0;
$Nmp[10]      = 0;
$Nmmp[10]     = 0;
$Nkou[10]     = 0;
$Nmam[10]     = 0;
$Nsub[10]     = 0;
$Nhai[10]     = 0;
$Ncount[10]   = 0;
$Nnecount[10] = 0;
$Nsex[10]     = 0;
$Nsei[10]     = 0;

if($KMONS == 1){
$Nlev[1]     = $Klev[2];
$Nmlev[1]    = $Kmlev[2];
$Nimg[1]     = $Kimg[2];
$Nhp[1]      = $Khp[2];
$Nmhp[1]     = $Kmhp[2];
$Nmp[1]      = $Kmp[2];
$Nmmp[1]     = $Kmmp[2];
$Nkou[1]     = $Kkou[2];
$Nmam[1]     = $Kmam[2];
$Nsub[1]     = $Ksub[2];
$Nhai[1]     = $Khai[2];
$Ncount[1]   = $Kcount[2];
$Nnecount[1] = $Knecount[2];
$Nsex[1]     = $Ksex[2];
$Nsei[1]     = $Ksei[2];

$Nlev[2]     = $Klev[3];
$Nmlev[2]    = $Kmlev[3];
$Nimg[2]     = $Kimg[3];
$Nhp[2]      = $Khp[3];
$Nmhp[2]     = $Kmhp[3];
$Nmp[2]      = $Kmp[3];
$Nmmp[2]     = $Kmmp[3];
$Nkou[2]     = $Kkou[3];
$Nmam[2]     = $Kmam[3];
$Nsub[2]     = $Ksub[3];
$Nhai[2]     = $Khai[3];
$Ncount[2]   = $Kcount[3];
$Nnecount[2] = $Knecount[3];
$Nsex[2]     = $Ksex[3];
$Nsei[2]     = $Ksei[3];

$Nlev[3]     = $Klev[4];
$Nmlev[3]    = $Kmlev[4];
$Nimg[3]     = $Kimg[4];
$Nhp[3]      = $Khp[4];
$Nmhp[3]     = $Kmhp[4];
$Nmp[3]      = $Kmp[4];
$Nmmp[3]     = $Kmmp[4];
$Nkou[3]     = $Kkou[4];
$Nmam[3]     = $Kmam[4];
$Nsub[3]     = $Ksub[4];
$Nhai[3]     = $Khai[4];
$Ncount[3]   = $Kcount[4];
$Nnecount[3] = $Knecount[4];
$Nsex[3]     = $Ksex[4];
$Nsei[3]     = $Ksei[4];

$Nlev[4]     = $Klev[5];
$Nmlev[4]    = $Kmlev[5];
$Nimg[4]     = $Kimg[5];
$Nhp[4]      = $Khp[5];
$Nmhp[4]     = $Kmhp[5];
$Nmp[4]      = $Kmp[5];
$Nmmp[4]     = $Kmmp[5];
$Nkou[4]     = $Kkou[5];
$Nmam[4]     = $Kmam[5];
$Nsub[4]     = $Ksub[5];
$Nhai[4]     = $Khai[5];
$Ncount[4]   = $Kcount[5];
$Nnecount[4] = $Knecount[5];
$Nsex[4]     = $Ksex[5];
$Nsei[4]     = $Ksei[5];

$Nlev[5]     = $Klev[6];
$Nmlev[5]    = $Kmlev[6];
$Nimg[5]     = $Kimg[6];
$Nhp[5]      = $Khp[6];
$Nmhp[5]     = $Kmhp[6];
$Nmp[5]      = $Kmp[6];
$Nmmp[5]     = $Kmmp[6];
$Nkou[5]     = $Kkou[6];
$Nmam[5]     = $Kmam[6];
$Nsub[5]     = $Ksub[6];
$Nhai[5]     = $Khai[6];
$Ncount[5]   = $Kcount[6];
$Nnecount[5] = $Knecount[6];
$Nsex[5]     = $Ksex[6];
$Nsei[5]     = $Ksei[6];

$Nlev[6]     = $Klev[7];
$Nmlev[6]    = $Kmlev[7];
$Nimg[6]     = $Kimg[7];
$Nhp[6]      = $Khp[7];
$Nmhp[6]     = $Kmhp[7];
$Nmp[6]      = $Kmp[7];
$Nmmp[6]     = $Kmmp[7];
$Nkou[6]     = $Kkou[7];
$Nmam[6]     = $Kmam[7];
$Nsub[6]     = $Ksub[7];
$Nhai[6]     = $Khai[7];
$Ncount[6]   = $Kcount[7];
$Nnecount[6] = $Knecount[7];
$Nsex[6]     = $Ksex[7];
$Nsei[6]     = $Ksei[7];

$Nlev[7]     = $Klev[8];
$Nmlev[7]    = $Kmlev[8];
$Nimg[7]     = $Kimg[8];
$Nhp[7]      = $Khp[8];
$Nmhp[7]     = $Kmhp[8];
$Nmp[7]      = $Kmp[8];
$Nmmp[7]     = $Kmmp[8];
$Nkou[7]     = $Kkou[8];
$Nmam[7]     = $Kmam[8];
$Nsub[7]     = $Ksub[8];
$Nhai[7]     = $Khai[8];
$Ncount[7]   = $Kcount[8];
$Nnecount[7] = $Knecount[8];
$Nsex[7]     = $Ksex[8];
$Nsei[7]     = $Ksei[8];

$Nlev[8]     = $Klev[9];
$Nmlev[8]    = $Kmlev[9];
$Nimg[8]     = $Kimg[9];
$Nhp[8]      = $Khp[9];
$Nmhp[8]     = $Kmhp[9];
$Nmp[8]      = $Kmp[9];
$Nmmp[8]     = $Kmmp[9];
$Nkou[8]     = $Kkou[9];
$Nmam[8]     = $Kmam[9];
$Nsub[8]     = $Ksub[9];
$Nhai[8]     = $Khai[9];
$Ncount[8]   = $Kcount[9];
$Nnecount[8] = $Knecount[9];
$Nsex[8]     = $Ksex[9];
$Nsei[8]     = $Ksei[9];

$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}

if($KMONS == 2){
$Nlev[2]     = $Klev[3];
$Nmlev[2]    = $Kmlev[3];
$Nimg[2]     = $Kimg[3];
$Nhp[2]      = $Khp[3];
$Nmhp[2]     = $Kmhp[3];
$Nmp[2]      = $Kmp[3];
$Nmmp[2]     = $Kmmp[3];
$Nkou[2]     = $Kkou[3];
$Nmam[2]     = $Kmam[3];
$Nsub[2]     = $Ksub[3];
$Nhai[2]     = $Khai[3];
$Ncount[2]   = $Kcount[3];
$Nnecount[2] = $Knecount[3];
$Nsex[2]     = $Ksex[3];
$Nsei[2]     = $Ksei[3];

$Nlev[3]     = $Klev[4];
$Nmlev[3]    = $Kmlev[4];
$Nimg[3]     = $Kimg[4];
$Nhp[3]      = $Khp[4];
$Nmhp[3]     = $Kmhp[4];
$Nmp[3]      = $Kmp[4];
$Nmmp[3]     = $Kmmp[4];
$Nkou[3]     = $Kkou[4];
$Nmam[3]     = $Kmam[4];
$Nsub[3]     = $Ksub[4];
$Nhai[3]     = $Khai[4];
$Ncount[3]   = $Kcount[4];
$Nnecount[3] = $Knecount[4];
$Nsex[3]     = $Ksex[4];
$Nsei[3]     = $Ksei[4];

$Nlev[4]     = $Klev[5];
$Nmlev[4]    = $Kmlev[5];
$Nimg[4]     = $Kimg[5];
$Nhp[4]      = $Khp[5];
$Nmhp[4]     = $Kmhp[5];
$Nmp[4]      = $Kmp[5];
$Nmmp[4]     = $Kmmp[5];
$Nkou[4]     = $Kkou[5];
$Nmam[4]     = $Kmam[5];
$Nsub[4]     = $Ksub[5];
$Nhai[4]     = $Khai[5];
$Ncount[4]   = $Kcount[5];
$Nnecount[4] = $Knecount[5];
$Nsex[4]     = $Ksex[5];
$Nsei[4]     = $Ksei[5];

$Nlev[5]     = $Klev[6];
$Nmlev[5]    = $Kmlev[6];
$Nimg[5]     = $Kimg[6];
$Nhp[5]      = $Khp[6];
$Nmhp[5]     = $Kmhp[6];
$Nmp[5]      = $Kmp[6];
$Nmmp[5]     = $Kmmp[6];
$Nkou[5]     = $Kkou[6];
$Nmam[5]     = $Kmam[6];
$Nsub[5]     = $Ksub[6];
$Nhai[5]     = $Khai[6];
$Ncount[5]   = $Kcount[6];
$Nnecount[5] = $Knecount[6];
$Nsex[5]     = $Ksex[6];
$Nsei[5]     = $Ksei[6];

$Nlev[6]     = $Klev[7];
$Nmlev[6]    = $Kmlev[7];
$Nimg[6]     = $Kimg[7];
$Nhp[6]      = $Khp[7];
$Nmhp[6]     = $Kmhp[7];
$Nmp[6]      = $Kmp[7];
$Nmmp[6]     = $Kmmp[7];
$Nkou[6]     = $Kkou[7];
$Nmam[6]     = $Kmam[7];
$Nsub[6]     = $Ksub[7];
$Nhai[6]     = $Khai[7];
$Ncount[6]   = $Kcount[7];
$Nnecount[6] = $Knecount[7];
$Nsex[6]     = $Ksex[7];
$Nsei[6]     = $Ksei[7];

$Nlev[7]     = $Klev[8];
$Nmlev[7]    = $Kmlev[8];
$Nimg[7]     = $Kimg[8];
$Nhp[7]      = $Khp[8];
$Nmhp[7]     = $Kmhp[8];
$Nmp[7]      = $Kmp[8];
$Nmmp[7]     = $Kmmp[8];
$Nkou[7]     = $Kkou[8];
$Nmam[7]     = $Kmam[8];
$Nsub[7]     = $Ksub[8];
$Nhai[7]     = $Khai[8];
$Ncount[7]   = $Kcount[8];
$Nnecount[7] = $Knecount[8];
$Nsex[7]     = $Ksex[8];
$Nsei[7]     = $Ksei[8];

$Nlev[8]     = $Klev[9];
$Nmlev[8]    = $Kmlev[9];
$Nimg[8]     = $Kimg[9];
$Nhp[8]      = $Khp[9];
$Nmhp[8]     = $Kmhp[9];
$Nmp[8]      = $Kmp[9];
$Nmmp[8]     = $Kmmp[9];
$Nkou[8]     = $Kkou[9];
$Nmam[8]     = $Kmam[9];
$Nsub[8]     = $Ksub[9];
$Nhai[8]     = $Khai[9];
$Ncount[8]   = $Kcount[9];
$Nnecount[8] = $Knecount[9];
$Nsex[8]     = $Ksex[9];
$Nsei[8]     = $Ksei[9];

$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}
if($KMONS == 3){
$Nlev[3]     = $Klev[4];
$Nmlev[3]    = $Kmlev[4];
$Nimg[3]     = $Kimg[4];
$Nhp[3]      = $Khp[4];
$Nmhp[3]     = $Kmhp[4];
$Nmp[3]      = $Kmp[4];
$Nmmp[3]     = $Kmmp[4];
$Nkou[3]     = $Kkou[4];
$Nmam[3]     = $Kmam[4];
$Nsub[3]     = $Ksub[4];
$Nhai[3]     = $Khai[4];
$Ncount[3]   = $Kcount[4];
$Nnecount[3] = $Knecount[4];
$Nsex[3]     = $Ksex[4];
$Nsei[3]     = $Ksei[4];

$Nlev[4]     = $Klev[5];
$Nmlev[4]    = $Kmlev[5];
$Nimg[4]     = $Kimg[5];
$Nhp[4]      = $Khp[5];
$Nmhp[4]     = $Kmhp[5];
$Nmp[4]      = $Kmp[5];
$Nmmp[4]     = $Kmmp[5];
$Nkou[4]     = $Kkou[5];
$Nmam[4]     = $Kmam[5];
$Nsub[4]     = $Ksub[5];
$Nhai[4]     = $Khai[5];
$Ncount[4]   = $Kcount[5];
$Nnecount[4] = $Knecount[5];
$Nsex[4]     = $Ksex[5];
$Nsei[4]     = $Ksei[5];

$Nlev[5]     = $Klev[6];
$Nmlev[5]    = $Kmlev[6];
$Nimg[5]     = $Kimg[6];
$Nhp[5]      = $Khp[6];
$Nmhp[5]     = $Kmhp[6];
$Nmp[5]      = $Kmp[6];
$Nmmp[5]     = $Kmmp[6];
$Nkou[5]     = $Kkou[6];
$Nmam[5]     = $Kmam[6];
$Nsub[5]     = $Ksub[6];
$Nhai[5]     = $Khai[6];
$Ncount[5]   = $Kcount[6];
$Nnecount[5] = $Knecount[6];
$Nsex[5]     = $Ksex[6];
$Nsei[5]     = $Ksei[6];

$Nlev[6]     = $Klev[7];
$Nmlev[6]    = $Kmlev[7];
$Nimg[6]     = $Kimg[7];
$Nhp[6]      = $Khp[7];
$Nmhp[6]     = $Kmhp[7];
$Nmp[6]      = $Kmp[7];
$Nmmp[6]     = $Kmmp[7];
$Nkou[6]     = $Kkou[7];
$Nmam[6]     = $Kmam[7];
$Nsub[6]     = $Ksub[7];
$Nhai[6]     = $Khai[7];
$Ncount[6]   = $Kcount[7];
$Nnecount[6] = $Knecount[7];
$Nsex[6]     = $Ksex[7];
$Nsei[6]     = $Ksei[7];

$Nlev[7]     = $Klev[8];
$Nmlev[7]    = $Kmlev[8];
$Nimg[7]     = $Kimg[8];
$Nhp[7]      = $Khp[8];
$Nmhp[7]     = $Kmhp[8];
$Nmp[7]      = $Kmp[8];
$Nmmp[7]     = $Kmmp[8];
$Nkou[7]     = $Kkou[8];
$Nmam[7]     = $Kmam[8];
$Nsub[7]     = $Ksub[8];
$Nhai[7]     = $Khai[8];
$Ncount[7]   = $Kcount[8];
$Nnecount[7] = $Knecount[8];
$Nsex[7]     = $Ksex[8];
$Nsei[7]     = $Ksei[8];

$Nlev[8]     = $Klev[9];
$Nmlev[8]    = $Kmlev[9];
$Nimg[8]     = $Kimg[9];
$Nhp[8]      = $Khp[9];
$Nmhp[8]     = $Kmhp[9];
$Nmp[8]      = $Kmp[9];
$Nmmp[8]     = $Kmmp[9];
$Nkou[8]     = $Kkou[9];
$Nmam[8]     = $Kmam[9];
$Nsub[8]     = $Ksub[9];
$Nhai[8]     = $Khai[9];
$Ncount[8]   = $Kcount[9];
$Nnecount[8] = $Knecount[9];
$Nsex[8]     = $Ksex[9];
$Nsei[8]     = $Ksei[9];

$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}
if($KMONS == 4){
$Nlev[4]     = $Klev[5];
$Nmlev[4]    = $Kmlev[5];
$Nimg[4]     = $Kimg[5];
$Nhp[4]      = $Khp[5];
$Nmhp[4]     = $Kmhp[5];
$Nmp[4]      = $Kmp[5];
$Nmmp[4]     = $Kmmp[5];
$Nkou[4]     = $Kkou[5];
$Nmam[4]     = $Kmam[5];
$Nsub[4]     = $Ksub[5];
$Nhai[4]     = $Khai[5];
$Ncount[4]   = $Kcount[5];
$Nnecount[4] = $Knecount[5];
$Nsex[4]     = $Ksex[5];
$Nsei[4]     = $Ksei[5];

$Nlev[5]     = $Klev[6];
$Nmlev[5]    = $Kmlev[6];
$Nimg[5]     = $Kimg[6];
$Nhp[5]      = $Khp[6];
$Nmhp[5]     = $Kmhp[6];
$Nmp[5]      = $Kmp[6];
$Nmmp[5]     = $Kmmp[6];
$Nkou[5]     = $Kkou[6];
$Nmam[5]     = $Kmam[6];
$Nsub[5]     = $Ksub[6];
$Nhai[5]     = $Khai[6];
$Ncount[5]   = $Kcount[6];
$Nnecount[5] = $Knecount[6];
$Nsex[5]     = $Ksex[6];
$Nsei[5]     = $Ksei[6];

$Nlev[6]     = $Klev[7];
$Nmlev[6]    = $Kmlev[7];
$Nimg[6]     = $Kimg[7];
$Nhp[6]      = $Khp[7];
$Nmhp[6]     = $Kmhp[7];
$Nmp[6]      = $Kmp[7];
$Nmmp[6]     = $Kmmp[7];
$Nkou[6]     = $Kkou[7];
$Nmam[6]     = $Kmam[7];
$Nsub[6]     = $Ksub[7];
$Nhai[6]     = $Khai[7];
$Ncount[6]   = $Kcount[7];
$Nnecount[6] = $Knecount[7];
$Nsex[6]     = $Ksex[7];
$Nsei[6]     = $Ksei[7];

$Nlev[7]     = $Klev[8];
$Nmlev[7]    = $Kmlev[8];
$Nimg[7]     = $Kimg[8];
$Nhp[7]      = $Khp[8];
$Nmhp[7]     = $Kmhp[8];
$Nmp[7]      = $Kmp[8];
$Nmmp[7]     = $Kmmp[8];
$Nkou[7]     = $Kkou[8];
$Nmam[7]     = $Kmam[8];
$Nsub[7]     = $Ksub[8];
$Nhai[7]     = $Khai[8];
$Ncount[7]   = $Kcount[8];
$Nnecount[7] = $Knecount[8];
$Nsex[7]     = $Ksex[8];
$Nsei[7]     = $Ksei[8];

$Nlev[8]     = $Klev[9];
$Nmlev[8]    = $Kmlev[9];
$Nimg[8]     = $Kimg[9];
$Nhp[8]      = $Khp[9];
$Nmhp[8]     = $Kmhp[9];
$Nmp[8]      = $Kmp[9];
$Nmmp[8]     = $Kmmp[9];
$Nkou[8]     = $Kkou[9];
$Nmam[8]     = $Kmam[9];
$Nsub[8]     = $Ksub[9];
$Nhai[8]     = $Khai[9];
$Ncount[8]   = $Kcount[9];
$Nnecount[8] = $Knecount[9];
$Nsex[8]     = $Ksex[9];
$Nsei[8]     = $Ksei[9];

$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}
if($KMONS == 5){
$Nlev[5]     = $Klev[6];
$Nmlev[5]    = $Kmlev[6];
$Nimg[5]     = $Kimg[6];
$Nhp[5]      = $Khp[6];
$Nmhp[5]     = $Kmhp[6];
$Nmp[5]      = $Kmp[6];
$Nmmp[5]     = $Kmmp[6];
$Nkou[5]     = $Kkou[6];
$Nmam[5]     = $Kmam[6];
$Nsub[5]     = $Ksub[6];
$Nhai[5]     = $Khai[6];
$Ncount[5]   = $Kcount[6];
$Nnecount[5] = $Knecount[6];
$Nsex[5]     = $Ksex[6];
$Nsei[5]     = $Ksei[6];

$Nlev[6]     = $Klev[7];
$Nmlev[6]    = $Kmlev[7];
$Nimg[6]     = $Kimg[7];
$Nhp[6]      = $Khp[7];
$Nmhp[6]     = $Kmhp[7];
$Nmp[6]      = $Kmp[7];
$Nmmp[6]     = $Kmmp[7];
$Nkou[6]     = $Kkou[7];
$Nmam[6]     = $Kmam[7];
$Nsub[6]     = $Ksub[7];
$Nhai[6]     = $Khai[7];
$Ncount[6]   = $Kcount[7];
$Nnecount[6] = $Knecount[7];
$Nsex[6]     = $Ksex[7];
$Nsei[6]     = $Ksei[7];

$Nlev[7]     = $Klev[8];
$Nmlev[7]    = $Kmlev[8];
$Nimg[7]     = $Kimg[8];
$Nhp[7]      = $Khp[8];
$Nmhp[7]     = $Kmhp[8];
$Nmp[7]      = $Kmp[8];
$Nmmp[7]     = $Kmmp[8];
$Nkou[7]     = $Kkou[8];
$Nmam[7]     = $Kmam[8];
$Nsub[7]     = $Ksub[8];
$Nhai[7]     = $Khai[8];
$Ncount[7]   = $Kcount[8];
$Nnecount[7] = $Knecount[8];
$Nsex[7]     = $Ksex[8];
$Nsei[7]     = $Ksei[8];

$Nlev[8]     = $Klev[9];
$Nmlev[8]    = $Kmlev[9];
$Nimg[8]     = $Kimg[9];
$Nhp[8]      = $Khp[9];
$Nmhp[8]     = $Kmhp[9];
$Nmp[8]      = $Kmp[9];
$Nmmp[8]     = $Kmmp[9];
$Nkou[8]     = $Kkou[9];
$Nmam[8]     = $Kmam[9];
$Nsub[8]     = $Ksub[9];
$Nhai[8]     = $Khai[9];
$Ncount[8]   = $Kcount[9];
$Nnecount[8] = $Knecount[9];
$Nsex[8]     = $Ksex[9];
$Nsei[8]     = $Ksei[9];

$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}
if($KMONS == 6){
$Nlev[6]     = $Klev[7];
$Nmlev[6]    = $Kmlev[7];
$Nimg[6]     = $Kimg[7];
$Nhp[6]      = $Khp[7];
$Nmhp[6]     = $Kmhp[7];
$Nmp[6]      = $Kmp[7];
$Nmmp[6]     = $Kmmp[7];
$Nkou[6]     = $Kkou[7];
$Nmam[6]     = $Kmam[7];
$Nsub[6]     = $Ksub[7];
$Nhai[6]     = $Khai[7];
$Ncount[6]   = $Kcount[7];
$Nnecount[6] = $Knecount[7];
$Nsex[6]     = $Ksex[7];
$Nsei[6]     = $Ksei[7];

$Nlev[7]     = $Klev[8];
$Nmlev[7]    = $Kmlev[8];
$Nimg[7]     = $Kimg[8];
$Nhp[7]      = $Khp[8];
$Nmhp[7]     = $Kmhp[8];
$Nmp[7]      = $Kmp[8];
$Nmmp[7]     = $Kmmp[8];
$Nkou[7]     = $Kkou[8];
$Nmam[7]     = $Kmam[8];
$Nsub[7]     = $Ksub[8];
$Nhai[7]     = $Khai[8];
$Ncount[7]   = $Kcount[8];
$Nnecount[7] = $Knecount[8];
$Nsex[7]     = $Ksex[8];
$Nsei[7]     = $Ksei[8];

$Nlev[8]     = $Klev[9];
$Nmlev[8]    = $Kmlev[9];
$Nimg[8]     = $Kimg[9];
$Nhp[8]      = $Khp[9];
$Nmhp[8]     = $Kmhp[9];
$Nmp[8]      = $Kmp[9];
$Nmmp[8]     = $Kmmp[9];
$Nkou[8]     = $Kkou[9];
$Nmam[8]     = $Kmam[9];
$Nsub[8]     = $Ksub[9];
$Nhai[8]     = $Khai[9];
$Ncount[8]   = $Kcount[9];
$Nnecount[8] = $Knecount[9];
$Nsex[8]     = $Ksex[9];
$Nsei[8]     = $Ksei[9];

$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}
if($KMONS == 7){
$Nlev[7]     = $Klev[8];
$Nmlev[7]    = $Kmlev[8];
$Nimg[7]     = $Kimg[8];
$Nhp[7]      = $Khp[8];
$Nmhp[7]     = $Kmhp[8];
$Nmp[7]      = $Kmp[8];
$Nmmp[7]     = $Kmmp[8];
$Nkou[7]     = $Kkou[8];
$Nmam[7]     = $Kmam[8];
$Nsub[7]     = $Ksub[8];
$Nhai[7]     = $Khai[8];
$Ncount[7]   = $Kcount[8];
$Nnecount[7] = $Knecount[8];
$Nsex[7]     = $Ksex[8];
$Nsei[7]     = $Ksei[8];

$Nlev[8]     = $Klev[9];
$Nmlev[8]    = $Kmlev[9];
$Nimg[8]     = $Kimg[9];
$Nhp[8]      = $Khp[9];
$Nmhp[8]     = $Kmhp[9];
$Nmp[8]      = $Kmp[9];
$Nmmp[8]     = $Kmmp[9];
$Nkou[8]     = $Kkou[9];
$Nmam[8]     = $Kmam[9];
$Nsub[8]     = $Ksub[9];
$Nhai[8]     = $Khai[9];
$Ncount[8]   = $Kcount[9];
$Nnecount[8] = $Knecount[9];
$Nsex[8]     = $Ksex[9];
$Nsei[8]     = $Ksei[9];

$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}
if($KMONS == 8){
$Nlev[8]     = $Klev[9];
$Nmlev[8]    = $Kmlev[9];
$Nimg[8]     = $Kimg[9];
$Nhp[8]      = $Khp[9];
$Nmhp[8]     = $Kmhp[9];
$Nmp[8]      = $Kmp[9];
$Nmmp[8]     = $Kmmp[9];
$Nkou[8]     = $Kkou[9];
$Nmam[8]     = $Kmam[9];
$Nsub[8]     = $Ksub[9];
$Nhai[8]     = $Khai[9];
$Ncount[8]   = $Kcount[9];
$Nnecount[8] = $Knecount[9];
$Nsex[8]     = $Ksex[9];
$Nsei[8]     = $Ksei[9];

$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}
if($KMONS == 9){
$Nlev[9]     = $Klev[10];
$Nmlev[9]    = $Kmlev[10];
$Nimg[9]     = $Kimg[10];
$Nhp[9]      = $Khp[10];
$Nmhp[9]     = $Kmhp[10];
$Nmp[9]      = $Kmp[10];
$Nmmp[9]     = $Kmmp[10];
$Nkou[9]     = $Kkou[10];
$Nmam[9]     = $Kmam[10];
$Nsub[9]     = $Ksub[10];
$Nhai[9]     = $Khai[10];
$Ncount[9]   = $Kcount[10];
$Nnecount[9] = $Knecount[10];
$Nsex[9]     = $Ksex[10];
$Nsei[9]     = $Ksei[10];
}
$newline = "$Kname<>$Kpass<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Nlev[3]<>$Nmlev[3]<>$Nimg[3]<>$Nhp[3]<>$Nmhp[3]<>$Nmp[3]<>$Nmmp[3]<>$Nkou[3]<>$Nmam[3]<>$Nsub[3]<>$Nhai[3]<>$Ncount[3]<>$Nnecount[3]<>$Nsex[3]<>$Nsei[3]<>$Nlev[4]<>$Nmlev[4]<>$Nimg[4]<>$Nhp[4]<>$Nmhp[4]<>$Nmp[4]<>$Nmmp[4]<>$Nkou[4]<>$Nmam[4]<>$Nsub[4]<>$Nhai[4]<>$Ncount[4]<>$Nnecount[4]<>$Nsex[4]<>$Nsei[4]<>$Nlev[5]<>$Nmlev[5]<>$Nimg[5]<>$Nhp[5]<>$Nmhp[5]<>$Nmp[5]<>$Nmmp[5]<>$Nkou[5]<>$Nmam[5]<>$Nsub[5]<>$Nhai[5]<>$Ncount[5]<>$Nnecount[5]<>$Nsex[5]<>$Nsei[5]<>$Nlev[6]<>$Nmlev[6]<>$Nimg[6]<>$Nhp[6]<>$Nmhp[6]<>$Nmp[6]<>$Nmmp[6]<>$Nkou[6]<>$Nmam[6]<>$Nsub[6]<>$Nhai[6]<>$Ncount[6]<>$Nnecount[6]<>$Nsex[6]<>$Nsei[6]<>$Nlev[7]<>$Nmlev[7]<>$Nimg[7]<>$Nhp[7]<>$Nmhp[7]<>$Nmp[7]<>$Nmmp[7]<>$Nkou[7]<>$Nmam[7]<>$Nsub[7]<>$Nhai[7]<>$Ncount[7]<>$Nnecount[7]<>$Nsex[7]<>$Nsei[7]<>$Nlev[8]<>$Nmlev[8]<>$Nimg[8]<>$Nhp[8]<>$Nmhp[8]<>$Nmp[8]<>$Nmmp[8]<>$Nkou[8]<>$Nmam[8]<>$Nsub[8]<>$Nhai[8]<>$Ncount[8]<>$Nnecount[8]<>$Nsex[8]<>$Nsei[8]<>$Nlev[9]<>$Nmlev[9]<>$Nimg[9]<>$Nhp[9]<>$Nmhp[9]<>$Nmp[9]<>$Nmmp[9]<>$Nkou[9]<>$Nmam[9]<>$Nsub[9]<>$Nhai[9]<>$Ncount[9]<>$Nnecount[9]<>$Nsex[9]<>$Nsei[9]<>$Nlev[10]<>$Nmlev[10]<>$Nimg[10]<>$Nhp[10]<>$Nmhp[10]<>$Nmp[10]<>$Nmmp[10]<>$Nkou[10]<>$Nmam[10]<>$Nsub[10]<>$Nhai[10]<>$Ncount[10]<>$Nnecount[10]<>$Nsex[10]<>$Nsei[10]<>$Kdummy<>$Kkey<>$Kmoney";

open(FH, ">${datadir}/$Kname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);

open(FH,"${datadir}/$BBNAME.cgi") || &error("Can't open open3");
@Alines = <FH>;
close(FH);

foreach $Aline (@Alines) {
   ($Aname,$Apass,$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Alev[3],$Amlev[3],$Aimg[3],$Ahp[3],$Amhp[3],$Amp[3],$Ammp[3],$Akou[3],$Amam[3],$Asub[3],$Ahai[3],$Acount[3],$Anecount[3],$Asex[3],$Asei[3],$Alev[4],$Amlev[4],$Aimg[4],$Ahp[4],$Amhp[4],$Amp[4],$Ammp[4],$Akou[4],$Amam[4],$Asub[4],$Ahai[4],$Acount[4],$Anecount[4],$Asex[4],$Asei[4],$Alev[5],$Amlev[5],$Aimg[5],$Ahp[5],$Amhp[5],$Amp[5],$Ammp[5],$Akou[5],$Amam[5],$Asub[5],$Ahai[5],$Acount[5],$Anecount[5],$Asex[5],$Asei[5],$Alev[6],$Amlev[6],$Aimg[6],$Ahp[6],$Amhp[6],$Amp[6],$Ammp[6],$Akou[6],$Amam[6],$Asub[6],$Ahai[6],$Acount[6],$Anecount[6],$Asex[6],$Asei[6],$Alev[7],$Amlev[7],$Aimg[7],$Ahp[7],$Amhp[7],$Amp[7],$Ammp[7],$Akou[7],$Amam[7],$Asub[7],$Ahai[7],$Acount[7],$Anecount[7],$Asex[7],$Asei[7],$Alev[8],$Amlev[8],$Aimg[8],$Ahp[8],$Amhp[8],$Amp[8],$Ammp[8],$Akou[8],$Amam[8],$Asub[8],$Ahai[8],$Acount[8],$Anecount[8],$Asex[8],$Asei[8],$Alev[9],$Amlev[9],$Aimg[9],$Ahp[9],$Amhp[9],$Amp[9],$Ammp[9],$Akou[9],$Amam[9],$Asub[9],$Ahai[9],$Acount[9],$Anecount[9],$Asex[9],$Asei[9],$Alev[10],$Amlev[10],$Aimg[10],$Ahp[10],$Amhp[10],$Amp[10],$Ammp[10],$Akou[10],$Amam[10],$Asub[10],$Ahai[10],$Acount[10],$Anecount[10],$Asex[10],$Asei[10],$Adummy,$Akey,$Amoney) = split(/<>/,$Aline);}

for($B=1;$B<11;$B++){
$Plev[$B]     = $Alev[$B];
$Pmlev[$B]    = $Amlev[$B];
$Pimg[$B]     = $Aimg[$B];
$Php[$B]      = $Ahp[$B];
$Pmhp[$B]     = $Amhp[$B];
$Pmp[$B]      = $Amp[$B];
$Pmmp[$B]     = $Ammp[$B];
$Pkou[$B]     = $Akou[$B];
$Pmam[$B]     = $Amam[$B];
$Psub[$B]     = $Asub[$B];
$Phai[$B]     = $Ahai[$B];
$Pcount[$B]   = $Acount[$B];
$Pnecount[$B] = $Anecount[$B];
$Psex[$B]     = $Asex[$B];
$Psei[$B]     = $Asei[$B];
}

$Tlev[2]     = $Alev[$AMONS];
$Tmlev[2]    = $Amlev[$AMONS];
$Timg[2]     = $Aimg[$AMONS];
$Thp[2]      = $Ahp[$AMONS];
$Tmhp[2]     = $Amhp[$AMONS];
$Tmp[2]      = $Amp[$AMONS];
$Tmmp[2]     = $Ammp[$AMONS];
$Tkou[2]     = $Akou[$AMONS];
$Tmam[2]     = $Amam[$AMONS];
$Tsub[2]     = $Asub[$AMONS];
$Thai[2]     = $Ahai[$AMONS];
$Tcount[2]   = $Acount[$AMONS];
$Tnecount[2] = $Anecount[$AMONS];
$Tsex[2]     = $Asex[$AMONS];
$Tsei[2]     = $Asei[$AMONS];

$Plev[10]     = 0;
$Pmlev[10]    = 0;
$Pimg[10]     = 0;
$Php[10]      = 0;
$Pmhp[10]     = 0;
$Pmp[10]      = 0;
$Pmmp[10]     = 0;
$Pkou[10]     = 0;
$Pmam[10]     = 0;
$Psub[10]     = 0;
$Phai[10]     = 0;
$Pcount[10]   = 0;
$Pnecount[10] = 0;
$Psex[10]     = 0;
$Psei[10]     = 0;

if($AMONS == 1){
$Plev[1]     = $Alev[2];
$Pmlev[1]    = $Amlev[2];
$Pimg[1]     = $Aimg[2];
$Php[1]      = $Ahp[2];
$Pmhp[1]     = $Amhp[2];
$Pmp[1]      = $Amp[2];
$Pmmp[1]     = $Ammp[2];
$Pkou[1]     = $Akou[2];
$Pmam[1]     = $Amam[2];
$Psub[1]     = $Asub[2];
$Phai[1]     = $Ahai[2];
$Pcount[1]   = $Acount[2];
$Pnecount[1] = $Anecount[2];
$Psex[1]     = $Asex[2];
$Psei[1]     = $Asei[2];

$Plev[2]     = $Alev[3];
$Pmlev[2]    = $Amlev[3];
$Pimg[2]     = $Aimg[3];
$Php[2]      = $Ahp[3];
$Pmhp[2]     = $Amhp[3];
$Pmp[2]      = $Amp[3];
$Pmmp[2]     = $Ammp[3];
$Pkou[2]     = $Akou[3];
$Pmam[2]     = $Amam[3];
$Psub[2]     = $Asub[3];
$Phai[2]     = $Ahai[3];
$Pcount[2]   = $Acount[3];
$Pnecount[2] = $Anecount[3];
$Psex[2]     = $Asex[3];
$Psei[2]     = $Asei[3];

$Plev[3]     = $Alev[4];
$Pmlev[3]    = $Amlev[4];
$Pimg[3]     = $Aimg[4];
$Php[3]      = $Ahp[4];
$Pmhp[3]     = $Amhp[4];
$Pmp[3]      = $Amp[4];
$Pmmp[3]     = $Ammp[4];
$Pkou[3]     = $Akou[4];
$Pmam[3]     = $Amam[4];
$Psub[3]     = $Asub[4];
$Phai[3]     = $Ahai[4];
$Pcount[3]   = $Acount[4];
$Pnecount[3] = $Anecount[4];
$Psex[3]     = $Asex[4];
$Psei[3]     = $Asei[4];

$Plev[4]     = $Alev[5];
$Pmlev[4]    = $Amlev[5];
$Pimg[4]     = $Aimg[5];
$Php[4]      = $Ahp[5];
$Pmhp[4]     = $Amhp[5];
$Pmp[4]      = $Amp[5];
$Pmmp[4]     = $Ammp[5];
$Pkou[4]     = $Akou[5];
$Pmam[4]     = $Amam[5];
$Psub[4]     = $Asub[5];
$Phai[4]     = $Ahai[5];
$Pcount[4]   = $Acount[5];
$Pnecount[4] = $Anecount[5];
$Psex[4]     = $Asex[5];
$Psei[4]     = $Asei[5];

$Plev[5]     = $Alev[6];
$Pmlev[5]    = $Amlev[6];
$Pimg[5]     = $Aimg[6];
$Php[5]      = $Ahp[6];
$Pmhp[5]     = $Amhp[6];
$Pmp[5]      = $Amp[6];
$Pmmp[5]     = $Ammp[6];
$Pkou[5]     = $Akou[6];
$Pmam[5]     = $Amam[6];
$Psub[5]     = $Asub[6];
$Phai[5]     = $Ahai[6];
$Pcount[5]   = $Acount[6];
$Pnecount[5] = $Anecount[6];
$Psex[5]     = $Asex[6];
$Psei[5]     = $Asei[6];

$Plev[6]     = $Alev[7];
$Pmlev[6]    = $Amlev[7];
$Pimg[6]     = $Aimg[7];
$Php[6]      = $Ahp[7];
$Pmhp[6]     = $Amhp[7];
$Pmp[6]      = $Amp[7];
$Pmmp[6]     = $Ammp[7];
$Pkou[6]     = $Akou[7];
$Pmam[6]     = $Amam[7];
$Psub[6]     = $Asub[7];
$Phai[6]     = $Ahai[7];
$Pcount[6]   = $Acount[7];
$Pnecount[6] = $Anecount[7];
$Psex[6]     = $Asex[7];
$Psei[6]     = $Asei[7];

$Plev[7]     = $Alev[8];
$Pmlev[7]    = $Amlev[8];
$Pimg[7]     = $Aimg[8];
$Php[7]      = $Ahp[8];
$Pmhp[7]     = $Amhp[8];
$Pmp[7]      = $Amp[8];
$Pmmp[7]     = $Ammp[8];
$Pkou[7]     = $Akou[8];
$Pmam[7]     = $Amam[8];
$Psub[7]     = $Asub[8];
$Phai[7]     = $Ahai[8];
$Pcount[7]   = $Acount[8];
$Pnecount[7] = $Anecount[8];
$Psex[7]     = $Asex[8];
$Psei[7]     = $Asei[8];

$Plev[8]     = $Alev[9];
$Pmlev[8]    = $Amlev[9];
$Pimg[8]     = $Aimg[9];
$Php[8]      = $Ahp[9];
$Pmhp[8]     = $Amhp[9];
$Pmp[8]      = $Amp[9];
$Pmmp[8]     = $Ammp[9];
$Pkou[8]     = $Akou[9];
$Pmam[8]     = $Amam[9];
$Psub[8]     = $Asub[9];
$Phai[8]     = $Ahai[9];
$Pcount[8]   = $Acount[9];
$Pnecount[8] = $Anecount[9];
$Psex[8]     = $Asex[9];
$Psei[8]     = $Asei[9];

$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}

if($AMONS == 2){
$Plev[2]     = $Alev[3];
$Pmlev[2]    = $Amlev[3];
$Pimg[2]     = $Aimg[3];
$Php[2]      = $Ahp[3];
$Pmhp[2]     = $Amhp[3];
$Pmp[2]      = $Amp[3];
$Pmmp[2]     = $Ammp[3];
$Pkou[2]     = $Akou[3];
$Pmam[2]     = $Amam[3];
$Psub[2]     = $Asub[3];
$Phai[2]     = $Ahai[3];
$Pcount[2]   = $Acount[3];
$Pnecount[2] = $Anecount[3];
$Psex[2]     = $Asex[3];
$Psei[2]     = $Asei[3];

$Plev[3]     = $Alev[4];
$Pmlev[3]    = $Amlev[4];
$Pimg[3]     = $Aimg[4];
$Php[3]      = $Ahp[4];
$Pmhp[3]     = $Amhp[4];
$Pmp[3]      = $Amp[4];
$Pmmp[3]     = $Ammp[4];
$Pkou[3]     = $Akou[4];
$Pmam[3]     = $Amam[4];
$Psub[3]     = $Asub[4];
$Phai[3]     = $Ahai[4];
$Pcount[3]   = $Acount[4];
$Pnecount[3] = $Anecount[4];
$Psex[3]     = $Asex[4];
$Psei[3]     = $Asei[4];

$Plev[4]     = $Alev[5];
$Pmlev[4]    = $Amlev[5];
$Pimg[4]     = $Aimg[5];
$Php[4]      = $Ahp[5];
$Pmhp[4]     = $Amhp[5];
$Pmp[4]      = $Amp[5];
$Pmmp[4]     = $Ammp[5];
$Pkou[4]     = $Akou[5];
$Pmam[4]     = $Amam[5];
$Psub[4]     = $Asub[5];
$Phai[4]     = $Ahai[5];
$Pcount[4]   = $Acount[5];
$Pnecount[4] = $Anecount[5];
$Psex[4]     = $Asex[5];
$Psei[4]     = $Asei[5];

$Plev[5]     = $Alev[6];
$Pmlev[5]    = $Amlev[6];
$Pimg[5]     = $Aimg[6];
$Php[5]      = $Ahp[6];
$Pmhp[5]     = $Amhp[6];
$Pmp[5]      = $Amp[6];
$Pmmp[5]     = $Ammp[6];
$Pkou[5]     = $Akou[6];
$Pmam[5]     = $Amam[6];
$Psub[5]     = $Asub[6];
$Phai[5]     = $Ahai[6];
$Pcount[5]   = $Acount[6];
$Pnecount[5] = $Anecount[6];
$Psex[5]     = $Asex[6];
$Psei[5]     = $Asei[6];

$Plev[6]     = $Alev[7];
$Pmlev[6]    = $Amlev[7];
$Pimg[6]     = $Aimg[7];
$Php[6]      = $Ahp[7];
$Pmhp[6]     = $Amhp[7];
$Pmp[6]      = $Amp[7];
$Pmmp[6]     = $Ammp[7];
$Pkou[6]     = $Akou[7];
$Pmam[6]     = $Amam[7];
$Psub[6]     = $Asub[7];
$Phai[6]     = $Ahai[7];
$Pcount[6]   = $Acount[7];
$Pnecount[6] = $Anecount[7];
$Psex[6]     = $Asex[7];
$Psei[6]     = $Asei[7];

$Plev[7]     = $Alev[8];
$Pmlev[7]    = $Amlev[8];
$Pimg[7]     = $Aimg[8];
$Php[7]      = $Ahp[8];
$Pmhp[7]     = $Amhp[8];
$Pmp[7]      = $Amp[8];
$Pmmp[7]     = $Ammp[8];
$Pkou[7]     = $Akou[8];
$Pmam[7]     = $Amam[8];
$Psub[7]     = $Asub[8];
$Phai[7]     = $Ahai[8];
$Pcount[7]   = $Acount[8];
$Pnecount[7] = $Anecount[8];
$Psex[7]     = $Asex[8];
$Psei[7]     = $Asei[8];

$Plev[8]     = $Alev[9];
$Pmlev[8]    = $Amlev[9];
$Pimg[8]     = $Aimg[9];
$Php[8]      = $Ahp[9];
$Pmhp[8]     = $Amhp[9];
$Pmp[8]      = $Amp[9];
$Pmmp[8]     = $Ammp[9];
$Pkou[8]     = $Akou[9];
$Pmam[8]     = $Amam[9];
$Psub[8]     = $Asub[9];
$Phai[8]     = $Ahai[9];
$Pcount[8]   = $Acount[9];
$Pnecount[8] = $Anecount[9];
$Psex[8]     = $Asex[9];
$Psei[8]     = $Asei[9];

$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}
if($AMONS == 3){
$Plev[3]     = $Alev[4];
$Pmlev[3]    = $Amlev[4];
$Pimg[3]     = $Aimg[4];
$Php[3]      = $Ahp[4];
$Pmhp[3]     = $Amhp[4];
$Pmp[3]      = $Amp[4];
$Pmmp[3]     = $Ammp[4];
$Pkou[3]     = $Akou[4];
$Pmam[3]     = $Amam[4];
$Psub[3]     = $Asub[4];
$Phai[3]     = $Ahai[4];
$Pcount[3]   = $Acount[4];
$Pnecount[3] = $Anecount[4];
$Psex[3]     = $Asex[4];
$Psei[3]     = $Asei[4];

$Plev[4]     = $Alev[5];
$Pmlev[4]    = $Amlev[5];
$Pimg[4]     = $Aimg[5];
$Php[4]      = $Ahp[5];
$Pmhp[4]     = $Amhp[5];
$Pmp[4]      = $Amp[5];
$Pmmp[4]     = $Ammp[5];
$Pkou[4]     = $Akou[5];
$Pmam[4]     = $Amam[5];
$Psub[4]     = $Asub[5];
$Phai[4]     = $Ahai[5];
$Pcount[4]   = $Acount[5];
$Pnecount[4] = $Anecount[5];
$Psex[4]     = $Asex[5];
$Psei[4]     = $Asei[5];

$Plev[5]     = $Alev[6];
$Pmlev[5]    = $Amlev[6];
$Pimg[5]     = $Aimg[6];
$Php[5]      = $Ahp[6];
$Pmhp[5]     = $Amhp[6];
$Pmp[5]      = $Amp[6];
$Pmmp[5]     = $Ammp[6];
$Pkou[5]     = $Akou[6];
$Pmam[5]     = $Amam[6];
$Psub[5]     = $Asub[6];
$Phai[5]     = $Ahai[6];
$Pcount[5]   = $Acount[6];
$Pnecount[5] = $Anecount[6];
$Psex[5]     = $Asex[6];
$Psei[5]     = $Asei[6];

$Plev[6]     = $Alev[7];
$Pmlev[6]    = $Amlev[7];
$Pimg[6]     = $Aimg[7];
$Php[6]      = $Ahp[7];
$Pmhp[6]     = $Amhp[7];
$Pmp[6]      = $Amp[7];
$Pmmp[6]     = $Ammp[7];
$Pkou[6]     = $Akou[7];
$Pmam[6]     = $Amam[7];
$Psub[6]     = $Asub[7];
$Phai[6]     = $Ahai[7];
$Pcount[6]   = $Acount[7];
$Pnecount[6] = $Anecount[7];
$Psex[6]     = $Asex[7];
$Psei[6]     = $Asei[7];

$Plev[7]     = $Alev[8];
$Pmlev[7]    = $Amlev[8];
$Pimg[7]     = $Aimg[8];
$Php[7]      = $Ahp[8];
$Pmhp[7]     = $Amhp[8];
$Pmp[7]      = $Amp[8];
$Pmmp[7]     = $Ammp[8];
$Pkou[7]     = $Akou[8];
$Pmam[7]     = $Amam[8];
$Psub[7]     = $Asub[8];
$Phai[7]     = $Ahai[8];
$Pcount[7]   = $Acount[8];
$Pnecount[7] = $Anecount[8];
$Psex[7]     = $Asex[8];
$Psei[7]     = $Asei[8];

$Plev[8]     = $Alev[9];
$Pmlev[8]    = $Amlev[9];
$Pimg[8]     = $Aimg[9];
$Php[8]      = $Ahp[9];
$Pmhp[8]     = $Amhp[9];
$Pmp[8]      = $Amp[9];
$Pmmp[8]     = $Ammp[9];
$Pkou[8]     = $Akou[9];
$Pmam[8]     = $Amam[9];
$Psub[8]     = $Asub[9];
$Phai[8]     = $Ahai[9];
$Pcount[8]   = $Acount[9];
$Pnecount[8] = $Anecount[9];
$Psex[8]     = $Asex[9];
$Psei[8]     = $Asei[9];

$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}
if($AMONS == 4){
$Plev[4]     = $Alev[5];
$Pmlev[4]    = $Amlev[5];
$Pimg[4]     = $Aimg[5];
$Php[4]      = $Ahp[5];
$Pmhp[4]     = $Amhp[5];
$Pmp[4]      = $Amp[5];
$Pmmp[4]     = $Ammp[5];
$Pkou[4]     = $Akou[5];
$Pmam[4]     = $Amam[5];
$Psub[4]     = $Asub[5];
$Phai[4]     = $Ahai[5];
$Pcount[4]   = $Acount[5];
$Pnecount[4] = $Anecount[5];
$Psex[4]     = $Asex[5];
$Psei[4]     = $Asei[5];

$Plev[5]     = $Alev[6];
$Pmlev[5]    = $Amlev[6];
$Pimg[5]     = $Aimg[6];
$Php[5]      = $Ahp[6];
$Pmhp[5]     = $Amhp[6];
$Pmp[5]      = $Amp[6];
$Pmmp[5]     = $Ammp[6];
$Pkou[5]     = $Akou[6];
$Pmam[5]     = $Amam[6];
$Psub[5]     = $Asub[6];
$Phai[5]     = $Ahai[6];
$Pcount[5]   = $Acount[6];
$Pnecount[5] = $Anecount[6];
$Psex[5]     = $Asex[6];
$Psei[5]     = $Asei[6];

$Plev[6]     = $Alev[7];
$Pmlev[6]    = $Amlev[7];
$Pimg[6]     = $Aimg[7];
$Php[6]      = $Ahp[7];
$Pmhp[6]     = $Amhp[7];
$Pmp[6]      = $Amp[7];
$Pmmp[6]     = $Ammp[7];
$Pkou[6]     = $Akou[7];
$Pmam[6]     = $Amam[7];
$Psub[6]     = $Asub[7];
$Phai[6]     = $Ahai[7];
$Pcount[6]   = $Acount[7];
$Pnecount[6] = $Anecount[7];
$Psex[6]     = $Asex[7];
$Psei[6]     = $Asei[7];

$Plev[7]     = $Alev[8];
$Pmlev[7]    = $Amlev[8];
$Pimg[7]     = $Aimg[8];
$Php[7]      = $Ahp[8];
$Pmhp[7]     = $Amhp[8];
$Pmp[7]      = $Amp[8];
$Pmmp[7]     = $Ammp[8];
$Pkou[7]     = $Akou[8];
$Pmam[7]     = $Amam[8];
$Psub[7]     = $Asub[8];
$Phai[7]     = $Ahai[8];
$Pcount[7]   = $Acount[8];
$Pnecount[7] = $Anecount[8];
$Psex[7]     = $Asex[8];
$Psei[7]     = $Asei[8];

$Plev[8]     = $Alev[9];
$Pmlev[8]    = $Amlev[9];
$Pimg[8]     = $Aimg[9];
$Php[8]      = $Ahp[9];
$Pmhp[8]     = $Amhp[9];
$Pmp[8]      = $Amp[9];
$Pmmp[8]     = $Ammp[9];
$Pkou[8]     = $Akou[9];
$Pmam[8]     = $Amam[9];
$Psub[8]     = $Asub[9];
$Phai[8]     = $Ahai[9];
$Pcount[8]   = $Acount[9];
$Pnecount[8] = $Anecount[9];
$Psex[8]     = $Asex[9];
$Psei[8]     = $Asei[9];

$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}
if($AMONS == 5){
$Plev[5]     = $Alev[6];
$Pmlev[5]    = $Amlev[6];
$Pimg[5]     = $Aimg[6];
$Php[5]      = $Ahp[6];
$Pmhp[5]     = $Amhp[6];
$Pmp[5]      = $Amp[6];
$Pmmp[5]     = $Ammp[6];
$Pkou[5]     = $Akou[6];
$Pmam[5]     = $Amam[6];
$Psub[5]     = $Asub[6];
$Phai[5]     = $Ahai[6];
$Pcount[5]   = $Acount[6];
$Pnecount[5] = $Anecount[6];
$Psex[5]     = $Asex[6];
$Psei[5]     = $Asei[6];

$Plev[6]     = $Alev[7];
$Pmlev[6]    = $Amlev[7];
$Pimg[6]     = $Aimg[7];
$Php[6]      = $Ahp[7];
$Pmhp[6]     = $Amhp[7];
$Pmp[6]      = $Amp[7];
$Pmmp[6]     = $Ammp[7];
$Pkou[6]     = $Akou[7];
$Pmam[6]     = $Amam[7];
$Psub[6]     = $Asub[7];
$Phai[6]     = $Ahai[7];
$Pcount[6]   = $Acount[7];
$Pnecount[6] = $Anecount[7];
$Psex[6]     = $Asex[7];
$Psei[6]     = $Asei[7];

$Plev[7]     = $Alev[8];
$Pmlev[7]    = $Amlev[8];
$Pimg[7]     = $Aimg[8];
$Php[7]      = $Ahp[8];
$Pmhp[7]     = $Amhp[8];
$Pmp[7]      = $Amp[8];
$Pmmp[7]     = $Ammp[8];
$Pkou[7]     = $Akou[8];
$Pmam[7]     = $Amam[8];
$Psub[7]     = $Asub[8];
$Phai[7]     = $Ahai[8];
$Pcount[7]   = $Acount[8];
$Pnecount[7] = $Anecount[8];
$Psex[7]     = $Asex[8];
$Psei[7]     = $Asei[8];

$Plev[8]     = $Alev[9];
$Pmlev[8]    = $Amlev[9];
$Pimg[8]     = $Aimg[9];
$Php[8]      = $Ahp[9];
$Pmhp[8]     = $Amhp[9];
$Pmp[8]      = $Amp[9];
$Pmmp[8]     = $Ammp[9];
$Pkou[8]     = $Akou[9];
$Pmam[8]     = $Amam[9];
$Psub[8]     = $Asub[9];
$Phai[8]     = $Ahai[9];
$Pcount[8]   = $Acount[9];
$Pnecount[8] = $Anecount[9];
$Psex[8]     = $Asex[9];
$Psei[8]     = $Asei[9];

$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}
if($AMONS == 6){
$Plev[6]     = $Alev[7];
$Pmlev[6]    = $Amlev[7];
$Pimg[6]     = $Aimg[7];
$Php[6]      = $Ahp[7];
$Pmhp[6]     = $Amhp[7];
$Pmp[6]      = $Amp[7];
$Pmmp[6]     = $Ammp[7];
$Pkou[6]     = $Akou[7];
$Pmam[6]     = $Amam[7];
$Psub[6]     = $Asub[7];
$Phai[6]     = $Ahai[7];
$Pcount[6]   = $Acount[7];
$Pnecount[6] = $Anecount[7];
$Psex[6]     = $Asex[7];
$Psei[6]     = $Asei[7];

$Plev[7]     = $Alev[8];
$Pmlev[7]    = $Amlev[8];
$Pimg[7]     = $Aimg[8];
$Php[7]      = $Ahp[8];
$Pmhp[7]     = $Amhp[8];
$Pmp[7]      = $Amp[8];
$Pmmp[7]     = $Ammp[8];
$Pkou[7]     = $Akou[8];
$Pmam[7]     = $Amam[8];
$Psub[7]     = $Asub[8];
$Phai[7]     = $Ahai[8];
$Pcount[7]   = $Acount[8];
$Pnecount[7] = $Anecount[8];
$Psex[7]     = $Asex[8];
$Psei[7]     = $Asei[8];

$Plev[8]     = $Alev[9];
$Pmlev[8]    = $Amlev[9];
$Pimg[8]     = $Aimg[9];
$Php[8]      = $Ahp[9];
$Pmhp[8]     = $Amhp[9];
$Pmp[8]      = $Amp[9];
$Pmmp[8]     = $Ammp[9];
$Pkou[8]     = $Akou[9];
$Pmam[8]     = $Amam[9];
$Psub[8]     = $Asub[9];
$Phai[8]     = $Ahai[9];
$Pcount[8]   = $Acount[9];
$Pnecount[8] = $Anecount[9];
$Psex[8]     = $Asex[9];
$Psei[8]     = $Asei[9];

$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}
if($AMONS == 7){
$Plev[7]     = $Alev[8];
$Pmlev[7]    = $Amlev[8];
$Pimg[7]     = $Aimg[8];
$Php[7]      = $Ahp[8];
$Pmhp[7]     = $Amhp[8];
$Pmp[7]      = $Amp[8];
$Pmmp[7]     = $Ammp[8];
$Pkou[7]     = $Akou[8];
$Pmam[7]     = $Amam[8];
$Psub[7]     = $Asub[8];
$Phai[7]     = $Ahai[8];
$Pcount[7]   = $Acount[8];
$Pnecount[7] = $Anecount[8];
$Psex[7]     = $Asex[8];
$Psei[7]     = $Asei[8];

$Plev[8]     = $Alev[9];
$Pmlev[8]    = $Amlev[9];
$Pimg[8]     = $Aimg[9];
$Php[8]      = $Ahp[9];
$Pmhp[8]     = $Amhp[9];
$Pmp[8]      = $Amp[9];
$Pmmp[8]     = $Ammp[9];
$Pkou[8]     = $Akou[9];
$Pmam[8]     = $Amam[9];
$Psub[8]     = $Asub[9];
$Phai[8]     = $Ahai[9];
$Pcount[8]   = $Acount[9];
$Pnecount[8] = $Anecount[9];
$Psex[8]     = $Asex[9];
$Psei[8]     = $Asei[9];

$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}
if($AMONS == 8){
$Plev[8]     = $Alev[9];
$Pmlev[8]    = $Amlev[9];
$Pimg[8]     = $Aimg[9];
$Php[8]      = $Ahp[9];
$Pmhp[8]     = $Amhp[9];
$Pmp[8]      = $Amp[9];
$Pmmp[8]     = $Ammp[9];
$Pkou[8]     = $Akou[9];
$Pmam[8]     = $Amam[9];
$Psub[8]     = $Asub[9];
$Phai[8]     = $Ahai[9];
$Pcount[8]   = $Acount[9];
$Pnecount[8] = $Anecount[9];
$Psex[8]     = $Asex[9];
$Psei[8]     = $Asei[9];

$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}
if($AMONS == 9){
$Plev[9]     = $Alev[10];
$Pmlev[9]    = $Amlev[10];
$Pimg[9]     = $Aimg[10];
$Php[9]      = $Ahp[10];
$Pmhp[9]     = $Amhp[10];
$Pmp[9]      = $Amp[10];
$Pmmp[9]     = $Ammp[10];
$Pkou[9]     = $Akou[10];
$Pmam[9]     = $Amam[10];
$Psub[9]     = $Asub[10];
$Phai[9]     = $Ahai[10];
$Pcount[9]   = $Acount[10];
$Pnecount[9] = $Anecount[10];
$Psex[9]     = $Asex[10];
$Psei[9]     = $Asei[10];
}
$newline = "$Aname<>$Apass<>$Plev[1]<>$Pmlev[1]<>$Pimg[1]<>$Php[1]<>$Pmhp[1]<>$Pmp[1]<>$Pmmp[1]<>$Pkou[1]<>$Pmam[1]<>$Psub[1]<>$Phai[1]<>$Pcount[1]<>$Pnecount[1]<>$Psex[1]<>$Psei[1]<>$Plev[2]<>$Pmlev[2]<>$Pimg[2]<>$Php[2]<>$Pmhp[2]<>$Pmp[2]<>$Pmmp[2]<>$Pkou[2]<>$Pmam[2]<>$Psub[2]<>$Phai[2]<>$Pcount[2]<>$Pnecount[2]<>$Psex[2]<>$Psei[2]<>$Plev[3]<>$Pmlev[3]<>$Pimg[3]<>$Php[3]<>$Pmhp[3]<>$Pmp[3]<>$Pmmp[3]<>$Pkou[3]<>$Pmam[3]<>$Psub[3]<>$Phai[3]<>$Pcount[3]<>$Pnecount[3]<>$Psex[3]<>$Psei[3]<>$Plev[4]<>$Pmlev[4]<>$Pimg[4]<>$Php[4]<>$Pmhp[4]<>$Pmp[4]<>$Pmmp[4]<>$Pkou[4]<>$Pmam[4]<>$Psub[4]<>$Phai[4]<>$Pcount[4]<>$Pnecount[4]<>$Psex[4]<>$Psei[4]<>$Plev[5]<>$Pmlev[5]<>$Pimg[5]<>$Php[5]<>$Pmhp[5]<>$Pmp[5]<>$Pmmp[5]<>$Pkou[5]<>$Pmam[5]<>$Psub[5]<>$Phai[5]<>$Pcount[5]<>$Pnecount[5]<>$Psex[5]<>$Psei[5]<>$Plev[6]<>$Pmlev[6]<>$Pimg[6]<>$Php[6]<>$Pmhp[6]<>$Pmp[6]<>$Pmmp[6]<>$Pkou[6]<>$Pmam[6]<>$Psub[6]<>$Phai[6]<>$Pcount[6]<>$Pnecount[6]<>$Psex[6]<>$Psei[6]<>$Plev[7]<>$Pmlev[7]<>$Pimg[7]<>$Php[7]<>$Pmhp[7]<>$Pmp[7]<>$Pmmp[7]<>$Pkou[7]<>$Pmam[7]<>$Psub[7]<>$Phai[7]<>$Pcount[7]<>$Pnecount[7]<>$Psex[7]<>$Psei[7]<>$Plev[8]<>$Pmlev[8]<>$Pimg[8]<>$Php[8]<>$Pmhp[8]<>$Pmp[8]<>$Pmmp[8]<>$Pkou[8]<>$Pmam[8]<>$Psub[8]<>$Phai[8]<>$Pcount[8]<>$Pnecount[8]<>$Psex[8]<>$Psei[8]<>$Plev[9]<>$Pmlev[9]<>$Pimg[9]<>$Php[9]<>$Pmhp[9]<>$Pmp[9]<>$Pmmp[9]<>$Pkou[9]<>$Pmam[9]<>$Psub[9]<>$Phai[9]<>$Pcount[9]<>$Pnecount[9]<>$Psex[9]<>$Psei[9]<>$Plev[10]<>$Pmlev[10]<>$Pimg[10]<>$Php[10]<>$Pmhp[10]<>$Pmp[10]<>$Pmmp[10]<>$Pkou[10]<>$Pmam[10]<>$Psub[10]<>$Phai[10]<>$Pcount[10]<>$Pnecount[10]<>$Psex[10]<>$Psei[10]<>$Adummy<>$Akey<>$Amoney";

&lock;

open(FH, ">${datadir}/$BBNAME.cgi") || &error("Can't open ");
print FH $newline;
close(FH);

open(FH,"omiai/$BBNAME.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);}

$newline = "$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>$Tlev[2]<>$Tmlev[2]<>$Timg[2]<>$Thp[2]<>$Tmhp[2]<>$Tmp[2]<>$Tmmp[2]<>$Tkou[2]<>$Tmam[2]<>$Tsub[2]<>$Thai[2]<>$Tcount[2]<>$Tnecount[2]<>$Tsex[2]<>$Tsei[2]<>$Aname[1]<>$Alev[1]<>$Amlev[1]<>$Aimg[1]<>$Ahp[1]<>$Amhp[1]<>$Amp[1]<>$Ammp[1]<>$Akou[1]<>$Amam[1]<>$Asub[1]<>$Ahai[1]<>$Acount[1]<>$Anecount[1]<>$Asex[1]<>$Asei[1]<>$inname<>$Slev[1]<>$Smlev[1]<>$Simg[1]<>$Shp[1]<>$Smhp[1]<>$Smp[1]<>$Smmp[1]<>$Skou[1]<>$Smam[1]<>$Ssub[1]<>$Shai[1]<>$Scount[1]<>$Snecount[1]<>$Ssex[1]<>$Ssei[1]<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[1]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";

open(FH, ">omiai/$BBNAME.cgi") || &error("Can't open ");
print FH $newline;
close(FH);

open(FH,"omiai/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);}

$newline = "$Slev[1]<>$Smlev[1]<>$Simg[1]<>$Shp[1]<>$Smhp[1]<>$Smp[1]<>$Smmp[1]<>$Skou[1]<>$Smam[1]<>$Ssub[1]<>$Shai[1]<>$Scount[1]<>$Snecount[1]<>$Ssex[1]<>$Ssei[1]<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>$BBNAME<>$Tlev[2]<>$Tmlev[2]<>$Timg[2]<>$Thp[2]<>$Tmhp[2]<>$Tmp[2]<>$Tmmp[2]<>$Tkou[2]<>$Tmam[2]<>$Tsub[2]<>$Thai[2]<>$Tcount[2]<>$Tnecount[2]<>$Tsex[2]<>$Tsei[2]<>$Aname[2]<>$Alev[2]<>$Amlev[2]<>$Aimg[2]<>$Ahp[2]<>$Amhp[2]<>$Amp[2]<>$Ammp[2]<>$Akou[2]<>$Amam[2]<>$Asub[2]<>$Ahai[2]<>$Acount[2]<>$Anecount[2]<>$Asex[2]<>$Asei[2]<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[1]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";

open(FH, ">omiai/$inname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
&unlock;

&header;
print <<"EOF";
<CENTER>
<TABLE border="0" bgcolor="#000000">
<TBODY>
<TR>
<TD width="600" height="70" align="center">
<HR>
<FONT size="5pt" color="#0000FF"><B>お見合い設定が完了しました</B>
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

