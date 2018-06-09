use utf8;
use open IO => ":utf8";
use open ":std";

$inname= $FORM{'name'};
$inpass= $FORM{'password'};
$inimg = $FORM{'img'};
$haigou1 = $FORM{'haigou1'};
$haigou2 = $FORM{'haigou2'};
$Kmoney  = $FORM{'money'};

if($haigou1 eq "no" || $haigou2 eq "no") { &error("正しく設定されていません-1")}
if($haigou1 == $haigou2) { &error("正しく設定されていません-2")}

&open1;
if($Ksex[$haigou1] == $Ksex[$haigou2]){&error("性別が同じで配合出来ません");}
$passcheck = crypt($inpass, $inname);
if($passcheck ne $Kpass) {&error("パスワードが違います");}

if($Klev[$haigou1] <= ($haigoulevel-1)){ &error("<IMG src= $imgpath/$Kimg[$haigou1].gif border=0>のレベルが$haigoulevelに達していません")}
if($Klev[$haigou2] <= ($haigoulevel-1)){ &error("<IMG src= $imgpath/$Kimg[$haigou2].gif border=0>のレベルが$haigoulevelに達していません")}
$Omoneys = (($Klev[$haigou1] + $Klev[$haigou2]) * 10);
if($Kmoney < $Omoneys ) { &error("お金が足りません")}
$list3 = $Kimg[$haigou1];
$list4 = $Kimg[$haigou2];

$l3 = $list3;
$l4 = $list4;

&hlist;

