use utf8;
use open IO => ":utf8";
use open ":std";

$inname=$FORM{'name'};
$inpass=$FORM{'password'};

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

if($Nimg[1] != 0 && $Nimg[2] != 0){&error("誕生モンスターがLOGIN画面に戻るまでお見合いが出来ません");}
if($Kimg[2] == 0){&error("現在お見合いは申\し込まれていません");}
$Vname = $Aname[2];

open(FH,"omiai/$Vname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);
}

if($Nimg[1] != 0 && $Nimg[2] != 0){&error("$Vnameさんの誕生モンスターがLOGIN画面に戻るまでお見合いが出来ません");}
if($Kimg[1] == 0){&error("現在お見合いは申\し込まれていません");}

open(FH,"dat/omiai.cgi");
@lines = <FH>;
close(FH);

$omi = 0;

foreach $line (@lines) {
   ($sei1,$sei2,$omiok,$dummy) = split(/<>/,$line);
   if($Ksei[1] == $sei1 && $Asei[1] == $sei2){$omi = 1;last;}
}

if($omi == 0){
@omiai = (0,0,0,0,2);
$omi = $omiai[int(rand(5))];
}

$list3 = $Kimg[1];
$list4 = $Aimg[1];

if($list3 == 1 && $list4 == 1)                                     {$newname = 1;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 91 && $list4 <= 110)  {$newname = 2;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 71 && $list4 <= 90)   {$newname = 3;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 111 && $list4 <= 130) {$newname = 4;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 156 && $list4 <= 175) {$newname = 5;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 131 && $list4 <= 155) {$newname = 6;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 46 && $list4 <= 70)   {$newname = 7;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 176 && $list4 <= 200) {$newname = 8;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 21 && $list4 <= 45)   {$newname = 9;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 1 && $list4 <= 20)   {$newname = 21;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 91 && $list4 <= 110) {$newname = 22;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 71 && $list4 <= 90)  {$newname = 23;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 111 && $list4 <= 130){$newname = 24;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 156 && $list4 <= 175){$newname = 25;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 131 && $list4 <= 155){$newname = 26;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 46 && $list4 <= 70)  {$newname = 27;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 176 && $list4 <= 200){$newname = 28;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 1 && $list4 <= 20)   {$newname = 46;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 91 && $list4 <= 110) {$newname = 47;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 71 && $list4 <= 90)  {$newname = 48;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 111 && $list4 <= 130){$newname = 49;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 156 && $list4 <= 175){$newname = 50;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 175 && $list4 <= 194){$newname = 51;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 21 && $list4 <= 45)  {$newname = 52;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 201 && $list4 <= 215){$newname = 70;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 1 && $list4 <= 20)   {$newname = 71;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 91 && $list4 <= 110) {$newname = 72;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 111 && $list4 <= 130){$newname = 73;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 156 && $list4 <= 175){$newname = 74;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 131 && $list4 <= 155){$newname = 75;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 46 && $list4 <= 70)  {$newname = 76;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 1 && $list4 <= 20)  {$newname = 91;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 71 && $list4 <= 90) {$newname = 92;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 111 && $list4 <= 130){$newname = 93;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 156 && $list4 <= 175){$newname = 94;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 131 && $list4 <= 155){$newname = 95;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 46 && $list4 <= 70)  {$newname = 96;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 176 && $list4 <= 200){$newname = 97;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 21 && $list4 <= 45)  {$newname = 98;}
if($list3 == 97 &&  $list4 >= 46  && $list4 <= 70)                  {$newname = 99;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 118)                 {$newname = 100;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 176)                 {$newname = 101;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 131)                 {$newname = 102;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 166)                 {$newname = 103;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 85)                  {$newname = 104;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 47)                  {$newname = 105;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 132)                 {$newname = 106;}
if($list3 == 106 && $list4 == 106)                                  {$newname = 107;}
if($list3 == 107 && $list4 == 107)                                  {$newname = 108;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 201 && $list4 <= 215){$newname = 109;}
if($list3 == 110 && $list4 == 110)                                  {$newname = 110;}
if($list3 == 111 && $list4 == 111)                                  {$newname = 111;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 1 && $list4 <= 20)  {$newname = 112;}
if($list3 == 112 && $list4 >= 1 && $list4 <= 20)                    {$newname = 113;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 91 && $list4 <= 110){$newname = 114;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 71 && $list4 <= 90) {$newname = 115;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 156 && $list4 <= 175){$newname = 116;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 131 && $list4 <= 155){$newname = 117;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 46 && $list4 <= 70)  {$newname = 118;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 176 && $list4 <= 200){$newname = 119;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 21 && $list4 <= 45)  {$newname = 120;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 96)                  {$newname = 121;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 61)                  {$newname = 122;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 97)                  {$newname = 123;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 49)                  {$newname = 124;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 156)                 {$newname = 125;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 159)                 {$newname = 126;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 56)                  {$newname = 127;}
if($list3 == 119 &&  $list4 == 119)                                  {$newname = 128;}
if($list3 == 128 &&  $list4 == 128)                                  {$newname = 129;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 201 && $list4 <= 215){$newname = 130;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 1 && $list4 <= 20)   {$newname = 131;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 91 && $list4 <= 110) {$newname = 132;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 71 && $list4 <= 90)  {$newname = 133;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 111 && $list4 <= 130){$newname = 134;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 156 && $list4 <= 175){$newname = 135;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 46 && $list4 <= 70)  {$newname = 136;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 176 && $list4 <= 200){$newname = 137;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 21 && $list4 <= 38)  {$newname = 138;}
if($list3 == 131 &&  $list4 >= 1 && $list4 <= 20)                    {$newname = 139;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 105)                 {$newname = 140;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 54)                  {$newname = 141;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 70)                  {$newname = 142;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 26)                  {$newname = 143;}
if($list3 >= 131 &&  $list3 <= 155 && ($list4 == 16 or $list4 == 17 or $list4 == 19)){$newname = 144;}
if($list3 == 133 && $list4 == 133)                                   {$newname = 145;}
if($list3 == 139 && $list4 == 139)                                   {$newname = 146;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 36)                  {$newname = 147;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 39 && $list4 <= 45)  {$newname = 148;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 184)                 {$newname = 149;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 67)                  {$newname = 150;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 122)                 {$newname = 151;}
if($list3 == 145 && $list4 >= 46 && $list4 <= 70)                    {$newname = 152;}
if($list3 == 154 && $list4 == 90)                                    {$newname = 153;}
if($list3 == 147 && $list4 == 147)                                   {$newname = 154;}
if($list3 == 152 && $list4 == 200)                                   {$newname = 155;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 1 && $list4 <= 20)   {$newname = 156;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 91 && $list4 <= 110) {$newname = 157;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 71 && $list4 <= 90)  {$newname = 158;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 111 && $list4 <= 130){$newname = 159;}
if($list3 == 156 && $list4 >= 46 && $list4 <= 70)                    {$newname = 160;}
if($list3 >= 157 &&  $list3 <= 175 && $list4 >= 46 && $list4 <= 70)  {$newname = 161;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 131 && $list4 <= 155){$newname = 162;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 21 && $list4 <= 45)  {$newname = 163;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 176 && $list4 <= 200){$newname = 164;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 112)                 {$newname = 165;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 79)                  {$newname = 166;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 51)                  {$newname = 167;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 28)                  {$newname = 168;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 114)                 {$newname = 169;}
if($list3 == 162 &&  $list4 == 162)                                  {$newname = 170;}
if($list3 == 160 &&  $list4 == 160)                                  {$newname = 171;}
if($list3 == 172 &&  $list4 == 172)                                  {$newname = 172;}
if($list3 == 171 &&  $list4 == 171)                                  {$newname = 173;}
if($list3 == 173 &&  $list4 == 173)                                  {$newname = 174;}
if($list3 == 171 &&  $list4 == 32)                                   {$newname = 175;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 91 && $list4 <= 110) {$newname = 176;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 1 && $list4 <= 20)   {$newname = 177;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 71 && $list4 <= 90)  {$newname = 178;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 111 && $list4 <= 130){$newname = 179;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 131 && $list4 <= 155){$newname = 180;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 46 && $list4 <= 70)  {$newname = 181;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 21 && $list4 <= 45)  {$newname = 182;}
if($list3 == 177 && $list4 >= 1 && $list4 <= 20)                     {$newname = 183;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 156 && $list4 <= 175){$newname = 184;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 116)                 {$newname = 185;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 117)                 {$newname = 186;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 92)                  {$newname = 187;}
if($list3 == 183 &&  $list4 == 98)                                   {$newname = 188;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 4)                   {$newname = 189;}
if($list3 == 183 &&  $list4 == 183)                                  {$newname = 190;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 8)                   {$newname = 191;}
if($list3 == 190 &&  $list4 == 190)                                  {$newname = 192;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 192)                 {$newname = 194;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 135)                 {$newname = 195;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 32)                  {$newname = 196;}
if($list3 == 196 &&  $list4 == 144)                                  {$newname = 197;}
if($list3 == 195 &&  $list4 == 69)                                   {$newname = 198;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 201 && $list4 <= 215){$newname = 199;}
if($list3 == 198 &&  $list4 == 197)                                  {$newname = 200;}
if($list3 == 174 &&  $list4 == 40)                                   {$newname = 201;}
if($list3 == 174 &&  $list4 == 32)                                   {$newname = 201;}
if($list3 == 201 &&  $list4 == 45)                                   {$newname = 202;}
if($list3 == 175 &&  $list4 == 19)                                   {$newname = 203;}
if($list3 == 153 &&  $list4 == 109)                                  {$newname = 204;}
if($list3 == 203 &&  $list4 == 44)                                   {$newname = 205;}
if($list3 == 201 &&  $list4 == 204)                                  {$newname = 206;}
if($list3 == 202 &&  $list4 == 204)                                  {$newname = 206;}
if($list3 == 155 &&  $list4 == 45)                                   {$newname = 207;}
if($list3 == 207 &&  $list4 == 69)                                   {$newname = 208;}
if($list3 == 208 &&  $list4 == 20)                                   {$newname = 209;}
if($list3 == 209 &&  $list4 == 35)                                   {$newname = 210;}
if($list3 == 205 &&  $list4 == 70)                                   {$newname = 211;}
if($list3 == 206 &&  $list4 == 209)                                  {$newname = 212;}
if($list3 == 212 &&  $list4 == 129)                                  {$newname = 213;}
if($list3 == 213 &&  $list4 == 211)                                  {$newname = 214;}
if($list3 == 214 &&  $list4 == 110)                                  {$newname = 215;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 124)               {$newname = 5;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 25)                {$newname = 5;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 91)                {$newname = 10;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 47)                {$newname = 10;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 85)                {$newname = 10;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 172)               {$newname = 10;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 52)                {$newname = 11;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 68)                {$newname = 11;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 50)                {$newname = 12;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 194)               {$newname = 13;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 192)               {$newname = 13;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 195)               {$newname = 14;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 196)               {$newname = 15;}
if($list3 == 7 && $list4 == 7)                                  {$newname = 16;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 152)               {$newname = 17;}
if($list3 == 16 && $list4 == 66)                                {$newname = 17;}
if($list3 == 15 && $list4 == 15)                                {$newname = 18;}
if($list3 == 18 && $list4 == 18)                                {$newname = 19;}
if($list3 == 16 && $list4 == 196)                               {$newname = 19;}
if($list3 == 17 && $list4 == 196)                               {$newname = 19;}
if($list3 == 19 && $list4 == 19)                                {$newname = 20;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 71)               {$newname = 29;}
if($list3 == 21 &&  $list4 == 21)                               {$newname = 30;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 5)                {$newname = 31;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 95)               {$newname = 32;}
if($list3 == 43 &&  $list4 == 192)                              {$newname = 32;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 78)               {$newname = 33;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 111)              {$newname = 34;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 126)              {$newname = 35;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 63)               {$newname = 36;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 185)              {$newname = 37;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 84)               {$newname = 38;}
if($list3 == 26 &&  $list4 == 143)                              {$newname = 38;}
if($list3 == 33 &&  $list4 == 33)                               {$newname = 39;}
if($list3 >= 21 &&  $list3 <= 45 && ($list4 == 16 or $list4 == 17 or $list4 == 19)){$newname = 40;}
if($list3 == 30 &&  $list4 == 42)                               {$newname = 40;}
if($list3 == 39 &&  $list4 == 39)                               {$newname = 41;}
if($list3 == 23 &&  $list4 == 149)                              {$newname = 41;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 143)              {$newname = 42;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 86)               {$newname = 43;}
if(($list3 == 32 or $list3 == 40) &&  $list4 == 138)            {$newname = 44;}
if($list3 == 43 &&  $list4 == 44)                               {$newname = 45;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 73)               {$newname = 53;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 99)               {$newname = 54;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 186)              {$newname = 55;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 34)               {$newname = 56;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 30)               {$newname = 57;}
if($list4 >= 21 &&  $list4 <= 45 && $list3 == 49)               {$newname = 58;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 165)               {$newname = 60;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 27)               {$newname = 61;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 131 && $list4 <= 155){$newname = 62;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 140)              {$newname = 59;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 195 && $list4 <= 200){$newname = 63;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 75)               {$newname = 64;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 9)                {$newname = 65;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 11)               {$newname = 66;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 12)               {$newname = 66;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 134)              {$newname = 67;}
if($list3 == 64 &&  $list4 == 64)                               {$newname = 68;}
if($list3 == 68 &&  $list4 == 68)                               {$newname = 69;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 195)              {$newname = 69;}
if($list3 == 71 &&  $list4 >= 1  && $list4 <= 20)               {$newname = 77;}
if($list3 == 78 &&  $list4 == 78)                               {$newname = 78;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 176 && $list4 <= 200){$newname = 79;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 21 && $list4 <= 45)  {$newname = 80;}
if($list3 == 76 &&  $list4 >= 46 && $list4 <= 70)               {$newname = 81;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 13)               {$newname = 82;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 125)              {$newname = 83;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 178)              {$newname = 84;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 101)              {$newname = 85;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 188)              {$newname = 86;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 198)              {$newname = 87;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 59)               {$newname = 87;}
if($list3 == 73 &&  $list4 == 65)                               {$newname = 87;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 38)               {$newname = 88;}
if($list3 == 81 &&  $list4 == 193)                              {$newname = 88;}
if($list3 == 88 &&  $list4 == 188)                              {$newname = 89;}
if($list3 == 87 &&  $list4 == 86)                               {$newname = 90;}
if($list3 == 192 &&  $list4 == 192)                             {$newname = 193;}
if($list3 == 28 &&  $list4 == 66)                               {$newname = 40;}

