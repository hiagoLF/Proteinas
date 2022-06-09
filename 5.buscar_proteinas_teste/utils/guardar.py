import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
def guardarFastaEmArquivo(proteinasFasta: str):
    with open(dir_path+'/../../output/proteinas_para_teste.fasta', 'w') as f:
        f.write(proteinasFasta)