# Django Web App 作成 ~ Heroku -> Deploy

1. Python Django を用いて web app 開発
2. Material Design Bootstrap を用いた Design
3. Heroku, GitHub, AWS S3 を用いて、世界に service を公開
## 1. 環境構築と初期設定
- 仮想環境とdjango install と upgrade
### 1. 仮想環境構築
    python3 -m venv venv
### 2. 仮想環境を立ち上げる
    source venv/bin/activate
### 3. django install
    pip install django
### 4. django upgrade
    pip install --upgrade pip
### 5. プロジェクト名
    django-admin startproject < directory名 > .
- directory 名はその時によって変更
### 6. プロジェクト directory に降りて下記のコマンド実行
    python manage.py runserver
- Starting development server at http://127.0.0.1:8000/
- server が立ち上がっている事を確認
### 7. runserver (127.0.0.1.:8000)
    localhost:127.0.0.1.:8000
- brawer にアクセスする
- localhost = 127.0.0.1.:8000 = 自分の PC brawser
- 8000 = ポート
- Quit the server with CONTROL-C
  - CONTROL-Cでサーバーを終了する
### 8. App 作成
    python manage.py startapp < app名 >
## 2. setting file
### 1. settings.py に app を作成した事を記述する
- INSTALLED_APPS に 'myapp', を記述
- LANGUAGE_CODE = 'ja'
- TIME_ZONE = 'Asia/Tokyo'
### 2. project urls.py file に path 追加
- path(' ', include('myapp.urls')),　
- include method も import する
  -  '  ' に admin 以外が入った場合に、いかなる場合でも app の url を呼び出す
### 3. App urls.py file に記述
    from django.urls import path, include
    from . import views

    app_name = 'myapp'

    urlpatterns = [
        path('', views.Index, name='index'),
    ]
### 4. App views.py file に記述
    from django.http import HttpResponse

    def Index(reqest):
        return HttpResponse("hello")
### 5. server 立ち上げ
- top page 確認
## 3. directory と html file 作成
- myapp の下層に templates/myapp/indx.html を作成
### 1. material desgin bootstrap  node.js install
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
> https://github.com/nvm-sh/nvm
- nvm (Node Version Manager) install
### 2. install されているか確認
    nvm --version
### 3. node.js version 確認
    nvm ls-remote
- 緑色になっている所： Latest LTS:(最新ver)
  - Long Term Support(安定版)
- node.js page でも最新ver を確認する
> https://nodejs.org/en/
### 4. 最新の安定版を install
    nvm install 14.17.1
### 5. nvm ls コマンドで確認
    nvm ls
- node -> stable (-> v14.17.1) (default)
- default -> 14.17.1 (-> v14.17.1)
### 6. node の version も確認
    node --version
- v14.17.1
- Node.js install 完了！！
### 7. 手動 install zip packaeg
> https://mdbootstrap.com/docs/standard/getting-started/installation/
- index.html の不要なスタイルなどを削除する
- CDN
  - CDNを介したインストールは、MDB UIKITをプロジェクトに統合する最も簡単な方法の1つです。最新のコンパイル済みJSスクリプトタグとCSSリンクタグをcdnjs からアプリケーションにコピーする
  - CSS, JS 両方を copy & ps
### 8. jumbotron と Cards
> https://mdbootstrap.com/docs/standard/navigation/headers/
### 9. base.html と index.html を分けて関連づける
- 重複する記述をなくす
## 4. post model 作成
### 1. data base の初期設定
    python manage.py migrate
### 2. user 作成
    python manage.py createsuperuser
- superuser (なんでもできる全権限をもったuser)を作成する必要がある
- user名, メール(アドレスは認証には使わないので適当でよい), password を入力
- runserver で確認 : http://127.0.0.1:8000/admin/
### 3. post model 作成
- class based view で作成
- App models.py file に Blog に必要な model を作成していく
### 4. makemigrations
    python manage.py makemigrations

    python manage.py migrate