if($newname eq ""){$newname = $Kimg[1];}

if($omi == 0){$newname = $Kimg[1];}
if($omi == 2){$newname = 1;}

open(FH,"$monsdata") || &error("Can't open $monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
    if($newname == $Mimg){
    $NEWhai = $Khai[1];
    $NEWhai++;
    $Nimg[3]     = $newname;
    $Nhai[3]     = $NEWhai;
    $Nlev[3]     = 1;
    $Nmlev[3]    = int(($Alev[1] + $Klev[1]) * 2);
    $Nmhp[3]     = int($Mhp + $NEWhai);
    $Nmmp[3]     = int($Mmp + $NEWhai);
    $Nkou[3]     = int($Mkou + $NEWhai);
    $Nmam[3]     = int($Mmam + $NEWhai);
    $Nsub[3]     = int($Msub + $NEWhai);
    $Nhp[3]      = int($Mhp + $NEWhai);
    $Nmp[3]      = int($Mmp + $NEWhai);
    $Ncount[3]   = 0;
    $Nnecount[3] = $nextup;
    
    @sexs = (1,2,1,2,1,2,1,2,1,2);
    $Nsex[3] = $sexs[int(rand(10))];
    
    @sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
    $Nsei[3] = $sei[int(rand(27))];
    last;}
    }

