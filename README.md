# cancerscan/fizzbuzz
## 事前準備
### 1. GitHubのアカウントを作成する
### 2. SSH用の鍵を作成する
```
$ ssh-keygen -t rsa -b 2048 -C "your_name@cancerscan.jp"
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/your_name/.ssh/id_rsa):
Created directory '/Users/your_name/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/your_name/.ssh/id_rsa.
Your public key has been saved in /Users/your_name/.ssh/id_rsa.pub.
The key fingerprint is:
.
.
.
```
### 3. 秘密鍵の権限を設定する
```
$ chmod 600 ~/.ssh/id_rsa
```
### 4. 公開鍵をクリップボードにコピーする
```
$ cat ~/.ssh/id_rsa.pub | pbcopy
```
### 5. GitHubに公開鍵を登録する
- [Settings] -> [SSH and GPG keys] -> [New SSH key]
- テキストエリアにペーストする
- [Add SSH key]

## 作業用ブランチの作成

### 1. ローカルリポジトリを作成する
```
$ cd /path/to/working/directory
$ git clone git@github.com:cancerscan/fizzbuzz.git
```
もしSSHによる接続に失敗する場合はHTTPSを利用する
"https://github.com/cancerscan/fizzbuzz"

### 2. チュートリアル用の仮のmasterブランチを作成する
```
$ cd fizzbuzz
$ git branch master_your_name
```

### 3. 仮のmasterブランチへ移動する
```
$ git checkout master_your_name
```

### 4. 仮のmasterブランチをリモートリポジトリにpushする
```
$ git push origin master_your_name
```

### 5. 仮のmasterブランチからトピックブランチを作成する
```
$ git branch feature/fizzbuzz_your_name
```

### 6. トピックブランチへ移動する
```
$ git checkout feature/fizzbuzz_your_name
```

### 7. トピックブランチをリモートリポジトリにpushする
```
$ git push origin feature/fizzbuzz_your_name
```

## FizzBuzzの実装
- 任意のエディタでfizzbuzz.pyを編集する
- fizzbuzz関数を実装し、doctestを通過できるようにする

## Pull Requestの作成
### 1. 変更内容をadd, commitする
```
$ git add .
$ git commit -m "Your commit message"
```

### 2. 変更内容をリモートリポジトリにpushする
```
$ git push
```
次のエラーが表示された場合はエラー内容のとおりに上流ブランチを設定する
```
$ git push
fatal: The current branch feature/fizzbuzz_your_name has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin feature/fizzbuzz_your_name
$ git push --set-upstream origin feature/fizzbuzz_your_name
```

### 3. Pull Requestの作成
- [New pull request]
- [base: master_your_name] <- [compare: feature/fizzbuzz_your_name]
- [Create pull request]
- [Reviewers] -> レビュアーを選択
- Pull Requestのタイトル, 本文を入力する
  - 作業途中の場合はタイトルの先頭に[WIP]をつけること
  - 本文にはレビュアーへのメンションをいれること
  - 本文にはレビューしてほしい観点を記載すること

## Pull Requestのレビュー
- [Pull requests] -> Pull Requestを選択
- [Files changed]から変更内容が確認できる
  - 行単位でコメントを行うことができる

## Pull Requestのマージ
- [Pull requests] -> Pull Requestを選択
- [Merge pull request]
- [Close pull request]