- Applying myapp.0001_initial... OK
- runserver で http://127.0.0.1:8000/admin/  確認
## 5. django と CRUD の繋がり
### 1.Views.py の記述はシンプル
- CreateView : Create (作成する
  - class PostCreate
- DetailView : Read (読み込む『情報を取る』)
  - class PostDetail
- UpdateView : Update (更新する)
  - class PostUpdate
- DeleteView : Delete (削除する)
  - class PostDelete
- django で元々用意されている View を継承する事により、非常に少ない記述で実装できる
### 2. post_form.html
- post_form.html は django が自動で post の更新・登録をする時にこの html を使用してくれる。認識してくれる
### 3. messages
- django で準備されているメッセージフレームワーク
  - 機能をパッケージしたもの
> https://docs.djangoproject.com/ja/3.2/ref/contrib/messages/
- 何かしらの action 後にメッセージを表示してくれる
  - 色々なメッセージの性質がある
    - info(情報), success(成功), warning(警告), debug(設計ミス)
  - MDBootstrap と合わせて使用できる(表示のメッセージの color など)
### 4. django 独自の code 記述
#### urls.py と link button の関係
      <a href="{% url 'myapp:post_detail' item.pk %}">{{ item.title }}</a>
- {% %}　->　django のロジック使用・文法的な事を行う時に使用する
  - urls.py　->　views.py　->　post_detail.html に遷移する
- {{    }}　->　django の database の値を表示する時に使用する
  - data を取ってきて表示する場合に使う
## 6. login, logout 機能を付ける
### 1.機能実装
- AuthenticationForm
  - 上記を呼び出す事により機能を継承して、重複する機能は記述せずに実装できる
  - 認証の昨日の form を呼び出す
### 2. LoginView・LogoutView
    #  login 機能の追加
    LOGIN_URL = 'myapp:login'
    LOGIN_REDIRECT_URL = 'myapp:index'
- setting.py file に上記を記述
  - login 画面 URL, login.html, urls.py, views.py に記述
  - login 後の遷移画面 index.html (top page)
### 3. login, logout 切り替え
- if文を使用して表示の切り替え
### 4. user 登録機能実装
- UserCreationForm
  - 色々な User が登録できるよにする
### 5. django での if文記述
    {% if.... %}
        .....

    {% elif %}
        .....

    {% else %}
        .....

    {% endif %}
### 6. Login している、していないの切り分け(myapp/base.html)
    {% if request.user.is_authenticated %}
        <li><a class="dropdown-item" href="">{{ request.user }}</a> </li>
        <li><a class="dropdown-item" href="{% url 'myapp:logout' %}">ログアウト</a></li>
    {% else %}
        <li><a class="dropdown-item" href="{% url 'myapp:login' %}">ログイン</a></li>
        <li><a class="dropdown-item" href="{% url 'myapp:signup' %}">ユーザー登録</a></li>
    {% endif %}
- request.user で login している user を取得する
  - .is_authenticated (login しているかしていないか)
    - login している user が認証している場合は True
    - 認証していない場合は False
## 7. User Login, Loguout 機能の切り分けと実装
### 1. login しないとできない機能を実装
    from django.contrib.auth.mixins import LoginRequiredMixin

    class PostCreate(LoginRequiredMixin, CreateView):
        model = Post
        form_class = PostForm
        success_url = reverse_lazy('myapp:index')
- class based view の場合
  - 1行の import と 引数に **LoginRequiredMixin** を記述するだけ
  - PostUpdate, PostDelete の引数にも **LoginRequiredMixin** 追加
  - **注意点は引数の Create View の前に記述する事** そうでないと error が出てしまう。※ error の表示も分かりづらいので注意する
- mixin(ミックスイン)
  - 多重継承
### 2. User 制限実装
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
- models.py file に記述
- ForeignKey で user との紐付けを定義
- user 間での削除防止策
  - on_delete=models.PROTECT
### 3. models.py を編集した場合は必ず下記コマンドを実施
    python manage.py makemigrations
- database に反映する data が作られただけ。migrations file に追記されただけ
- myapp/migrations/0002_post_author.py
  - Add field author to post
### 4. migrate を実行で database に保存される
    python manage.py migrate
- Applying myapp.0002_post_author... OK
- これで登録完了
### 5. class PostCreate に記述
        def form_valid(self, form):
            form.instance.author_id =self.request.user.id
            return super(PostCreate, self).form_valid(form)
- form の入力に error がなければ実行
  - タイトルと内容：title, content
- 今ログインしている author(user) に id を付与する
- PostCreate の内容を上書き
### 6. 自分の投稿だけの更新・削除の実装
    from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

    class OnlyMyPostMixin(UserPassesTestMixin):
        raise_exception = True
        def test_func(self):
            post = Post.objects.get(id = self.kwargs['pk'])
            return post.author == self.request.use
- views.py file に記述
- **UserPassesTestMixin** : django が元々持っている mixin
  - UserPassesTestMixin を継承して original の class を作成
0. raise_exception = True : 例外処理をするかどうか
1. False の場合 403 error が表示される
2. True の場合は test func の中で 今開いている記事を post に代入しまする
3. その post(記事の記述者 : author) と今ログインしている author(user) が同じかどうか (True か False か)
   - False の場合は例外処理なので 403 error になる
4. **OnlyMyPostMixin** を PostUpdate, PostDelete の引数にも追加
5. 現在記述されている **LoginRequiredMixin**  と意味が重なってしまうので **LoginRequiredMixin** は削除して **OnlyMyPostMixin** を記述する
  - **注意点は引数の View の前に記述する事** そうでないと error が出てしまう。※ error の表示も分かりづらいので注意する
5. server で確認
- 更新・削除で確認 **403 Forbidden** が出れば成功
  - 禁止ですよの表示
### 7. **403 Forbidden** UI を編集
- templates/403.html file を作成する
  - django が templat folder を読み込む順番を加味する為
  - 403.html はどの project でも使用するので template folder 直下で作成する
- 中身は、login.html をcp & ps で form の内容は削除する
## 8. お気に入りButton
- post_detail.html にお気に入り Button 追加
- 投稿に対してお気に入りに入れる機能を実装
  - お気に入り管理 model
  - お気に入りが重複しないように実装
### 1. models.py file に下記を記述
    class Like(models.Model):
        post = models.ForeignKey(Post, verbose_name='投稿', on_delete=models.PROTECT)
        user = models.ForeignKey(User, verbose_name='Likeしたユーザー', on_delete=models.PROTECT)
### 2. models.py を編集した場合は必ず下記コマンドを実施
    python manage.py makemigrations
### 3. migrate を実行で database に保存される
    python manage.py migrate
### 4. views.py に記述
    def Like_add(request, post_id):
        post = Post.objects.get(id = post_id)
        like = Like()
        like.user = request.user
        like.post = post
        like.save()

        messages.success(request, 'お気に入りに追加しました')
        return redirect('myapp:post_detail', post.id)
- Like の import も忘れずに
### 5. urls.py に記述
    path('like/<int:post_id>', views.Like_add, name='like_add'),
- function based view なので、as_view（）の記述はいらない
- views.Like_add が読み込まれると view の Like_add 関数が読み込まれる
### 6. post_detail.html に記述
    <a href="{% url 'myapp:like_add' object.pk %}" class="btn btn-light" data-mdb-ripple-color="dark">お気に入り</a>
- **{% url 'myapp:like_add' object.pk %}**
  - 実際にはお気に入りをクリックした後は記事の詳細画面にそのまま止まる
  - object.pk　->　post_detail(post) の id を呼び出す
  - なので myapp: の後ろの記述は **like_add** になる
    - urls.py  の name= 'like_add'
### 6. decorator を function based view に付ける
    from django.contrib.auth.decorators import login_required

    @login_required
    def Like_add(request, post_id):
        post = Post.objects.get(id = post_id)
        is_like = Like.objects.filter(user = request.user, post = post_id).count()
        if is_like > 0:
            messages.warning(request, '既にお気に入りに追加済です')
            return redirect('myapp:post_detail', post.id)
- @login_required 役割
  - Login している場合に Like_add が動く。Logout だと動かない
  - login required は django が用意している機能
1. post に post_detail の id を代入する
2. is_like に filter(条件記述：条件に合わせた data を取得してくる) を代入
   - and 条件：２つの条件を　, (カンマ)で結ぶ
   - 条件が２つが満たされたら data が抽出される
3. if 文の内容は下記
- user id と post id に一致するものがある場合には、お気に入りに登録している事を知らせる
### 7. Like_add の続き
            like = Like()
            like.user = request.user
            like.post = post
            like.save()
            messages.success(request, 'お気に入りに追加しました')
            return redirect('myapp:post_detail', post.id)
1. Like() model 空の箱 data を like に代入する
2. request.user(今ログイン中のuser), post(post id)
3. Like(request.user, post の data が入る)
4. save で Like の箱に data が保存される
5. message で、お気に入りに追加したことを知らせる
6. 関数を記述する時は、必ず return を付ける
7. return.redirect (遷移する page 記述)
# DB migrate error 問題
- models.py file のタイポに気づかず migrate してしまった…
  - makemigrations -> migrate をしてしまい、models.py file を修正して直して migrate しても error がでて migrate 出来ない
### 0. アプリ内の「migrations」フォルダの error table 削除
- わからなければ「__init__.py」以外の「.py」ファイルを削除
### 1. error 確認
    sqlite3.OperationalError: table "myapp_post" already exists
sqlite3 操作上のエラー：テーブル「myapp_post」がすでに存在します
### 2. db.sqlite3を操作してエラーが起きているテーブルを削除
    python manage.py dbshell
### 3. table 一覧表示
    .tables
### 4. error table 削除
    drop table myapp_post;
- drop table < table名 >；
  - セミコロンを忘れずに記述
### 5. 削除されているか確認
    .tables
### 6. sqlite3 から抜ける
 - Crt + C で抜ける
### 7. makemigrations と migrate をやり直す
- これで完了！！ error 解決
## 9. カテゴリ を実装する
1. カテゴリ model を定義
2. Post に対してカテゴリを紐付ける
3. カテゴリの一覧画面を作成
4. カテゴリ詳細 page で、そのカテゴリの記事を一覧表示
5. Post の詳細画面で、同じカテゴリに属する他の記事を表示する
### 1. models.py file 記述
1. class Category(models.Model): 作成
2. python manage.py makemigrations
3. python manage.py migrate
4. database に反映させる
5. class Post(models.Model): と紐付け
6. category = models.ForeignKey('Category', on_delete=models.PROTECT)
7. makemigrations で default で 1を設定
8. migrate はまだ出来ない category が１つもないから
- runserver で管理画面で category を作成してしまう
9. migrate ができる。もう一度 runserver で確認する
## 10.画像表示の実装
1. pillow の ライブラリ install
2. Post model に Thumbanail(サムネイル)を追加
3. setting.py で画像の場所を設定(media)
4. 画像がない場合の設定
    - 画像がないと error になってしまうので、無かった場合の設定を if 文で追記していく
5. enctype="multipart/form-data" を form タグに入れる
   - 上記がないと画像 file を入れる時に error になってしまう
   - 新規登録画面で画像を登録しようとしたら、その画面を表示する .html file の form tag には必ず必要になってくるので覚えておく
- 画像を表示させる為には色々と細かい設定があって error も出やすいので1つ1つしっかり確認しながら実装していく
### 1. 仮想環境に pillow
    pip install pillow
- python の program 群を拡張する機能
### 2. post model に画像を保持する項目を作成
    thumbnail = models.ImageField(upload_to='images/', blank=True)
1. models.py file の class Post に上記を追記
   - thumbani(サムネイル)：親指のつめ、非常に小さいもの
   - お試し縮小表示画像のこと
   - 実際に開かなくても中身が何となく分かるように、その内容（の一部）を縮小表示した画像のこと
2. database に反映させる
3. makemigrasions
4. migrate
### 3. thumbnail で扱う画像設定
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
- media の保存先を setting.py file に記述する
  - 上記を記述
  - **import os** を忘れずに記述すること！！
  - os.path.join(BASE_DIR, 'media') が読み込めずに error になるので…
- media directory 作成。その直下に images directory も作成
### 4. 投稿画面で media を選択可能にする
    class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'content', 'category', 'thumbnail')