open(FH,"waza/$Vname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($waza[1],$waza[2],$waza[3],$waza[4],$waza[5],$waza[6],$waza[7],$waza[8],$waza[9],$waza[10],$waza[11],$waza[12],$waza[13],$waza[14],$waza[15],$waza[16],$waza[17],$waza[18],$waza[19],$waza[20],$waza[21],$waza[22],$waza[23],$waza[24],$waza[25],$waza[26],$waza[27],$waza[28],$waza[29],$waza[30],$waza[31],$waza[32],$waza[33],$waza[34],$waza[35],$waza[36],$waza[37],$waza[38],$waza[39],$waza[40],$waza[41],$waza[42],$waza[43],$waza[44],$waza[45],$waza[46],$waza[47],$waza[48],$waza[49],$waza[50],$waza[51],$waza[52]) = split(/<>/,$line);
}

$waza[$Ntoku] = $Ntoku;

$NEWWAZA = "$waza[1]<>$waza[2]<>$waza[3]<>$waza[4]<>$waza[5]<>$waza[6]<>$waza[7]<>$waza[8]<>$waza[9]<>$waza[10]<>$waza[11]<>$waza[12]<>$waza[13]<>$waza[14]<>$waza[15]<>$waza[16]<>$waza[17]<>$waza[18]<>$waza[19]<>$waza[20]<>$waza[21]<>$waza[22]<>$waza[23]<>$waza[24]<>$waza[25]<>$waza[26]<>$waza[27]<>$waza[28]<>$waza[29]<>$waza[30]<>$waza[31]<>$waza[32]<>$waza[33]<>$waza[34]<>$waza[35]<>$waza[36]<>$waza[37]<>$waza[38]<>$waza[39]<>$waza[40]<>$waza[41]<>$waza[42]<>$waza[43]<>$waza[44]<>$waza[45]<>$waza[46]<>$waza[47]<>$waza[48]<>$waza[49]<>$waza[50]<>$waza[51]<>$waza[52]";