if($l3 == $スライム && $l4 == $スライム)	{$newname = $スライム;}
if($スライム系A && $植物系B)				{$newname = $スライムツリー;}
if($スライム系A && $鳥系B)					{$newname = $はねスライム;}
if($スライム系A && $虫系B)					{$newname = $スライムつむり;}
if($スライム系A && $ゾンビ系B)				{$newname = $バブルスライム;}
if($スライム系A && $悪魔系B)				{$newname = $スライムナイト;}
if($スライム系A && $けもの系B)				{$newname = $ぶちスライム;}
if($スライム系A && $物質系B)				{$newname = $ボックススライム;}
if($スライム系A && $ドラゴン系B)			{$newname = $ドラゴスライム;}
if($ドラゴン系A && $スライム系B)			{$newname = $ドラゴンキッズ;}
if($ドラゴン系A && $植物系B)				{$newname = $フーセンドラゴン;}
if($ドラゴン系A && $鳥系B)					{$newname = $プテラノドン;}
if($ドラゴン系A && $虫系B)					{$newname = $フェアリードラゴン;}
if($ドラゴン系A && $ゾンビ系B)				{$newname = $ポイズンリザード;}
if($ドラゴン系A && $悪魔系B)				{$newname = $リザードマン;}
if($ドラゴン系A && $けもの系B)				{$newname = $ガメゴン;}
if($ドラゴン系A && $物質系B)				{$newname = $ソードドラゴン;}
if($けもの系A && $スライム系B)				{$newname = $ベロゴン;}
if($けもの系A && $植物系B)					{$newname = $ファーラット;}
if($けもの系A && $鳥系B)					{$newname = $キャットフライ;}
if($けもの系A && $虫系B)					{$newname = $ミノーン;}
if($けもの系A && $ゾンビ系B)				{$newname = $スカルガルー;}
if($けもの系A && $物質系B)					{$newname = $かまいたち;}
if($けもの系A && $ドラゴン系B)				{$newname = $アルミラージ;}
if($けもの系A && $はてな系B)				{$newname = $ダークホーン;}
if($鳥系A && $スライム系B)					{$newname = $ピッキー;}
if($鳥系A && $植物系B)						{$newname = $はなカワセミ;}
if($鳥系A && $虫系B)						{$newname = $ダックカイト;}
if($鳥系A && $ゾンビ系B)					{$newname = $デスフラッター;}
if($鳥系A && $悪魔系B)						{$newname = $デッドペッカー;}
if($鳥系A && $けもの系B)					{$newname = $あばれうしどり;}
if($植物系A && $スライム系B)				{$newname = $マッドプラント;}
if($植物系A && $鳥系B)						{$newname = $ふゆうじゅ;}
if($植物系A && $虫系B)						{$newname = $サボテンボール;}
if($植物系A && $ゾンビ系B)					{$newname = $マタンゴ;}
if($植物系A && $悪魔系B)					{$newname = $ガップリン;}
if($植物系A && $けもの系B)					{$newname = $はなまどう;}
if($植物系A && $物質系B)					{$newname = $コハクそう;}
if($植物系A && $ドラゴン系B)				{$newname = $かりゅうそう;}
if($l3 == $コハクそう && $けもの系B)		{$newname = $きりかぶおばけ;}
if($植物系A && $l4 == $せみもぐら)			{$newname = $オニオーン;}
if($植物系A && $l4 == $トーテムキラー)		{$newname = $ダンスキャロット;}
if($植物系A && $l4 == $ピクシー)			{$newname = $ヘルボックル;}
if($植物系A && $l4 == $ナイトウィプス)		{$newname = $じんめんじゅ;}
if($植物系A && $l4 == $ファンキーバード)	{$newname = $マンドラゴラ;}
if($植物系A && $l4 == $ファーラット)		{$newname = $ビーンファイター;}
if($植物系A && $l4 == $ダークアイ)			{$newname = $エビルシード;}
if($l3 == $エビルシード && $l4 == $エビルシード)	{$newname = $マンイーター;}
if($l3 == $マンイーター && $l4 == $マンイーター)	{$newname = $ひとくいそう;}
if($植物系A && $はてな系B)							{$newname = $ローズバトラー;}
if($l3 == $わたぼう && $l4 == $わたぼう)			{$newname = $わたぼう;}
if($l3 == $きりきりバッタ && $l4 == $きりきりバッタ){$newname = $きりきりバッタ;}
if($虫系A && $スライム系B)							{$newname = $おおなめくじ;}
if($l3 == $おおなめくじ && $スライム系B)			{$newname = $ぐんたいアリ;}
if($虫系A && $植物系B)								{$newname = $とうちゅうかそう;}
if($虫系A && $鳥系B)								{$newname = $じんめんちょう;}
if($虫系A && $ゾンビ系B)							{$newname = $リップス;}
if($虫系A && $悪魔系B)								{$newname = $おおみみず;}
if($虫系A && $けもの系B)							{$newname = $せみもぐら;}
if($虫系A && $物質系B)								{$newname = $はさみくわがた;}
if($虫系A && $ドラゴン系B)							{$newname = $キャタピラー;}
if($虫系A && $l4 == $はなまどう)					{$newname = $テールイーター;}
if($虫系A && $l4 == $アイアンタートル)				{$newname = $よろいムカデ;}
if($虫系A && $l4 == $コハクそう)					{$newname = $メーダ;}
if($虫系A && $l4 == $ミノーン)						{$newname = $デスファレーナ;}
if($虫系A && $l4 == $ゴースト)						{$newname = $ドロル;}
if($虫系A && $l4 == $ダーククラブ)					{$newname = $ぐんたいガニ;}
if($虫系A && $l4 == $フェアリーラット)				{$newname = $ヘルホーネット;}
if($l3 == $はさみくわがた && $l4 == $はさみくわがた)	{$newname = $ホーンビートル;}
if($l3 == $ホーンビートル && $l4 == $ホーンビートル)	{$newname = $さそりアーマー;}
if($虫系A && $はてな系B)					{$newname = $ダンジョンえび;}
if($悪魔系A && $スライム系B)				{$newname = $ピクシー;}
if($悪魔系A && $植物系B)					{$newname = $ダークアイ;}
if($悪魔系A && $鳥系B)						{$newname = $ベビーサタン;}
if($悪魔系A && $虫系B)						{$newname = $おおめだま;}
if($悪魔系A && $ゾンビ系B)					{$newname = $スカルライダー;}
if($悪魔系A && $けもの系B)					{$newname = $グレムリン;}
if($悪魔系A && $物質系B)					{$newname = $ヘルビースト;}
if($悪魔系A && $ドラゴン系B)			{$newname = $メドーサボール;}
if($l3 == $ピクシー &&  $スライム系B)		{$newname = $ひとつめピエロ;}
if($悪魔系A && $l4 == $ビーンファイター)	{$newname = $オーク;}
if($悪魔系A && $l4 == $おおきづち)			{$newname = $オーガー;}
if($悪魔系A && $l4 == $ダークホーン)  		{$newname = $アンクルホーン;}
if($悪魔系A && $l4 == $リザードマン)		{$newname = $ライオネック;}
if($悪魔系A && $l4 == $ぶちキング)			{$newname = $アークデーモン;}
if($悪魔系A && $l4 == $キングスライム)		{$newname = $アークデーモン;}
if($悪魔系A && $l4 == $メタルキング)		{$newname = $アークデーモン;}
if($l3 == $ベビーサタン && $l4 == $ベビーサタン)		{$newname = $じごくのもんばん;}
if($l3 == $ひとつめピエロ && $l4 == $ひとつめピエロ)	{$newname = $きりさきピエロ;}
if($悪魔系A && $l4 == $ドラゴンマッド)					{$newname = $グレンデル;}
if($悪魔系A && $l4 >= $ウィングスネーク && $l4 <= $しんりゅう)	{$newname = $シルバーデビル;}
if($悪魔系A && $l4 == $さまようよろい)			{$newname = $あくまのきし;}
if($悪魔系A && $l4 == $ビックアイ)				{$newname = $ギガンデス;}
if($悪魔系A && $l4 == $よろいムカデ)			{$newname = $デビルアーマー;}
if($l3 == $じごくのもんばん && $けもの系B)		{$newname = $ずしおうまる;}
if($l3 == $アクバー && $l4 == $にじくじゃく)	{$newname = $ジャミラス;}
if($l3 == $グレンデル && $l4 == $グレンデル)	{$newname = $アクバー;}
if($l3 == $ずしおうまる && $l4 == $ゴールデンゴーレム)	{$newname = $デュラン;}
if($ゾンビ系A && $スライム系B)						{$newname = $ゴースト;}
if($ゾンビ系A && $植物系B)							{$newname = $マミー;}
if($ゾンビ系A && $鳥系B)							{$newname = $やたがらす;}
if($ゾンビ系A && $虫系B)							{$newname = $ダーククラブ;}
if($l3 == $ゴースト && $けもの系B)					{$newname = $くさったしたい;}
if($ゾンビ系A && $けもの系B)						{$newname = $アニマルゾンビ;}
if($ゾンビ系A && $悪魔系B)							{$newname = $しりょうのきし;}
if($ゾンビ系A && $ドラゴン系B)						{$newname = $エビルスピリッツ;}
if($ゾンビ系A && $物質系B)							{$newname = $シャドー;}
if($ゾンビ系A && $l4 == $おおなめくじ)  			{$newname = $マッドロン;}
if($ゾンビ系A && $l4 == $ミストウイング)			{$newname = $ナイトウィプス;}
if($ゾンビ系A && $l4 == $かまいたち)				{$newname = $ウインドマージ;}
if($ゾンビ系A && $l4 == $ソードドラゴン)			{$newname = $スカルゴン;}
if($ゾンビ系A && $l4 == $とうちゅうかそう)			{$newname = $しにがみ;}
if($l3 == $しりょうのきし && $l4 == $しりょうのきし)	{$newname = $しにがみきぞく;}
if($l3 == $くさったしたい && $l4 == $くさったしたい)	{$newname = $ボーンプリズナー;}
if($l3 == $マネマネ && $l4 == $マネマネ)				{$newname = $マネマネ;}
if($l3 == $ボーンプリズナー && $l4 == $ボーンプリズナー)	{$newname = $がいこつけんし;}
if($l3 == $がいこつけんし && $l4 == $がいこつけんし)		{$newname = $まおうのつかい;}
if($l3 == $ボーンプリズナー && $l4 == $アンドレアル)		{$newname = $ワイトキング;}
if($物質系A && $植物系B)							{$newname = $トーテムキラー;}
if($物質系A && $スライム系B)						{$newname = $おどるほうせき;}
if($物質系A && $鳥系B)								{$newname = $ネジまきどり;}
if($物質系A && $虫系B)								{$newname = $とげぼうず;}
if($物質系A && $悪魔系B)							{$newname = $あくまのカガミ;}
if($物質系A && $けもの系B)							{$newname = $おばけキャンドル;}
if($物質系A && $ドラゴン系B)						{$newname = $エビルワンド;}
if($l3 == $おどるほうせき && $スライム系B)			{$newname = $マドハンド;}
if($物質系A && $ゾンビ系B)							{$newname = $さまようよろい;}
if($物質系A && $l4 == $リップス)					{$newname = $ミステリードール;}
if($物質系A && $l4 == $おおみみず)					{$newname = $ひとくいサーベル;}
if($物質系A && $l4 == $ふゆうじゅ)					{$newname = $のろいのランプ;}
if($l3 == $マドハンド && $l4 == $かりゅうそう)		{$newname = $ギズモ;}
if($物質系A && $l4 == $スライムつむり)				{$newname = $あくまのつぼ;}
if($l3 == $マドハンド && $l4 == $マドハンド)		{$newname = $どろにんぎょう;}
if($物質系A && $l4 == $ボックススライム)			{$newname = $ミミック;}
if($l3 == $どろにんぎょう && $l4 == $どろにんぎょう)	{$newname = $ゴーレム;}
if($物質系A && $l4 == $ゴーレム)						{$newname = $ばくだんいわ;}
if($物質系A && $l4 == $スカルライダー)					{$newname = $キラーマシーン;}
if($物質系A && $l4 == $アンドレアル)					{$newname = $メタルドラゴン;}
if($l3 == $メタルドラゴン && $l4 == $アークデーモン)	{$newname = $ようがんまじん;}
if($l3 == $キラーマシーン && $l4 == $キングレオ)		{$newname = $ひょうがまじん;}
if($物質系A && $はてな系B)								{$newname = $バルザック;}
if($l3 == $ひょうがまじん && $l4 == $ようがんまじん)	{$newname = $ゴールデンゴーレム;}
if($l3 == $まおうのつかい && $l4 == $グレイトドラゴン)	{$newname = $りゅうおう;}
if($l3 == $まおうのつかい && $l4 == $アンドレアル)		{$newname = $りゅうおう;}
if($l3 == $りゅうおう && $l4 == $しんりゅう)			{$newname = $竜王DRAGON;}
if($l3 == $ワイトキング && $l4 == $メタルキング)		{$newname = $ハーゴン;}
if($l3 == $ジャミラス && $l4 == $ローズバトラー)		{$newname = $シドー;}
if($l3 == $ハーゴン && $l4 == $やまたのおろち)			{$newname = $バラモス;}
if($l3 == $りゅうおう && $l4 == $シドー)				{$newname = $ゾーマ;}
if($l3 == $竜王DRAGON && $l4 == $シドー)				{$newname = $ゾーマ;}
if($l3 == $デュラン && $l4 == $しんりゅう)				{$newname = $デスピサロ;}
if($l3 == $デスピサロ && $l4 == $キングレオ)			{$newname = $エスターク;}
if($l3 == $エスターク && $l4 == $ゴールデンスライム)	{$newname = $ミルドラース;}
if($l3 == $ミルドラース && $l4 == $デンタザウルス)		{$newname = $ミルドラース変身;}
if($l3 == $バラモス && $l4 == $ダークホーン)			{$newname = $ムドー;}
if($l3 == $ゾーマ && $l4 == $ミルドラース)				{$newname = $デスタムーア;}
if($l3 == $デスタムーア && $l4 == $さそりアーマー)		{$newname = $デスタムーア変身;}
if($l3 == $デスタムーア変身 && $l4 == $ムドー)			{$newname = $デスタムーア最終;}
if($l3 == $デスタムーア最終 && $l4 == $わたぼう)		{$newname = $ダークドレアム;}
if($スライム系A && $l4 == $デスファレーナ)				{$newname = $バブルスライム;}
if($スライム系A && $l4 == $ポイズンリザード)			{$newname = $バブルスライム;}
if($スライム系A && $l4 == $マッドプラント)				{$newname = $ホイミスライム;}
if($スライム系A && $l4 == $ファーラット)				{$newname = $ホイミスライム;}
if($スライム系A && $l4 == $ファンキーバード)			{$newname = $ホイミスライム;}
if($スライム系A && $l4 == $マネマネ)					{$newname = $ホイミスライム;}
if($スライム系A && $l4 == $アルミラージ)				{$newname = $スライムファング;}
if($スライム系A && $l4 == $パオーム)					{$newname = $スライムファング;}
if($スライム系A && $l4 == $スカルガルー)				{$newname = $スラッピー;}
if($スライム系A && $l4 == $ばくだんいわ)				{$newname = $ストーンスライム;}
if($スライム系A && $l4 == $ゴーレム)					{$newname = $ストーンスライム;}
if($スライム系A && $l4 == $キラーマシーン)				{$newname = $スライムボーグ;}
if($スライム系A && $l4 == $メタルドラゴン)				{$newname = $メタルスライム;}
if($l3 == $ぶちスライム && $l4 == $ぶちスライム)		{$newname = $ぶちキング;}
if($スライム系A && $l4 == $ずしおうまる)				{$newname = $キングスライム;}
if($l3 == $ぶちキング && $l4 == $ユニコーン)			{$newname = $キングスライム;}
if($l3 == $メタルスライム && $l4 == $メタルスライム)	{$newname = $はぐれメタル;}
if($l3 == $はぐれメタル && $l4 == $はぐれメタル)		{$newname = $メタルキング;}
if($l3 == $ぶちキング && $l4 == $メタルドラゴン)		{$newname = $メタルキング;}
if($l3 == $キングスライム && $l4 == $メタルドラゴン)	{$newname = $メタルキング;}
if($l3 == $メタルキング && $l4 == $メタルキング)		{$newname = $ゴールデンスライム;}
if($ドラゴン系A && $l4 == $ピッキー)					{$newname = $コドラ;}
if($l3 == $ドラゴンキッズ && $l4 == $ドラゴンキッズ)	{$newname = $ドラゴン;}
if($ドラゴン系A && $l4 == $バブルスライム)				{$newname = $キングコブラ;}
if($ドラゴン系A && $l4 == $ガップリン)					{$newname = $アンドレアル;}
if($l3 == $スカイドラゴン && $l4 == $ゴーレム)			{$newname = $アンドレアル;}
if($ドラゴン系A && $l4 == $おおにわとり)				{$newname = $とさかへび;}
if($ドラゴン系A && $l4 == $きりきりバッタ)				{$newname = $リザードフライ;}
if($ドラゴン系A && $l4 == $ぐんたいガニ)				{$newname = $デンタザウルス;}
if($ドラゴン系A && $l4 == $ストロングアニマル)			{$newname = $ドラゴンマッド;}
if($ドラゴン系A && $l4 == $ミステリードール)			{$newname = $おおイグアナ;}
if($ドラゴン系A && $l4 == $ライオネック)				{$newname = $バトルレックス;}
if($ドラゴン系A && $l4 == $ヘルコンドル)				{$newname = $ライバーン;}
if($l3 == $リザードマン && $l4 == $ライオネック)		{$newname = $ライバーン;}
if($l3 == $とさかへび && $l4 == $とさかへび)			{$newname = $ウィングスネーク;}
if($ドラゴン系A && $l4 == $ぶちキング)					{$newname = $グレイトドラゴン;}
if($ドラゴン系A && $l4 == $キングスライム)				{$newname = $グレイトドラゴン;}
if($ドラゴン系A && $l4 == $メタルキング)				{$newname = $グレイトドラゴン;}
if($l3 == $ドラゴン && $l4 == $バトルレックス)			{$newname = $グレイトドラゴン;}
if($l3 == $ウィングスネーク && $l4 == $ウィングスネーク)	{$newname = $コアトル;}
if($l3 == $プテラノドン && $l4 == $あくまのきし)			{$newname = $コアトル;}
if($ドラゴン系A && $l4 == $ひくいどり)						{$newname = $スカイドラゴン;}
if($l3 == $アンドレアル && $l4 == $メドーサボール)			{$newname = $やまたのおろち;}
if($l3 == $グレイトドラゴン && $l4 == $メドーサボール)		{$newname = $やまたのおろち;}
if($l3 == $スカイドラゴン && $l4 == $やまたのおろち)		{$newname = $しんりゅう;}
if($けもの系A && $l4 == $ダックカイト)						{$newname = $ももんじゃ;}
if($けもの系A && $l4 == $きりかぶおばけ)					{$newname = $おおきづち;}
if($けもの系A && $l4 == $ひとくいサーベル)					{$newname = $キラースコップ;}
if($けもの系A && $l4 == $リザードフライ)					{$newname = $フェアリーラット;}
if($けもの系A && $l4 == $ドラゴン)							{$newname = $キラーパンサー;}
if($l3 == $ミノーン && $ドラゴン系B)						{$newname = $アントベア;}
if($けもの系A && $l4 == $マッドロン)						{$newname = $スーパーテンツク;}
if($けもの系A && $l4 == $ガメゴン)							{$newname = $アイアンタートル;}
if($けもの系A && $悪魔系B)									{$newname = $グリズリー;}
if($けもの系A && $l4 == $オーク)							{$newname = $イエティ;}
if($けもの系A && $l4 >= $キラーマシーン && $l4 <= $ゴールデンゴーレム)	{$newname = $ストロングアニマル;}
if($けもの系A && $l4 == $デッドペッカー)					{$newname = $キラーエイプ;}
if($けもの系A && $l4 == $ドラゴスライム)					{$newname = $ゴートドン;}
if($けもの系A && $l4 == $スライムファング)					{$newname = $ユニコーン;}
if($けもの系A && $l4 == $スラッピー)						{$newname = $ユニコーン;}
if($けもの系A && $l4 == $おおめだま)						{$newname = $ビックアイ;}
if($l3 == $キラーエイプ && $l4 == $キラーエイプ)			{$newname = $パオーム;}
if($l3 == $パオーム && $l4 == $パオーム)					{$newname = $キングレオ;}
if($けもの系A && $l4 == $キラーマシーン)					{$newname = $キングレオ;}
if($l3 == $ピッキー &&  $スライム系B)						{$newname = $ドラキー;}
if($l3 == $おおにわとり && $l4 == $おおにわとり)			{$newname = $おおにわとり;}
if($鳥系A && $物質系B)										{$newname = $ミストウイング;}
if($鳥系A && $ドラゴン系B)									{$newname = $キメラ;}
if($l3 == $あばれうしどり &&  $けもの系B)					{$newname = $モーザ;}
if($鳥系A && $l4 == $ストーンスライム)						{$newname = $ガンコどり;}
if($鳥系A && $l4 == $ドロル)								{$newname = $キラーグース;}
if($鳥系A && $l4 == $ネジまきどり)							{$newname = $ヘルコンドル;}
if($鳥系A && $l4 == $ダンスキャロット)						{$newname = $ファンキーバード;}
if($鳥系A && $l4 == $ギズモ)								{$newname = $ひくいどり;}
if($鳥系A && $l4 == $ひょうがまじん)						{$newname = $ホークブリザード;}
if($鳥系A && $l4 == $イエティ)								{$newname = $ホークブリザード;}
if($l3 == $ダックカイト && $l4 == $ゴートドン)				{$newname = $ホークブリザード;}
if($鳥系A && $l4 == $ライバーン)							{$newname = $ロックちょう;}
if($l3 == $モーザ && $l4 == $うごくせきぞう)				{$newname = $ロックちょう;}
if($l3 == $ロックちょう && $l4 == $ギズモ)					{$newname = $サンダーバード;}
if($l3 == $ホークブリザード && $l4 == $ひくいどり)			{$newname = $にじくじゃく;}
if($l3 == $ゴーレム && $l4 == $ゴーレム)					{$newname = $うごくせきぞう;}
if($l3 == $ソードドラゴン && $l4 == $ユニコーン)			{$newname = $グレイトドラゴン;}
#新規モンスターここから
#スライム
if($list3 == 20 && $list4 == 20)                                 {$newname = 217;}
if($list3 == 217 && $list4 == 217)                               {$newname = 218;}
if($list3 == 218 && $list4 == 218)                               {$newname = 219;}
#せいれい
if($list3 == 220 &&  $list4 == 221)                              {$newname = 224;}
if($list3 == 221 &&  $list4 == 220)                              {$newname = 224;}
if($list3 == 222 &&  $list4 == 223)                              {$newname = 225;}
if($list3 == 223 &&  $list4 == 222)                              {$newname = 225;}
#らきすた
if($list3 == 219 &&  $list4 == 224)                              {$newname = 226;}
if($list3 == 209 &&  $list4 == 225)                              {$newname = 227;}
if($list3 == 227 &&  $list4 == 1)                                {$newname = 228;}
if($list3 == 110 &&  $list4 == 216)                              {$newname = 229;}
if($list3 == 227 &&  $list4 == 228)                              {$newname = 230;}
if($list3 == 226 &&  $list4 == 139)                              {$newname = 231;}
if($list3 == 223 &&  $list4 == 226)                              {$newname = 232;}
if($list3 == 220 &&  $list4 == 215)                              {$newname = 233;}
if($list3 == 206 &&  $list4 == 110)                              {$newname = 234;}
if($list3 == 224 &&  $list4 == 226)                              {$newname = 235;}
if($list3 == 227 &&  $list4 == 76)                               {$newname = 236;}
if($list3 == 229 &&  $list4 == 20)                               {$newname = 237;}