1. forms.py file の class PostForm に thumbnail を追記
- post_form.html の中にfields = ('title', 'content', 'category', 'thumbnail')
   - fields に記載したものが {{ form.〇〇〇〇 }} のようにして反映できる
- post_form.html file に {{ form.thumbanil }} を追記
### 5. index.html に if文を記述
    {% if item.thumbnail %}
    <img src="{{ item.thumbnail.url }}" class="img-fluid" alt="{{ item.title }}" />
    {% else %}
    <img src="https://mdbootstrap.com/img/new/standard/nature/111.jpg" class="img-fluid" alt="{{ item.title }}" />
    {% endif %}
    <a href="{% url 'myapp:post_detail' item.id %}">
        <div class="mask" style="background-color: rgba(251, 251, 251, 0.15);"></div>
    </a>
1. このままでは、まだ画像が表示されない
   - Page not found (404)
### 6. setting.py file に追記 (画像を表示させる為には必須)
    'django.template.context_processors.media',
1. TEMPLATES -> 'context_processors' に上記を追記する
2. link error で画像がまだ表示されない
### 7. project urls.py file に下記を記述
    from django.conf import settings
    from django.conf.urls.static import static

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
- static : 静的 file (css file, image file などをおく場所)
  - 常に link として参照されるものを static folder に置く