&lock;
open(FH, ">waza/$Vname.cgi") || &error("Can't open!");
print FH $NEWWAZA;
close(FH);
&unlock;

if($Nimg[1] == 0){
$newline = "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Aname[2]<>$Alev[2]<>$Amlev[2]<>$Aimg[2]<>$Ahp[2]<>$Amhp[2]<>$Amp[2]<>$Ammp[2]<>$Akou[2]<>$Amam[2]<>$Asub[2]<>$Ahai[2]<>$Acount[2]<>$Anecount[2]<>$Asex[2]<>$Asei[2]<>$Nlev[3]<>$Nmlev[3]<>$Nimg[3]<>$Nhp[3]<>$Nmhp[3]<>$Nmp[3]<>$Nmmp[3]<>$Nkou[3]<>$Nmam[3]<>$Nsub[3]<>$Nhai[3]<>$Ncount[3]<>$Nnecount[3]<>$Nsex[3]<>$Nsei[3]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[1]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";
}

if($Nimg[1] != 0 && $Nimg[2] == 0){
$newline = "0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Klev[2]<>$Kmlev[2]<>$Kimg[2]<>$Khp[2]<>$Kmhp[2]<>$Kmp[2]<>$Kmmp[2]<>$Kkou[2]<>$Kmam[2]<>$Ksub[2]<>$Khai[2]<>$Kcount[2]<>$Knecount[2]<>$Ksex[2]<>$Ksei[2]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Aname[2]<>$Alev[2]<>$Amlev[2]<>$Aimg[2]<>$Ahp[2]<>$Amhp[2]<>$Amp[2]<>$Ammp[2]<>$Akou[2]<>$Amam[2]<>$Asub[2]<>$Ahai[2]<>$Acount[2]<>$Anecount[2]<>$Asex[2]<>$Asei[2]<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[3]<>$Nmlev[3]<>$Nimg[3]<>$Nhp[3]<>$Nmhp[3]<>$Nmp[3]<>$Nmmp[3]<>$Nkou[3]<>$Nmam[3]<>$Nsub[3]<>$Nhai[3]<>$Ncount[3]<>$Nnecount[3]<>$Nsex[3]<>$Nsei[3]<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[2]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";
}

