# GIT TOOLS
## Task 1
git show aefea или git rev-parse aefea  
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545  
Update CHANGELOG.md

## Task 2
git show 85024d3  
tag: v0.12.23

## Task 3
git checkout b8d720 | git log --pretty=format:'%h %s' --graph -3 | git rev-parse 56cd7859e0 9ea88f22fc  
или git show b8d720 | git rev-parse 56cd7859e0 9ea88f22fc  
P1 - commit 56cd7859e05c36c06b56d013b55a252d0bb7e158   
P2 - commit 9ea88f22fc6269854151c571162c5bcf958bee2b

## Task 4
git log v0.12.23..v0.12.24  
git show 225466bc3e5f35baa5d07197bbc079345b77525e^  
commit 33ff1c03bb960b332be3af2e333462dde88b279e (tag: v0.12.24)  
commit b14b74c4939dcab573326f4e3ee2a62e23e12f89   
commit 3f235065b9347a758efadc92295b540ee0a5e26e   
commit 6ae64e247b332925b872447e9ce869657281c2bf   
commit 5c619ca1baf2e21a155fcdb4c264cc9e24a2a353   
commit 06275647e2b53d97d4f0a19a0fec11f6d69820b5   
commit d5f9411f5108260320064349b757f55c09bc4b80   
commit 4b6d06cc5dcb78af637bbb19c198faff37a066ed   
commit dd01a35078f040ca984cdd349f18d0b67e486c35   
commit 225466bc3e5f35baa5d07197bbc079345b77525e   
commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)

## Task 5
git log -S 'func providerSource('  
commit 8c928e83589d90a031f811fae52a81be7153e82f

## Task 6
git grep -n --heading globalPluginDirs   
git log -L :globalPluginDirs:plugins.go  
commit 78b12205587fe839f10d946ea3fdc06719decb05  
commit 52dbf94834cb970b510f2fba853a5b49ad9b1a46   
commit 41ab0aef7a0fe030e84018973a64135b11abcd70  
commit 66ebff90cdfaa6938f26f908c7ebad8d547fea17  
commit 8364383c359a6b738a436d1b7745ccdce178df47 тут функцию создали, не знаю, надо ли указывать этот коммит?

## Task 7
git log -S 'func synchronizedWriters' --pretty=format:'%H - %an'  
git show 5ac311e2a91e381e2f52234668b49ba670aa0fe5 

5ac311e2a91e381e2f52234668b49ba670aa0fe5 - Martin Atkins