- この形で media file も存在させる必要がある
- DEBUG = True
  - DEBUG(デバック) : True は error の時に error message がしっかりと表示される
  - **fileの paht も出てしまうので、本番環境では True にしてはいけない！！**
  - False だと server error ような形になって検証しようが無くなる
## 10. 検索機能
- ナビゲーションバーにあるsearch box で freeword 検索
- 記事タイトルか内容にその言葉が含まれればヒット
1. forms.py に class SearchForm 作成
2. views.py に funcion based views を記述
   - import SearchForm
   - form django.db.models import Q
   - **Q** は filter の or 検索の時に使用するもの
3. urls.py に paht を記述する
   path('search', views.Search, name='search'),
4. base.html に search box 作成
### form 記述
    <form action="{% url 'myapp:search' %}" class="d-flex input-group w-auto" method="POST">
        {% csrf_token %}
        <input type="search" id="form1" class="form-dark form-control" aria-label="Search" name="freeword" />
    </form>
- {% url 'myapp:search' %} で url と紐付け
- method　->　GET : page を参照するだけ
- method　->　POST : data に対して処理や検索をかける場合に使用
- form の場合は必ず **{% csrf_token %}** を記述すること
  - django で error が出ないようにする為
### views.py func 抜粋
    if searchform.is_valid():
            freeword = searchform.cleaned_data['freeword']
            search_list = Post.objects.filter(Q(title__icontains = freeword)|Q(content__icontains = freeword))

    params = {
        'search_list': search_list,
    }

    return render (request, 'myapp/search.html', params)