&lock;
open(FH, ">omiai/$Vname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
&unlock;

open(FH,"omiai/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($Klev[1],$Kmlev[1],$Kimg[1],$Khp[1],$Kmhp[1],$Kmp[1],$Kmmp[1],$Kkou[1],$Kmam[1],$Ksub[1],$Khai[1],$Kcount[1],$Knecount[1],$Ksex[1],$Ksei[1],$Klev[2],$Kmlev[2],$Kimg[2],$Khp[2],$Kmhp[2],$Kmp[2],$Kmmp[2],$Kkou[2],$Kmam[2],$Ksub[2],$Khai[2],$Kcount[2],$Knecount[2],$Ksex[2],$Ksei[2],$Aname[1],$Alev[1],$Amlev[1],$Aimg[1],$Ahp[1],$Amhp[1],$Amp[1],$Ammp[1],$Akou[1],$Amam[1],$Asub[1],$Ahai[1],$Acount[1],$Anecount[1],$Asex[1],$Asei[1],$Aname[2],$Alev[2],$Amlev[2],$Aimg[2],$Ahp[2],$Amhp[2],$Amp[2],$Ammp[2],$Akou[2],$Amam[2],$Asub[2],$Ahai[2],$Acount[2],$Anecount[2],$Asex[2],$Asei[2],$Nlev[1],$Nmlev[1],$Nimg[1],$Nhp[1],$Nmhp[1],$Nmp[1],$Nmmp[1],$Nkou[1],$Nmam[1],$Nsub[1],$Nhai[1],$Ncount[1],$Nnecount[1],$Nsex[1],$Nsei[1],$Nlev[2],$Nmlev[2],$Nimg[2],$Nhp[2],$Nmhp[2],$Nmp[2],$Nmmp[2],$Nkou[2],$Nmam[2],$Nsub[2],$Nhai[2],$Ncount[2],$Nnecount[2],$Nsex[2],$Nsei[2],$Flev[1],$Fmlev[1],$Fimg[1],$Fhp[1],$Fmhp[1],$Fmp[1],$Fmmp[1],$Fkou[1],$Fmam[1],$Fsub[1],$Fhai[1],$Fcount[1],$Fnecount[1],$Fsex[1],$Fsei[1],$Flev[2],$Fmlev[2],$Fimg[2],$Fhp[2],$Fmhp[2],$Fmp[2],$Fmmp[2],$Fkou[2],$Fmam[2],$Fsub[2],$Fhai[2],$Fcount[2],$Fnecount[2],$Fsex[2],$Fsei[2]) = split(/<>/,$line);
}

$list3 = $Kimg[2];
$list4 = $Aimg[2];
$newname ="";

if($list3 == 1 && $list4 == 1)                                     {$newname = 1;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 91 && $list4 <= 110)  {$newname = 2;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 71 && $list4 <= 90)   {$newname = 3;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 111 && $list4 <= 130) {$newname = 4;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 156 && $list4 <= 175) {$newname = 5;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 131 && $list4 <= 155) {$newname = 6;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 46 && $list4 <= 70)   {$newname = 7;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 176 && $list4 <= 200) {$newname = 8;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 >= 21 && $list4 <= 45)   {$newname = 9;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 1 && $list4 <= 20)   {$newname = 21;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 91 && $list4 <= 110) {$newname = 22;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 71 && $list4 <= 90)  {$newname = 23;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 111 && $list4 <= 130){$newname = 24;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 156 && $list4 <= 175){$newname = 25;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 131 && $list4 <= 155){$newname = 26;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 46 && $list4 <= 70)  {$newname = 27;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 >= 176 && $list4 <= 200){$newname = 28;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 1 && $list4 <= 20)   {$newname = 46;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 91 && $list4 <= 110) {$newname = 47;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 71 && $list4 <= 90)  {$newname = 48;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 111 && $list4 <= 130){$newname = 49;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 156 && $list4 <= 175){$newname = 50;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 175 && $list4 <= 194){$newname = 51;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 21 && $list4 <= 45)  {$newname = 52;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 201 && $list4 <= 215){$newname = 70;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 1 && $list4 <= 20)   {$newname = 71;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 91 && $list4 <= 110) {$newname = 72;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 111 && $list4 <= 130){$newname = 73;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 156 && $list4 <= 175){$newname = 74;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 131 && $list4 <= 155){$newname = 75;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 46 && $list4 <= 70)  {$newname = 76;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 1 && $list4 <= 20)  {$newname = 91;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 71 && $list4 <= 90) {$newname = 92;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 111 && $list4 <= 130){$newname = 93;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 156 && $list4 <= 175){$newname = 94;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 131 && $list4 <= 155){$newname = 95;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 46 && $list4 <= 70)  {$newname = 96;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 176 && $list4 <= 200){$newname = 97;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 21 && $list4 <= 45)  {$newname = 98;}
if($list3 == 97 &&  $list4 >= 46  && $list4 <= 70)                  {$newname = 99;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 118)                 {$newname = 100;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 176)                 {$newname = 101;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 131)                 {$newname = 102;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 166)                 {$newname = 103;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 85)                  {$newname = 104;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 47)                  {$newname = 105;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 == 132)                 {$newname = 106;}
if($list3 == 106 && $list4 == 106)                                  {$newname = 107;}
if($list3 == 107 && $list4 == 107)                                  {$newname = 108;}
if($list3 >= 91 &&  $list3 <= 110 && $list4 >= 201 && $list4 <= 215){$newname = 109;}
if($list3 == 110 && $list4 == 110)                                  {$newname = 110;}
if($list3 == 111 && $list4 == 111)                                  {$newname = 111;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 1 && $list4 <= 20)  {$newname = 112;}
if($list3 == 112 && $list4 >= 1 && $list4 <= 20)                    {$newname = 113;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 91 && $list4 <= 110){$newname = 114;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 71 && $list4 <= 90) {$newname = 115;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 156 && $list4 <= 175){$newname = 116;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 131 && $list4 <= 155){$newname = 117;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 46 && $list4 <= 70)  {$newname = 118;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 176 && $list4 <= 200){$newname = 119;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 21 && $list4 <= 45)  {$newname = 120;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 96)                  {$newname = 121;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 61)                  {$newname = 122;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 97)                  {$newname = 123;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 49)                  {$newname = 124;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 156)                 {$newname = 125;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 159)                 {$newname = 126;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 == 56)                  {$newname = 127;}
if($list3 == 119 &&  $list4 == 119)                                  {$newname = 128;}
if($list3 == 128 &&  $list4 == 128)                                  {$newname = 129;}
if($list3 >= 111 &&  $list3 <= 130 && $list4 >= 201 && $list4 <= 215){$newname = 130;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 1 && $list4 <= 20)   {$newname = 131;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 91 && $list4 <= 110) {$newname = 132;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 71 && $list4 <= 90)  {$newname = 133;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 111 && $list4 <= 130){$newname = 134;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 156 && $list4 <= 175){$newname = 135;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 46 && $list4 <= 70)  {$newname = 136;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 176 && $list4 <= 200){$newname = 137;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 21 && $list4 <= 38)  {$newname = 138;}
if($list3 == 131 &&  $list4 >= 1 && $list4 <= 20)                    {$newname = 139;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 105)                 {$newname = 140;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 54)                  {$newname = 141;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 70)                  {$newname = 142;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 26)                  {$newname = 143;}
if($list3 >= 131 &&  $list3 <= 155 && ($list4 == 16 or $list4 == 17 or $list4 == 19)){$newname = 144;}
if($list3 == 133 && $list4 == 133)                                   {$newname = 145;}
if($list3 == 139 && $list4 == 139)                                   {$newname = 146;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 36)                  {$newname = 147;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 >= 39 && $list4 <= 45)  {$newname = 148;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 184)                 {$newname = 149;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 67)                  {$newname = 150;}
if($list3 >= 131 &&  $list3 <= 155 && $list4 == 122)                 {$newname = 151;}
if($list3 == 145 && $list4 >= 46 && $list4 <= 70)                    {$newname = 152;}
if($list3 == 154 && $list4 == 90)                                    {$newname = 153;}
if($list3 == 147 && $list4 == 147)                                   {$newname = 154;}
if($list3 == 152 && $list4 == 200)                                   {$newname = 155;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 1 && $list4 <= 20)   {$newname = 156;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 91 && $list4 <= 110) {$newname = 157;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 71 && $list4 <= 90)  {$newname = 158;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 111 && $list4 <= 130){$newname = 159;}
if($list3 == 156 && $list4 >= 46 && $list4 <= 70)                    {$newname = 160;}
if($list3 >= 157 &&  $list3 <= 175 && $list4 >= 46 && $list4 <= 70)  {$newname = 161;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 131 && $list4 <= 155){$newname = 162;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 21 && $list4 <= 45)  {$newname = 163;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 >= 176 && $list4 <= 200){$newname = 164;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 112)                 {$newname = 165;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 79)                  {$newname = 166;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 51)                  {$newname = 167;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 28)                  {$newname = 168;}
if($list3 >= 156 &&  $list3 <= 175 && $list4 == 114)                 {$newname = 169;}
if($list3 == 162 &&  $list4 == 162)                                  {$newname = 170;}
if($list3 == 160 &&  $list4 == 160)                                  {$newname = 171;}
if($list3 == 172 &&  $list4 == 172)                                  {$newname = 172;}
if($list3 == 171 &&  $list4 == 171)                                  {$newname = 173;}
if($list3 == 173 &&  $list4 == 173)                                  {$newname = 174;}
if($list3 == 171 &&  $list4 == 32)                                   {$newname = 175;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 91 && $list4 <= 110) {$newname = 176;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 1 && $list4 <= 20)   {$newname = 177;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 71 && $list4 <= 90)  {$newname = 178;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 111 && $list4 <= 130){$newname = 179;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 131 && $list4 <= 155){$newname = 180;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 46 && $list4 <= 70)  {$newname = 181;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 21 && $list4 <= 45)  {$newname = 182;}
if($list3 == 177 && $list4 >= 1 && $list4 <= 20)                     {$newname = 183;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 156 && $list4 <= 175){$newname = 184;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 116)                 {$newname = 185;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 117)                 {$newname = 186;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 92)                  {$newname = 187;}
if($list3 == 183 &&  $list4 == 98)                                   {$newname = 188;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 4)                   {$newname = 189;}
if($list3 == 183 &&  $list4 == 183)                                  {$newname = 190;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 8)                   {$newname = 191;}
if($list3 == 190 &&  $list4 == 190)                                  {$newname = 192;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 192)                 {$newname = 194;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 135)                 {$newname = 195;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 == 32)                  {$newname = 196;}
if($list3 == 196 &&  $list4 == 144)                                  {$newname = 197;}
if($list3 == 195 &&  $list4 == 69)                                   {$newname = 198;}
if($list3 >= 176 &&  $list3 <= 200 && $list4 >= 201 && $list4 <= 215){$newname = 199;}
if($list3 == 198 &&  $list4 == 197)                                  {$newname = 200;}
if($list3 == 174 &&  $list4 == 40)                                   {$newname = 201;}
if($list3 == 174 &&  $list4 == 32)                                   {$newname = 201;}
if($list3 == 201 &&  $list4 == 45)                                   {$newname = 202;}
if($list3 == 175 &&  $list4 == 19)                                   {$newname = 203;}
if($list3 == 153 &&  $list4 == 109)                                  {$newname = 204;}
if($list3 == 203 &&  $list4 == 44)                                   {$newname = 205;}
if($list3 == 201 &&  $list4 == 204)                                  {$newname = 206;}
if($list3 == 202 &&  $list4 == 204)                                  {$newname = 206;}
if($list3 == 155 &&  $list4 == 45)                                   {$newname = 207;}
if($list3 == 207 &&  $list4 == 69)                                   {$newname = 208;}
if($list3 == 208 &&  $list4 == 20)                                   {$newname = 209;}
if($list3 == 209 &&  $list4 == 35)                                   {$newname = 210;}
if($list3 == 205 &&  $list4 == 70)                                   {$newname = 211;}
if($list3 == 206 &&  $list4 == 209)                                  {$newname = 212;}
if($list3 == 212 &&  $list4 == 129)                                  {$newname = 213;}
if($list3 == 213 &&  $list4 == 211)                                  {$newname = 214;}
if($list3 == 214 &&  $list4 == 110)                                  {$newname = 215;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 124)               {$newname = 5;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 25)                {$newname = 5;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 91)                {$newname = 10;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 47)                {$newname = 10;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 85)                {$newname = 10;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 172)               {$newname = 10;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 52)                {$newname = 11;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 68)                {$newname = 11;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 50)                {$newname = 12;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 194)               {$newname = 13;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 192)               {$newname = 13;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 195)               {$newname = 14;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 196)               {$newname = 15;}
if($list3 == 7 && $list4 == 7)                                  {$newname = 16;}
if($list3 >= 1 &&  $list3 <= 20 && $list4 == 152)               {$newname = 17;}
if($list3 == 16 && $list4 == 66)                                {$newname = 17;}
if($list3 == 15 && $list4 == 15)                                {$newname = 18;}
if($list3 == 18 && $list4 == 18)                                {$newname = 19;}
if($list3 == 16 && $list4 == 196)                               {$newname = 19;}
if($list3 == 17 && $list4 == 196)                               {$newname = 19;}
if($list3 == 19 && $list4 == 19)                                {$newname = 20;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 71)               {$newname = 29;}
if($list3 == 21 &&  $list4 == 21)                               {$newname = 30;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 5)                {$newname = 31;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 95)               {$newname = 32;}
if($list3 == 43 &&  $list4 == 192)                              {$newname = 32;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 78)               {$newname = 33;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 111)              {$newname = 34;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 126)              {$newname = 35;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 63)               {$newname = 36;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 185)              {$newname = 37;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 84)               {$newname = 38;}
if($list3 == 26 &&  $list4 == 143)                              {$newname = 38;}
if($list3 == 33 &&  $list4 == 33)                               {$newname = 39;}
if($list3 >= 21 &&  $list3 <= 45 && ($list4 == 16 or $list4 == 17 or $list4 == 19)){$newname = 40;}
if($list3 == 30 &&  $list4 == 42)                               {$newname = 40;}
if($list3 == 39 &&  $list4 == 39)                               {$newname = 41;}
if($list3 == 23 &&  $list4 == 149)                              {$newname = 41;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 143)              {$newname = 42;}
if($list3 >= 21 &&  $list3 <= 45 && $list4 == 86)               {$newname = 43;}
if(($list3 == 32 or $list3 == 40) &&  $list4 == 138)            {$newname = 44;}
if($list3 == 43 &&  $list4 == 44)                               {$newname = 45;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 73)               {$newname = 53;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 99)               {$newname = 54;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 186)              {$newname = 55;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 34)               {$newname = 56;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 30)               {$newname = 57;}
if($list4 >= 21 &&  $list4 <= 45 && $list3 == 49)               {$newname = 58;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 165)               {$newname = 60;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 27)               {$newname = 61;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 131 && $list4 <= 155){$newname = 62;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 140)              {$newname = 59;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 >= 195 && $list4 <= 200){$newname = 63;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 75)               {$newname = 64;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 9)                {$newname = 65;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 11)               {$newname = 66;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 12)               {$newname = 66;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 134)              {$newname = 67;}
if($list3 == 64 &&  $list4 == 64)                               {$newname = 68;}
if($list3 == 68 &&  $list4 == 68)                               {$newname = 69;}
if($list3 >= 46 &&  $list3 <= 70 && $list4 == 195)              {$newname = 69;}
if($list3 == 71 &&  $list4 >= 1  && $list4 <= 20)               {$newname = 77;}
if($list3 == 78 &&  $list4 == 78)                               {$newname = 78;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 176 && $list4 <= 200){$newname = 79;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 >= 21 && $list4 <= 45)  {$newname = 80;}
if($list3 == 76 &&  $list4 >= 46 && $list4 <= 70)               {$newname = 81;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 13)               {$newname = 82;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 125)              {$newname = 83;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 178)              {$newname = 84;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 101)              {$newname = 85;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 188)              {$newname = 86;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 198)              {$newname = 87;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 59)               {$newname = 87;}
if($list3 == 73 &&  $list4 == 65)                               {$newname = 87;}
if($list3 >= 71 &&  $list3 <= 90 && $list4 == 38)               {$newname = 88;}
if($list3 == 81 &&  $list4 == 193)                              {$newname = 88;}
if($list3 == 88 &&  $list4 == 188)                              {$newname = 89;}
if($list3 == 87 &&  $list4 == 86)                               {$newname = 90;}
if($list3 == 192 &&  $list4 == 192)                             {$newname = 193;}
if($list3 == 28 &&  $list4 == 66)                               {$newname = 40;}

if($newname eq ""){$newname = $Kimg[2];}

if($omi == 0){$newname = $Kimg[2];}
if($omi == 2){$newname = 1;}

open(FH,"$monsdata") || &error("Can't open $monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
    ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
    if($newname == $Mimg){
    $NEWhai = $Khai[2];
    $NEWhai++;
    $Nimg[3]     = $newname;
    $Nhai[3]     = $NEWhai;
    $Nlev[3]     = 1;
    $Nmlev[3]    = int(($Alev[2] + $Klev[2]) * 2);
    $Nmhp[3]     = int($Mhp + $NEWhai);
    $Nmmp[3]     = int($Mmp + $NEWhai);
    $Nkou[3]     = int($Mkou + $NEWhai);
    $Nmam[3]     = int($Mmam + $NEWhai);
    $Nsub[3]     = int($Msub + $NEWhai);
    $Nhp[3]      = int($Mhp + $NEWhai);
    $Nmp[3]      = int($Mmp + $NEWhai);
    $Ncount[3]   = 0;
    $Nnecount[3] = $nextup;
    
    @sexs = (1,2,1,2,1,2,1,2,1,2);
    $Nsex[3] = $sexs[int(rand(10))];
    
    @sei = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
    $Nsei[3] = $sei[int(rand(27))];
    last;}
    }

open(FH,"waza/$inname.cgi");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
   ($waza[1],$waza[2],$waza[3],$waza[4],$waza[5],$waza[6],$waza[7],$waza[8],$waza[9],$waza[10],$waza[11],$waza[12],$waza[13],$waza[14],$waza[15],$waza[16],$waza[17],$waza[18],$waza[19],$waza[20],$waza[21],$waza[22],$waza[23],$waza[24],$waza[25],$waza[26],$waza[27],$waza[28],$waza[29],$waza[30],$waza[31],$waza[32],$waza[33],$waza[34],$waza[35],$waza[36],$waza[37],$waza[38],$waza[39],$waza[40],$waza[41],$waza[42],$waza[43],$waza[44],$waza[45],$waza[46],$waza[47],$waza[48],$waza[49],$waza[50],$waza[51],$waza[52]) = split(/<>/,$line);
}

