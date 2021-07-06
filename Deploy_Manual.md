# Heroku への Deploy
- **GitHub**
  - source code GitHub で管理
- **heroku**
  - web App の運用・構築・公開をする Pass(platform as a service)
##  deploy の手順(準備編)
1. 必要なライブラリーの install
   - gunicorn : (web server gateway interface)
     - web server と web app をつなげる役割をする
   - dj-batabase-url : heroku では sqlite3が使用できないので
     - posgreSQL を使用する databeas を変更する時に必要なのが dj-database-url
   - whitenoise : gunicorn に向けて file を配信するのを簡単にしてくれるライブラリ
     - gunicorn と セットで使用
2. requirements.txt の作成
   - heroku に必要なライブラリを示す file
   - requirements.txt の内容を確認して heroku が必要な ライブラリを install する
   - project folder 直下に作成する
3. runtime.txt の作成
   - project folder 直下に作成する
   - heroku に python の version を伝える為に作成する
4. Procfile の作成
   - 拡張子は無いが１つの file
   - project folder 直下に作成する
   - 頭文字が ' P ' 大文字になるので注意
   - どういった comand で  web app を起動するのか heroku に伝える
5. wsgi.py の編集
6. local_settings.py の作成
   - settings.py と同じ場所に作成
   - 記述内容は、local の仮想環境で開発してきた。その環境のみで動作する settings.py という位置付け file
7. settings.py の編集
   - 本番環境に対応できるように、記述内容を編集
8. static フォルダーと style.css の作成
9. .gitignore の作成
   - git 上で version 管理の対象としないものを記述する
10. local 環境の source code に対して git 導入する
## 1. venv (仮想環境)にライブラリ install
    # gunicorn install
    pip install gunicorn

    #  dj-database-url install
    pip install dj-database-url

    #  whitenoise install
    pip install whitenoise
### 1-1. version を指定して install する場合
    pip install gunicorn == 20.04
- 上記のように version を指定して install する
### 1-2. uninstall する場合は下記コマンドを実行
    pip uninstall gunicorn
### 2. requirements.txt の作成
    pip freeze > requirements.txt
- 記述内容は、今回はリソースをcp & ps
### 3. runtime.txt の作成
    python --version

    Python 3.9.5
- python の version を runtime.txt に記述する
  - python - 3.9.5
- - project folder 直下に作成する
### 4. Procfile の作成
    web: gunicorn myproject.wsgi
- project folder 直下に作成する
- 上記の内容を記述する
### 5. myproject の wsgi.py 編集
- 今回は リソースを cp & ps
### 6. local_settings.py の作成
- settings.py と同じ場所に作成
- settings.py の下記を cp & ps
  - import os
  - BASE_DIR
  - SECRET_KEY : ※ **基本的には非表示にする事**
  - DEBUG = True
  - DATABASES
### 7. settings.py の編集
- SECRET_KEY を削除
- MIDDLEWARE
  - 'whitenoise.middleware.WhiteNoiseMiddleware', を上から二行目に追記
- 一番下に heroku の為の記述を追記する(リソース cp & ps)
### 8. static フォルダーと style.css の作成
- BAIS_DIRE の階層に static folder 作成。その中に style.css file 作成。中身は空でOK
### 9. .gitignore の作成
- 今回はリソース cp & ps
- git 導入
## 2. deploy 手順 (heroku編)
1. heroku CLI の install (heroku site から)
2. heroku で設定した app とローカルの source を紐付け
3. heroku に push
4. heroku で Dyno を起動
5. heroku で migrate
6. heroku で superuser 作成
7. heroku を開く
- 上記の作業は仮想環境内で行う
### 1. heroku CLI の install (heroku site から)
    brew tap heroku/brew && brew install heroku
### 2. heroku で設定した app とローカルの source を紐付け\
    heroku login

    heroku git:remote -a django-blog-app-moto-labo

    git remote
- heroku , origin が出ていれば完了
### 3. この時点で heroku の setting へ
- Config Vars : key , value を入力
  - local_settings.py で記述した SECRET_KEY =  ' '(シングルコーテーション)の中身を入力
### 4. git に push
    git push heroku main
## python version 問題...
> https://devcenter.heroku.com/articles/python-support
- heroku が python 3.9.5 をサポートしていない…
- venv の python version 変更
### 1.  brew upgrate
    brew upgrate
### 2.  pyenv version 確認
    pyenv versions

    # install できる version 一覧表示
    pyenv install --list
### 3. pyenv install
    pyenv install 3.9.6

    # version 切り替え・登録
    pyenv global 3.9.6

    # python --version 確認
    python --version
### 4.  仮想環境のバージョンを切り替え
    # 仮想環境からでる
    deactivate
### 5.  --clera potion 使用
    python3 -m venv --clear venv
### 6. 仮想環境に入る
    source venv/bin/activate
- version 3.9.6 に変更になっている
- v3.9.6 (venv)
## python の version 問題ではなかった…
> https://devcenter.heroku.com/articles/python-support
- version 変更しても同じ error ・・・？
- よくよく調べたら
  - **runtime.txt** の python version の記述の仕方がよくなかっただけ…
  - Supported runtimes
  - python-3.9.6
  - お使いのPythonバージョンはherokuスタック20でサポートされていません-**実行時のPythonバージョンが小文字**であることを確認してください
- **python-3.9.6**　を site からcp & ps で解決
### terminal の表示
    ..............
    remote: Verifying deploy... done.
    To https://git.heroku.com/django-blog-app-moto-labo.git
    * [new branch]      main -> main
- git push heroku main 完了！！！
### 5. heroku で Dyno を起動
    heroku ps:scale web=1
- Scaling dynos... done, now running web at 1:Free
- Dyno 起動
- heroku site の overview page 確認
  - web gunicorn myproject.wsgi　ON の表示
### 6. heroku で migrate
    heroku run python manage.py migrate
- 全てOK 表示であれば次へ
### 7. heroku で superuser 作成
    heroku run python manage.py createsuperuser
1. user name 入力
2. mail address
3. password
- Superuser created successfully
  - スーパーユーザーの作成に成功
### 8. heroku を開く
- heroku site の setting page へ
  - Domains Your app can be found at URL をクリック
  - site が表示されたら OK!
## 3.
