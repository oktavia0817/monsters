use utf8;
use open IO => ":utf8";
use open ":std";

require './cgi/fight/fight1A.cgi';
require './cgi/fight/fight1B.cgi';


#戦闘開始処理fight1A
&bat1;

#戦闘終わってなしfight1A
&nend;

#戦闘終了処理fight1B
&taktak;



&footer;