$waza[$Ntoku] = $Ntoku;

$NEWWAZA = "$waza[1]<>$waza[2]<>$waza[3]<>$waza[4]<>$waza[5]<>$waza[6]<>$waza[7]<>$waza[8]<>$waza[9]<>$waza[10]<>$waza[11]<>$waza[12]<>$waza[13]<>$waza[14]<>$waza[15]<>$waza[16]<>$waza[17]<>$waza[18]<>$waza[19]<>$waza[20]<>$waza[21]<>$waza[22]<>$waza[23]<>$waza[24]<>$waza[25]<>$waza[26]<>$waza[27]<>$waza[28]<>$waza[29]<>$waza[30]<>$waza[31]<>$waza[32]<>$waza[33]<>$waza[34]<>$waza[35]<>$waza[36]<>$waza[37]<>$waza[38]<>$waza[39]<>$waza[40]<>$waza[41]<>$waza[42]<>$waza[43]<>$waza[44]<>$waza[45]<>$waza[46]<>$waza[47]<>$waza[48]<>$waza[49]<>$waza[50]<>$waza[51]<>$waza[52]";

&lock;
open(FH, ">waza/$inname.cgi") || &error("Can't open!");
print FH $NEWWAZA;
close(FH);
&unlock;

if($Nimg[1] == 0){
$newline = "$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Aname[1]<>$Alev[1]<>$Amlev[1]<>$Aimg[1]<>$Ahp[1]<>$Amhp[1]<>$Amp[1]<>$Ammp[1]<>$Akou[1]<>$Amam[1]<>$Asub[1]<>$Ahai[1]<>$Acount[1]<>$Anecount[1]<>$Asex[1]<>$Asei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Nlev[3]<>$Nmlev[3]<>$Nimg[3]<>$Nhp[3]<>$Nmhp[3]<>$Nmp[3]<>$Nmmp[3]<>$Nkou[3]<>$Nmam[3]<>$Nsub[3]<>$Nhai[3]<>$Ncount[3]<>$Nnecount[3]<>$Nsex[3]<>$Nsei[3]<>$Nlev[2]<>$Nmlev[2]<>$Nimg[2]<>$Nhp[2]<>$Nmhp[2]<>$Nmp[2]<>$Nmmp[2]<>$Nkou[2]<>$Nmam[2]<>$Nsub[2]<>$Nhai[2]<>$Ncount[2]<>$Nnecount[2]<>$Nsex[2]<>$Nsei[2]<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[1]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";
}

