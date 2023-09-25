from pathlib import Path
from tqdm import tqdm
#from g2p_zh_en.g2p_zh_en import G2P
#from pypinyin import pinyin, lazy_pinyin, Style
#from pinyin_to_ipa import pinyin_to_ipa
from phonemizer import phonemize

from phonemizer.backend import EspeakBackend
backend = EspeakBackend('cmn')



wav_list = Path("aishell").rglob("*.wav")

spk_list = []
path_dict = {}
for wav in tqdm(wav_list):
    path_dict[wav.stem] = wav.absolute()
    spk = wav.stem[6:11]
    spk_list.append(spk)

spk_list = set(spk_list)
spk_list = sorted(spk_list)


#wav24_silence_trimmed/p278/p278_367.wav|ðɛɹ kəndˈɪʃən ɪz dᵻskɹˈaɪbd æz sˌæɾɪsfˈæktɚɹi.|22

trans_file = list(Path("aishell").rglob("*.txt"))[0]
#g2p = G2P()

o_file = "t.txt"
with open(o_file,"w") as of:
    with open(trans_file) as f:
        lines = f.readlines()
        for line in tqdm(lines):      
            segs = line[0:-1].split(" ")
            name = segs[0]
            trans = "".join(segs[1:]).strip()

            #phs = lazy_pinyin(trans, style=Style.TONE3, neutral_tone_with_five=True)
            try:
                phs = backend.phonemize(
                     [trans],   
                )
    
                phs_txt = phs[0].strip()

                spk = name[6:11]
                spk_id = spk_list.index(spk)
                if path_dict.__contains__(name):
                    ofs = f"{path_dict[name]}|{phs_txt}|{spk_id}\n"
                    of.write(ofs)

            #phs_txt = " ".join(phs)
            #print(phs_txt)
            #r = []
            #try:
            #    for p in phs:
            #        ipa = pinyin_to_ipa(p)
            #        i = ipa[0]
            #        r.append("".join(i))
            #    phs_txt = " ".join(r)
            #    spk = name[6:11]
            #    spk_id = spk_list.index(spk)
            #    if path_dict.__contains__(name):
            #        ofs = f"{path_dict[name]}|{phs_txt}|{spk_id}\n"
            #        of.write(ofs)
            except Exception as e:
                print(spk,e,trans)



