from mediawiki import MediaWiki
wikipedia = MediaWiki()
res = wikipedia.opensearch("ru:Малоохтинский парк")
print(res)