if($Nimg[1] != 0 && $Nimg[2] == 0){
$newline = "$Klev[1]<>$Kmlev[1]<>$Kimg[1]<>$Khp[1]<>$Kmhp[1]<>$Kmp[1]<>$Kmmp[1]<>$Kkou[1]<>$Kmam[1]<>$Ksub[1]<>$Khai[1]<>$Kcount[1]<>$Knecount[1]<>$Ksex[1]<>$Ksei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Aname[1]<>$Alev[1]<>$Amlev[1]<>$Aimg[1]<>$Ahp[1]<>$Amhp[1]<>$Amp[1]<>$Ammp[1]<>$Akou[1]<>$Amam[1]<>$Asub[1]<>$Ahai[1]<>$Acount[1]<>$Anecount[1]<>$Asex[1]<>$Asei[1]<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>0<>$Nlev[1]<>$Nmlev[1]<>$Nimg[1]<>$Nhp[1]<>$Nmhp[1]<>$Nmp[1]<>$Nmmp[1]<>$Nkou[1]<>$Nmam[1]<>$Nsub[1]<>$Nhai[1]<>$Ncount[1]<>$Nnecount[1]<>$Nsex[1]<>$Nsei[1]<>$Nlev[3]<>$Nmlev[3]<>$Nimg[3]<>$Nhp[3]<>$Nmhp[3]<>$Nmp[3]<>$Nmmp[3]<>$Nkou[3]<>$Nmam[3]<>$Nsub[3]<>$Nhai[3]<>$Ncount[3]<>$Nnecount[3]<>$Nsex[3]<>$Nsei[3]<>$Flev[1]<>$Fmlev[1]<>$Fimg[1]<>$Fhp[1]<>$Fmhp[1]<>$Fmp[1]<>$Fmmp[1]<>$Fkou[1]<>$Fmam[1]<>$Fsub[1]<>$Fhai[1]<>$Fcount[1]<>$Fnecount[1]<>$Fsex[1]<>$Fsei[1]<>$Flev[2]<>$Fmlev[2]<>$Fimg[2]<>$Fhp[2]<>$Fmhp[2]<>$Fmp[2]<>$Fmmp[2]<>$Fkou[2]<>$Fmam[2]<>$Fsub[2]<>$Fhai[2]<>$Fcount[2]<>$Fnecount[2]<>$Fsex[2]<>$Fsei[2]";
}

&lock;
open(FH, ">omiai/$inname.cgi") || &error("Can't open ");
print FH $newline;
close(FH);
&unlock;

if($omi == 1){$mes ="お見合いは成功しました";}
if($omi == 0){$mes ="性格の不一致で失敗しました";}
if($omi == 2){$mes ="性格の不一致でスライムになりました";}

&header;

print <<"EOF";
<P align="center">
<FONT face="Times New Roman" color="#0000cc" size="6"><B>$mes</B></FONT>
</P>
<HR>
<BR>
<CENTER>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="hidden" name="mode" value="omiai">
<INPUT type="hidden" name="name" value="$inname">
<INPUT type="hidden" name="password" value="$inpass">
<INPUT type="submit"  value="お見合い所へ">
</FORM>
</CENTER>
EOF

&footer;

