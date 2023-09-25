import soundfile as sf
import librosa
import os
from tqdm import tqdm
from pathlib import Path


from multiprocessing.pool import ThreadPool



if __name__ == '__main__':
    wav_list = Path("Data/wav48_silence_trimmed").rglob("*.flac")

    pool = ThreadPool(10)
    
    
    def do_it(wav_path):
         wav, sr = sf.read(wav_path)
         wav = librosa.resample(wav, sr, 24000)
         #Data/wav48_silence_trimmed/p343/p343_384_mic2.flac
    
         p = str(wav_path.parent)
         p = p.replace("wav48_silence_trimmed","wav24_silence_trimmed")
         print(p)
         os.makedirs(p,exist_ok = True)     
         #print(wav_path.parent)
         name =str(wav_path.stem)
         name = name[0:8]
         sf.write(p+"/"+name+".wav",wav,24000) 
    
    
    for wav_path in tqdm(wav_list):
        pool.apply_async(do_it,(wav_path,))
         #librosa.output.write_wav('file_trim_5s.wav', wave, sr)
    
         #break
    
    pool.close()
    pool.join()