- filter(Q(title__icontains = freeword)|Q(content__icontains = freeword))
  - or文の記述 or の区切りは、｜（パイプライン）を使用
  - ['freeword'] ＝ search 検索で入力された文字
- **title(記事タイトル) に freeword が入っているかどうか？または、content(記事の内容) に freeword が入っているかどうか？**
- どちらか一方が当てはまれば search_list にそれが代入される
  - .filterにしている理由は複数のdataが入るから
  - .get にしていると場合によっては error になってしまう（1つのdataしか取得できないから。取得できない場合でも error になってしまう)
## 11. 組み込みフィルターの実装
1. HTML tag を反映させる
2. top page の内容を一部を表示して、それ以上は「続きを読む」としてクリックを促す
3. Post 内容に URL を書いた時に、link が機能するようにする
4. Post 内容で改行を反映されるようにする
### 0. 組み込みフィルター記述について
    {{ object.content|safe }
    {{ object.content | safe | linebreaksbr | urlize }}
- | (パイプライン) の前後はスペースがあってもなくてもどちらでも良い
- **codeの読みやすさを考えて 半角スペースは入れる事！！** ※ 入れなくても機能自体は動く
### 1. django 独自の組み込みフィルター
> https://docs.djangoproject.com/ja/3.0/ref/templates/builtins/
- **safe**
  - 文字列に対して HTML tag を使用することができる
  - content(内容)記述で、太文字や改行、見出しetc... が使用できる
- {{ object.content|safe }
### 2. top page の内容表示(文字数)コントロール
- **truncatechars**(トランケイトチャーズ)
  - {{ item.content|safe|truncatechars_html:12 }}
  - top page の content(内容）表示が12文字になる
  - １２文字以降が.....表示になる
  - **truncatechars** というもの同じ機能なので使用はできるが、html tag と併用する場合には tag が閉じられる前に文字数制限されると、レイアウトが崩れてしまう。safe を使用する場合には **truncatechars_html** を使用する
### 3. content (内容) を html tag がなくても改行ができるようにする
- **linebreaksbr**(ラインブレイクスビーアール)
  - content(内容)の中すべての改行を、HTMLの改行（< br >）に変換
  - {{ object.content|safe|linebreaksbr }}
  - なのでわざわざ br tag を使用しなくてもよい
  - linebreaks というのもあるが、こちらは 改行を、HTMLの改行（< br >）に変換、その他全て< p > タグに変換されてしまうので safe を使用する場合は **linebreaksbr** を使用する
### 4. content(内容) 内での URL の反映（Linkの反映）
- **urlize**
  - テキスト内の URL と Email アドレスをクリック可能なリンクに変換
- **urlizetrunc**
  - urlize と同じように、URL と　email アドレスをクリック可能なリンクに変換。ただし、指定の文字数以上の表示を切り詰める
  - 引数: URL を切り詰める長さ。省略記号の長さを含み、省略記号は省略が必要な場合につけられる
- {{ object.content | safe | linebreaksbr | urlize }}
## 12. site 共有設定 App 追加
1. site 共通設定 App
2. site 共通設定を保持する model 作成
3. 管理画面から site 共通設定を入力し、実際に適用されているか確認
### site 管理をなぜ App 化するのか？
- 例
  - site のタイトルを管理 App で設定可能にすると
    - 簡単に admin の管理画面から変更できる
  - もし App 化してなければ、source code を変更して運用しなけれならない。とても手間がかかる
- 製品(本番環境)では、必須でとても便利な機能なので実装する
### 0. django の site フレームワークで共通の設定を実装
> https://docs.djangoproject.com/ja/3.2/ref/contrib/sites/
### 1. terminal から app 作成
    python manage.py startapp sitemanage
### 2. myproject の setting.py に記述
    INSTALLED_APPS = [
    'django.contrib.sites',
    'sitemanage',
    ]

    SITE_ID = 1

    MIDDLEWARE = [
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    ]
- 上記を追記して sitemanage App を使用できるようにする
### 3. site models.py file に記述
    from django.contrib.sites.models import Site

    class SiteConfig(models.Model):
        site = models.OneToOneField(Site, verbose_name='Site', on_delete=models.PROTECT)
        meta_title = models.CharField('meta_title', max_length=100)
        meta_description = models.CharField('meta_description', max_length=300)
        meta_keywords = models.CharField('SEOキーワード', max_length=300)
        author = models.CharField('管理者', max_length=30)
        top_title = models.CharField('TOPページタイトル', max_length=100)
        top_subtitle = models.CharField('TOPページサブタイトル', max_length=200)

        def __str__(self):
            return self.meta_title
1. makemigrations -> migrate
2. database に反映させる
### 4. site admin.py 記述
    from .models import SiteConfig
    from django.contrib.sites.models import Site


    @admin.register(SiteConfig)
    class SiteConfigAdmin(admin.ModelAdmin):
        list_display = ('id', 'meta_title', )
        list_display_links = ('meta_title', )
- これで管理画面（admin）の中で記述した項目を編集できるようになる
### 5. base.html, index.html に記述して 4. の設定が反映されるようにする
- {{ request.site.siteconfig.meta_title }}
- {{ request.site.siteconfig.top_title }}
- {{ request.site.siteconfig.top_subtitle }}
- 上記のように database から値をとてくるという方法を取ることによって、変更の手間が凄く簡単に楽になる
## 13. Category List page 整理
### 1. 組み込みとフィルタリング
- slice
- 表示数指定
- {% for post in category.post_set.all | slice:":5" %}
- カテゴリ一覧表示で 5件まで表示させる指定
> https://docs.djangoproject.com/ja/3.2/ref/templates/builtins/#built-in-filter-reference
### 実装例:
    {{ some_list|slice:":2" }}
- some_list が ['a', 'b', 'c'] ならば、出力は ['a', 'b'] となる
### 2. myapp に context processors.py file を作成
    from .models import Category

    def all_category(request):
        category_list = Category.objects.all()

        params = {
            'category_list': category_list,
        }

        return params
- 上記の記述により HTML に Caregory の全てのdata を反映できる
### 3. myproject setting.py filen に下記を記述する
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'myapp.context_processors.all_category',
                ],
            },
        },
    ]