if($newname eq ""){$newname = $Kimg[$haigou1];}

open(FH,"$monsdata") || &error("Can't open $monsdata");
@lines = <FH>;
close(FH);

foreach $line (@lines) {
  ($Mimg,$Mcname,$Mkou,$Mmam,$Msub,$Mhp,$Mmp,$Mex,$Mmoney,$Mtoku,$pp) = split(/<>/,$line);
  if($newname == $Mimg){
  $newmons  = $Mcname;
  last;}
  }

&header;

print <<"EOF";
<CENTER>
<B><FONT face="Times New Roman" color="#000000" size="5">MONSTER Farm</FONT></B>
<BR>
<BR>
<TABLE bgcolor="#000000">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff" width="250"><FONT color="#000000" size="5"><B>ベース</B></FONT></TD>
<TD align="center" width="50" bgcolor="#000000"></TD>
<TD align="center" bgcolor="#ffffff" width="250"><FONT color="#000000" size="5"><B>材  料</B></FONT></TD>
</TR>
<TR>
<TD align="center" bgcolor="#ffffff" width="250"><FONT face="Times New Roman" color="#0000cc" size="5"><B>$itemlist[$list3]</B></FONT></TD>
<TD align="center" width="50" bgcolor="#000000">
<HR>
</TD>
<TD align="center" bgcolor="#ffffff" width="250"><FONT face="Times New Roman" color="#ff0000" size="5"><B>$itemlist[$list4]</B></FONT></TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center" width="250" height="52"><IMG src="$imgpath/$list3.gif" border="0"></TD>
<TD align="center" width="50" bgcolor="#000000" height="52">
<HR>
</TD>
<TD align="center" bgcolor="#ffffff" width="250" height="52"><IMG src="$imgpath/$list4.gif" border="0"></TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<HR>
<B><FONT face="Times New Roman" color="#000000" size="5"><U>NEW MONSTER</U></FONT></B><BR>
<TABLE bgcolor="#000000">
<TBODY>
<TR>
<TD align="center" bgcolor="#ffffff"><B><FONT face="Times New Roman" color="#0000cc" size="5">$newmons</FONT></B></TD>
</TR>
<TR>
<TD bgcolor="#ffffff" align="center" height="52"><IMG src="$imgpath/$newname.gif" border="0"></TD>
</TR>
</TBODY>
</TABLE>
<BR>
<BR>
<FORM ACTION="$cgiurl" METHOD="POST">
<BLOCKQUOTE>
<INPUT type="submit" value="配合 OK!">
<INPUT type="hidden" name="mode" value="hensin">
<INPUT type="hidden" name="newmonster" value= $newname>
<INPUT type="hidden" name=name value= $inname>
<INPUT type="hidden" name=password value= $inpass>
<INPUT type="hidden" name=haimoney value= $Omoneys>
<INPUT type="hidden" name=haigou1 value= $haigou1>
<INPUT type="hidden" name=haigou2 value= $haigou2>
<INPUT type="hidden" name=img1 value= $list3>
<INPUT type="hidden" name=img2 value= $list4>
</FORM>
</BLOCKQUOTE>
<FORM ACTION="$cgiurl" METHOD="POST">
<INPUT type="submit" value="キャンセル">
<INPUT type="hidden" name="mode" value="">
</FORM>
<BR>
</CENTER>
EOF

&footer;
