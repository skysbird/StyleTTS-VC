from phonemizer.backend import EspeakBackend
backend = EspeakBackend('en-us')

a = backend.phonemize(["hello"])
print(a)


from g2p_zh_en.g2p_zh_en import G2P


g2p = G2P()

trans="这是中国田径队在本次世锦赛夺得的首枚金牌"
phs = g2p.g2p(text=trans, language="zh-cn")

print(phs)
