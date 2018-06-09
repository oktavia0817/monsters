use utf8;
use open IO => ":utf8";
use open ":std";

require './cgi/fight/fight10A.cgi';
require './cgi/fight/fight10B.cgi';

#戦闘開始処理fight10A
&wbat;

#戦闘終わってなしfight10A
&wnend("fight11");

#戦闘終了処理fight10B
&wtaktak(2);


&footer;


