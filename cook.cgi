#!C:/perl64/bin/perl
# ↑サーバーに合わせてください

use utf8;
use open IO => ":utf8";
use open ":std";

require './set.cgi';

&decode;

if($FORM{'mode'} eq "")            {  &openset; exit; }
elsif($FORM{'mode'} eq "sets")    {  &sets; }

sub openset {

&header;

print <<"EOF";

<font size=5p><B>画像のローカル設定について</B></font><BR>
<BR>
負荷軽減の為、各プレイヤー様に画像をダウンロードして頂きそれをマイドキュメントの中の<BR>
マイピクチャーに入れて頂きPCから画像を呼び出すようにして頂きたいと思います。<BR>
箱庭諸島や箱庭RAでやってるものと同一です。<BR>
<BR>
画像を、<a href="http://park16.wakwak.com/~mikio-palace/monimg.zip">ここ</A>からダウンロードして下さい。<BR>
<BR>
<BR>
WINDOWSのみしか私が使用してませんのでWINDOWS用の説明になります。<BR>
<BR>
monimg.zipを解凍してください。<BR>
monimgというフォルダが完成すると思います。<BR>
そのmonimgフォルダをCドライブかDドライブに直接入れて下さい。<BR>
<BR>
<BR>
次に下の参照ボタンをクリックして「マイコンピューター」⇒「CかDドライブ」⇒「monimg」⇒「0.gif」<BR>
と開いていってください。（Win XPの場合）<BR>
「C:\\monimg\\0.gif」か「D:\\monimg\\0.gif」という風になると思います。
そして「\\0.gif」を消してください。<BR>
「C:\\monimg」か「D:\\monimg」<BR>
<BR>
<FORM ACTION="$ncook" METHOD="POST">
<TABLE BORDER>
<TR><TD>画像のローカル設定<BR>
<INPUT TYPE=file name="setimg">
<INPUT TYPE=submit VALUE="設定">
<INPUT type="hidden" name="mode" value="sets">
</TD></TR></TABLE>
</FORM>
<BR>
その後設定ボタンを押すだけで、設定が完了します。<BR>
<BR>
これで、アイコン画像が表\示\されれば成功です。

EOF

&footer;

}

sub sets {

$setimg = $FORM{'setimg'};
&set_cookie2;

&header;

print <<"EOF";

<font size=5p><B>$setimgにローカル設定が完了しました</B></font><BR>
<BR>
EOF

&footer;

}