- 'myapp.context_processors.all_category', を記述
### 4. base.html を編集
    {% for item in category_list %}
    <li><a class="dropdown-item" href="{% url 'myapp:category_detail' item.name_en %}">{{ item.name }}</a></li>
    {% endfor %}
    <li>
1. context processors.py を作成して function を記述し、この中で必要な data を取得する
2. それを setting.py の OPTIONS context_processors に記述し呼び出す事によって、全ての page (全ての view)に置いて funcion(all_category)を使用する事ができる
3. category list を loop で回す事によって全ての page で database から data を取得・表示する事ができる
### 5. 各 category の件数を表示させる
    def post_count(self):
        n = Post.objects.filter(category = self).count()
        return n
1. myapp models.py file class Category(models.Model): に funcion 追記
2. category_list.html に {{ category.post_count }} 追記
3. カテゴリ一覧表示に今現在の記事の件数が表示される
4. 今回は、DB への操作は行っていないので、makemigrations, migrate は必要ない
- DB は１つも変わっていない。HTML は model 内の項目をみて情報をとってくる
  - 取得の際に post_count があればとってくるし、DB にあればその情報を取得してくる。なければ error を返す
  - function or DB 項目どちらかの条件を満たせば, HTML 常に表示できる
#### **models.py に function(関数)として新しい項目を追加する事は、状況によっては非常に便利に多用できる機能
- makemigrations も migrate もいらない DB 操作もいらない
### 特殊な記述
    &nbsp;<small>[&nbsp; {{ category.post_count }}&nbsp;]</small>
- &nbsp; [&nbsp; A &nbsp; ] =>  [ A ] と表示される
### 6. pagenation(ページネイション)の作成
> https://docs.djangoproject.com/ja/3.2/topics/pagination/
